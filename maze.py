from turtle import *
from freegames import floor, vector

path = Turtle(visible=False) #tortuga invisible

#matriz que le da forma al laberinto
tiles=[
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0,
    0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0,
    0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0,
    0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1,
    0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0,
    0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0,
    0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0,
    0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0,
    1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

#función que se encarga de dibujar el rectángulo del tablero
#toma como parámetro la ruta en (x,y)
def rectangle(x,y):
    path.up() #que no pinte
    path.goto(x,y) #manda a (x,y)
    path.down #permite que pinte
    path.begin_fill #previo al llenado del dibujo

    #ciclo para hacer el dibujo
    for count in range(4):
        #dibujar largo
        if count%2 == 0:
             path.forward(20)
             path.left(90)

        #dibujar el ancho
        else:
             path.forward(16)
             path.left(90)

    path.end_fill() #termina llenado de dibujo

#función para el retorno de puntos desplazados en el rectángulo
def offset(point):
        x=(floor(point.x, 20) + 200)/20
        y=(120 - floor(point.y, 20))/20
        index= int(x + y * 14)
        return index

#función para validar el punto en el tablero 
def valid(point):
        index=offset(point)

        #condicional para hacer la validación
        if tiles[index]==0:
             return False
        
        return point.x % 20 == 0 or point.y % 16 == 0

#función para dibujar el laberinto usando el camino
def maze():
    bgcolor('black')
    path.color('pink')

    #ciclo que toma en cuenta el tamaño del laberinto
    for index in range(len(tiles)):
        tile = tiles[index]

        #condicional para pintar solo el camino
        if tile > 0:
             x=(index % 20) * 20 - 200
             y = 120 - (index // 16) * 20
             rectangle(x,y)


