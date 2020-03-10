import pyglet

win = pyglet.window.Window(fullscreen=True)

class Timer:

    def __init__(self):
        self.label = pyglet.text.Label('00:00', font_size=65,
                                       x=win.width // 15,
                                       y=win.height // 1.05,
                                       anchor_x='center', anchor_y='center')
        self.reset()

    def reset(self):
        self.time = 0
        self.running = True
        self.label.text = '00:00'
        self.label.color = (255, 255, 255, 255)

    def update(self, dt):
        if self.running:
            self.time += dt
            m, s = divmod(self.time, 60)
            self.label.text = '%02d:%02d' % (m, s)
            if m >= 5:
                self.label.color = (180, 0, 0, 255)


def draw_rect(x, y, width, height):
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
        ('v2f', [x, y, x + width, y, x + width, y + height, x, y + height]))


animation = pyglet.image.load_animation('images/assets/snow_fall3.gif')
fall = pyglet.sprite.Sprite(animation, x=0, y=0)
fall.scale = 5

water= pyglet.image.load('images/assets/ground/graphics-tiles-waterflow.png')
wet = pyglet.sprite.Sprite(water, x=0, y =0)
wet.scale = 15
land= pyglet.image.load('images/assets/ground/snow_stones.png')
snow = pyglet.sprite.Sprite(land, x=500, y =40)
snow.scale = 4

talltree= pyglet.image.load('images/assets/ground/tall_snow_tree.png')
tree1 = pyglet.sprite.Sprite(talltree, x=1100, y =680)
tree1.scale = 3.4
shorttree= pyglet.image.load('images/assets/ground/short_snow_tree.png')
tree2 = pyglet.sprite.Sprite(shorttree, x=550, y =125)
tree2.scale = 3

fire= pyglet.image.load('images/assets/ground/litfire.png')
deadfire= pyglet.image.load('images/assets/ground/deadfire.png')
hot = pyglet.sprite.Sprite(fire, x=950, y=500)
hot.scale = 2

player= pyglet.image.load('images/assets/girl/girl_stand.png')
playerleft= pyglet.image.load('images/assets/girl/girl_walk_left.png')
playerright= pyglet.image.load('images/assets/girl/girl_walk_right.png')
playerup= pyglet.image.load('images/assets/girl/girl_walk_up.png')
playerdown= pyglet.image.load('images/assets/girl/girl_walk_down.png')
play = pyglet.sprite.Sprite(player, x=875, y =500)
play.scale = 3

# Get the key state handler object
keys = pyglet.window.key.KeyStateHandler()

def update(dt):
    win.push_handlers(keys) # update the key object
    play.image = player
    if keys[pyglet.window.key.UP]:
        print("Moving Up")
        play.image = playerup
        play.y+=5
    if keys[pyglet.window.key.DOWN]:
        print("Moving Down")
        play.image = playerdown
        play.y-=5
    if keys[pyglet.window.key.LEFT]:
        print("Moving Left")
        play.image = playerleft
        play.x-=5
    if keys[pyglet.window.key.RIGHT]:
        print("Moving Right")
        play.image = playerright
        play.x+=5


@win.event
def on_draw():
    win.clear()
    #img.blit(200, 100)
    wet.draw()
    snow.draw()
    hot.draw()
    play.draw()
    tree1.draw()
    tree2.draw()
    timer.label.draw()
    draw_rect(50, 50, 400, 10)
    fall.draw()

timer = Timer()
pyglet.clock.schedule_interval(timer.update, 1)
pyglet.clock.schedule(update)
pyglet.app.run()