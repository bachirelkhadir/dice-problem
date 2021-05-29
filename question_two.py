#!/usr/bin/env python3

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

    hstack(obj[(i+1)*width:], buff)

def string_to_dice(game):
    game = map(int, game)
    game = map(make_dice_face, game)
    game = hstack([*game], SMALL_BUFF)
    game = VGroup(*game, )
    return game


class QuestionTwo(Scene):

    def construct(self):

        num_throws = 100
        frame = self.camera.frame
        frame.set_height(20)

        np.random.seed(1)
        games = np.random.randint(1, 7, num_throws)# burn in to make seq nice
        games = "".join(map(str, games)).split("6")
        dice = [
            string_to_dice(s+"6") for s in games
        ]

        vstack([ d for d in dice], SMALL_BUFF)

        even_games = [d for g, d in zip(games, dice)
                      if len(set(g) & set("135")) == 0]

        odd_games = [d for g, d in zip(games, dice)
                      if len(set(g) & set("135")) == 0]

        self.play(ShowIncreasingSubsets(VGroup(*dice)))
