#!/usr/bin/env python3


from manimlib import *


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
    text = Text("Not the most exciting.")

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


class ThirdWayQuestion(TextScene):
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

class Current(ThirdWayQuestion):
    pass
