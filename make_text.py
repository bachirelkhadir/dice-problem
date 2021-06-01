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
    text = Text("not the most exciting game", t2c={"exciting":BLUE_A})

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
            Text("to get two 6s in a row?", t2c=t2c))
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

class Sumkxk(TextScene):
    def construct(self):

        sigma = Tex(r"\sum_{\phantom{k}=1}^\infty")
        sigma_idx = Tex(r"k", color=YELLOW).scale(.7)
        sigma_idx.move_to(sigma.get_corner(DOWN)).shift(UP/10+.25*LEFT)
        sigma = VGroup(sigma, sigma_idx).shift(2*LEFT)

        summand = Tex(r" {{k}} \ x^{k-1} = \frac 1 {(1-x)^2}", tex_to_color_map={"k": YELLOW})
        hstack([sigma, summand], MED_SMALL_BUFF)

        self.play(Write(VGroup(sigma, summand)))
        self.wait()


class CaptionLLN(TextScene):
    text = Text("Law of Large Numbers", t2c={"Large": YELLOW})

class WhatIsMedian(TextScene):
    def construct(self):
        t2c = {"throws": YELLOW,
               "6": BLUE_A,
               "median": RED_A}
        self.text = text = VGroup(
            Text("What is the median number of throws", t2c=t2c),
            Text("required to get the first 6?", t2c=t2c),
            )
        text[1].shift(DOWN)

        for t in text:
            self.play(self.animate(t))
            self.wait()


class UnexpectedConsequence(TextScene):
    text = Text("unexpected consequence")

class Thankyou(TextScene):

    def construct(self):
        t2c = {
            "Thanks": YELLOW,
            "comments": BLUE_A,
        }
        text =vstack([Text(r"Thanks for watching", t2c=t2c),
                        Text("Share you answers in the comments!", t2c=t2c)])
        for t in text:
            self.add(t)
            self.wait()

class Current(ThirdWayQuestion):
    pass
