import pyglet
import random
import constants

def positionGenerator() :
    posicionesX = [25,75,125,175,225,275,325,375,425,475,525,575]
    x = int(random.randint(0,12))
    return posicionesX[x]

def spawApples(apples) :
    return pyglet.shapes.Star(positionGenerator(),positionGenerator(),5,10,4,0,(255,55,55),apples)
