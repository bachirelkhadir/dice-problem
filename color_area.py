#!/usr/bin/env python3

from manimlib import *
import numpy as np


COLOR_BAR = BLUE_A
COLOR_K = YELLOW


class ColorArea(Axes):
    CONFIG = {
        "x_axis_label": "",
        "y_axis_label": "",
        "x_min": 0,
        "x_max": 15,

        "x_axis_width": 12,
        "y_min": 0,
        "y_max": 0.5,
        "y_axis_height": 6,
        "y_tick_frequency": 0.125,

        "graph_origin": 2.5 * DOWN + 5.5 * LEFT,
    }

    def construct(self):
        self.setup_axes()
        self.y_axis.add_numbers(
            0.25, 0.5, 0.75, 1,
            number_config={
                "num_decimal_places": 2,
            },
            direction=LEFT,
        )
        self.x_axis.add_numbers(*range(1, 15))

        graph = self.get_prior_graph()
        self.play(ShowCreation(graph), run_time=3)
        self.wait()

        #riemann rectangle
        rect = self.get_riemann_rectangles(graph, dx=0.2)
        rect.set_color(YELLOW_D)
        rect.set_stroke(WHITE, 1)

        self.play(ShowCreation(rect), run_time=5)
        self.wait()

    def get_prior_graph(self):
        def prior(x):
            return ((x ** 3 / 6) * np.exp(-x))

        return self.get_graph(prior)
