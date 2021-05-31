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
        num_coins = 100
        width = 20

        coin1 = Coin().shift(UP)
        np.random.seed(11)

        coin_template = Coin().scale(.1*OUT+UR).scale(.2)
        coins = [coin_template.copy() for _ in range(num_coins)]
        heads = [coin for coin in coins if np.random.randn() >= 0]
        tails = [coin for coin in coins if coin not in heads]

        print(f"heads: {len(heads)}({len(coins)})")

        # center
        coins[0].to_edge(LEFT).shift(1.65*RIGHT).shift(DOWN/2)
        hstack_fixed_width(coins, width, SMALL_BUFF)



        self.add(coin1)
        self.wait()
        self.play(coin1.animate.flip())
        self.wait()
        self.play(coin1.animate.flip())
        self.wait()

        self.play(LaggedStart(*[TransformFromCopy(coin1, coin) for  coin in coins],
                              run_time=1))
        self.wait()

        self.play(*[coin.animate.flip() for coin in tails],)
        #self.play(*[coin.animate.flip() for coin in heads],)

        self.wait()


        # push head to the left and tail to the right
        heads_target = [coin.copy() for coin in heads]
        heads_target[0].move_to(coins[0])
        hstack_fixed_width(heads_target, width // 2, SMALL_BUFF)



        tails_target = [coin.copy() for coin in tails]
        tails_target[0].move_to(coins[width//2])
        hstack_fixed_width(tails_target, width // 2, SMALL_BUFF)

        self.play(
            *[Transform(coin, coin_target) for
            coin, coin_target in zip(heads+tails, heads_target+tails_target)])
        self.wait()

        # add brace with 50 %
        heads_group = heads[0]
        for coin in heads[1:]:
            heads_group.add(coin)
        brace1 = Brace(heads_group)
        fifty = Tex(r"\sim 50\%").next_to(brace1, DOWN)
        brace1 = VGroup(brace1, fifty)
        brace2 = brace1.copy().shift(-2*brace1.get_center()[0]*RIGHT)

        self.play(FadeIn(VGroup(brace1, brace2)))
        self.wait()

class ApproximationGetsBetter(Scene):
    def construct(self):
        angle = PI/3
        num_games = Text("# games").to_edge(LEFT)
        inc = Arrow().scale(.7).rotate(angle)
        hstack([num_games, inc], MED_SMALL_BUFF)
        self.add(num_games, inc)

        approx = Text("Approximation error")
        dec = inc.copy()
        dec.rotate(-2*angle)
        hstack([approx, dec])
        self.add(approx, dec)
        pass
