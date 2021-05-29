#!/usr/bin/env python3
from manimlib import *
exec(get_custom_config()["universal_import_line"])

from dice_utils import make_dice_face
import numpy as np

class QuestionOne(Scene):
    def construct(self):
        game = np.random.randint(1, 7, 1000)
        game = "".join(map(str, game))
        i = game.find("66")
        game = [*map(int, game[:i+2])]
        first_six = game.find("6")
        print(game)
        self.add(make_dice_face(1))
