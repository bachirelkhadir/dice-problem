#!/usr/bin/env python3

from manimlib import *
import numpy as np


COLOR_BAR = BLUE_A
COLOR_K = YELLOW


class ColorArea(Scene):
    def construct(self):
        axes = Axes((-4, 4), (-.1, 1))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        graph = axes.get_graph(
            lambda x: np.exp(-x*x/2)+2,
            color=BLUE,
        )
        label = axes.get_graph_label(graph, "\\sin(x)")
        #print(axes.get_riemann_rectangles(label,dx=0.5))

        self.play(
            ShowCreation(graph),
            FadeIn(label, RIGHT),
        )
        self.wait(2)
