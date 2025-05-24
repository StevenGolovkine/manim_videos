"""
Visual proof of the sums of cubes.
Proofs without Words I. Roger B. Nelsen. p. 87.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Dot, BraceBetweenPoints, RoundedRectangle, Square
from manim import Create, Uncreate, Write
from manim import VGroup, TransformFromCopy, FadeIn, FadeOut, FunctionGraph
from manim import Text, Tex

from manim import config

from manim import LEFT, RIGHT, DOWN, LIGHT

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
            Tex(r"Somme des cubes", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration I", font_size=36, color=BLACK),
            Tex(r"Cupillari and Lushbaugh", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        txt_formula = Tex(r"$1^3 + 2^3 + \cdots + n = \frac{1}{4}n^2(n + 1)^2$", font_size=28, color=BLACK)\
            .next_to(txt, 2 * DOWN)

        self.add(
            txt_title,
            txt,
            txt_formula
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt),
            Uncreate(txt_formula),
            run_time=0.5
        )
        self.wait(0.5)

        # Create small squares
        
        s_25 = 25 * [Square(side_length=0.1, color=BLUE, fill_opacity=1)]
        s_16 = 16 * [Square(side_length=0.1, color=VIOLET, fill_opacity=1)]
        s_9 = 9 * [Square(side_length=0.1, color=RED, fill_opacity=1)]
        s_4 = 4 * [Square(side_length=0.1, color=GREEN, fill_opacity=1)]
        s_1 = [Square(side_length=0.1, color=YELLOW, fill_opacity=1)]

        s1 = Square(side_length=0.1, color=BLUE, fill_opacity=1)
        s2 = Square(side_length=0.5, color=VIOLET, fill_opacity=1)
        s3 = Square(side_length=0.5, color=RED, fill_opacity=1)
        s4 = Square(side_length=0.5, color=GREEN, fill_opacity=1)

        self.play(
            FadeIn(s1),
            FadeIn(s2),
            FadeIn(s3),
            FadeIn(s4),
        )

        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine, vol. 62,", font_size=30, color=BLACK),
            Tex(r"no. 4 (Oct. 1989), p.259.", font_size=30, color=BLACK),
            Tex(r"Mathematical Gazette, vol. 49", font_size=30, color=BLACK),
            Tex(r"no. 368 (May 1965), p.200", font_size=30, color=BLACK),
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
