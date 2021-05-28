#!/usr/bin/env python3

from manimlib import *

TEXT_SCALE = .8

def vstack(objs, buff=LARGE_BUFF):
    for t1, t2 in zip(objs, objs[1:]):
        t2.next_to(t1, DOWN, buff)
    return objs

def hstack(objs, buff=LARGE_BUFF):
    for t1, t2 in zip(objs, objs[1:]):
        t2.next_to(t1, RIGHT, buff)
    return objs
def halign(objs):
    for t in objs[1:]:
        t.align_to(objs[0])
    return objs

tex_fn = lambda s: Tex(s, tex_to_color_map={"k": YELLOW})\
                                .scale(TEXT_SCALE)

class SolutionOne(Scene):

    def construct(self):
        numbers = [3, 2, 10, 4, "..."]
        numbers = [Tex(f"{i}").scale(TEXT_SCALE) for i in numbers]
        var_T = Tex("T").scale(TEXT_SCALE)
        desc_T = Text(": number of throws to get the first 6.").scale(TEXT_SCALE)

        vstack(numbers, LARGE_BUFF)
        var_T.to_corner(LEFT)
        desc_T.next_to(var_T, RIGHT)
        VGroup(*numbers).shift(-numbers[2].get_center())

        arr_T_numbers = [
            CurvedArrow(var_T.get_corner(RIGHT)+RIGHT, n.get_corner(LEFT)+LEFT/3,
                        angle = (i-2)*PI/10)
            for i, n in enumerate(numbers)
        ]

        # desc T
        self.add(var_T)
        self.play(ShowCreation(desc_T))
        self.wait()

        # realizations of T
        self.remove(desc_T)
        self.play(ShowCreation(VGroup(*arr_T_numbers)))
        self.play(ShowCreation(VGroup(*numbers)))

        self.wait()

        # make expectation appear
        var_T_save = var_T.copy()
        exp_T = Tex(r"\mathbb E[T]").scale(TEXT_SCALE).move_to(var_T)
        self.remove(*numbers)
        self.remove(*arr_T_numbers)
        self.play(Transform(var_T, exp_T))
        self.wait()

        self.play(Indicate(var_T))
        self.wait()

        # T = 1, 2, 3
        one_two_etc = Tex(r" = 1, 2, 3, \ldots").scale(TEXT_SCALE)
        one_two_etc.next_to(var_T_save, RIGHT)
        self.play(Transform(var_T, var_T_save),
                  ShowCreation(one_two_etc), run_time=0.01)
        self.wait()
        self.remove(one_two_etc)

        # P(T = k)
        probs = [
            Tex(("\\mathbb P(T = {{%s}})" % i)).scale(TEXT_SCALE)if i else Tex("{{\\ldots}}") for i in [1, 2, 3, "", "k"]
        ]
        for p, n in zip(probs, numbers):
            if len(p) > 1:
                p[1].set_color(YELLOW)
            p.move_to(n).shift(RIGHT)
        halign(probs)

        # keep track of rhs so we can remove it later
        rhs_obj = []

        # P(T = 1)
        equal = Tex("=").scale(TEXT_SCALE)
        one_sixth = Tex(r"\frac 1 6").scale(TEXT_SCALE)
        five_sixth = Tex(r"\frac 5 6").scale(TEXT_SCALE)
        equal.next_to(probs[0], RIGHT)
        one_sixth.next_to(equal, RIGHT)
        rhs_obj.extend([equal, one_sixth, ])

        self.play(ShowCreation(arr_T_numbers[0]))
        self.add(probs[0])
        self.wait()
        self.add(equal)
        self.add(one_sixth)
        self.wait()

        # P(T = 2)
        equal = equal.copy()
        five_sixth = five_sixth.copy()
        one_sixth = one_sixth.copy()
        equal.next_to(probs[1], RIGHT)
        five_sixth.next_to(equal, RIGHT)
        one_sixth.next_to(five_sixth, RIGHT, MED_LARGE_BUFF)
        rhs_obj.extend([equal, five_sixth, one_sixth])

        self.play(ShowCreation(arr_T_numbers[1]))
        self.add(probs[1])
        self.wait()
        self.add(equal)
        self.add(five_sixth)
        self.wait()
        self.add(one_sixth)
        self.wait()


        # P(T = 3)
        equal = equal.copy()
        five_sixth = five_sixth.copy()
        one_sixth = one_sixth.copy()
        one_sixth_2 = one_sixth.copy()
        equal.next_to(probs[2], RIGHT)
        five_sixth.next_to(equal, RIGHT)
        one_sixth.next_to(five_sixth, RIGHT, MED_LARGE_BUFF)
        one_sixth_2.next_to(one_sixth, RIGHT)
        rhs_obj.extend([equal, five_sixth, one_sixth, one_sixth_2])


        self.play(ShowCreation(arr_T_numbers[2]))
        self.add(probs[2])
        self.wait()
        self.add(equal)
        self.add(five_sixth)
        self.wait()
        self.add(one_sixth)
        self.wait()
        self.add(one_sixth_2)
        self.wait()

        # 5/6 5/6 to (5/6)^2
        paren_pow_2 = Tex(r"\left({{\frac 1 6}}\right)^{2}").scale(TEXT_SCALE)
        paren_pow_2 = VGroup(paren_pow_2[0], paren_pow_2[2])
        paren_pow_2.shift(one_sixth.get_center() -\
            (paren_pow_2[0].get_corner(RIGHT)+paren_pow_2[1].get_corner(LEFT))/2
            )


        self.play(Transform(one_sixth_2, paren_pow_2))
        self.wait()


        # P(T = k)
        equal = equal.copy()
        one_sixth = one_sixth.copy()
        five_sixth_k = Tex(r"\left(\frac 5 6\right)^{\phantom{k}-1}").scale(TEXT_SCALE)
        five_sixth_k_power = Tex(r"k", color=YELLOW).scale(.75).scale(TEXT_SCALE)
        five_sixth_k_power.move_to(five_sixth_k.get_corner(UP)).shift(.09*DOWN+.22*RIGHT)
        five_sixth_k = VGroup(five_sixth_k, five_sixth_k_power)

        equal.next_to(probs[-1], RIGHT)
        one_sixth.next_to(equal, RIGHT)
        five_sixth_k.next_to(one_sixth, RIGHT, MED_SMALL_BUFF)
        rhs_obj.extend([equal, one_sixth, five_sixth_k])
        prob_T_k = VGroup(one_sixth, five_sixth_k) # keep track of this bc we use it below

        self.play(ShowCreation(VGroup(*arr_T_numbers[3:])))

        self.add(*probs[1:])
        self.wait()
        self.add(equal)
        self.add(one_sixth)
        self.add(five_sixth_k)
        self.wait()

        # prepare for expectation

        # fade the rest and make expectation appear
        self.play(FadeOut(VGroup(
            *rhs_obj,
            *arr_T_numbers)),
                Transform(var_T, exp_T)
        )
        self.wait()

        # multiply by numbers
        multipliers = [
            VGroup(p[1].copy(), p) for p in probs if len(p) > 1
        ]

        self.play(
            *[
                n.animate.shift(p.get_width()*LEFT)
                for n, p in multipliers
            ]
        )
        self.wait()

        # make sum
        # E[T] = 1 P(1) + 2 P(2) + 3 P(3) + ... + k P(k) + ...
        sum_rhs = [] # keep track of terms appearing in rhs
        terms = [*multipliers]
        dotdotdot = probs[3]
        dotdotdot_copy = dotdotdot.copy() # to add at the end of the sum
        terms.insert(3, dotdotdot)
        terms.append(dotdotdot_copy)

        terms_target = [a.copy() for a in terms]
        pluss = [Tex("+").scale(TEXT_SCALE) for _ in terms[1:]]
        eq = Tex("=").scale(TEXT_SCALE)
        sum_rhs = [*terms, *pluss, dotdotdot, dotdotdot_copy]


        eq.next_to(var_T)

        a = terms_target[0]
        a.next_to(eq, RIGHT)

        # stack horizontally
        for a, b, plus in zip(terms_target, terms_target[1:], pluss):
            plus.next_to(a, RIGHT)
            b.next_to(plus, RIGHT)
            #hstack([plus, nn, pp,], SMALL_BUFF)
        self.play(Transform(VGroup(*terms), VGroup(*terms_target)),
                  FadeIn(VGroup(eq, *pluss)))
        self.wait()

        # sum_k=1 infinity k P(k)
        self.remove(*sum_rhs)
        # make the index k phantom so that we can create our own
        # because we want to replace its color freely
        sigma = Tex(r"\sum_{\phantom{k}=1}^\infty").scale(TEXT_SCALE)
        sigma_idx = Tex(r"k", color=YELLOW).scale(.7).scale(TEXT_SCALE)
        sigma_idx.move_to(sigma.get_corner(DOWN)).shift(UP/10+.19*LEFT)
        sigma = VGroup(sigma, sigma_idx)
        generic_term = terms[4]
        generic_term_target = generic_term.copy()
        generic_term_target.next_to(sigma, RIGHT)
        self.add(sigma)
        self.play(Transform(generic_term, generic_term_target))
        self.play(VGroup(var_T, eq).animate.shift(4.5*RIGHT))
        self.wait()


        # P(T = k) ==> 1/6 5/6^k
        prob_T_k.move_to(generic_term[1]).shift(RIGHT/10.)
        self.play(Transform(generic_term[1], prob_T_k))
        generic_term[1] = prob_T_k
        self.wait()

        # take 1/6 out
        one_sixth = generic_term[1][:2]
        self.play(one_sixth.animate.shift(1.5*LEFT))
        self.wait()



        # complicated formula
        left_paren = Tex(r"\left(\phantom{\frac11}\right.")
        right_paren = Tex(r"\left.\phantom{\frac11}\right)'")
        buff = Line(stroke_opacity=0).scale(.2)
        deriv_inf_series = VGroup(*hstack([tex_fn(r"1 + "),
                                           sigma.copy(),
                                           buff.copy().scale(.5),
                                           tex_fn(r"x^k"),
                                           buff,
                                           buff,
                                           tex_fn(r"="),
                                           buff,
                                           tex_fn(r"\frac{1}{1 - x}")
                                           ],
                                          SMALL_BUFF))
        lhs = deriv_inf_series[:4] # 1 + sum x^k
        x_k = lhs[-1] # x^k
        rhs = deriv_inf_series[-1]
        deriv_inf_series.shift(2*DOWN+2*LEFT)
        self.add(deriv_inf_series)
        self.wait()

        # take derivatives

        # lhs
        left_paren_1 = left_paren.copy() .next_to(lhs, LEFT, 0*SMALL_BUFF)
        right_paren_1 = right_paren.copy() .next_to(lhs, RIGHT, 0*SMALL_BUFF)
        self.add(left_paren_1, right_paren_1)

        # rhs
        left_paren_2 = left_paren.copy() .next_to(rhs, LEFT, 0*SMALL_BUFF)
        right_paren_2 = right_paren.copy() .next_to(rhs, RIGHT, 0*SMALL_BUFF)
        self.add(left_paren_2, right_paren_2)
        self.wait()


        # take derivative rhs
        num = tex_fn("1")
        denum = tex_fn(r"({{1}}-{{x}})^{{2}}")
        frac_line = Tex("\\over \\,")
        frac_line.stretch_to_fit_width(denum.get_width())
        frac_line.next_to(num, DOWN, SMALL_BUFF)
        denum.next_to(frac_line, DOWN, SMALL_BUFF)
        deriv_1_over_1_x  = VGroup(num, frac_line, denum)
        deriv_1_over_1_x = deriv_1_over_1_x.move_to(rhs).shift(DOWN/10)
        self.play(Transform(rhs, deriv_1_over_1_x),
                  FadeOut(VGroup(left_paren_2, right_paren_2)))
        deriv_1_over_1_x = rhs
        self.wait()


        # take derivatives inside
        self.play(
            FadeOut(lhs[0]), # 1' = 0
            Transform(left_paren_1, left_paren_1.copy().scale(.5).next_to(x_k, LEFT, 0)),
            Transform(right_paren_1, right_paren_1.copy().scale(.5).next_to(x_k, RIGHT, 0)))
        self.wait()

        # derivative x^k
        deriv_x_k = tex_fn(r"k \quad x^{k-1}").move_to(x_k).shift(RIGHT/3)

        self.play(Transform(x_k, deriv_x_k),
                  FadeOut(VGroup(left_paren_1, right_paren_1)))
        deriv_x_k = x_k
        self.wait()

        # multiply lhs by (1-x)
        one_minus_x_left = tex_fn(r"(1-x)")
        one_minus_x_right= one_minus_x_left.copy()
        one_minus_x_left.next_to(lhs, LEFT, 0*SMALL_BUFF)
        self.add(one_minus_x_left)
        self.wait()

        # multiply rhs by (1-x)

        #one_over_1_x = tex_fn(r"\frac{1}{1-{{x}}}").move_to(deriv_1_over_1_x)
        # remove the square
        self.play(Transform(deriv_1_over_1_x[2][0], Tex("")),
                  Transform(deriv_1_over_1_x[2][4:], Tex("")),
                  )
        one_over_1_x = deriv_1_over_1_x
        self.wait()



        # x = 5/6
        x_5_6 = tex_fn(r"x = \frac 56")
        one_minus_x_1_6 = tex_fn(r"1-x = \frac 16")
        x_5_6.to_corner(UR).shift(LEFT)
        one_minus_x_1_6.next_to(x_5_6, DOWN).align_to(x_5_6, RIGHT)


        self.add(x_5_6)
        self.wait()
        self.add(one_minus_x_1_6)
        self.wait()

        # replace lhs
        one_sixth = tex_fn(r"\frac 1 6").move_to(one_minus_x_left).shift(RIGHT/2)
        five_sixth = tex_fn(r"\left(\frac 5 6\right)").scale(.7).move_to(deriv_x_k[1]).shift(LEFT/8)
        self.play(Transform(deriv_x_k[1], five_sixth),
                  Transform(one_minus_x_left, one_sixth))
        self.wait()

        # replace rhs
        x = one_over_1_x[2][3]
        five_sixth = tex_fn(r"\frac 5 6").scale(.7).move_to(x).shift(DOWN/10)
        self.play(Transform(x, five_sixth))
        self.wait()


        # equal 6
        equal_6 = tex_fn("= 6").next_to(one_over_1_x[1])
        self.add(equal_6)
        self.play(ShowCreation(SurroundingRectangle(equal_6)))

        # clean up
        inf_sum_1 = [  ]
