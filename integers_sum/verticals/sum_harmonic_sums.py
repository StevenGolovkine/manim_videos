"""
Visual proof of the sums of harmonic sums.
Proofs without Words II. Roger B. Nelsen. p. 116.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Dot, Brace, RoundedRectangle, Square, MobjectTable
from manim import Create, Uncreate, Write
from manim import VGroup, Transform, FadeIn, FadeOut, FunctionGraph
from manim import Text, Tex

from manim import config

from manim import LEFT, RIGHT, DOWN, LIGHT, UP, PI

# COLORS
BLUE = "#B0E1FA"
VIOLET = "#E8C9FA"
RED = "#F79BC5"
GREEN = "#DBF9E7"
YELLOW = "#EFE9B7"
ORANGE = "#F6CCB0"
BLACK = "#000000"
WHITE = "#F4EDDE"

# Make it vertical
SCALE_FACTOR = 1
# Flip width => height, height => width
tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height
# Change coord system dimensions
config.frame_height = config.frame_height / SCALE_FACTOR
config.frame_width = config.frame_height * 9 / 16

class Sums(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame.save_state()

        txt_copy = Text(
            r"@chill.maths", font_size=12,
            font="CMU Typewriter Text", weight=LIGHT, color=BLACK
        ).to_edge(RIGHT + DOWN, buff=0.1)
        self.add(txt_copy)


        # Introduction text
        txt_title = [
            Tex(r"La somme des", font_size=48, color=BLACK),
            Tex(r"sommes", font_size=48, color=BLACK),
            Tex(r"harmoniques", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Roger B. Nelsen", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        self.add(
            txt_title,
            txt,
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt),
            run_time=0.5
        )
        self.wait(0.5)

        # Text sums
        text_sums = [
            Tex(r"$H_n = \sum_{k=1}^{n} \frac{1}{k}$", font_size=36, color=BLACK),
            Tex(
                r"$\Rightarrow \sum_{k=1}^{n-1} H_k = n H_n - n$",
                font_size=36, color=BLACK
            ),
        ]
        text_sums = VGroup(*text_sums).arrange(DOWN).move_to([0, 3, 0])
        self.play(Write(text_sums))

        # Create the table
        squares = VGroup()
        squares.add(Square(side_length=0.5, color=BLACK, stroke_width=1))
        for idx in range(6):
            new_square = Square(side_length=0.5, color=BLACK, stroke_width=1).\
                next_to(squares[idx], direction=RIGHT, buff=0)
            squares.add(new_square)
        for idx in range(42):
            new_square = Square(side_length=0.5, color=BLACK, stroke_width=1).\
                next_to(squares[idx], direction=DOWN, buff=0)
            squares.add(new_square)
        squares.move_to([0, 0, 0])

        self.play(
            Create(squares)
        )

        # Text 1
        for idx in [0, 7, 14, 21, 28, 35, 42]:
            text_1 = Tex(r"$1$", font_size=24, color=BLACK).\
                move_to(squares[idx].get_center())
            self.play(Write(text_1), run_time=0.1)

        # Text 1/2
        for idx in [1, 8, 15, 22, 29, 36, 43]:
            text_12 = Tex(r"$\frac{1}{2}$", font_size=24, color=BLACK).\
                move_to(squares[idx].get_center())
            self.play(Write(text_12), run_time=0.1)

        # Text 1/3
        for idx in [2, 9, 16, 23, 30, 37, 44]:
            text_13 = Tex(r"$\frac{1}{3}$", font_size=24, color=BLACK).\
                move_to(squares[idx].get_center())
            self.play(Write(text_13), run_time=0.1)

        # Text ...
        for idx in [3, 10, 17, 24, 31, 38, 45]:
            text_14 = Tex(r"$\dots$", font_size=24, color=BLACK).\
                move_to(squares[idx].get_center())
            self.play(Write(text_14), run_time=0.1)
        for idx in [4, 11, 18, 25, 32, 39, 46]:
            text_15 = Tex(r"$\dots$", font_size=24, color=BLACK).\
                move_to(squares[idx].get_center())
            self.play(Write(text_15), run_time=0.1)

        # Text 1 / n-1
        for idx in [5, 12, 19, 26, 33, 40, 47]:
            text_1n_1 = Tex(r"$\frac{1}{n-1}$", font_size=24, color=BLACK).\
                move_to(squares[idx].get_center())
            self.play(Write(text_1n_1), run_time=0.1)
        
        # Text 1 / n
        for idx in [6, 13, 20, 27, 34, 41, 48]:
            text_1n = Tex(r"$\frac{1}{n}$", font_size=24, color=BLACK).\
                move_to(squares[idx].get_center())
            self.play(Write(text_1n), run_time=0.1)

        # Text nH_n
        text_nHn = Tex(
            r"$n H_n = $",
            font_size=36, color=BLACK
        ).next_to(squares, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(text_nHn))

        # Color upper diagonal of squares
        upper_idx = [
            0, 1, 2, 3, 4, 5, 6,
            8, 9, 10, 11, 12, 13,
            16, 17, 18, 19, 20,
            24, 25, 26, 27,
            32, 33, 34,
            40, 41,
            48
        ]
        self.play(
            *[
                squares[idx].animate.set_fill(color=BLUE, opacity=0.5)
                for idx in upper_idx
            ]
        )

        txt_n = Tex(r"$n$", font_size=36, color=BLACK).\
            next_to(text_nHn, RIGHT, buff=0.2)
        self.play(Write(txt_n))

        # Color lower diagonal of squares
        lower_idx = [
            42, 43, 44, 45, 46, 47,
            35, 36, 37, 38, 39,
            28, 29, 30, 31,
            21, 22, 23,
            14, 15,
            7
        ]
        self.play(
            *[
                squares[idx].animate.set_fill(color=RED, opacity=0.5)
                for idx in lower_idx
            ]
        )

        txt_plus = Tex(r"$+$", font_size=36, color=BLACK).\
            next_to(txt_n, RIGHT, buff=0.2)
        self.play(Write(txt_plus))

        txt_sum = Tex(r"$\sum_{k=1}^{n-1} H_k$", font_size=36, color=BLACK).\
            next_to(txt_plus, RIGHT, buff=0.2)
        self.play(Write(txt_sum))


        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Proofs without words II,", font_size=30, color=BLACK),
            Tex(r"Roger B. Nelsen (2000)", font_size=30, color=BLACK),
        ]
        ref = VGroup(*ref)\
            .arrange(DOWN, aligned_edge=LEFT, center=False, buff=0.1)\
            .move_to([0, 2, 0])

        self.play(Write(ref))

        text = Text(
            "chill.maths", font="CMU Typewriter Text", weight=LIGHT, color=BLACK
        )
        # Ajouter un élément mathématique, par exemple une sinusoïde
        sine_wave = FunctionGraph(
            lambda x: 0.1 * np.sin(2 * np.pi * x),
            x_range=[-3, 3],
            color=BLACK
        )
        sine_wave.next_to(text, DOWN, buff=0.2)
        
        self.play(
            FadeIn(text, scale=0.5),
            Create(sine_wave),
            run_time=2
        )

        self.wait(1)
