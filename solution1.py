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

class Solution1(Scene):

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
        #self.add(desc_T)

        # P(T = k)
        probs = [
            Tex(("\\mathbb P(T = {{%s}})" % i)).scale(TEXT_SCALE)if i else Tex("{{\\ldots}}") for i in [1, 2, 3, "", "k"]
        ]
        for p, n in zip(probs, numbers):
            if len(p) > 1:
                p[1].set_color(YELLOW)
            p.move_to(n).shift(RIGHT)
        halign(probs)
        self.remove(*numbers)
        self.remove(*arr_T_numbers)

        # keep track of rhs so we can remove it later
        rhs_obj = []

        # P(T = 1)
        equal = Tex("=").scale(TEXT_SCALE)
        one_sixth = Tex(r"\frac 1 6").scale(TEXT_SCALE)
        five_sixth = Tex(r"\frac 5 6").scale(TEXT_SCALE)
        equal.next_to(probs[0], RIGHT)
        one_sixth.next_to(equal, RIGHT)
        rhs_obj.extend([equal, one_sixth, five_sixth])

        self.add(arr_T_numbers[0])
        self.add(probs[0])
        self.add(equal)
        self.add(one_sixth)
        self.wait()

        # P(T = 2)
        equal = equal.copy()
        one_sixth = one_sixth.copy()
        five_sixth = five_sixth.copy()
        equal.next_to(probs[1], RIGHT)
        one_sixth.next_to(equal, RIGHT)
        five_sixth.next_to(one_sixth, RIGHT, MED_LARGE_BUFF)
        rhs_obj.extend([equal, one_sixth, five_sixth])

        self.add(arr_T_numbers[1])
        self.add(probs[1])
        self.add(equal)
        self.add(one_sixth)
        self.add(five_sixth)
        self.wait()


        # P(T = 3)
        equal = equal.copy()
        one_sixth = one_sixth.copy()
        five_sixth = five_sixth.copy()
        five_sixth_2 = five_sixth.copy()
        equal.next_to(probs[2], RIGHT)
        one_sixth.next_to(equal, RIGHT)
        five_sixth.next_to(one_sixth, RIGHT, MED_LARGE_BUFF)
        five_sixth_2.next_to(five_sixth, RIGHT)
        rhs_obj.extend([equal, one_sixth, five_sixth, five_sixth_2])

        self.add(arr_T_numbers[2])
        self.add(probs[2])
        self.add(equal)
        self.add(one_sixth)
        self.add(five_sixth)
        self.add(five_sixth_2)
        self.wait()

        # 5/6 5/6 to (5/6)^2
        paren_pow_2 = Tex(r"\left({{\frac 1 6}}\right)^{2}").scale(TEXT_SCALE)
        paren_pow_2 = VGroup(paren_pow_2[0], paren_pow_2[2])
        paren_pow_2.shift(five_sixth.get_center() -\
            (paren_pow_2[0].get_corner(RIGHT)+paren_pow_2[1].get_corner(LEFT))/2
            )


        self.play(Transform(five_sixth_2, paren_pow_2))

        # P(T = k)
        equal = equal.copy()
        one_sixth = one_sixth.copy()
        five_sixth_k = Tex(r"\left(\frac 5 6\right)^{k-1}").scale(TEXT_SCALE)
        equal.next_to(probs[-1], RIGHT)
        one_sixth.next_to(equal, RIGHT)
        five_sixth_k.next_to(one_sixth, RIGHT, MED_LARGE_BUFF)
        rhs_obj.extend([equal, one_sixth, five_sixth_k])

        self.add(*arr_T_numbers[1:])
        self.add(*probs[1:])
        self.add(equal)
        self.add(one_sixth)
        self.add(five_sixth_k)
        self.wait()

        # prepare for expectation

        # fade the rest and make expectation appear
        exp_T = Tex(r"\mathbb E[T]").scale(TEXT_SCALE).move_to(var_T)
        self.play(FadeOut(VGroup(
            *rhs_obj,
            *arr_T_numbers)),
                Transform(var_T, exp_T)
        )

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
        self.wait()


        # P(T = k) ==>
