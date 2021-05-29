from manimlib import *

tex = lambda s: Tex(s, tex_to_color_map = {"p": YELLOW, "X": RED_A,
                                           "2": YELLOW, "H": RED_A})

class Coin(Group):
    CONFIG = {
        "disk_resolution": (4, 51),
        "height": 1,
        "depth": 0.1,
        "color": GOLD_D,
        "tails_color": RED,
        "include_labels": True,
        "numeric_labels": False,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        res = self.disk_resolution
        self.top = Disk3D(resolution=res, gloss=0.2)
        self.bottom = self.top.copy()
        self.top.shift(OUT)
        self.bottom.shift(IN)
        self.edge = Cylinder(height=2, resolution=(res[1], 2))
        self.add(self.top, self.bottom, self.edge)
        self.rotate(90 * DEGREES, OUT)
        self.set_color(self.color)
        self.bottom.set_color(RED)

        if self.include_labels:
            chars = "10" if self.numeric_labels else "HT"
            labels = VGroup(*[TexText(c) for c in chars])
            for label, vect in zip(labels, [OUT, IN]):
                label.shift(1.02 * vect)
                label.set_height(0.8)
            labels[1].rotate(PI, RIGHT)
            labels.apply_depth_test()
            labels.set_stroke(width=0)
            self.add(*labels)
            self.labels = labels

        #self.set_height(self.height)
        #self.set_depth(self.depth, stretch=True)

    def is_heads(self):
        return self.top.get_center()[2] > self.bottom.get_center()[2]

    def flip(self, axis=RIGHT):
        super().flip(axis)
        return self


class IntroducePuzzle(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }

    def construct(self):
        coin = Coin().shift(UP)
        self.add(coin)
        self.play(coin.animate.flip())
        self.play(coin.animate.flip())

class CoinToss(Scene):

    def construct(self):

        prob = tex(r"\mathbb P({{X}}) = p")
        exp = tex(r"\mathbb E[ \text{number of tries before } {{X}} ] = \frac {1}{\, p \,}")
        prob.to_corner(LEFT).shift(RIGHT+UP)
        exp.to_corner(RIGHT).shift(LEFT+UP)
        self.play(ShowCreation(prob))
        self.play(ShowCreation(exp))
        self.wait()

        coin = Coin(disk_resolution=(60, 60)).shift(DOWN)
        self.add(coin)
        self.wait()
        self.play(coin.animate.flip())
        self.play(coin.animate.flip())
        self.wait()

        H = tex("H").move_to(prob[1])
        half = tex(r"1/2").move_to(prob[-1]).shift(RIGHT/3)
        half_2 = tex(r"1/2").move_to(exp[3])
        eq_2 = tex(r"= 2").next_to(exp, RIGHT)
        self.play(Transform(prob[1], H))
        self.wait()

        self.play(Transform(prob[-1], half))
        self.wait()

        self.play(Transform(exp[3], half_2))
        self.wait()
        self.add(eq_2)
        self.wait()

        self.add(coin)
        self.wait()
        self.play(coin.animate.flip())
        self.play(coin.animate.flip())
        self.wait()
