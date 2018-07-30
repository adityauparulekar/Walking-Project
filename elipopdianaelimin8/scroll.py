import arcade
import pymunk
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

TORSO_SCALING = 1
GRAVITY = -1
RESTITUTION = 0

TORSO_LENGTH = 267
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
        self.angle = 0
        self.mass = 10
        self.length = TORSO_SCALING*TORSO_LENGTH
        self.width = TORSO_SCALING*TORSO_WIDTH
        self.moment = self.mass*self.length*self.length / 12
        self.top_right = [0,0]
        self.top_left = [0,0]
        self.bottom_right = [0,0]
        self.bottom_left = [0,0]

    def update(self):
        self.center_x += self.x_vel
        self.center_y += self.y_vel
        self.angle += self.angular_vel

        if self.bottom <= -1:
            self.bottom = 0



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
            if sprite.bottom <= 0:
                sprite.y_force = 0
                sprite.torque += sprite.mass * GRAVITY * sprite.length / 2 * math.cos(math.radians(sprite.angle))
                #print(sprite.torque)
                if sprite.angle < 91 and sprite.angle > 89:
                    sprite.torque = 0
                    sprite.angular_vel = 0
                    sprite.angle = 90
                if sprite.angle < 271 and sprite.angle > 269:
                    sprite.torque = 0
                    sprite.angular_vel = 0
                    sprite.angle = 270
            sprite.y_vel += sprite.y_force/sprite.mass
            sprite.x_vel += sprite.x_force/sprite.mass
            sprite.angular_vel -= sprite.torque/sprite.moment
            #print(sprite.angular_vel)
            #print(sprite.angle)
            #print(sprite.torque)
            #print("")


def main():
    game = MyGame()
    #game.set_update_rate(1/6)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
