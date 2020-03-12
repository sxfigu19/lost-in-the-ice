import pyglet

win = pyglet.window.Window(fullscreen=True)

t = 90
timerLabel = pyglet.text.Label(str(t), font_size=65,
                                       x=win.width // 15,
                                       y=win.height // 1.05,
                                       anchor_x='center', anchor_y='center')

animation = pyglet.image.load_animation('images/assets/ground/snow_fall3.gif')
fall = pyglet.sprite.Sprite(animation, x=0, y=0)
fall.scale = 5

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

middle= pyglet.image.load('images/assets/ground/tundra/slice33_33.png')
ground = pyglet.sprite.Sprite(middle, x=0, y=0)

green= pyglet.image.load('images/assets/Green/greenfront.png')
greenup= pyglet.image.load('images/assets/Green/greenbackwalk2.png')
greendown= pyglet.image.load('images/assets/Green/greendown1.png')
greenleft= pyglet.image.load('images/assets/Green/greenleftwalk2.png')
greenright= pyglet.image.load('images/assets/Green/greenrightwalk2.png')
play1 = pyglet.sprite.Sprite(green, x=0, y =0)
play1.scale = 2

red= pyglet.image.load('images/assets/Red/redfront.png')
redup= pyglet.image.load('images/assets/Red/redbackwalk2.png')
reddown= pyglet.image.load('images/assets/Red/reddown1.png')
redleft= pyglet.image.load('images/assets/Red/redleftwalk2.png')
redright= pyglet.image.load('images/assets/Red/redrightwalk2.png')
play2 = pyglet.sprite.Sprite(red, x=100, y =100)
play2.scale = 2

keys = pyglet.window.key.KeyStateHandler()

def update(dt):
    win.push_handlers(keys) # update the key object
    play1.image = green
    if keys[pyglet.window.key.UP]:
        print("Moving Up")
        play1.image = greenup
        play1.y+=10
    if keys[pyglet.window.key.DOWN]:
        print("Moving Down")
        play1.image = greendown
        play1.y-=10
    if keys[pyglet.window.key.LEFT]:
        print("Moving Left")
        play1.image = greenleft
        play1.x-=10
    if keys[pyglet.window.key.RIGHT]:
        print("Moving Right")
        play1.image = greenright
        play1.x+=10

    play2.image = red
    if keys[pyglet.window.key.W]:
        print("Moving W Up")
        play2.image = redup
        play2.y+=10
    if keys[pyglet.window.key.S]:
        print("Moving S Down")
        play2.image = reddown
        play2.y-=10
    if keys[pyglet.window.key.A]:
        print("Moving A Left")
        play2.image = redleft
        play2.x-=10
    if keys[pyglet.window.key.D]:
        print("Moving D Right")
        play2.image = redright
        play2.x+=10
    
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
mid = []
for i in range(26):
    for j in range(26):
        mid.append(pyglet.sprite.Sprite(middle, x = i * 70 + 70, y = j * 35 + 70))

@win.event
def on_draw():
    win.clear()
    c1.draw()
    c2.draw()
    c3.draw()
    c4.draw()
    for i in range(676):
        mid[i].draw()
    for i in range(26):
        low[i].draw()
    for i in range(26):
        high[i].draw()
    for j in range(26):
        left[j].draw()
    for j in range(26):   
        right[j].draw()    
    fall.draw()
    play1.draw()
    play2.draw()
    timerLabel.draw()

pyglet.clock.schedule(update)
pyglet.app.run()