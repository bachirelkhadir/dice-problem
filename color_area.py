#!/usr/bin/env python3

from manimlib import *
import numpy as np


COLOR_GRAPH = RED
COLOR_AREA= RED_A


def get_norm(vect):
    return sum([x**2 for x in vect])**0.5

def get_area_under_graph(ax, graph, x_range, dx):
    rects = []
    for sample in np.arange(*x_range, dx):
        height =  get_norm(
            ax.i2gp(sample, graph) - ax.c2p(sample, 0)
        ) - .1*graph.stroke_width
        rect = Rectangle(width=dx, height=height,
                         stroke_opacity=0,
                         fill_opacity=0.5,
                         fill_color=COLOR_AREA)
        rect.move_to(ax.c2p(sample, 0), DL)
        rects.append(rect)

    return VGroup(*rects)

class ColorArea(Scene):
    def construct(self):
        x_range = (-4, 4)
        axes = Axes(x_range, (-.1, 1))
        axes.add_coordinate_labels()

        # self.play(Write(axes, lag_ratio=0.01, run_time=1))

        graph = axes.get_graph(
            lambda x: np.exp(-x*x/2),
            color=COLOR_GRAPH
        )
        #label = axes.get_graph_label(graph, "\\sin(x)")

        self.play(
            ShowCreation(graph),
            #FadeIn(label, RIGHT),
        )
        #self.wait()
        self.play(Write(get_area_under_graph(axes, graph, x_range, .01), lag_ratio=0.01, run_time=1))
        self.wait()
