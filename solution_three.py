#!/usr/bin/env python3

from manimlib import *
exec(get_custom_config()["universal_import_line"])
import numpy as np
from dice_utils import make_dice_face
from common import vstack, hstack, halign




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
    game_copy = game.copy().scale(1.2)
    game_save = game.copy()
    rect = Rectangle(stroke_width=10, stroke_color=YELLOW_D, fill_color=BLACK, fill_opacity=.9)
    rect.surround(game_copy, stretch=True).scale(1.2*UP + 1.1*RIGHT)

    scene.play(
        ShowCreation(rect),
        Transform(game, game_copy))

    scene.wait()
    # highligh 6
    scene.play(Indicate(game[-1]))
    scene.wait()

    # cleanup
    scene.remove(rect)
    scene.play(
        Transform(game, game_save), run_time=.01)
        #scene.add(rect)


def highlight_all_6s(scene, dice):
    # highlight all 6s
    sixes = [d for d in dice if d.value == 6]
    scene.play(Indicate(VGroup(*sixes), scale_factor=1), run_time=3)
    scene.wait()
    return sixes


COLOR1 = YELLOW
COLOR2 = RED_A
COLOR3 = BLUE_A

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
        num_games =  50 # 30
        camera_height = 20


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
        print("info:", len(dice_on_games), "dice")
        print("info:", len(dice), "games")


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

        game_counter.add_updater(lambda m: m.align_to(frame, LEFT).shift(RIGHT))
        #always(game_counter.align_to, frame, LEFT)


        total_time = 2
        game_counter[1].curr_time = 0
        def game_counter_updater(m, dt):
            m.curr_time += dt
            m.set_value(6 + int((101 - 6) * m.curr_time / total_time))

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

        # #################
        # Method 1
        # #################
        # num throws = E[T] * 100
        tex_scale = 1.5
        # num_throws = Text("# throws").scale(tex_scale).set_color(COLOR2)
        # num_throws.align_to(game_counter, LEFT).shift(5*DOWN)
        # self.add(num_throws)
        # self.wait()

        # almost_eq = Tex(r"\approx").scale(tex_scale)
        # almost_eq.next_to(num_throws, RIGHT, MED_SMALL_BUFF)
        # ET = Tex(r"\mathbb E[T]").scale(1.4*tex_scale).set_color(COLOR1)
        # ET.next_to(almost_eq, RIGHT).shift(2*RIGHT)

        # num_games = game_counter[1].copy().scale(tex_scale)
        # num_games.next_to(ET, LEFT, MED_SMALL_BUFF).shift(UP/20)

        # approx_1 = VGroup(ET, num_games)
        # # brin down 100
        # self.add(almost_eq)
        # self.play(TransformFromCopy(game_counter[1], num_games))
        # self.wait()

        # self.add(ET)
        # self.wait()

        # #################
        # Method 2
        # #################
        # num throws / 6 = 100
        #
        # highlight particular game that ends with 6
        highlight_game(self, VGroup(*dice[5]))
        self.wait()


        num_throws = Text("# throws").scale(tex_scale).set_color(COLOR2)

        num_games = game_counter[1].copy().scale(tex_scale)
        num_games.align_to(game_counter, LEFT).shift(2*DOWN)
        num_6 = Text(r"= #6s").scale(tex_scale)
        one_sixth = Tex(r"\approx {{\frac 1 6}}").scale(1.2*tex_scale)
        one_sixth[1].set_color(COLOR3)


        ET = Tex(r"\mathbb E[T]").scale(1.4*tex_scale).set_color(COLOR1)


        hstack([num_games, num_6, num_throws], MED_SMALL_BUFF)
        one_sixth.move_to(num_6)

        num_games2 = num_games.copy().move_to(num_throws).shift(1.4*LEFT)
        ET.next_to(num_games2, RIGHT).shift(DOWN/10)



        # brin down 100
        self.play(TransformFromCopy(game_counter[1], num_games))
        self.wait()

        # highlight all 6
        self.add(num_6)
        sixes = highlight_all_6s(self, dice_on_grid)
        self.wait()
        self.wait()

        self.play(ReplacementTransform(num_6, one_sixth))
        self.wait()

        self.add(num_throws)
        self.wait()


        self.play(ReplacementTransform(num_throws, num_games2))
        self.wait()

        self.add(ET)
        self.wait()

        # zoom on and solve
        frame_target = frame.copy().set_height(10).move_to(one_sixth)

        self.play(
            FadeOut(VGroup(*dice_on_games, *sixes, game_counter)),

            Transform(frame, frame_target))
        self.wait()

        approx_6 = Tex(r"\approx 6").set_color(COLOR3).scale(2*tex_scale).move_to(ET).shift(3*LEFT)
        eq_6 = Tex(r"= 6").set_color(COLOR3).scale(2*tex_scale).move_to(approx_6)

        self.play(
            LaggedStartMap(
                FadeOut,
                VGroup(num_games, num_games2, one_sixth),
                lambda m: (m, DOWN)),
            ET.animate.shift(6*LEFT),
        )
        self.add(approx_6)
        self.wait()

        self.play(ReplacementTransform(approx_6, eq_6))
        self.wait()
