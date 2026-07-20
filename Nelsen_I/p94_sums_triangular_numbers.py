"""
Visual proof of the sums of triangular numbers I.
Proofs without Words. Roger B. Nelsen. p. 94.
"""
import numpy as np

from manim import ThreeDScene
from manim import Create, Uncreate, Write
from manim import VGroup, FadeIn, FadeOut, FunctionGraph, Transform
from manim import MathTable, Brace, RoundedRectangle
from manim import Arrow, Cube, Line, Text, Tex

from manim import config
from manim import DEGREES, LEFT, RIGHT, DOWN, LIGHT, UP, PI

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


class Sums(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE

        txt_copy = Text(
            r"@chill.maths", font_size=12,
            font="CMU Typewriter Text", weight=LIGHT, color=BLACK
        ).to_edge(RIGHT + DOWN, buff=0.1)
        self.add(txt_copy)
        self.add_fixed_in_frame_mobjects(txt_copy)

        # Introduction text
        txt_title = [
            Tex(r"Somme des nombres", font_size=48, color=BLACK),
            Tex(r"triangulaires", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Monte J. Zerger", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        results = [
            Tex(r"Si $T_k = 1 + 2 + \cdots + k$,", font_size=24, color=BLACK),
            Tex(r"alors $\sum_{k = 1}^n T_k = \frac{1}{6}n(n+1)(n+2)$", font_size=24, color=BLACK),
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


        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine,", font_size=26, color=BLACK),
            Tex(r"vol. 63, no. 5 (Dec. 1990)", font_size=26, color=BLACK),
            Tex(r"p. 314.", font_size=26, color=BLACK),
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
