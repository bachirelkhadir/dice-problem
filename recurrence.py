#!/usr/bin/env python3
from manimlib import *


def make_node(s, r=1.2):
    text = Text(s)
    rect = Circle().scale(r)
    #rect.surround(text)
    return VGroup(text, rect)

class RecurrenceScene(Scene):

    def construct(self):

        self.bring_to_back(ImageMobject("media/dice1.png").shift(4*LEFT))


        start = make_node("start")
        end = make_node("end")
        start.shift(4*LEFT)
        end.shift(4*RIGHT)

        s_t = CurvedArrow(start[1].get_edge_center(UP),
                             end[1].get_edge_center(UP),
                             angle=-PI/2)
        s_s = CurvedArrow(start[1].get_edge_center(UP),
                            start[1].get_edge_center(UP)+LEFT/3.,
                             angle=1.5*PI)
        self.add(start, end, s_t, s_s)

        prob_s_t = Tex(r"\frac 56")
        prob_s_s = Tex(r"\frac 16")
        prob_s_t.next_to(s_t, UP)
        prob_s_s.next_to(s_s, UP)
        self.add(prob_s_t, prob_s_s)

        self.wait(0.1)


        # diagram to tree


        # Move end down
        end_2 = end.copy()
        start_2 = start.copy()
        prob_s_t_2 = prob_s_t.copy()
        #start_2.shift(3*UP+RIGHT)
        end_2.next_to(start, RIGHT+3*DOWN)

        s_t_2 = CurvedArrow(start_2[1].get_edge_center(RIGHT),
                             end_2[1].get_edge_center(UP),
                             angle=-PI/3)
        prob_s_t_2.next_to(s_t_2, RIGHT)

        self.wait()
        frame = self.camera.frame
        self.add(frame)
        frame.set_height(8)

        def raise_camera(m, dt):
            m.set_height(m.get_height() * (1 + 0.5 * dt))
        frame.add_updater(raise_camera)

        self.play(
            ApplyMethod(frame.move_to, start_2.get_center()+2*DOWN),
            Transform(start, start_2),
            Transform(end, end_2),
            Transform(s_t, s_t_2),
            Transform(prob_s_t, prob_s_t_2),
            wait=2, rate_func=lambda t: t, )

        frame.remove_updater(raise_camera)

        self.wait(1.)

        # Copy the whole tree branch
        shift = LEFT+3*DOWN
        branch  = VGroup(start, end, s_t, prob_s_t).copy()
        branch.next_to(start, shift)
        self.add(branch)

        # make arrow to tree
        s_tree = CurvedArrow(start_2[1].get_edge_center(LEFT),
                          branch[0][1].get_edge_center(UP),
                        angle=PI/3)

        self.add(branch)


        self.play(Transform(s_s, s_tree),
                  ApplyMethod(prob_s_s.next_to, s_tree, LEFT))
        self.wait(.2)

        branch_2 = branch.copy()
        branch_2.next_to(branch[0][1], shift)
        self.add(branch_2)


        # make arrow to second tree
        tree_tree = CurvedArrow(branch[0][1].get_edge_center(LEFT),
                          branch_2[0][1].get_edge_center(UP),
                        angle=PI/3)
        self.add(tree_tree)
        self.wait(.2)


        # make arrow from second tree

        frame.set_height(18)
        dots = Tex("...").scale(3).rotate(PI/2)
        dots.next_to(branch_2[0][1], shift+2*DOWN+4*LEFT)

        tree_dots= CurvedArrow(branch_2[0][1].get_edge_center(LEFT),
                          dots.get_edge_center(UP)+UP/2,
                        angle=PI/3)
        self.add(dots)
        self.add(tree_dots)

        # add image
        #Eself.add(Rectangle(fill_color=WHITE, fill_opacity=1).scale(4))
        self.embed()
        self.wait(10)
