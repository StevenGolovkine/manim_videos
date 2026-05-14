"""
Visual proof of Recursion
Proofs without Words I. Roger B. Nelsen. p. 143.
"""
import numpy as np

from manim import MovingCameraScene, Scene, ManimColor
from manim import Create, Uncreate, Write, Transform, TransformFromCopy
from manim import VGroup, FadeIn, FadeOut , FunctionGraph, Rotate
from manim import Line, Square, Polygon, RoundedRectangle, Circle, Angle
from manim import line_intersection, DashedLine, RightAngle
from manim import Text, Tex, Intersection, LaggedStart

from manim import config
from manim import ORIGIN, LEFT, RIGHT, DOWN, LIGHT, UP, PI, DEGREES

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


class Trio(MovingCameraScene):
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
            Tex(r"Récursivité", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Shirley Wakin", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        self.add(
            txt_title,
            txt
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt)
        )

        # First elements
        square_size = 0.7
        bottom_left = Square(
            side_length=square_size, color=BLACK, fill_color=RED,
            fill_opacity=0.8, stroke_width=2
        )
        top_left = Square(
            side_length=square_size, color=BLACK, fill_color=RED,
            fill_opacity=0.8, stroke_width=2
        ).next_to(bottom_left, UP, buff=0)
        bottom_right = Square(
            side_length=square_size, color=BLACK, fill_color=RED,
            fill_opacity=0.8, stroke_width=2
        ).next_to(bottom_left, RIGHT, buff=0)

        l_shape = VGroup(bottom_left, top_left, bottom_right).\
            move_to([0, -0.25, 0])
        txt_A2 = Tex(r"$A_2 = 3$", font_size=24, color=BLACK).\
            move_to([0, -3, 0])
        self.play(
            Create(l_shape),
            Write(txt_A2)
        )
        self.wait(1)

        # Second elements
        reduction_factor = 0.75
        self.play(
            l_shape.animate.scale(reduction_factor).move_to([0, -0.6, 0])
        )

        l_shape_copy = l_shape.copy().rotate(-PI).\
            next_to(l_shape[2], UP, aligned_edge=RIGHT, buff=0)
        self.play(TransformFromCopy(l_shape, l_shape_copy))

        top_left_square = Square(
            side_length=square_size * reduction_factor, color=BLACK,
            fill_color=RED, fill_opacity=0.8, stroke_width=2
        ).next_to(l_shape_copy[2], UP, buff=0)
        self.play(Create(top_left_square))

        new_figure = VGroup(l_shape, l_shape_copy, top_left_square)

        txt_A3 = Tex(r"$A_3 = 2 A_2 + 1$", font_size=24, color=BLACK).\
            move_to([0, -3, 0])
        self.play(Transform(txt_A2, txt_A3))

        self.wait(1)

        # Third elements
        self.play(
            new_figure.animate.scale(reduction_factor).move_to([0, -0.9, 0])
        )

        new_figure_copy = new_figure.copy().rotate(-PI).\
            next_to(new_figure[1][0], UP, aligned_edge=RIGHT, buff=0)
        self.play(TransformFromCopy(new_figure, new_figure_copy))

        top_left_square_2 = Square(
            side_length=square_size * reduction_factor ** 2, color=BLACK,
            fill_color=RED, fill_opacity=0.8, stroke_width=2
        ).next_to(new_figure_copy, UP, aligned_edge=LEFT, buff=0)
        self.play(Create(top_left_square_2))

        new_figure_2 = VGroup(new_figure, new_figure_copy, top_left_square_2)

        txt_A4 = Tex(r"$A_4 = 2 A_3 + 1$", font_size=24, color=BLACK).\
            move_to([0, -3, 0])
        self.play(Transform(txt_A2, txt_A4))

        self.wait(1)

        # Fourth elements
        self.play(
            new_figure_2.animate.scale(reduction_factor).move_to([0, -1.1, 0])
        )

        new_figure_2_copy = new_figure_2.copy().rotate(-PI).\
            next_to(new_figure_2[1][0], UP, aligned_edge=RIGHT, buff=0)
        self.play(TransformFromCopy(new_figure_2, new_figure_2_copy))

        top_left_square_3 = Square(
            side_length=square_size * reduction_factor ** 3, color=BLACK,
            fill_color=RED, fill_opacity=0.8, stroke_width=2
        ).next_to(new_figure_2_copy, UP, aligned_edge=LEFT, buff=0)
        self.play(Create(top_left_square_3))

        new_figure_3 = VGroup(new_figure_2, new_figure_2_copy, top_left_square_3)

        txt_A5 = Tex(r"$A_5 = 2 A_4 + 1$", font_size=24, color=BLACK).\
            move_to([0, -3, 0])
        self.play(Transform(txt_A2, txt_A5))

        # Write general formula
        txt_general = Tex(
            r"$A_n = 2 A_{n-1} + 1 = 2^n - 1$", font_size=24, color=BLACK
        ).move_to([0, 3, 0])
        self.play(
            Write(txt_general)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine", font_size=30, color=BLACK),
            Tex(r"vol. 62, no. 3,", font_size=30, color=BLACK),
            Tex(r"(June 1994), p. 187.", font_size=30, color=BLACK),
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
