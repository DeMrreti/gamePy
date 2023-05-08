import pyglet
from pyglet.window import key, mouse
from pyglet import shapes
import generadorNivel

main = pyglet.window.Window(400, 450, "Game")
gui = pyglet.graphics.Batch()
manzanas = pyglet.graphics.Batch()
jugador = pyglet.graphics.Batch()

x = 0
y = 0
score = 0
msg = 'SCORE:'
fps_display = pyglet.window.FPSDisplay(main)

tierra = shapes.Rectangle(0,0,400,400,(60,152,0), batch=gui)
puntos = pyglet.text.Label(text=str(score),font_size=18,x=350,y=415,color=(255,255,255,255),align='right',batch=gui)
linea = shapes.Line(0,401,400,401,1,(255,255,255),batch=gui)
texto = pyglet.text.Label(text=msg,font_size=18,x=25,y=415,color=(255,255,255,255),batch=gui)
circulo = shapes.Rectangle(x,y,50,50,(55,55,255),batch=jugador)
star = generadorNivel.spawApples(manzanas)

def comprobarFronteras(x,y):
    if x >= 400:
        circulo.x = 0
    elif x <= -50:
        circulo.x = 350
    if y >= 400:
        circulo.y = 0
    elif y <= -50:
        circulo.y = 350

def comprobarPuntos(x,y,x2,y2):
    if x == x2-25 and y == y2-25:
        star.color = (0,0,0,0)
        score += 10

@main.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        circulo.x -= 50
    elif symbol == key.D:
        circulo.x += 50
    elif symbol == key.W:
        circulo.y += 50
    elif symbol == key.S:
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