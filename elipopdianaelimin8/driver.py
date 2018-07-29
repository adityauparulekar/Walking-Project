
import arcade
import pymunk
import timeit
import math

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800


class PhysicsSprite(arcade.Sprite):
    def __init__(self, pymunk_shape, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling, center_x=pymunk_shape.body.position.x, center_y=pymunk_shape.body.position.y)
        self.pymunk_shape = pymunk_shape


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)

        # -- Pymunk
        self.space = pymunk.Space()
        self.space.gravity = (0.0, -900.0)

        # Lists of sprites or lines
        self.sprite_list = arcade.SpriteList()
        self.static_lines = []

        self.draw_time = 0
        self.processing_time = 0

        # Create the floor
        floor_height = 100
        floor_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        floor_shape = pymunk.Segment(floor_body, [0, floor_height], [SCREEN_WIDTH, floor_height], 0.0)
        floor_shape.friction = 10
        self.space.add(floor_shape)
        self.static_lines.append(floor_shape)

        torso_mass = 100
        torso_length = 50
        thigh_mass = 50
        thigh_length = 25
        shin_mass = 30
        shin_length = 25
        foot_mass = 10
        foot_length = 5

        #torso
        torso_moment = pymunk.moment_for_segment(torso_mass, (0, 0), (0, torso_length), 3)
        torso_body = pymunk.Body(torso_mass, torso_moment)
        torso_body.position = pymunk.Vec2d(300, 500)
        torso_shape = pymunk.Poly.create_box(torso_body, (10, 100))
        self.space.add(torso_body, torso_shape)
        torso_sprite = PhysicsSprite(torso_shape, "torso.png", 1)
        self.sprite_list.append(torso_sprite)

        #thigh
        thigh_moment = pymunk.moment_for_segment(thigh_mass, (0, 0), (0, thigh_length), 3)

        l_thigh_body = pymunk.Body(thigh_mass, thigh_moment)
        l_thigh_body.position = pymunk.Vec2d(300, 300)
        l_thigh_shape = pymunk.Poly.create_box(l_thigh_body, (10, 100))
        self.space.add(l_thigh_body, l_thigh_shape)
        l_thigh_sprite = PhysicsSprite(l_thigh_shape, "torso.png", 0.5)
        self.sprite_list.append(l_thigh_sprite)

        r_thigh_body = pymunk.Body(thigh_mass, thigh_moment)
        r_thigh_body.position = pymunk.Vec2d(300, 300)
        r_thigh_shape = pymunk.Poly.create_box(r_thigh_body, (10, 100))
        self.space.add(r_thigh_body, r_thigh_shape)
        r_thigh_sprite = PhysicsSprite(r_thigh_shape, "torso.png", 0.5)
        self.sprite_list.append(r_thigh_sprite)

        #j = pymunk.PinJoint(l_thigh_body, torso_body)
        #self.space.add(j)


    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Start timing how long this takes
        draw_start_time = timeit.default_timer()

        # Draw all the sprites
        self.sprite_list.draw()

        # Draw the lines that aren't sprites
        for line in self.static_lines:
            body = line.body
            pv1 = body.position + line.a.rotated(body.angle)
            pv2 = body.position + line.b.rotated(body.angle)
            arcade.draw_line(pv1.x, pv1.y, pv2.x, pv2.y, arcade.color.WHITE, 2)

        # Display timings
        output = f"Processing time: {self.processing_time:.3f}"
        arcade.draw_text(output, 20, SCREEN_HEIGHT - 20, arcade.color.WHITE, 12)

        output = f"Drawing time: {self.draw_time:.3f}"
        arcade.draw_text(output, 20, SCREEN_HEIGHT - 40, arcade.color.WHITE, 12)

        self.draw_time = timeit.default_timer() - draw_start_time


    def update(self, delta_time):
        start_time = timeit.default_timer()


        # Update physics
        # Use a constant time step, don't use delta_time
        # See "Game loop / moving time forward"
        # http://www.pymunk.org/en/latest/overview.html#game-loop-moving-time-forward
        self.space.step(1 / 60.0)


        # Move sprites to where physics objects are
        for sprite in self.sprite_list:
            sprite.center_x = sprite.pymunk_shape.body.position.x
            sprite.center_y = sprite.pymunk_shape.body.position.y
            sprite.angle = math.degrees(sprite.pymunk_shape.body.angle)
            print(sprite.center_y)

        # Save the time it took to do this.
        self.processing_time = timeit.default_timer() - start_time


def main():
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)

    arcade.run()


if __name__ == "__main__":
    main()
