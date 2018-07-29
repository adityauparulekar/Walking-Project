import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
SPRITE_TORSO_SCALING = 1
SPRITE_FEMUR_SCALING = 0.8
SPRITE_CALF_SCALING = 0.6
SPRITE_FOOT_SCALING = 0.2

SPRITE_JOINT_SCALING = 0.5

TORSO_HEIGHT = 267
TORSO_WIDTH = 23

CIRCLE_RADIUS = 71

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.sprite_list = None
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

    def on_draw(self):

    def update(self, delta_time):

class Person():
    def __init__(self, dna):
        self.dna = dna

        torso_shape =
        self.torso = Body_parts("torso.png", )

class Body_parts(arcade.Sprite):
    def __init__(self, filename, pymunk_shape):
        super().__init__(filename, center_x=pymunk_shape.body.position.x, center=pymunk_shape.body.position.y)
        self.pymunk_shape = pymunk_shape
