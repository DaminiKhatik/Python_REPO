import pyglet 
from pyglet.gl import *

win = pyglet.window.Window() 
glClear(GL_COLOR_BUFFER_BIT)
@win.event 
def on_draw():  
 pyglet.glBegin(GL_POINTS)   
glVertex2f=(3,4) #x is desired distance from left side of window, y is desired distance from bottom of window    #make as many vertexes as you want    
pyglet.gl.glEnd()
