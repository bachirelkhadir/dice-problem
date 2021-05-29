#!/usr/bin/env python3
from manimlib import *
exec(get_custom_config()["universal_import_line"])

import numpy as np
from dice_utils import make_dice_face
from common import vstack, hstack, halign

class QuestionOne(Scene):
    def construct(self):
        np.random.seed(1)
        game = np.random.randint(1, 7, 1000)
        game = "".join(map(str, game))
        first_66 = game.find("66")
        game = game[:first_66+2]
        first_six = game.find("6")
        print("first 66:", first_66)
        print("first 6:", first_6)

        dice = VGroup(*map(lambda i: make_dice_face(int(i)), game))
        hstack(dice, SMALL_BUFF)
        dice.to_edge(LEFT)
        self.add(dice)
