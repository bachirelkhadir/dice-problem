#!/usr/bin/env python3
from manimlib import *
exec(get_custom_config()["universal_import_line"])

import numpy as np
from dice_utils import make_dice_face
from common import vstack, hstack, halign

def hstack_fixed_width(obj, width, buff):
    vstack(obj[::width], buff)
    for i in range(len(obj) // width):
        hstack(obj[i*width:(i+1)*width], buff)


class QuestionOne(Scene):
    def construct(self):
        np.random.seed(0)
        game = np.random.randint(1, 7, 1000)[100:] # burn in to make seq nice
        game = "".join(map(str, game))
        first_66 = game.find("66")
        game = game[:first_66+2]
        first_6 = game.find("6")
        print("first 66:", first_66)
        print("first 6:", first_6)

        dice = VGroup(*map(lambda i: make_dice_face(int(i)), game))
        hstack_fixed_width(dice, 10, SMALL_BUFF)

        dice_until_6 = dice[:first_6+1]
        dice.to_edge(LEFT)
        self.add(dice_until_6)
