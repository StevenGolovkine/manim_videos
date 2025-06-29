"""
Visual proof of Sums of Products of Consecutive Integers.
Proofs without Words II. Roger B. Nelsen. p. 106.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import Brace, VGroup, FadeIn, FadeOut, FunctionGraph, Rotate
from manim import Text, Tex, Rectangle, RoundedRectangle, Transform

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
            Tex(r"Sur la somme des", font_size=48, color=BLACK),
            Tex(r"produits des entiers", font_size=48, color=BLACK),
            Tex(r"consécutifs", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"James O. Chilaka", font_size=36, color=BLACK),
        ]
        txt = VGroup(*txt).arrange(DOWN)

        results = [
            Tex(r"$\sum_{k = 1}^n k(k + 1)(k + 2) = \frac{n(n + 1)(n + 2)(n + 3)}{4}$",
            font_size=20, color=BLACK),
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


        # Rectangle
        rect = Rectangle(
            width=3, height=2, color=BLACK, fill_color=WHITE, fill_opacity=1,
            stroke_width=2
        ).move_to([0, 1.5, 0])
        txt_1 = Tex(
            r"$1 + 2 + \cdots + (k + 1) + (k + 2)$", font_size=20, color=BLACK
        ).next_to(rect, UP, buff=0.1)
        txt_2 = Tex(r"$1 + 2 + \cdots + k$", font_size=20, color=BLACK).\
            rotate(PI / 2).\
            next_to(rect, LEFT, buff=0.1)

        self.play(
            Create(rect),
            Write(txt_1),
            Write(txt_2),
            run_time=1
        )

        # Inside rectangle
        inside_rect1 = Rectangle(
            width=2, height=1, color=RED, fill_color=RED, fill_opacity=0.5,
            stroke_width=0
        ).align_to(rect, LEFT + DOWN)
        txt_inside1 = Tex(
            r"$1 + 2 + \cdots + k + (k +1 )$", font_size=15, color=BLACK
        ).next_to(inside_rect1, UP, buff=0.1)
        txt_inside11 = Tex(
            r"$k$", font_size=15, color=BLACK
        ).next_to(inside_rect1, LEFT, buff=-0.15)

        self.play(
            Create(inside_rect1),
            Write(txt_inside1),
            Write(txt_inside11),
        )

        inside_rect2 = Rectangle(
            width=1, height=2, color=BLUE, fill_color=BLUE, fill_opacity=0.5,
            stroke_width=0
        ).align_to(rect, RIGHT + DOWN)
        txt_inside2 = Tex(
            r"$k + 2$", font_size=15, color=BLACK
        ).next_to(inside_rect2, UP, buff=-0.2)

        self.play(
            Create(inside_rect2),
            Write(txt_inside2)
        )


        # Second rectangle
        rect2 = Rectangle(
            width=3, height=2, color=BLACK, fill_color=WHITE, fill_opacity=1,
            stroke_width=2
        ).move_to([0, -1.5, 0])
        txt_3 = Tex(
            r"$1 + 2 + \cdots + (n + 1) + (n + 2)$", font_size=20, color=BLACK
        ).next_to(rect2, UP, buff=0.1)
        txt_4 = Tex(r"$1 + 2 + \cdots + n$", font_size=20, color=BLACK).\
            rotate(PI / 2).\
            next_to(rect2, LEFT, buff=0.1)

        self.play(
            Create(rect2),
            Write(txt_3),
            Write(txt_4),
            run_time=1
        )

        # Inside rectangle
        inside_rect3 = Rectangle(
            width=1, height=0.25, color=RED, fill_color=RED, fill_opacity=0.5,
            stroke_width=0
        ).align_to(rect2, LEFT + UP)
        txt_5 = Tex(
            r"$1 \times 2 \times 3$", font_size=15, color=BLACK
        ).move_to(inside_rect3.get_center_of_mass())
        self.play(
            Create(inside_rect3),
            Write(txt_5)
        )

        inside_rect7 = Rectangle(
            width=2.25, height=0.75, color=RED, fill_color=RED, fill_opacity=0.5,
            stroke_width=0
        ).align_to(rect2, LEFT + DOWN)
        inside_rect8 = Rectangle(
            width=0.75, height=2, color=RED, fill_color=RED, fill_opacity=0.5,
            stroke_width=0
        ).align_to(rect2, RIGHT + DOWN)
        inside_rect_n = VGroup(inside_rect7, inside_rect8)
        txt_n = Tex(
            r"$n(n + 1)(n + 2)$", font_size=15, color=BLACK
        ).move_to(inside_rect7.get_center_of_mass() + [0.75, 0, 0])

        self.play(
            Create(inside_rect_n),
            Write(txt_n)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine,", font_size=30, color=BLACK),
            Tex(r"vol. 69, no. 1,", font_size=30, color=BLACK),
            Tex(r"(Feb. 1996), p. 63.", font_size=30, color=BLACK)
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