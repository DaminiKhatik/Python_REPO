""" Installation of Pyglet:
with pip:
pip install pyglet
"""

# Hello World in Pyglet
import pyglet
window = pyglet.window.Window()
label = pyglet.text.Label("Hello World!",
                            color=(255,255,255,255),
                            font_size=36,
                            x=window.width//2, y=window.height//2,
                            anchor_x="center", anchor_y="center")
@window.event
def on_draw():
        window.clear()
        label.draw()
        window.flip()
        pyglet.app.run()