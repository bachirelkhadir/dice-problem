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

    def construct(self):
        dice = make_dice_face(6)
        not_six = dice
