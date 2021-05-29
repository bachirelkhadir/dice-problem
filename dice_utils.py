#!/usr/bin/env python3
from manimlib import *#




def make_dice_face(i):
    dot = lambda: Dot().scale(1.1)
    dots = {
        1: dot(),
        2: VGroup(*[dot().shift(DL/3), dot().shift(UR/3)]),
        3: VGroup(*[dot().shift(UL/3), dot(), dot().shift(DR/3)]),
        4: VGroup(*[dot().shift((i*UP+j*LEFT)/3) for i in (-1, 1) for j in (-1, 1)]),
        5: VGroup(*[dot().shift((i*UP+j*LEFT)/3) for i in (-1, 1) for j in (-1, 1)], dot()),
        6: VGroup(*[dot().shift( (i-1) * DOWN/3 + (j-.5) * RIGHT/2) for i in range(3) for j in range(2)])
    }
    sq = Square(1.2, fill_opacity=.8, fill_color=BLACK).round_corners(.25).move_to(dots[i])
    face = VGroup(sq, dots[i])
    face.value = i
    return face
