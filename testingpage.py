import pyglet

win = pyglet.window.Window(fullscreen=True)

t = 90
timerLabel = pyglet.text.Label(str(t), font_size=65,
                                       x=win.width // 20,
                                       y=win.height // 1.05,
                                       anchor_x='center', anchor_y='center')

corner1= pyglet.image.load('images/assets/ground/tundra/slice19_19.png')
c1 = pyglet.sprite.Sprite(corner1, x=0, y=1010)
corner2= pyglet.image.load('images/assets/ground/tundra/slice20_20.png')
c2 = pyglet.sprite.Sprite(corner2, x=1850, y=1010)
corner3= pyglet.image.load('images/assets/ground/tundra/slice19_192.png')
c3 = pyglet.sprite.Sprite(corner3, x=1850, y=0)
corner4= pyglet.image.load('images/assets/ground/tundra/slice20_202.png')
c4 = pyglet.sprite.Sprite(corner4, x=0, y=0)

bottom= pyglet.image.load('images/assets/ground/tundra/slice03_032.png')
bot = pyglet.sprite.Sprite(bottom, x=55, y=0)
top= pyglet.image.load('images/assets/ground/tundra/slice03_03.png')
topp = pyglet.sprite.Sprite(top, x=55, y=0)
side1= pyglet.image.load('images/assets/ground/tundra/slice23_23.png')
lef = pyglet.sprite.Sprite(top, x=55, y=0)
side2= pyglet.image.load('images/assets/ground/tundra/slice23_232.png')
rig = pyglet.sprite.Sprite(top, x=55, y=0)

def update(dt):
    global t
    t -= dt
    timerLabel.text = str(round(t))
    #if t == 0 :
        
low = []
for i in range(26):
        low.append(pyglet.sprite.Sprite(bottom, x = i * 70 + 70, y = 0))
high = []
for i in range(26):
        high.append(pyglet.sprite.Sprite(top, x = i * 70 + 70, y = 1010))
left = []
for j in range(26):
        left.append(pyglet.sprite.Sprite(side1, x = 0, y = j * 35 + 70))
right = []
for j in range(26):
       right.append(pyglet.sprite.Sprite(side2, x = 1850, y = j * 35 + 70))

@win.event
def on_draw():
    win.clear()
    c1.draw()
    c2.draw()
    c3.draw()
    c4.draw()
    for i in range(26):
        low[i].draw()
    for i in range(26):
        high[i].draw()
    for j in range(26):
        left[j].draw()
    for j in range(26):   
        right[j].draw()    
    timerLabel.draw()

pyglet.clock.schedule(update)
pyglet.app.run()