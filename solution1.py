#!/usr/bin/env python3

from manimlib import *



class Solution1(Scene):

    def construct(self):
        numbers = [3, 2, 10, 4, 8]
        numbers = [Tex(f"{i}") for i in numbers]

        var_T = Tex("T")
        desc_T = Text(": number of throws to get the first 6.")
        var_T.to_corner(LEFT)
        desc_T.next_to(var_T, RIGHT)
        self.add(var_T, desc_T)
        self.wait()
