import arcade
import pymunk
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

TORSO_SCALING = 1
GRAVITY = -1
RESTITUTION = 0

TORSO_HEIGHT = 267
TORSO_WIDTH = 23
class BoxSprite(arcade.Sprite):
    def __init__(self, filename):
        super().__init__(filename, TORSO_SCALING)
        self.x_vel = 0
        self.y_vel = 0
        self.x_force = 0
        self.y_force = 0
        self.torque = 0
        self.angular_vel = 0
        self.impulse = 0
        self.angle = 0
        self.mass = 10
        self.length = TORSO_SCALING*TORSO_HEIGHT
        self.width = TORSO_SCALING*TORSO_WIDTH
        self.moment = self.mass*self.length*self.length / 12
        self.top_coords = [0,0]
        self.bottom_coords = [0,0]

    def update(self):
        self.center_x += self.x_vel
        self.center_y += self.y_vel
        self.angle += self.angular_vel

        if self.bottom <= -1:
            self.bottom = 0
        self.top_coords = [self.center_x - (TORSO_HEIGHT*TORSO_SCALING*0.5*math.sin(math.radians(self.angle)))
                            , self.center_y + (TORSO_HEIGHT*TORSO_SCALING*0.5*math.cos(math.radians(self.angle)))]
        self.bottom_coords = [self.center_x + (TORSO_HEIGHT*TORSO_SCALING*0.5*math.sin(math.radians(self.angle)))
                            , self.center_y - (TORSO_HEIGHT*TORSO_SCALING*0.5*math.cos(math.radians(self.angle)))]

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.sprite_list = None
        arcade.set_background_color(arcade.color.AMAZON)


    def setup(self):
        self.sprite_list = arcade.SpriteList()

        torso = BoxSprite("torso.png")
        torso.center_x = 400
        torso.center_y = 800
        torso.x_vel = 0
        torso.y_force = GRAVITY*torso.mass
        torso.angle = 132

        self.sprite_list.append(torso)

    def on_draw(self):
        arcade.start_render()
        self.sprite_list.draw()

    def update(self, delta_time):
        self.sprite_list.update()

        for sprite in self.sprite_list:
            if sprite.bottom_coords[1] <= 0:
                imp_x = sprite.x_vel + (sprite.length * sprite.angular_vel * math.sin(math.radians(sprite.angle)) / 2)
                imp_y = sprite.y_vel + (sprite.length * sprite.angular_vel * math.cos(math.radians(sprite.angle)) / 2)
                sprite.x_vel -= imp_x
                sprite.y_vel -= imp_y
                sprite.y_force -= sprite.mass*GRAVITY
            sprite.y_vel += sprite.y_force/sprite.mass
            sprite.x_vel += sprite.x_force/sprite.mass
            sprite.angular_vel -= sprite.torque/sprite.moment

def main():
    game = MyGame()
    #game.set_update_rate(1/6)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
