import pyglet
import manzana
import constants

#CONFIGURAR VENTANA, OPENGL, BUFFER, SIZES

config = pyglet.gl.Config(
    double_buffer=True
)

main = pyglet.window.Window(
    constants.width,
    constants.height,
    constants.name
)
icon = pyglet.image.load('apple.ico')
main.set_icon(icon)

#COGER ENTRADA DE TECLADO DE LA VENTANA PRINCIPAL

key_handler = pyglet.window.key.KeyStateHandler()
main.push_handlers(key_handler)

#DESLIMITAR EL RELOJ DE EJECUCION

clock = pyglet.clock.Clock()
clock.tick_func = None

#GESTIONAR PANELES

gui = pyglet.graphics.Batch()
manzanas = pyglet.graphics.Batch()
jugador = pyglet.graphics.Batch()

#GENERAR PERSONAJE, MANZANAS, FONDOS Y VISUALES

fps_display = pyglet.window.FPSDisplay(
    window = main,
    samples = 240
)
fps_display.label.color = (255, 255, 255, 255)
fps_display.label.font_size = 18
fps_display.label.x = 100
fps_display.label.y = constants.width+15

player = {
    "name" : "Player1",
    "score" : 0
}

tierra = pyglet.shapes.Rectangle(
    x = 0,
    y = 0,
    width=constants.width,
    height=constants.width,
    color=(60,152,0),
    batch=gui
)

puntos = pyglet.text.Label(
    text=str(player["score"]),
    font_size=18,
    x=500,
    y=constants.width+15,
    color=(255,255,255,255),
    batch=gui,
    align='right',
    width=80
)

linea = pyglet.shapes.Line(
    x = 0,
    y = constants.width+1,
    x2 = constants.width,
    y2 = constants.width+1,
    width = 1,
    color=(255,255,255),
    batch=gui
)

fps = pyglet.text.Label(
    text="FPS:",
    font_size=18,
    x=20,
    y=constants.width+15,
    color=(255,255,255,255),
    batch=gui
)

texto = pyglet.text.Label(
    text=constants.msg,
    font_size=18,
    x=400,
    y=constants.width+15,
    color=(255,255,255,255),
    batch=gui
)

circulo = pyglet.shapes.Rectangle(
    x = 250,
    y = 250,
    width = 50,
    height = 50,
    color = (55,55,255,0),
    batch=jugador
)

bird = pyglet.resource.image("bird.png")
bird.x , bird.y = circulo.x, circulo.y
bird.width, bird.height = 50, 50
bird_sprite = pyglet.sprite.Sprite(
    img = bird,
    x=circulo.x,
    y=circulo.y
)

star = manzana.apple(manzanas)

apple = pyglet.resource.image("apple.png")
apple.width, apple.height = 30, 30
apple_sprite = pyglet.sprite.Sprite(img = apple,
    x=star.apple.x-15,
    y=star.apple.y-15
)

fondo = pyglet.resource.image("fondo.jpg")
fondo.width, fondo.height = constants.width, constants.width
fondo_sprite = pyglet.sprite.Sprite(
    fondo
)

background_image = pyglet.resource.image("fondo.jpg")
background_image.width, background_image.height = constants.width, constants.width
background = pyglet.sprite.Sprite(
    background_image
)

play_button_image = pyglet.resource.image("play.png")
play_button = pyglet.sprite.Sprite(
    play_button_image,
    x=main.width//2 - play_button_image.width//2,
    y=main.height//3 - play_button_image.height//3
)

pause_button_image = pyglet.resource.image("pause.png")
pause_button_image.width , pause_button_image.height = 50, 50
pause_button = pyglet.sprite.Sprite(
    pause_button_image,
    x = 245,
    y = constants.height - 50
)

panel_time_button_image = pyglet.resource.image("panel_tiempo.png")
panel_time_button_image.width , panel_time_button_image.height = 50, 50
panel_time_button = pyglet.sprite.Sprite(
    panel_time_button_image,
    x = 305,
    y = constants.height - 50
)

title = pyglet.text.Label(
    text="AppleGame",
    color=(0,0,0,255),
    font_size=28,
    bold=True,
    align='center',
    x = 240,
    y = 350
)

icon2 = pyglet.resource.image('apple.ico')
icon2.width, icon2.height = 80, 80
icon_menu = pyglet.sprite.Sprite(
    img=icon2,
    x=150,
    y=330
)

cuentaRegresiva = pyglet.text.Label(
    text=str(constants.cuentaRegresiva),
    color=(255,255,255,255),
    font_size=22,
    bold=True,
    align='center',
    x = 313,
    y = constants.height - 35,
    width=35,
    height=40,
)

panel_final = pyglet.resource.image("panel_tiempo.png")
panel_final.width , panel_final.height = 300, 200
panel_final_sprite = pyglet.sprite.Sprite(
    panel_final,
    x = 150,
    y = 200
)

final_score = pyglet.text.Label(
    text="Score: " + str(player["score"]),
    color=(255,255,255,255),
    font_size=24,
    bold=True,
    align='center',
    x = 250,
    y = 330
)

button_restar_game = pyglet.resource.image("play.png")
button_restar_game.width , button_restar_game.height = 250, 150
button_restar_game_sprite = pyglet.sprite.Sprite(
    button_restar_game,
    x = 180,
    y = 200
)

#FUNCIONES

def comprobarFronteras(x,y):
    global bird
    if x >= constants.width:
        circulo.x = 0
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

def cuenta(dt):
    if constants.menu == False and constants.cuentaRegresiva > 0:
        constants.cuentaRegresiva -= 1
        cuentaRegresiva.text = str(constants.cuentaRegresiva)
    elif constants.cuentaRegresiva == 0:
        pass

def update(dt):
    global bird
    if constants.cuentaRegresiva > 0:
        if key_handler[pyglet.window.key.A]:
            circulo.x -= 50
        elif key_handler[pyglet.window.key.D]:
            circulo.x += 50
        elif key_handler[pyglet.window.key.W]:
            circulo.y += 50
        elif key_handler[pyglet.window.key.S]:
            circulo.y -= 50
        elif key_handler[pyglet.window.key.LEFT]:
            circulo.x -= 50
        elif key_handler[pyglet.window.key.RIGHT]:
            circulo.x += 50
        elif key_handler[pyglet.window.key.UP]:
            circulo.y += 50
        elif key_handler[pyglet.window.key.DOWN]:
            circulo.y -= 50
        bird_sprite.x, bird_sprite.y = circulo.x, circulo.y
    comprobarFronteras(circulo.x,circulo.y)
    comprobarPuntos(circulo.x,circulo.y,star.apple.x,star.apple.y)
    
@main.event
def on_mouse_press(x, y, button, modifiers):
    if play_button.x < x < play_button.x + play_button.width and \
            play_button.y < y < play_button.y + play_button.height:
        launch_game()

def launch_game():
    constants.menu = False

@main.event
def on_draw():
    if constants.menu == True:
        main.clear()
        background.draw()
        play_button.draw()
        title.draw()
        icon_menu.draw()
    if constants.menu == False:
        main.clear()
        gui.draw()
        fondo_sprite.draw()
        pause_button.draw()
        panel_time_button.draw()
        manzanas.draw()
        jugador.draw()
        bird_sprite.draw()
        apple_sprite.draw()
        fps_display.draw()
        cuentaRegresiva.draw()
    if constants.cuentaRegresiva == 0:
        panel_final_sprite.draw()
        final_score.draw()
        button_restar_game_sprite.draw()

pyglet.clock.schedule_interval(cuenta, 1/1)
pyglet.clock.schedule_interval(update, 1/10)

pyglet.app.run()