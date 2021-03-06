#!/usr/bin/env python3

#!/usr/bin/env python3

from manimlib import *
exec(get_custom_config()["universal_import_line"])
import numpy as np
from dice_utils import make_dice_face
from common import vstack, hstack, halign

class EquallyLikely(Scene):
    def construct(self):
        dice =[
            make_dice_face(i) for i in range(1, 7)
        ]
        dice[0].to_edge(LEFT)
        hstack(dice)
        probs = [
            Tex(r"\frac 1 6").next_to(d, UP)
            for d in dice
        ]
        self.play(Write(VGroup(*dice), lagged_start=0.01), run_time=1)
        self.play(LaggedStartMap(
            FadeIn,
            VGroup(*probs,),
            lambda m: (m, DOWN)
        ))

class Not6Then6(Scene):
    CONFIG = {
        "stroke_color": YELLOW_D,
        "stroke_width": 10,
        "num_not_six": 1,
    }

    def construct(self):
        dice = [make_dice_face(6) for _ in range(self.num_not_six+1)]
        hstack(dice)

        for i in range(self.num_not_six):
            not_six = VGroup(Cross(dice[i],), dice[i])
            not_six[0].set_stroke(self.stroke_color, self.stroke_width)

            self.add(dice[i])
            self.play(FadeIn(not_six[0]))
            self.wait()

        self.add(dice[-1])
        self.wait()

class Not6Not6Then6(Not6Then6):
    CONFIG = {
        "num_not_six": 2,
    }
