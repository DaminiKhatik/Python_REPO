import pyglet
# import all of opengl functions
from pyglet.gl import *

win = pyglet.window.Window()

@win.event
def on_draw():
 pyglet.app.run()