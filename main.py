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
        play1.y+=5
    if keys[pyglet.window.key.DOWN]:
        print("Moving Down")
        play1.image = greendown
        play1.y-=5
    if keys[pyglet.window.key.LEFT]:
        print("Moving Left")
        play1.image = greenleft
        play1.x-=5
    if keys[pyglet.window.key.RIGHT]:
        print("Moving Right")
        play1.image = greenright
        play1.x+=5

    play2.image = red
    if keys[pyglet.window.key.W]:
        print("Moving W Up")
        play2.image = redup
        play2.y+=5
    if keys[pyglet.window.key.S]:
        print("Moving S Down")
        play2.image = reddown
        play2.y-=5
    if keys[pyglet.window.key.A]:
        print("Moving A Left")
        play2.image = redleft
        play2.x-=5
    if keys[pyglet.window.key.D]:
        print("Moving D Right")
        play2.image = redright
        play2.x+=5
    
    global t
    t -= dt
    timerLabel.text = str(round(t))
    #if t == 0 :
        

@win.event
def on_draw():
    win.clear()
    fall.draw()
    play1.draw()
    play2.draw()
    timerLabel.draw()

pyglet.clock.schedule(update)
pyglet.app.run()