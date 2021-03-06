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

        num_throws = 300
        frame = self.camera.frame
        frame.set_height(20)

        np.random.seed(10)
        games = np.random.randint(1, 7, num_throws)
        games = "".join(map(str, games)).split("6")
        dice = [
            string_to_dice(s+"6") for s in games
        ]

        vstack([ d for d in dice], SMALL_BUFF)
        VGroup(*dice).align_to(frame, UP).shift(DOWN)

        even_games = [d for g, d in zip(games, dice)
                      if len(set(g) & set("135")) == 0]

        odd_games = [d for g, d in zip(games, dice)
                      if len(set(g) & set("135")) != 0]

        self.play(ShowIncreasingSubsets(VGroup(*dice[:30])), run_time=3)
        self.add(*dice)
        self.wait()

        self.play(
            LaggedStartMap(
                FadeOut,
                VGroup(*odd_games),
                lambda m: (m, RIGHT)),
        )

        self.wait()

        even_games_stacked = [d.copy() for d in even_games]
        vstack(even_games_stacked, SMALL_BUFF)
        self.play(
            Transform(VGroup(*even_games), VGroup(*even_games_stacked))
        )
        return
