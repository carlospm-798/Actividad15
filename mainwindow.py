"""
Carlos Paredes Márquez.
Importar window a code. xd
28/10/2020.
"""
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import Slot
from PySide2.QtGui import QPen, QColor, QTransform
from random import randint
from ui_mainwindow import Ui_MainWindow
from libreria import Libreria #particulas - Particulas
from particula import Particula
from pprint import pprint
from pprint import pformat, pformat

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
    
        self.libreria = Libreria()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.agregar_pushButton.clicked.connect(self.click_agregar) #agregado
        self.ui.mostrar_pushButton.clicked.connect(self.mostrar) #agregado
        self.ui.ordenar_velocidad_pushButton.clicked.connect(self.ordenar_velocidad)
        self.ui.ordenar_distancia_pushButton.clicked.connect(self.ordenar_distancia)

        self.ui.actionguardar.triggered.connect(self.action_guardar) #agregado
        self.ui.actionabrir.triggered.connect(self.action_abrir) #agregado
        self.ui.actiongrafo.triggered.connect(self.mostrar_diccionario)
        
        self.ui.actionRecorrido_en_Profundidad_Amplitud.triggered.connect(self.recorrido_p_a)
        self.grafo = {}

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)
    
    @Slot()
    def recorrido_p_a(self):
        origen_x = self.ui.origen_x_spinBox.value() #toma de valores
        origen_y = self.ui.origen_y_spinBox.value() 
        if not self.libreria.metodo_p(self.grafo, origen_x, origen_y): #acceder a metodos y cargar parametros
            QMessageBox.warning(
                self,
                'Aviso',
                'No es posible leer los valores'
            )
        else:
            profundidad = self.libreria.metodo_p(self.grafo, origen_x, origen_y)
            print('Profundidad: \n')

            self.ui.salida.clear()
            self.ui.salida.insertPlainText('Profundidad: ' + '\n')
            for i in profundidad:
                self.ui.salida.insertPlainText(str(i) + '\n')
                print(i)

            amplitud = self.libreria.metodo_a(self.grafo, origen_x, origen_y)
            print('Amplitud: \n')
            self.ui.salida.insertPlainText('Amplitud:' + '\n')
            for i in amplitud:
                self.ui.salida.insertPlainText(str(i) + '\n')
                print(i)

    @Slot()
    def mostrar_diccionario(self):
        self.ui.salida.clear()
        self.grafo.clear()
        grafo = self.libreria.mostrar_diccionario(self.grafo)
        self.ui.salida.insertPlainText(grafo)
        QMessageBox.information(
            self,
            'Exito',
            "Se imprimio el diccionario "
        )

    @Slot()
    def click_agregar(self):
        id = self.ui.id_spinBox.value()
        origen_x = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.libreria.agregar(particula)

    @Slot()
    def mostrar(self):
        self.ui.salida.clear()
        self.libreria.mostrar()
        self.ui.salida.insertPlainText(str(self.libreria))

        self.ui.tabla.setColumnCount(10)
        headers = ['ID', 'origen x', 'origen y', 'destino x', 'destino y', 'velocidad', 'red', 'green', 'blue', 'distancia']
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.libreria))

        row = 0

        for particula in self.libreria:
            id_widget = QTableWidgetItem(str(particula.id))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origen_x_widget)
            self.ui.tabla.setItem(row, 2, origen_y_widget)
            self.ui.tabla.setItem(row, 3, destino_x_widget)
            self.ui.tabla.setItem(row, 4, destino_y_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row += 1

        pen = QPen()
        pen.setWidth(2)

        for particula in self.libreria: #'MainWindow' object has no attribute 'particulas'
            r = particula.red
            g = particula.green
            b = particula.blue
            color = QColor(r, g, b)
            pen.setColor(color)

            self.scene.addEllipse(particula.origen_x, particula.origen_y, 4, 4, pen)
            self.scene.addEllipse(particula.destino_x, particula.destino_y, 4, 4, pen)
            self.scene.addLine(particula.origen_x, particula.origen_y, particula.destino_x, particula.destino_y, pen)

    
    @Slot()
    def ordenar_velocidad(self): #ascendente
        self.ui.tabla.clear()
        self.ui.salida.clear()
        headers = ['ID', 'origen x', 'origen y', 'destino x', 'destino y', 'velocidad', 'red', 'green', 'blue', 'distancia']
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.libreria))

        particulas = []

        for particula in self.libreria:
            particulas.append(particula)
        particulas.sort(key = lambda particula: particula.velocidad, reverse = False)

        row = 0
        for particula in particulas:

            id_widget = QTableWidgetItem(str(particula.id))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origen_x_widget)
            self.ui.tabla.setItem(row, 2, origen_y_widget)
            self.ui.tabla.setItem(row, 3, destino_x_widget)
            self.ui.tabla.setItem(row, 4, destino_y_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row += 1

        for particula in particulas:
            self.ui.salida.insertPlainText(str(particula) + '\n')
    
    @Slot()
    def ordenar_distancia(self): #descendente
        self.ui.tabla.clear()
        self.ui.salida.clear()
        headers = ['ID', 'origen x', 'origen y', 'destino x', 'destino y', 'velocidad', 'red', 'green', 'blue', 'distancia']
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.libreria))

        particulas = []

        for particula in self.libreria:
            particulas.append(particula)
        particulas.sort(key = lambda particula: particula.distancia, reverse = True)

        row = 0
        for particula in particulas:

            id_widget = QTableWidgetItem(str(particula.id))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origen_x_widget)
            self.ui.tabla.setItem(row, 2, origen_y_widget)
            self.ui.tabla.setItem(row, 3, destino_x_widget)
            self.ui.tabla.setItem(row, 4, destino_y_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row += 1

        for particula in particulas:
            self.ui.salida.insertPlainText(str(particula) + '\n')

    @Slot()
    def action_abrir(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.libreria.abrir(ubicacion):
            QMessageBox.information(
                self,
                'Éxito',
                'Se abrio el archivo ' + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                'Error',
                'Error al abrir el archivo ' + ubicacion
            )
    
    @Slot() #Hacer uso de la biblioteca json
    def action_guardar(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar como',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.libreria.guardar(ubicacion):
            QMessageBox.information(
                self,
                'Éxito',
                'Se pudo crear el archivo ' + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                'Error',
                'No se pudo crear el archivo ' + ubicacion
            )