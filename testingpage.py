import pyglet

win = pyglet.window.Window(fullscreen=True)

t = 90
timerLabel = pyglet.text.Label(str(t), font_size=65,
                                       x=win.width // 15,
                                       y=win.height // 1.05,
                                       anchor_x='center', anchor_y='center')

corner1= pyglet.image.load('images/assets/ground/tundra/slice19_19.png')
c1 = pyglet.sprite.Sprite(corner1, x=0, y=0)
c1.scale = 1

def update(dt):
    global t
    t -= dt
    timerLabel.text = str(round(t))
    #if t == 0 :
        

@win.event
def on_draw():
    win.clear()
    timerLabel.draw()
    c1.draw()

pyglet.clock.schedule(update)
pyglet.app.run()