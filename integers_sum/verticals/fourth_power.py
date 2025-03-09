"""
Visual proof of Every Fourth Power Greater than One is the Sum of Two Non-consecutive
Triangular Numbers.
Proofs without Words III. Roger B. Nelsen. p. 137.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, Group
from manim import Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Dot, Line, Polygon
from manim import Text, Tex, Square, DashedLine, RoundedRectangle

from manim import config
from manim import LEFT, RIGHT, DOWN, LIGHT, UP

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


class FourthPower(MovingCameraScene):
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
            Tex(r"Les puissances 4", font_size=48, color=BLACK),
            Tex(r"sont la somme de", font_size=48, color=BLACK),
            Tex(r"triangulaires", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
        ]
        txt = VGroup(*txt).arrange(DOWN)

        results = [
            Tex(r"Si $T_k = 1 + 2 + \cdots + k$,", font_size=24, color=BLACK),
            Tex(r"alors $n^4 = T_{n^2 + n - 1} + T_{n^2 - n - 1}$", font_size=24, color=BLACK),
        ]
        results = VGroup(*results).arrange(DOWN).move_to([0, -1, 0])

        self.add(
            txt_title,
            txt,
            results
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt),
            Uncreate(results),
            run_time=0.5
        )
        self.wait(0.5)

        # Create the table
        squares = VGroup()
        squares.add(Square(side_length=0.1, color=BLACK, stroke_width=1))
        for idx in range(3):
            new_square = Square(side_length=0.1, color=BLACK, stroke_width=1).\
                next_to(squares[idx], direction=RIGHT, buff=0)
            squares.add(new_square)
        for idx in range(12):
            new_square = Square(side_length=0.1, color=BLACK, stroke_width=1).\
                next_to(squares[idx], direction=DOWN, buff=0)
            squares.add(new_square)

        big_squares = VGroup()
        big_squares.add(squares)
        for idx in range(3):
            new_square = squares.copy().\
                next_to(big_squares[idx], direction=RIGHT, buff=0.1)
            big_squares.add(new_square)
        for idx in range(12):
            new_square = squares.copy().\
                next_to(big_squares[idx], direction=DOWN, buff=0.1)
            big_squares.add(new_square)
        self.play(
            Create(big_squares)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Proofs without words III:", font_size=30, color=BLACK),
            Tex(r"Further exercises in", font_size=30, color=BLACK),
            Tex(r"visual thinking", font_size=30, color=BLACK),
            Tex(r"Roger B. Nelsen (2015), p. 137", font_size=30, color=BLACK)
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