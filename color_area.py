#!/usr/bin/env python3

from manimlib import *

COLOR_BAR = BLUE_A
COLOR_K = YELLOW


class ColorArea(Scene):
    def construct(self):
        xaxis = Vector().scale(8)
        yaxis = Vector(UP).scale(5)
        xaxis.shift(2*DOWN)
        yaxis.shift(3*LEFT)

        lab_k = Tex("k").next_to(xaxis, RIGHT).set_color(COLOR_K)
        lab_p = Tex(r"\mathbb P(T = {{k}})",
                    tex_to_color_map = {"k": COLOR_K}
                    ).next_to(yaxis, UP)
        ytick = Line(color=YELLOW).scale(.1)
        xtick = ytick.copy().rotate(PI/2)

        # xticks
        xtick.move_to(yaxis).shift(2.5*DOWN+RIGHT)
        step = 0.7 * RIGHT
        num_ticks = 9
        ticks_with_labels = []
        for k in range(num_ticks):
            tick = xtick.copy().shift(k*step)
            label = Tex(f"{k+1}").next_to(tick, DOWN)
            ticks_with_labels.append(VGroup(tick, label))

        # bars
        bars = []
        sizes = [ 1/6 * (5/6)**k for k in range(num_ticks) ]
        bar0 = Line(stroke_width=20, color=COLOR_BAR).rotate(PI/2)
        for s, (t, _) in zip(sizes, ticks_with_labels,):
            bar = bar0.copy().scale(s * 10).next_to(t, UP)
            bars.append(bar)







        self.play(
            Write(xaxis),
        )

        self.play(
            ShowCreation(VGroup(*ticks_with_labels))
        )
        self.play(ShowCreation(lab_k))
        self.wait()

        self.play(ShowCreation(yaxis))
        self.play(ShowCreation(lab_p))
        self.wait()

        self.play(ShowCreation(VGroup(*bars)))
        self.wait()
