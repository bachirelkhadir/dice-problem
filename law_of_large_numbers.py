#!/usr/bin/env python3

#!/usr/bin/env python3
from manimlib import *
exec(get_custom_config()["universal_import_line"])
import numpy as np
from dice_utils import make_dice_face
from common import vstack, hstack, halign, hstack_fixed_width
from coin_utils import Coin


class LawLargeNumbers(Scene):
    def construct(self):
        X = Tex("X")
        X.shift(UP)
        self.play(Write(X))
        self.wait()

        # X1, X2, X3, X4, ..., X_n
        colors = [BLUE_A, YELLOW, GOLD_A, MAROON_A, PURPLE_A]
        Xis = [Tex("X_{%s}" % i).set_color(c) for i, c in zip([1, 2, 3, 4, "n"],
                                              colors)]
        Xis.insert(-1, Tex("..."))
        # centering
        VGroup(*hstack(Xis)).move_to(0).shift(LEFT+DOWN)
        self.play(LaggedStart(*[TransformFromCopy(X, Xi) for Xi in Xis]))
        self.wait()

        # take sum
        plus = [Tex("+").next_to(Xi, RIGHT) for Xi in Xis[:-1]]

        # divide by n
        frac = Line().surround(VGroup(*Xis))
        denom = Tex("n")
        frac.shift(DOWN/3)
        denom.next_to(frac, DOWN)

        # E[X]
        exp_X = Tex(r"\longrightarrow \mathbb E[X]")
        exp_X.next_to(frac, RIGHT)

        self.play(ShowCreation(VGroup(*plus, frac, denom, exp_X)))
        self.wait()

class LLNWithCoins(Scene):
    def construct(self):
        num_coins = 10 # 50
        width = 5 # 10
        coin1 = Coin().shift(UP)
        np.random.seed(0)

        self.add(coin1)

        coins = [Coin().scale(.1*OUT+UR).scale(.2) for _ in range(num_coins)]
        heads = np.random.choice(coins, size=num_coins//2)
        coins[0].to_edge(LEFT).shift(DOWN)
        #hstack(coins, SMALL_BUFF)
        hstack_fixed_width(coins, width, SMALL_BUFF)
        self.add(*coins)

        self.play(*[coin.animate.flip() for coin in coins])
