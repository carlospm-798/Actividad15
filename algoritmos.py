"""
Carlos Paredes Márquez.
"""

import math #Importar libreria de Matemáticas.

def distancia_euclidiana(origen_x, origen_y, destino_x, destino_y): #Definir nuestra 'función'.
    return math.sqrt((destino_x - origen_x)**2 + (destino_y - origen_y)**2) #Retornar nuestra 'función'.