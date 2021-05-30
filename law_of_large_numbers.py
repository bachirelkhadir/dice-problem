#!/usr/bin/env python3

#!/usr/bin/env python3
from manimlib import *
exec(get_custom_config()["universal_import_line"])
import numpy as np
from dice_utils import make_dice_face
from common import vstack, hstack, halign


class LawLargeNumbers(Scene):
    def construct(self):
        X = Tex("X")
        X.shift(UP)
        self.add(X)

        # X1, X2, X3, X4, ..., X_n
        Xis = [Tex("X_{%s}" % i) for i in [1, 2, 3, 4, "n"]]
        Xis.insert(-1, Tex("..."))
        # centering
        VGroup(*hstack(Xis)).move_to(0)
        self.play(LaggedStart(*[TransformFromCopy(X, Xi) for Xi in Xis]))
        self.wait()

        # take sum
        plus = [Tex("+").next_to(Xi, RIGHT) for Xi in Xis[:-1]]
        self.add(*plus)
        self.wait()

        # divide by n
        frac = Line().surround(VGroup(*Xis))
        denom = Tex("n")
        frac.shift(DOWN/3)
        denom.next_to(frac, DOWN)
        self.add(frac)
        self.add(denom)
        self.wait()

        # E[X]
        exp_X = Tex(r"\longrightarrow \mathbb E[X]")
        exp_X.next_to(Xis[-1], RIGHT)
        self.add(exp_X)

        self.wait()
