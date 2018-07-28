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

class my_person(self):
    def __init__(self, dna):
        self.dna = dna

        self.torso = arcade.Sprite("torso.png", SPRITE_TORSO_SCALING)
        self.right_femur = arcade.Sprite("torso.png", SPRITE_FEMUR_SCALING)
        self.left_femur = arcade.Sprite("torso.png", SPRITE_FEMUR_SCALING)
        self.right_calf = arcade.Sprite("torso.png", SPRITE_CALF_SCALING)
        self.left_calf = arcade.Sprite("torso.png", SPRITE_CALF_SCALING)
        self.right_foot = arcade.Sprite("torso.png", SPRITE_FOOT_SCALING)
        self.left_foot = arcade.Sprite("torso.png", SPRITE_FOOT_SCALING)

        self.head = arcade.Sprite("circle.png", SPRITE_JOINT_SCALING)
        self.hip = arcade.Sprite("circle.png", SPRITE_JOINT_SCALING)
        self.right_knee = arcade.Sprite("circle.png", SPRITE_JOINT_SCALING)
        self.left_knee = arcade.Sprite("circle.png", SPRITE_JOINT_SCALING)
        self.right_ankle = arcade.Sprite("circle.png", SPRITE_JOINT_SCALING)
        self.left_ankle = arcade.Sprite("circle.png", SPRITE_JOINT_SCALING)

        self.torso.center_x = 
