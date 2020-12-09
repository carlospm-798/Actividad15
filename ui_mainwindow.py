# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(933, 766)
        self.actionguardar = QAction(MainWindow)
        self.actionguardar.setObjectName(u"actionguardar")
        self.actionabrir = QAction(MainWindow)
        self.actionabrir.setObjectName(u"actionabrir")
        self.actiongrafo = QAction(MainWindow)
        self.actiongrafo.setObjectName(u"actiongrafo")
        self.actionRecorrido_en_Profundidad_Amplitud = QAction(MainWindow)
        self.actionRecorrido_en_Profundidad_Amplitud.setObjectName(u"actionRecorrido_en_Profundidad_Amplitud")
        self.actionRecorrido_en_Amplitud = QAction(MainWindow)
        self.actionRecorrido_en_Amplitud.setObjectName(u"actionRecorrido_en_Amplitud")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_7 = QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.tabWidget = QTabWidget(self.groupBox_5)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(300, 50, 601, 641))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsView = QGraphicsView(self.tab)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_6 = QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_6.addWidget(self.tabla, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.groupBox = QGroupBox(self.groupBox_5)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 40, 283, 647))
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.destino_x_spinBox = QSpinBox(self.groupBox_3)
        self.destino_x_spinBox.setObjectName(u"destino_x_spinBox")
        self.destino_x_spinBox.setMaximum(1000)

        self.gridLayout_2.addWidget(self.destino_x_spinBox, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)

        self.destino_y_spinBox = QSpinBox(self.groupBox_3)
        self.destino_y_spinBox.setObjectName(u"destino_y_spinBox")
        self.destino_y_spinBox.setMaximum(1000)

        self.gridLayout_2.addWidget(self.destino_y_spinBox, 0, 3, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 3)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.red_spinBox = QSpinBox(self.groupBox_4)
        self.red_spinBox.setObjectName(u"red_spinBox")
        self.red_spinBox.setMaximum(1000)

        self.gridLayout_3.addWidget(self.red_spinBox, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 2, 1, 1)

        self.green_spinBox = QSpinBox(self.groupBox_4)
        self.green_spinBox.setObjectName(u"green_spinBox")
        self.green_spinBox.setMaximum(1000)

        self.gridLayout_3.addWidget(self.green_spinBox, 0, 3, 1, 1)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 0, 4, 1, 1)

        self.blue_spinBox = QSpinBox(self.groupBox_4)
        self.blue_spinBox.setObjectName(u"blue_spinBox")
        self.blue_spinBox.setMaximum(1000)

        self.gridLayout_3.addWidget(self.blue_spinBox, 0, 5, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_4, 3, 0, 1, 3)

        self.agregar_pushButton = QPushButton(self.groupBox)
        self.agregar_pushButton.setObjectName(u"agregar_pushButton")

        self.gridLayout_4.addWidget(self.agregar_pushButton, 5, 0, 1, 3)

        self.salida = QTextEdit(self.groupBox)
        self.salida.setObjectName(u"salida")

        self.gridLayout_4.addWidget(self.salida, 6, 0, 1, 3)

        self.id_spinBox = QSpinBox(self.groupBox)
        self.id_spinBox.setObjectName(u"id_spinBox")
        self.id_spinBox.setMaximum(1000)

        self.gridLayout_4.addWidget(self.id_spinBox, 0, 1, 1, 2)

        self.ordenar_velocidad_pushButton = QPushButton(self.groupBox)
        self.ordenar_velocidad_pushButton.setObjectName(u"ordenar_velocidad_pushButton")

        self.gridLayout_4.addWidget(self.ordenar_velocidad_pushButton, 8, 0, 1, 3)

        self.velocidad_spinBox = QSpinBox(self.groupBox)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")
        self.velocidad_spinBox.setMaximum(1000)

        self.gridLayout_4.addWidget(self.velocidad_spinBox, 4, 1, 1, 2)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.origen_x_spinBox = QSpinBox(self.groupBox_2)
        self.origen_x_spinBox.setObjectName(u"origen_x_spinBox")
        self.origen_x_spinBox.setMaximum(1000)

        self.gridLayout.addWidget(self.origen_x_spinBox, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.origen_y_spinBox = QSpinBox(self.groupBox_2)
        self.origen_y_spinBox.setObjectName(u"origen_y_spinBox")
        self.origen_y_spinBox.setMaximum(1000)

        self.gridLayout.addWidget(self.origen_y_spinBox, 0, 3, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 3)

        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout_4.addWidget(self.mostrar_pushButton, 7, 0, 1, 3)

        self.ordenar_distancia_pushButton = QPushButton(self.groupBox)
        self.ordenar_distancia_pushButton.setObjectName(u"ordenar_distancia_pushButton")

        self.gridLayout_4.addWidget(self.ordenar_distancia_pushButton, 9, 0, 1, 3)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 4, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_5, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 933, 26))
        self.menuguardar = QMenu(self.menubar)
        self.menuguardar.setObjectName(u"menuguardar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuguardar.menuAction())
        self.menuguardar.addAction(self.actionguardar)
        self.menuguardar.addAction(self.actionabrir)
        self.menuguardar.addAction(self.actiongrafo)
        self.menuguardar.addAction(self.actionRecorrido_en_Profundidad_Amplitud)
        self.menuguardar.addAction(self.actionRecorrido_en_Amplitud)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionguardar.setText(QCoreApplication.translate("MainWindow", u"guardar", None))
#if QT_CONFIG(shortcut)
        self.actionguardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionabrir.setText(QCoreApplication.translate("MainWindow", u"abrir", None))
#if QT_CONFIG(shortcut)
        self.actionabrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actiongrafo.setText(QCoreApplication.translate("MainWindow", u"grafo", None))
#if QT_CONFIG(shortcut)
        self.actiongrafo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.actionRecorrido_en_Profundidad_Amplitud.setText(QCoreApplication.translate("MainWindow", u"Recorrido en Profundidad", None))
#if QT_CONFIG(shortcut)
        self.actionRecorrido_en_Profundidad_Amplitud.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+H", None))
#endif // QT_CONFIG(shortcut)
        self.actionRecorrido_en_Amplitud.setText(QCoreApplication.translate("MainWindow", u"Recorrido en Amplitud", None))
#if QT_CONFIG(shortcut)
        self.actionRecorrido_en_Amplitud.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+J", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Main", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Visual", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particula", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"R:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"G:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"B:", None))
        self.agregar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.ordenar_velocidad_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar velocidad", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Origen", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.ordenar_distancia_pushButton.setText(QCoreApplication.translate("MainWindow", u"Ordenar distancia", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.menuguardar.setTitle(QCoreApplication.translate("MainWindow", u"archivo", None))
    # retranslateUi

