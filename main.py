import pyglet
import generadorNivel
import constants

main = pyglet.window.Window(constants.width, constants.height, constants.name)
gui = pyglet.graphics.Batch()
manzanas = pyglet.graphics.Batch()
jugador = pyglet.graphics.Batch()

score = 0
fps_display = pyglet.window.FPSDisplay(main)

tierra = pyglet.shapes.Rectangle(0,0,constants.width,constants.width,(60,152,0), batch=gui)
puntos = pyglet.text.Label(text=str(score),font_size=18,x=550,y=constants.width+15,color=(255,255,255,255),align='right',batch=gui)
linea = pyglet.shapes.Line(0,constants.width+1,constants.width,constants.width+1,1,(255,255,255),batch=gui)
texto = pyglet.text.Label(text=constants.msg,font_size=18,x=25,y=constants.width+15,color=(255,255,255,255),batch=gui)
circulo = pyglet.shapes.Rectangle(0,0,50,50,(55,55,255),batch=jugador)
star = generadorNivel.spawApples(manzanas)

def comprobarFronteras(x,y):
    if x >= constants.width:
        circulo.x = 0
    elif x <= -50:
        circulo.x = constants.width-50
    if y >= constants.width:
        circulo.y = 0
    elif y <= -50:
        circulo.y = constants.width-50

def comprobarPuntos(x,y,x2,y2):
    if x == x2-25 and y == y2-25:
        star.color = (0,0,0,0)

@main.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.A:
        circulo.x -= 50
    elif symbol == pyglet.window.key.D:
        circulo.x += 50
    elif symbol == pyglet.window.key.W:
        circulo.y += 50
    elif symbol == pyglet.window.key.S:
        circulo.y -= 50
    comprobarFronteras(circulo.x,circulo.y)
    comprobarPuntos(circulo.x,circulo.y,star.x,star.y)

@main.event
def on_draw():
    main.clear()
    gui.draw()
    manzanas.draw()
    jugador.draw()
    fps_display.draw()

pyglet.app.run()