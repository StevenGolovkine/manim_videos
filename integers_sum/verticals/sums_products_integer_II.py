"""
Visual proof of Sums of Products of Consecutive Integers I .
Proofs without Words II. Roger B. Nelsen. p. 105.
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
            Tex(r"James O. Chilaka", font_size=28, color=BLACK),
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

        # Modify txt
        txt_12 = Tex(
            r"$\frac{(k + 2)(k + 3)}{2}$", font_size=20, color=BLACK
        ).next_to(rect, UP, buff=0.1)
        txt_22 = Tex(r"$\frac{k(k + 1)}{2}$", font_size=20, color=BLACK).\
            rotate(PI / 2).\
            next_to(rect, LEFT, buff=0.1)
        self.play(
            Transform(txt_1, txt_12),
            Transform(txt_2, txt_22),
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

        txt_inside12 = Tex(
            r"$\frac{(k + 1)(k + 2)}{2}$", font_size=15, color=BLACK
        ).next_to(inside_rect1, UP, buff=0.1)
        self.play(
            Transform(txt_inside1, txt_inside12),
        )

        txt_inside13 = Tex(
            r"$k\frac{(k + 1)(k + 2)}{2}$", font_size=15, color=BLACK
        ).move_to(inside_rect1.get_center_of_mass())
        self.play(
            Write(txt_inside13)
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

        txt_inside21 = Tex(
            r"$(k + 2)\frac{k(k + 1)}{2}$", font_size=15, color=BLACK
        ).move_to(inside_rect2.get_center_of_mass())
        self.play(
            Write(txt_inside21)
        )

        # Area inside rectangle
        inside_rect3 = inside_rect2.copy().set_color(RED)
        inside_rect = VGroup(inside_rect1.copy(), inside_rect3)
        txt_inside3 = Tex(
            r"$k(k + 1)(k + 2)$", font_size=15, color=BLACK
        ).move_to(inside_rect.get_center_of_mass() + [0.25, -0.25, 0])
        self.play(
            FadeOut(txt_inside1),
            FadeOut(txt_inside11),
            FadeOut(txt_inside2),
            FadeOut(txt_inside13),
            FadeOut(txt_inside21),
            Uncreate(inside_rect1),
            Uncreate(inside_rect2),
            Create(inside_rect),
            Write(txt_inside3)
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

        inside_rect4 = Rectangle(
            width=1, height=0.35, color=BLUE, fill_color=BLUE, fill_opacity=0.5,
            stroke_width=0
        ).\
            next_to(inside_rect3, DOWN, buff=0).\
            align_to(inside_rect3, LEFT)
        inside_rect5 = Rectangle(
            width=0.25, height=0.6, color=BLUE, fill_color=BLUE, fill_opacity=0.5,
            stroke_width=0
        ).\
            next_to(inside_rect3, RIGHT, buff=0).\
            align_to(inside_rect3, UP)
        inside_rect_4 = VGroup(inside_rect4, inside_rect5)
        txt_6 = Tex(
            r"$2 \times 3 \times 4$", font_size=15, color=BLACK
        ).move_to(inside_rect4.get_center_of_mass() + [0.25, 0, 0])
        self.play(
            Create(inside_rect_4),
            Write(txt_6)
        )

        inside_rect6 = Rectangle(
            width=1.25, height=0.35, color=RED, fill_color=RED, fill_opacity=0.5,
            stroke_width=0
        ).\
            next_to(inside_rect_4, DOWN, buff=0).\
            align_to(inside_rect_4, LEFT)
        inside_rect61 = Rectangle(
            width=0.5, height=0.95, color=RED, fill_color=RED, fill_opacity=0.5,
            stroke_width=0
        ).\
            next_to(inside_rect_4, RIGHT, buff=0).\
            align_to(inside_rect_4, UP)
        inside_rect_5 = VGroup(inside_rect6, inside_rect61)
        txt_7 = Tex(
            r"$3 \times 4 \times 5$", font_size=15, color=BLACK
        ).move_to(inside_rect6.get_center_of_mass() + [0.25, 0, 0])
        self.play(
            Create(inside_rect_5),
            Write(txt_7)
        )

        inside_rect8 = Rectangle(
            width=1.75, height=0.3, color=BLUE, fill_color=BLUE, fill_opacity=0.5,
            stroke_width=0
        ).\
            next_to(inside_rect_5, DOWN, buff=0).\
            align_to(inside_rect_5, LEFT)
        inside_rect81 = Rectangle(
            width=0.5, height=1.25, color=BLUE, fill_color=BLUE, fill_opacity=0.5,
            stroke_width=0
        ).\
            next_to(inside_rect_5, RIGHT, buff=0).\
            align_to(inside_rect_5, UP)
        inside_rect_8 = VGroup(inside_rect8, inside_rect81)
        txt_8 = Tex(
            r"$\dots$", font_size=15, color=BLACK
        ).move_to(inside_rect8.get_center_of_mass() + [0.25, 0, 0])
        self.play(
            Create(inside_rect_8),
            Write(txt_8)
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

        # Transform txt
        txt_3_2 = Tex(
            r"$\frac{(n + 2)(n + 3)}{2}$", font_size=20, color=BLACK
        ).next_to(rect2, UP, buff=0.1)
        txt_4_2 = Tex(r"$\frac{n(n + 1)}{2}$", font_size=20, color=BLACK).\
            rotate(PI / 2).\
            next_to(rect2, LEFT, buff=0.1)
        self.play(
            Transform(txt_3, txt_3_2),
            Transform(txt_4, txt_4_2),
        )

        # Write the final result
        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, 0.5, 0])
        txt = Tex(
            r"$1 \cdot 2 \cdot 3 + 2 \cdot 3 \cdot 4$",
            r"$+ \dots + n(n + 1)(n + 2)$",
            r"$= \frac{n(n + 1)(n +2)(n + 3)}{4}$",
            font_size=15, color=BLACK
         ).move_to([0, 0.5, 0])

        rect.z_index = 0
        txt.z_index = 1
        self.play(
            Create(rect),
            Write(txt),
            run_time=0.5
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine,", font_size=30, color=BLACK),
            Tex(r"vol. 67, no. 5,", font_size=30, color=BLACK),
            Tex(r"(Dec. 1994), p. 365.", font_size=30, color=BLACK)
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
