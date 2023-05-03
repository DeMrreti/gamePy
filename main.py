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
pts = 0
msg = 'SCORE:'
fps_display = pyglet.window.FPSDisplay(main)

linea = shapes.Line(0,401,400,401,1,(255,255,255),batch=gui)
texto = pyglet.text.Label(text=msg,font_size=18,x=25,y=415,color=(255,255,255,255),batch=gui)
puntos = pyglet.text.Label(text=str(pts),font_size=18,x=375,y=415,color=(255,255,255,255),align='right',batch=gui)
circulo = shapes.Rectangle(x,y,50,50,(55,55,255),batch=jugador)
star = generadorNivel.spawApples(manzanas)

@main.event
def colision() : 
    if (x == (star.x-25) & y == (star.y-25)):
        pts =+ 10
        star.color = (0,0,0)

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

@main.event
def on_draw():
    main.clear()
    gui.draw()
    manzanas.draw()
    jugador.draw()
    fps_display.draw()

pyglet.app.run()