import pyglet

class apple():
    def __init__(self, x,y,batch):
        self.apple = pyglet.shapes.Star(x,y,8,5,5,0,color=(255,55,55),batch=batch)

        