#!/usr/bin/env python3
from manimlib import *
exec(get_custom_config()["universal_import_line"])

from dice_utils import make_dice_face

COLOR1 = YELLOW
COLOR2 = GOLD
COLOR3 = RED_A



class RecurrenceScene(Scene):

    def construct(self):

        frame = self.camera.frame
        frame.set_height(12)

        start = make_node("Throw")
        end = make_node(make_dice_face(6))
        start.shift(4*LEFT)
        end.shift(4*RIGHT)

        # arrows
        s_t = CurvedArrow(start[1].get_edge_center(UP),
                             end[1].get_edge_center(UP),
                             angle=-PI/2)
        s_s = CurvedArrow(start[1].get_edge_center(UP),
                            start[1].get_edge_center(UP)+LEFT/3.,
                             angle=1.5*PI)

        # probabilities
        prob_s_t = Tex(r"\frac 16")
        prob_s_s = Tex(r"\frac 56")
        prob_s_t.next_to(s_t, UP)
        prob_s_s.next_to(s_s, UP)


        self.play(ShowCreation(start))
        self.wait()

        self.play(ShowCreation(VGroup(s_t, end)))
        self.wait()
        self.add(prob_s_t)
        self.wait()
        self.play(ShowCreation(s_s))
        self.wait()
        self.add(prob_s_s)
        self.wait()

        # Zoom out and move end node down and to the left
        end_2 = end.copy()
        start_2 = start.copy()
        prob_s_t_2 = prob_s_t.copy()
        end_2.next_to(start, RIGHT+3*DOWN)

        s_t_2 = CurvedArrow(start_2[1].get_edge_center(RIGHT),
                             end_2[1].get_edge_center(UP),
                             angle=-PI/3)
        prob_s_t_2.next_to(s_t_2, RIGHT)


        frame_target = frame.copy().set_height(18).move_to(start_2.get_center()+2*DOWN)

        self.play(
            Transform(frame, frame_target),
            Transform(start, start_2),
            Transform(end, end_2),
            Transform(s_t, s_t_2),
            Transform(prob_s_t, prob_s_t_2),
            wait=2, rate_func=lambda t: t, )


        self.wait(1.)

        # Unwind

        # Copy the whole tree branch
        shift = LEFT+3*DOWN
        branch  = VGroup(start, end, s_t, prob_s_t).copy()
        branch.next_to(start, shift)

        # make arrow to tree
        s_tree = CurvedArrow(start_2[1].get_edge_center(LEFT),
                          branch[0][1].get_edge_center(UP),
                        angle=PI/3)



        self.play(Transform(s_s, s_tree),
                  ApplyMethod(prob_s_s.next_to, s_tree, LEFT))

        self.play(FadeIn(branch))

        branch_2 = branch.copy()
        branch_2.next_to(branch[0][1], shift)


        # make arrow to second tree
        tree_tree = CurvedArrow(branch[0][1].get_edge_center(LEFT),
                          branch_2[0][1].get_edge_center(UP),
                        angle=PI/3)
        self.play(
            FadeIn(tree_tree),
            FadeIn(branch_2),

        )

        self.wait()

        # make arrow from second tree

        frame.set_height(18)
        dots = Tex("...").scale(3).rotate(PI/2)
        dots.next_to(branch_2[0][1], shift+2*DOWN+4*LEFT)

        tree_dots= CurvedArrow(branch_2[0][1].get_edge_center(LEFT),
                          dots.get_edge_center(UP)+UP/2,
                        angle=PI/3)

        self.play(FadeIn(tree_dots),
                  FadeIn(dots))
        self.wait()

        # highlight left node
        left_node = VGroup(
            branch,
            branch_2,
            tree_tree,
            tree_dots,
            dots
        )
        rect_left_node = SurroundingRectangle(left_node)
        self.play(ShowCreation(rect_left_node))
        self.wait()

        # highlight root
        self.play(Indicate(start))
        self.wait()


        # write expectation
        exp_T = Tex(r"{{\mathbb E[T]}} = {{1}} {{+ \frac 16}} \times {{0}} {{+}} {{\frac 5 6}} \times {{\mathbb E[T]}} {{-}} {{\frac 16}} {{6}}")

        exp_T.scale(3).next_to(start, UP, LARGE_BUFF)

        ET1, eq, one, plus_onesixth, times1, zero, plus, fivesixth, times2, ET2, minus, one_sixth, six = exp_T
        plus_fivesixth = VGroup(plus, fivesixth)
        eq_1 = VGroup(eq, one)


        self.remove(rect_left_node)

        # match colors
        # E[T] <-> start
        ET1.set_color(COLOR1)
        start.set_color(COLOR1)

        self.play(
            ReplacementTransform(start.copy(), ET1) # E[T]
        )
        self.wait()

        self.add(eq, one) # = 1
        self.wait()


        # 1 <-> dice 6
        self.add(plus_onesixth) # + 1/6
        self.wait()

        zero.set_color(COLOR2)
        end.set_color(COLOR2)
        self.add(exp_T[4]) # x
        self.play(
            ReplacementTransform(end.copy(), zero) # 0
        )

        # E[T] <-> Left node
        self.add(plus_fivesixth) # 5/6
        self.wait()


        rect_left_node = SurroundingRectangle(left_node, color=COLOR3)
        ET2.set_color(COLOR3)
        self.add(times2) # x
        self.add(rect_left_node)
        self.play(
            ReplacementTransform(rect_left_node.copy(), ET2) # E[T]
        )
        self.wait()

        # focus camera on equation
        frame_target = frame.copy().set_height(15).move_to(exp_T[:10])
        self.play(Transform(frame, frame_target),
                  LaggedStartMap(
                      FadeOut,
                      VGroup(rect_left_node, left_node, start,
                             s_s, s_t,
                             prob_s_s, prob_s_t, end),
                      lambda m: (m, DOWN)
                  ))


        self.wait()

        # solve equation
        # step 1
        self.remove(plus_onesixth, times1, zero)

        minus.move_to(plus)
        self.play(ReplacementTransform(plus, minus))
        plus_fivesixth_ET = VGroup(minus, fivesixth, times2, ET2)
        self.play(
            plus_fivesixth_ET.animate.shift(7*LEFT),
            eq_1.animate.shift(10*RIGHT),)

        self.wait()


        # step 2

        self.remove(minus, ET1, times2, minus)
        one_sixth.next_to(ET2, LEFT, LARGE_BUFF)
        self.play(
            eq_1.animate.next_to(ET2, RIGHT, LARGE_BUFF),
            ReplacementTransform(fivesixth, one_sixth)
            )
        self.wait()

        # step 3
        self.remove(one_sixth)
        six.move_to(one)
        self.play(ReplacementTransform(one, six))
        self.wait()

        return
