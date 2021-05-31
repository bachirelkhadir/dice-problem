#!/usr/bin/env python3

from manimlib import *

COLOR_BAR = BLUE_A
COLOR_K = YELLOW


class ColorArea(Scene):
    CONFIG = {
            "x_min" : 0,
            "x_max" : 5,
            "y_min" : 0,
            "y_max" : 6,
            "y_tick_frequency" : 1,
            "x_tick_frequency" : 1,
            "x_labeled_nums" : [0,2,3]
        }
    def construct(self):
        self.setup_axes(animate=False)
        curve1 = self.get_graph(lambda x : 4*x-x**2, x_min=0,x_max=4)
        curve2 = self.get_graph(lambda x : 0.8*x**2-3*x+4, x_min=0,x_max=4)
        line1 = self.get_vertical_line_to_graph(2,curve1,DashedLine,color=YELLOW)
        line2 = self.get_vertical_line_to_graph(3,curve1,DashedLine,color=YELLOW)

        area = self.get_area(curve2,2,3,bounded=curve1)

        self.play(ShowCreation(curve1), ShowCreation(curve2),
            ShowCreation(line1), ShowCreation(line2))
        self.play(ShowCreation(area))
        self.wait()
