import pyglet

win = pyglet.window.Window(fullscreen=True)

t = 10
timerLabel = pyglet.text.Label(str(t), font_size=65,
                                       x=win.width // 15,
                                       y=win.height // 1.05,
                                       anchor_x='center', anchor_y='center')

corner1= pyglet.image.load('images/assets/ground/tundra/slice01_01.png')

grey = []
for i in range(14):
    for j in range(10):
        grey.append(pyglet.sprite.Sprite(corner1, x = i * 48, y = j * 50))

def update(dt):
    global t
    t -= dt
    timerLabel.text = str(round(t))
    #if t == 0 :
        

@win.event
def on_draw():
    win.clear()
    timerLabel.draw()
    for i in range(140):
        grey[i].draw()

pyglet.clock.schedule(update)
pyglet.app.run()