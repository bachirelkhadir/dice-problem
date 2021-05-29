#!/usr/bin/env python3

from manimlib import *
import numpy as np


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



def make_dice_face(i):
    dot = lambda: Dot().scale(1.1)
    dots = {
        1: dot(),
        2: VGroup(*[dot().shift(DL/3), dot().shift(UR/3)]),
        3: VGroup(*[dot().shift(UL/3), dot(), dot().shift(DR/3)]),
        4: VGroup(*[dot().shift((i*UP+j*LEFT)/3) for i in (-1, 1) for j in (-1, 1)]),
        5: VGroup(*[dot().shift((i*UP+j*LEFT)/3) for i in (-1, 1) for j in (-1, 1)], dot()),
        6: VGroup(*[dot().shift( (i-1) * DOWN/3 + (j-.5) * RIGHT/2) for i in range(3) for j in range(2)])
    }
    sq = Square(1.2, fill_opacity=.8, fill_color=BLACK).round_corners(.25).move_to(dots[i])
    face = VGroup(sq, dots[i])
    face.value = i
    return face

def put_dice_in_matrix(dice, num_cols):

        dice_matrix= sum(map(list, dice), [])
        len_row = len(dice_matrix)//num_cols
        dice_matrix = [ dice_matrix[num_cols * i: num_cols * (i+1)]
                        for i in range(len_row)] +  [dice_matrix[num_cols*len_row:]]
        return dice_matrix


def place_dice_in_matrix(dice_matrix):

        # Copy matrix and position it correctly
        dice_matrix_copy = [
            [o.copy() for o in row]
            for row in dice_matrix
        ]
        dice_matrix_copy[0][0].to_corner(UL)
        # hstack  every row
        for row in dice_matrix_copy:
            hstack(row, SMALL_BUFF)
        # vstack rows
        vstack([*map(lambda row: VGroup(*row), dice_matrix_copy)], SMALL_BUFF )
        return dice_matrix_copy


def highlight_game(scene, game):
        rect = Rectangle().surround(game, stretch=True).scale(1.1)
        scene.add(rect)


class SolutionThree(Scene):

    def generate_games(self, num_games):
        np.random.seed(0)
        games_outcome = np.random.randint(1, 7, 1000)
        games = []
        curr_seq = []
        for i in games_outcome:
            curr_seq.append(i)
            if i == 6:
                n = len(curr_seq)
                games.append(curr_seq)
                curr_seq = []

        return games[:num_games]

    def construct(self):
        face_scale = 0.8
        num_cols = 20
        num_games = 10 # 30
        camera_height = 20

        num_throws = Text("# throws")

        game_counter = VGroup(*hstack([Text("# games = "), Integer(0)], MED_SMALL_BUFF))
        game_counter.to_corner(UL)
        self.add(game_counter)

        games = self.generate_games(num_games)
        dice = [
            VGroup(*hstack([make_dice_face(i).scale(face_scale) for i in game], SMALL_BUFF))
            for game in games
        ]
        # stack games vertically
        dice = VGroup(*vstack(dice, MED_SMALL_BUFF)).to_edge(UP)


        # put all dice in a regular matrix

        dice_matrix = put_dice_in_matrix(dice, num_cols)
        dice_matrix_copy = place_dice_in_matrix(dice_matrix)

        # flatten
        dice_on_grid = sum(dice_matrix_copy, [])
        dice_on_games= sum(dice_matrix, [])


        # Add games on after the other
        # TODO:add counter
        # zoom out

        # Add 6 games
        for i, game in enumerate(dice[:6]):
            self.add(game)
            game_counter[1].set_value(i+1)
            self.wait(.1)

        self.wait()

        # zoom out and add rest of the games
        frame = self.camera.frame
        frame_target = frame.copy().set_height(camera_height).align_to(dice[0], UP).shift(UP)
        always(game_counter.align_to, frame, LEFT)

        total_time = 2
        game_counter[1].time_passed = 0
        def game_counter_updater(m, dt):
            m.time_passed += dt
            m.set_value(6 + int((len(dice) - 6) * m.time_passed / total_time ))
        game_counter[1].add_updater(game_counter_updater)
        self.play(Transform(frame, frame_target),
                  ShowCreation(VGroup(dice[6:])),
                  run_time = total_time
                  )

        game_counter[1].remove_updater(game_counter_updater)


        self.wait()

        # put games on a matrix
        start, end = 0, 0
        for game in games:
            end += len(game)
            self.play(Transform(VGroup(*dice_on_games[start:end]),
                                VGroup(*dice_on_grid[start:end]),
                                run_time=4./num_games))
            start = end

        # lenght sequence
        num_throws.align_to(frame, DOWN).shift(3*UP)
        self.add(num_throws)
        self.wait()


        # num throws = E[T] * 100
        tex_scale = 1.3
        ET = Tex(r"\mathbb E[T]").scale(tex_scale)
        num_games = game_counter[1].copy()
        ET.next_to(num_throws, RIGHT).shift(RIGHT)
        num_games.next_to(ET, LEFT).shift(UP/20)

        approx_1 = VGroup(ET, num_games)
        # brin down 100
        self.play(TransformFromCopy(game_counter[1], num_games))
        self.wait()

        self.add(ET)
        self.wait()

        # num throws / 6 = 100
        # highlight particular game that ends with 6
        highlight_game(self, VGroup(*dice[5]))

        # highlight all 6s
        #sixes = [d for d in dice_on_games if d.value == 6]
        #self.play(Indicate(VGroup(*sixes)))
        return


        one_sixth = Tex(r"\frac 1 6").scale(tex_scale)
        num_games = game_counter[1].copy()
        one_sixth.next_to(num_throws, DOWN).to_corner(RIGHT)
        num_games.next_to(one_sixth, RIGHT).shift(UP/20)

        approx_1 = VGroup(one_sixth, num_games)
        # brin down 100
        self.play(TransformFromCopy(game_counter[1], num_games))
        self.add(one_sixth)
        self.wait()
