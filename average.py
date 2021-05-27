#!/usr/bin/env python3
from manimlib import *

SCALE = 1.5
COLOR1 = YELLOW

class Average(Scene):
    def construct(self):
        numbers = [3, 2, 10, 4, 8]
        texts = [
            Tex(f"{i}\$").scale(SCALE) for i in numbers
        ]
        texts[0].to_corner(UR)
        for t1, t2 in zip(texts, texts[1:]):
            t2.next_to(t1, DOWN, LARGE_BUFF)

        for t in texts:
            self.add(t)
            self.wait(.25)

        copy_texts = [
            t.copy() for t in texts
        ]

        copy_texts[0].to_corner(LEFT).shift(3*DOWN+RIGHT)
        for t1, t2 in zip(copy_texts, copy_texts[1:]):
            t2.next_to(t1, RIGHT, LARGE_BUFF)


        self.play(*[Transform(t, tt) for t, tt in zip(texts, copy_texts)])

        plus = [Tex("+").scale(SCALE).next_to(t, RIGHT).set_color(COLOR1) for t in texts[:-1]]
        fraction = Line(LEFT, RIGHT).surround(VGroup(*texts)).shift(DOWN/2).set_color(COLOR1)
        five = Tex("5").scale(SCALE).next_to(fraction, DOWN)
        avg = Tex(f"\\approx {sum(numbers)/5:.2f}...").scale(SCALE).next_to(fraction, RIGHT)

        self.add(*plus)
        self.add(fraction, five)
        self.add(avg)
        self.wait()
