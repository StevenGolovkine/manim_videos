"""
Visual proof of the arithmetic mean - geometric mean inequality for three positive
numbers.
Proofs without Words II. Roger B. Nelsen. p. 74.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Rectangle
from manim import Text, Tex

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


class Mean(MovingCameraScene):
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
            Tex(r"Une inégalité", font_size=48, color=BLACK),
            Tex(r"de moyennes", font_size=48, color=BLACK),
            Tex(r"pour 3 nombres", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Claudi Alsina", font_size=28, color=BLACK)
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

        # Square
        rect_a = Rectangle(width=2, height=2, color=BLUE, fill_opacity=0.5)
        rect_b = Rectangle(width=1, height=1, color=VIOLET, fill_opacity=0.5).\
            next_to(rect_a, DOWN, buff=0).\
            align_to(rect_a, LEFT)
        rect_c = Rectangle(width=0.5, height=0.5, color=RED, fill_opacity=0.5).\
            next_to(rect_b, DOWN, buff=0).\
            align_to(rect_a, LEFT)
                
        self.play(
            FadeIn(rect_a),
            FadeIn(rect_b),
            FadeIn(rect_c)
        )

        # Rectangles
        rect_ab = Rectangle(width=2, height=1, color=GREEN, fill_opacity=0.5).\
            align_to(rect_a, UP)
        rect_bc = Rectangle(width=1, height=0.5, color=YELLOW, fill_opacity=0.5).\
            next_to(rect_ab, DOWN, buff=0).\
            align_to(rect_a, LEFT)
        rect_ac = Rectangle(width=0.5, height=2, color=ORANGE, fill_opacity=0.5).\
            next_to(rect_bc, DOWN, buff=0).\
            align_to(rect_a, LEFT)

        self.play(
            FadeIn(rect_ab),
            FadeIn(rect_bc),
            FadeIn(rect_ac)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine, vol. 73,", font_size=26, color=BLACK),
            Tex(r"no. 2 (April 2000), p.97", font_size=26, color=BLACK)
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