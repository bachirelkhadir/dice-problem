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

class QuestionOne(Scene):
    def construct(self):

        frame = self.camera.frame

        np.random.seed(0)
        game = np.random.randint(1, 7, 1000)[100:] # burn in to make seq nice
        game = "".join(map(str, game))
        first_66 = game.find("66")
        game = game[:first_66+2]
        first_6 = game.find("6")
        print("first 66:", first_66)
        print("first 6:", first_6)
        print(game)

        dice = VGroup(*map(lambda i: make_dice_face(int(i)), game))
        hstack_fixed_width(dice, 10, SMALL_BUFF)

        dice_until_6 = dice[:first_6+1]
        dice_after_6 = dice[first_6+1:]

        # show until 6
        frame.move_to(dice_until_6)
        self.play(ShowIncreasingSubsets(dice_until_6, ))
        self.play(Indicate(dice_until_6[-1]))
        self.wait()



        # zoom out and show until 66
        frame_copy = frame.copy().set_height(16).move_to(dice)
        self.play(ShowIncreasingSubsets(dice_after_6, ),
                  Transform(frame, frame_copy))

        self.play(Indicate(dice_until_66[-2:]))
        self.wait()

        #self.add(dice_after_6)
