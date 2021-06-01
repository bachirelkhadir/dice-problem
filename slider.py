#!/usr/bin/env python3

#!/usr/bin/env python3
from manimlib import *

SCALE = 1.5
COLOR1 = YELLOW
COLOR2 = BLUE_A
COLOR3 = RED_A

class Slider(Scene):
    def construct(self):
        t2c = {
            "3": COLOR1
        }
        three_sol = Text("3 Solutions", t2c=t2c).scale(SCALE).to_corner(UP)

        computational = Text("Straightforward,\ncomputational", color=COLOR2).scale(.6)
        elegant = Text("Elegant", color=COLOR3).scale(.6)


        self.add(three_sol)
        self.wait()

        slider = Line(stroke_width=10).scale(3)
        handle = Circle(color=WHITE).scale(0.3)

        left_slider = Line(stroke_width=10, color=COLOR3).scale(1.5)
        right_slider = Line(stroke_width=10, color=COLOR2).scale(1.5)
        left_slider.next_to(handle, LEFT)
        right_slider.next_to(handle, RIGHT)

        computational.next_to(slider, LEFT, LARGE_BUFF)
        elegant.next_to(slider, RIGHT, LARGE_BUFF)

        self.add(handle)
        self.add(left_slider)
        self.add(right_slider)

        def get_updater(d=LEFT):
            def updater(m):
                start = slider.get_corner(d)
                end = handle.get_corner(d)
                width = d[0] * (start - end)[0]
                if width < 0:
                    return
                m.set_width(width)
                m.next_to(handle, d)
            return updater

        left_slider.add_updater(get_updater(LEFT))
        right_slider.add_updater(get_updater(RIGHT))

        self.play(
            handle.animate.move_to(slider.get_corner(LEFT)+RIGHT/2)
        )

        self.add(computational)

        self.wait()
        self.play(
            handle.animate.move_to(slider.get_corner(RIGHT)+LEFT/2)
        )
        self.wait()
        self.add(elegant)

        self.wait()


class BouncingSolution(Slider):
    def construct(self):
        t2c = {
            "3": COLOR1,
            "Solution": WHITE, # hack to isolate
        }
        three_sol = Text("3 Solutions", t2c=t2c).scale(SCALE).to_corner(UP)

        sol = three_sol[1:-1]
        self.add(sol)
        self.wait()
        dt =self.frame_duration / number_of_computations_per_frame
        ball =self.ball
        box =self.box
        for i inrange(0,number_of_computations_per_frame):#Update ball
            ball.acceleration = np.array((0, -5, 0))
            ball.velocity = ball.velocity + ball.acceleration * dt                ball.shift(ball.velocity * dt)
            #Bounce off ground and roof
            if ball.get_bottom() <= box.bottom or ball.get_top() >=box.top:
                ball.velocity[1] =- ball.velocity[1]
