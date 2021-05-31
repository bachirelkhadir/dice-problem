#!/usr/bin/env python3


from manimlib import *
exec(get_custom_config()["universal_import_line"])
from dice_utils import make_dice_face
from common import vstack, hstack, halign

class TextScene(Scene):
    animate = Write

    def setup_text(self, text):
        text.to_corner(UL)
        self.play(self.animate(text))
        self.wait()

    def construct(self):
        self.setup_text(self.text)




class LetsPlay(TextScene):
    text = Text("Let's play a game...", t2c = {"game": YELLOW})


class NotTheMostExciting(TextScene):
    text = Text("Not the most exciting game.")

class OneThrowOneDollar(TextScene):
    text = Text("1 Throw = $1")

class ThirdWayQuestion(TextScene):
    def construct(self):
        t2c = {"throws": YELLOW,
               "6": BLUE_A,
               "average": RED_A}
        self.text = text = VGroup(
            Text("How many throws does it take,", t2c=t2c),
            Text("on average,", t2c=t2c),
            Text("to get a 6?", t2c=t2c))
        text[1].shift(DOWN)
        text[2].shift(2*DOWN)

        for t in text:
            self.play(self.animate(t))
            self.wait()


class TwoSixes(TextScene):
    def construct(self):
        t2c = {"throws": YELLOW,
               "6": BLUE_A,
               "average": RED_A}
        self.text = text = VGroup(
            Text("How many throws does it take,", t2c=t2c),
            Text("on average,", t2c=t2c),
            Text("to get a two 6s in a row?", t2c=t2c))
        text[1].shift(DOWN)
        text[2].shift(2*DOWN)

        for t in text:
            self.play(self.animate(t))
            self.wait()

class Conditional(TextScene):
    def construct(self):
        t2c = {"throw": RED_A,
               "T": YELLOW,}
        dice_2, dice_4, dice_6 =  [make_dice_face(i).scale(0.3) for i in (2,4,6)]
        lbrace =  Tex(r"\{ %}")
        rbrace =  lbrace.copy().rotate(PI)
        self.text = text = VGroup(
            *hstack([
                Tex(r"\mathbb E\left["),
                Tex("{{T}}", tex_to_color_map=t2c),
                Tex(r" | "),
                Text("every throw", t2c=t2c).scale(.7),
                Tex(r"\in "),
                lbrace,
                dice_2, Tex(r","),
                dice_4, Tex(r","),
                dice_6,
                rbrace,
                Tex(r"\right]"),
                Tex(r"?").scale(1.5),
                ],
                MED_SMALL_BUFF)
        )
        commas = VGroup(text[7], text[9]).shift(DOWN/5)

        part1 = text[:2]
        part2 = text[2:4]
        part3 = text[4:]
        text.to_edge(LEFT)

        for t in (part1, part2, part3):
            self.play(self.animate(t))
            self.wait()

class Current(ThirdWayQuestion):
    pass
