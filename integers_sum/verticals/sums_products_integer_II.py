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
            Tex(r"$\sum_{k = 1}^n k(k + 1) = \frac{n(n + 1)(n + 2)}{3}$",
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
            r"$1 + 2 + \cdots + n$", font_size=20, color=BLACK
        ).next_to(rect, UP, buff=0.1)
        txt_2 = Tex(r"$n + 2$", font_size=20, color=BLACK).\
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
            r"$\frac{n(n + 1)}{2}$", font_size=20, color=BLACK
        ).next_to(rect, UP, buff=0.1)
        self.play(
            Transform(txt_1, txt_12),
        )

        # Inside rectangle
        inside_rect1 = Rectangle(
            width=3, height=0.25, color=BLACK, fill_color=RED, fill_opacity=0.5,
            stroke_width=0.1
        ).align_to(rect, LEFT + UP)
        txt_inside1 = Tex(
            r"$1 + 2 + \cdots + n$", font_size=15, color=BLACK
        ).move_to(inside_rect1.get_center_of_mass())

        self.play(
            Create(inside_rect1),
            Write(txt_inside1),
        )

        inside_rect2 = Rectangle(
            width=2, height=0.25, color=BLACK, fill_color=RED, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect1, DOWN, buff=0).align_to(inside_rect1, LEFT)
        txt_inside2 = Tex(
            r"$\cdots$", font_size=15, color=BLACK
        ).move_to(inside_rect2.get_center_of_mass())
        self.play(
            Create(inside_rect2),
            Write(txt_inside2),
        )

        inside_rect3 = Rectangle(
            width=1, height=0.25, color=BLACK, fill_color=RED, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect2, DOWN, buff=0).align_to(inside_rect2, LEFT)
        txt_inside3 = Tex(
            r"$1 + 2 + 3$", font_size=15, color=BLACK
        ).move_to(inside_rect3.get_center_of_mass())
        self.play(
            Create(inside_rect3),
            Write(txt_inside3),
        )

        inside_rect4 = Rectangle(
            width=0.5, height=0.25, color=BLACK, fill_color=RED, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect3, DOWN, buff=0).align_to(inside_rect3, LEFT)
        txt_inside4 = Tex(
            r"$1 + 2$", font_size=15, color=BLACK
        ).move_to(inside_rect4.get_center_of_mass())
        self.play(
            Create(inside_rect4),
            Write(txt_inside4),
        )

        inside_rect5 = Rectangle(
            width=0.25, height=0.25, color=BLACK, fill_color=RED, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect4, DOWN, buff=0).align_to(inside_rect4, LEFT)
        txt_inside5 = Tex(
            r"$1$", font_size=15, color=BLACK
        ).move_to(inside_rect5.get_center_of_mass())
        self.play(
            Create(inside_rect5),
            Write(txt_inside5),
        )

        inside_rect6 = Rectangle(
            width=0.25, height=0.75, color=BLACK, fill_color=BLUE, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect5, DOWN, buff=0).align_to(inside_rect5, LEFT)
        txt_inside6 = Tex(
            r"$1 \cdot 2$", font_size=15, color=BLACK
        ).rotate(PI / 2).move_to(inside_rect6.get_center_of_mass())
        self.play(
            Create(inside_rect6),
            Write(txt_inside6)
        )

        inside_rect7 = Rectangle(
            width=0.25, height=1, color=BLACK, fill_color=BLUE, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect6, RIGHT, buff=0).align_to(inside_rect6, DOWN)
        txt_inside7 = Tex(
            r"$2 \cdot 3$", font_size=15, color=BLACK
        ).rotate(PI / 2).move_to(inside_rect7.get_center_of_mass())
        self.play(
            Create(inside_rect7),
            Write(txt_inside7)
        )

        inside_rect8 = Rectangle(
            width=0.5, height=1.25, color=BLACK, fill_color=BLUE, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect7, RIGHT, buff=0).align_to(inside_rect7, DOWN)
        txt_inside8 = Tex(
            r"$3 \cdot 4$", font_size=15, color=BLACK
        ).rotate(PI / 2).move_to(inside_rect8.get_center_of_mass())
        self.play(
            Create(inside_rect8),
            Write(txt_inside8)
        )

        inside_rect9 = Rectangle(
            width=1, height=1.5, color=BLACK, fill_color=BLUE, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect8, RIGHT, buff=0).align_to(inside_rect8, DOWN)
        txt_inside9 = Tex(
            r"$\cdots$", font_size=15, color=BLACK
        ).rotate(PI / 2).move_to(inside_rect9.get_center_of_mass())
        self.play(
            Create(inside_rect9),
            Write(txt_inside9)
        )

        inside_rect10 = Rectangle(
            width=1, height=1.75, color=BLACK, fill_color=BLUE, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect9, RIGHT, buff=0).align_to(inside_rect9, DOWN)
        txt_inside10 = Tex(
            r"$n \cdot (n+1)$", font_size=15, color=BLACK
        ).rotate(PI / 2).move_to(inside_rect10.get_center_of_mass())
        self.play(
            Create(inside_rect10),
            Write(txt_inside10)
        )


        # Transform txt
        txt_1 = Tex(
            r"$T_k = 1 + 2 + \cdots + k \Longrightarrow$", font_size=20, color=BLACK
        ).move_to([-0.5, 0, 0])
        self.play(
            Write(txt_1)
        )

        txt_21 = Tex(
            r"$1 \cdot 2 + \cdots +  n(n+1) + (T_1 + \cdots + T_k)$",
            font_size=20, color=BLACK
        )
        txt_22 = Tex(
            r"$= \frac{n(n + 1)(n + 2)}{2}$",
            font_size=20, color=BLACK
        )
        txt_2 = VGroup(txt_21, txt_22).\
            arrange(DOWN).\
            move_to([0, -0.75, 0])
        self.play(
            Write(txt_2)
        )

        txt_3 = Tex(
            r"Or $T_1 + \cdots + T_k = \frac{1 \cdot 2 + \cdots +  n(n+1)}{2}$",
            font_size=20, color=BLACK
        ).move_to([0, -1.5, 0])
        self.play(
            Write(txt_3)
        )

        txt_4 = Tex(
            r"Donc $\frac{3}{2}(1 \cdot 2 + \cdots +  n(n+1)) = \frac{n(n + 1)(n + 2)}{2}$",
            font_size=20, color=BLACK
        ).move_to([0, -2.25, 0])
        self.play(
            Write(txt_4)
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
