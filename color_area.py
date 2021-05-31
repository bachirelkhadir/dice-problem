#!/usr/bin/env python3

from manimlib import *

COLOR_BAR = BLUE_A
COLOR_K = YELLOW


class ColorArea(Scene):
    def construct(self):
        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        # Axes.get_graph will return the graph of a function
        sin_graph = axes.get_graph(
            lambda x: 2 * math.sin(x),
            color=BLUE,
        )
        # By default, it draws it so as to somewhat smoothly interpolate
        # between sampled points (x, f(x)).  If the graph is meant to have
        # a corner, though, you can set use_smoothing to False
        relu_graph = axes.get_graph(
            lambda x: max(x, 0),
            use_smoothing=False,
            color=YELLOW,
        )
        # For discontinuous functions, you can specify the point of
        # discontinuity so that it does not try to draw over the gap.
        step_graph = axes.get_graph(
            lambda x: 2.0 if x > 3 else 1.0,
            discontinuities=[3],
            color=GREEN,
        )

        # Axes.get_graph_label takes in either a string or a mobject.
        # If it's a string, it treats it as a LaTeX expression.  By default
        # it places the label next to the graph near the right side, and
        # has it match the color of the graph
        sin_label = axes.get_graph_label(sin_graph, "\\sin(x)")
        relu_label = axes.get_graph_label(relu_graph, Text("ReLU"))
        step_label = axes.get_graph_label(step_graph, Text("Step"), x=4)

        self.play(
            ShowCreation(sin_graph),
            FadeIn(sin_label, RIGHT),
        )
        self.wait(2)
