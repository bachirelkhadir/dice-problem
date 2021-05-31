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
            self.wait()        xaxis = Vector().scale(8)
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
