#!/usr/bin/env python3

from manimlib import *
import numpy as np


COLOR_BAR = BLUE_A
COLOR_K = YELLOW


def get_norm(vect):
    return sum([x**2 for x in vect])**0.5

def get_area_under_graph(ax, graph, x_range, dx):
    rects = []
    for sample in np.linspace(*x_range, dx):
        height = get_norm(
            self.i2gp(sample, graph) - self.c2p(sample, 0)
        )
        rect = Rectangle(width=x1 - x0, height=height)
        rect.move_to(axes.c2p(x0, 0), DL)
        rects.append(rect)

    return VGroup(*rects)

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

        self.play(
            ShowCreation(graph),
            FadeIn(label, RIGHT),
        )
        self.add(get_area_under_graph(axes, graph))
        self.wait(2)
