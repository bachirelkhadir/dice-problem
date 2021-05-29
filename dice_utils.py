#!/usr/bin/env python3
from manimlib import *#

def make_node(s, r=1.2):
    if type(s) == str:
        text = Text(s)
    else:
        text = s
    rect = Circle().scale(r)
    #rect.surround(text)
    return VGroup(text, rect)

def make_dice_face(i):
    dots = {
        6: VGroup(*[Dot().shift( (i-1) * DOWN/3 + (j-.5) * RIGHT/2).scale(1.1) for i in range(3) for j in range(2)])
    }
    sq = Square(1.2, fill_opacity=.8, fill_color=BLACK).round_corners(.25).move_to(dots[i])
    face = VGroup(sq, dots[i])
    return face
