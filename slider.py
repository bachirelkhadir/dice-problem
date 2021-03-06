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


def bounce_update(ball, dt, floor=0, eps=0.6):
    ball.velocity = ball.velocity + ball.acceleration * dt
    ball.shift(ball.velocity * dt)
    #Bounce off ground and roof
    if ball.get_bottom()[1] <= floor:
        ball.shift(-ball.get_bottom()[1]*UP)
        ball.velocity[1] = -(eps*ball.velocity[1])

class BouncingLabel(Scene):
    CONFIG = {
        "show_sol_3": True,
        "idx_sol": 1,
        "label": "Solution"
    }
    def construct(self):
        t2c = {
            "3": COLOR1,
            str(self.idx_sol): WHITE, # hack to isolate
            "1": COLOR1,
            "2": COLOR2
        }
        three_sol = Text(f"3 {self.label}s", t2c=t2c).scale(SCALE).to_corner(UP)
        three_sol = VGroup(*three_sol)
        sol = VGroup(*three_sol[1:-1]).copy()

        if self.show_sol_3:
            self.add(*three_sol)
        self.add(sol)
        #self.add(sol)
        #self.wait()

        dt = 1. / 60
        sol.velocity = 0*UP
        sol.acceleration = 10*DOWN
        if self.show_sol_3:
            self.play(FadeOut(three_sol), run_time=.5)
        sol.add_updater(bounce_update)
        self.wait(3)

        idx = Text(str(self.idx_sol)).scale(SCALE).next_to(sol).set_color(COLOR1)
        self.play(FadeIn(idx))
        self.wait()


class BouncingSolution1(BouncingLabel):
    CONFIG = {
        "show_sol_3": True,
        "idx_sol": 1,
        "label": "Solution"
    }

class BouncingSolution2(BouncingLabel):
    CONFIG = {
        "show_sol_3": False,
        "idx_sol": 2,
        "label": "Solution"
    }

class BouncingSolution3(BouncingLabel):
    CONFIG = {
        "show_sol_3": False,
        "idx_sol": 3,
        "label": "Solution"
    }


class BouncingQuestion1(BouncingLabel):
    CONFIG = {
        "show_sol_3": False,
        "idx_sol": 1,
        "label": "Question"
    }

class BouncingQuestion2(BouncingLabel):
    CONFIG = {
        "show_sol_3": False,
        "idx_sol": 2,
        "label": "Question"
    }

class BouncingQuestion3(BouncingLabel):
    CONFIG = {
        "show_sol_3": False,
        "idx_sol": 3,
        "label": "Question"
    }
