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
    return VGroup(*hstack(map(lambda s: make_dice_face(int(i)), game)))

class QuestionTwo(Scene):

    def construct(self):

        frame = self.camera.frame

        np.random.seed(1)
        games = np.random.randint(1, 7, 1000)# burn in to make seq nice
        games = "".join(map(str, games)).split("6")
        even_games = [g+"6" for g in games if len(set(g) & set("135")) == 0]
        odd_games = [g+"6" for g in games if len(set(g) & set("135")) != 0]
        print("even:", even_games)
        print("odd:", odd_games)

        even_dice = [
            string_to_dice(s) for s in even_games
        ]
        self.add(*even_dice)
