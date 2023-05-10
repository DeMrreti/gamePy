import pyglet
import random

def positionGenerator() :
    posicionesX = [25,75,125,175,225,275,325,375,425,475,525,575]
    x = int(random.randint(0,11))
    return posicionesX[x]

class apple():
    def __init__(self, batch):
        self.apple = pyglet.shapes.Star(positionGenerator(),positionGenerator(),8,5,5,0,color=(255,55,55),batch=batch)

        