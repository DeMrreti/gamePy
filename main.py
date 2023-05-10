import pyglet
import manzana
import constants


main = pyglet.window.Window(constants.width, constants.height, constants.name)
main.set_vsync(False)

gui = pyglet.graphics.Batch()
manzanas = pyglet.graphics.Batch()
jugador = pyglet.graphics.Batch()
fps_display = pyglet.window.FPSDisplay(main, color=(255,255,255,255), samples=240)
fps_display.update_period = 0.10

player = {
    "name" : "Player1",
    "score" : 0
}

tierra = pyglet.shapes.Rectangle(0,0,constants.width,constants.width,(60,152,0), batch=gui)
puntos = pyglet.text.Label(text=str(player["score"]),font_size=18,x=500,y=constants.width+15,color=(255,255,255,255),batch=gui,align='right',width=80)
linea = pyglet.shapes.Line(0,constants.width+1,constants.width,constants.width+1,1,(255,255,255),batch=gui)
fps = pyglet.text.Label(text="FPS:", font_size=18, x=20, y=constants.width+15, color=(255,255,255,255),batch=gui)
texto = pyglet.text.Label(text=constants.msg,font_size=18,x=400,y=constants.width+15,color=(255,255,255,255),batch=gui)
circulo = pyglet.shapes.Rectangle(0,0,50,50,(55,55,255,0),batch=jugador)

bird = pyglet.resource.image("bird.png")
bird.width, bird.height = 50, 50
bird_sprite = pyglet.sprite.Sprite(bird, x=circulo.x, y=circulo.y)

star = manzana.apple(manzanas)

apple = pyglet.resource.image("apple.png")
apple.width, apple.height = 30, 30
apple_sprite = pyglet.sprite.Sprite(apple, x=star.apple.x-15, y=star.apple.y-15)

fondo = pyglet.resource.image("fondo.jpg")
fondo.width, fondo.height = 600, 600
fondo_sprite = pyglet.sprite.Sprite(fondo)


def comprobarFronteras(x,y):
    global bird
    if x >= constants.width:
        circulo.x = 0;
    elif x <= -50:
        circulo.x = constants.width-50
    if y >= constants.width:
        circulo.y = 0
    elif y <= -50:
        circulo.y = constants.width-50
    bird_sprite.x, bird_sprite.y = circulo.x, circulo.y

def comprobarPuntos(x,y,x2,y2):
    global star
    if x == x2-25 and y == y2-25:
        star.apple.color = (0,0,0,0)
        player["score"] += 10
        puntos.text = str(player["score"])
        star = manzana.apple(manzanas)
        apple_sprite.x, apple_sprite.y = star.apple.x-15, star.apple.y-15

@main.event
def on_key_press(symbol, modifiers):
    global bird
    if symbol == pyglet.window.key.A:
        circulo.x -= 50
    elif symbol == pyglet.window.key.D:
        circulo.x += 50
    elif symbol == pyglet.window.key.W:
        circulo.y += 50
    elif symbol == pyglet.window.key.S:
        circulo.y -= 50
    bird_sprite.x, bird_sprite.y = circulo.x, circulo.y
    comprobarFronteras(circulo.x,circulo.y)
    comprobarPuntos(circulo.x,circulo.y,star.apple.x,star.apple.y)
    
@main.event
def on_draw():
    main.clear()
    gui.draw()
    fondo_sprite.draw()
    manzanas.draw()
    jugador.draw()
    bird_sprite.draw()
    apple_sprite.draw()
    fps_display.draw()


pyglet.clock.set_default(144)
    
pyglet.app.run()