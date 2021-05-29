#!/usr/bin/env python3
from manimlib import *
exec(get_custom_config()["universal_import_line"])

from dice_utils import make_dice_face
import numpy as np

class QuestionOne(Scene):
    def construct(self):
        np.random.seed(0)
        game = np.random.randint(1, 7, 1000)
        game = "".join(map(str, game))
        i = game.find("66")
        game = game[:i+2]
        first_six = game.find("6")

        dice = VGroup(*map(lambda i: make_dice_face(int(i)), game))
        hstack(dice, SMALL_BUFF)
        self.add(dice)
