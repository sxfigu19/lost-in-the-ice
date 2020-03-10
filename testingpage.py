import pyglet

win = pyglet.window.Window(fullscreen=True)

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

@win.event
def on_draw():
    win.clear()
    fall.draw()
    play1.draw()

pyglet.clock.schedule(update)
pyglet.app.run()