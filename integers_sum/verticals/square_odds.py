"""
Visual proof of The square of any odd number is the difference of two consecutive
triangular numbers.
Proofs without Words II. Roger B. Nelsen. p. 96.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import Brace, VGroup, FadeIn, FadeOut, FunctionGraph, Rotate
from manim import Text, Tex, Square, RoundedRectangle, Transform

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


class Odds(MovingCameraScene):
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
            Tex(r"Sur le carré de", font_size=48, color=BLACK),
            Tex(r"nombres impairs", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
        ]
        txt = VGroup(*txt).arrange(DOWN)

        results = [
            Tex(r"Si $T_k = 1 + 2 + \cdots + k$,", font_size=24, color=BLACK),
            Tex(r"alors $(2n + 1)^2 = T_{3n + 1} - T_{n}$", font_size=24, color=BLACK),
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
        squares.add(Square(side_length=0.2, color=BLACK, stroke_width=1))
        for idx in range(8):
            new_square = Square(side_length=0.2, color=BLACK, stroke_width=1).\
                next_to(squares[idx], direction=RIGHT, buff=0.05)
            squares.add(new_square)
        for idx in range(72):
            new_square = Square(side_length=0.2, color=BLACK, stroke_width=1).\
                next_to(squares[idx], direction=DOWN, buff=0.05)
            squares.add(new_square)
        squares.move_to([0, 1, 0])
        self.play(
            Create(squares)
        )

        brace = Brace(squares, direction=[0, -1, 0], sharpness=1, color=BLACK)
        txt_2n = Tex(r"$2n + 1$", font_size=30, color=BLACK).next_to(brace, 0.5 * DOWN)
        
        self.play(
            Create(brace),
            Write(txt_2n)
        )

        upper = [0, 1, 2, 3, 9, 10, 11, 18, 19, 27]
        lower = [*range(4, 9), *range(12, 18), *range(20, 27), *range(28, 81)]

        upper_group = VGroup(
            *[squares[i] for i in upper],
        )
        lower_group = VGroup(
            *[squares[i] for i in lower],
        )
        self.play(
            # Upper
            upper_group.animate.set_fill(RED, 1),
            # Lower
            lower_group.animate.set_fill(BLUE, 1)
        )

        brace_1 = Brace(upper_group, direction=[0, 1, 0], sharpness=1, color=BLACK)
        txt_n = Tex(r"$n$", font_size=30, color=BLACK).next_to(brace_1, 0.5 * UP)

        brace_2 = Brace(lower_group[:5], direction=[0, 1, 0], sharpness=1, color=BLACK)
        txt_n_2 = Tex(r"$n + 1$", font_size=30, color=BLACK).next_to(brace_2, 0.5 * UP)

        self.play(
            Create(brace_1),
            Write(txt_n),
            Create(brace_2),
            Write(txt_n_2)
        )

        self.wait(1)

        self.play(
            FadeOut(brace),
            FadeOut(brace_1),
            FadeOut(brace_2),
            FadeOut(txt_n),
            FadeOut(txt_2n),
            FadeOut(txt_n_2),
        )

        upper_group_copy = upper_group.copy()
        self.play(
            Rotate(upper_group_copy, PI),
            run_time=0.5   
        )
        self.play(
            upper_group_copy.animate.\
                next_to(lower_group, UP, aligned_edge=RIGHT, buff=0.05)
        )

        self.play(
            Rotate(upper_group, PI),
            run_time=0.5
        )
        self.play(
            upper_group.animate.\
                next_to(lower_group, LEFT, aligned_edge=DOWN, buff=0.05).\
                set_fill(RED, 0.2)
        )

        brace_3 = Brace(upper_group, direction=[0, -1, 0], sharpness=1, color=BLACK)
        txt_n_3 = Tex(r"$n$", font_size=30, color=BLACK).next_to(brace_3, 0.5 * DOWN)
        self.play(
            Create(brace_3),
            Write(txt_n_3)
        )

        big = VGroup(upper_group, lower_group, upper_group_copy)
        brace_3n = Brace(big, direction=[1, 0, 0], sharpness=1, color=BLACK)
        txt_3n_1 = Tex(r"$3n + 1$", font_size=30, color=BLACK).\
            rotate(-PI / 2).\
            next_to(brace_3n, 0.1 * RIGHT)
        self.play(
            Create(brace_3n),
            Write(txt_3n_1)
        )

        self.wait(1)

        # Write equation
        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, -2, 0])
        txt = Tex(
            r"$(2n + 1)^2 = T_{3n + 1} - T_{n}$",
            font_size=28, color=BLACK
        ).move_to([0, -2, 0])

        self.play(
            Create(rect),
            Write(txt)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"College Mathematics Journal,", font_size=30, color=BLACK),
            Tex(r"vol. 27, no. 2,", font_size=30, color=BLACK),
            Tex(r"(March 1996), p. 118.", font_size=30, color=BLACK)
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