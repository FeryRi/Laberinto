from turtle import *
from freegames import floor, vector

path = Turtle(visible=False) #tortuga invisible
aim = vector(5, 0)
person = vector(180, 20)

#matriz que le da forma al laberinto
tiles=[
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
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
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

#función que se encarga de dibujar el rectángulo del tablero
#toma como parámetro la ruta en (x,y)
def square(x, y):
    path.up() #que no pinte
    path.goto(x, y) #manda a (x,y)
    path.down() #permite que pinte
    path.begin_fill() #previo al llenado del dibujo

    #ciclo para hacer el dibujo
    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill() #termina llenado de dibujo

#función para el retorno de puntos desplazados en el rectángulo
def offset(point):
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index

#función para validar el punto en el tablero 
def valid(point):
    index = offset(point)

    #condicional para hacer la validación
    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0

#función para dibujar el laberinto usando el camino
def maze():
    bgcolor('black')
    path.color('pink')

    #ciclo que toma en cuenta el tamaño del laberinto
    for index in range(len(tiles)):
        tile = tiles[index]

        #condicional para pintar solo el camino
        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)


#función para el movimiento del objeto
def move():
  clear()

  if valid(person + aim):
      person.move(aim)

  up()
  goto(person.x + 10, person.y + 10)
  dot(20, 'blue')
  ontimer(move, 100)

  if person == vector(-200,-140):
      print("¡Has llegado al destino!")
      bye()
    
#función para cambiar la dirección del objeto si es válido
def change(x, y):
    if valid(person + vector(x, y)):
        aim.x = x
        aim.y = y
# Función para verificar la condición de pérdida
def check_loss():
    if (
        person == vector(160, 100)
        or person == vector(40, 20)
        or person == vector(-80, -40)
        or person == vector(-180, -60)
    ):
        clear()
        goto(0, 0)
        write("Game Over", align="center", font=("Arial", 24, "normal"))
        update()
          # Espera 2 segundos y reinicia el juego

    ontimer(check_loss, 100)

# Función para reiniciar el juego

# Función para reiniciar el juego cuando se presiona la tecla "r"
def restart():
    clear()
    global person, aim
    person = vector(180, 20)
    aim = vector(5, 0)
    maze()
    move()

setup(420, 340, 420, 340) #configura la ventana del juego
hideturtle()
tracer(False)
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
onkey(restart, "r")  # Cuando se presione la tecla "r" se reiniciará el juego
maze()
move()
check_loss()  # Llamar a la función para verificar la pérdida
done()

#Salidas falsas (160,100)(40,20)(-80-40)(-180,-60)