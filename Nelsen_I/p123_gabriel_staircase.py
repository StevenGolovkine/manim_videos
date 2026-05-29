"""
Visual proof of the Gabriel's staircase.
Proofs without Words I. Roger B. Nelsen. p. 123.
"""
import numpy as np

from manim import MovingCameraScene
from manim import DashedLine, Line, Arrow 
from manim import Create, Uncreate, Write
from manim import VGroup, Transform, FadeIn, FadeOut, FunctionGraph, BraceBetweenPoints
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

class Proof(MovingCameraScene):
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
            Tex(r"L'escalier de", font_size=48, color=BLACK),
            Tex(r"Gabriel", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Stuart G. Swain", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        txt_formula = Tex(r"$\sum_{k = 1}^{\infty} kr^k = \frac{r}{(1-r)^2}$", font_size=28, color=BLACK)\
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


        # Staircase
        baseline = Line([-1.75, -1, 0], [1.75, -1, 0], color=BLACK, stroke_width=2)
        right_arrow = Arrow(
            start=[1.75, -1, 0], end=[1.75, 3, 0], buff=0,
            color=BLACK, stroke_width=2, max_tip_length_to_length_ratio=0.05
        )

        self.play(
            Create(baseline),
            Create(right_arrow)
        )

        # Create the staircase
        line_1 = Line([-1.75, -1, 0], [-1.75, 0, 0], color=BLACK, stroke_width=2)
        txt_1 = Tex(r"$1$", font_size=24, color=BLACK).next_to(line_1.get_center(), LEFT, buff=0.05)
        self.play(
            Create(line_1),
            Write(txt_1)
        )

        line_2 = Line([-1.75, 0, 0], [-0.65, 0, 0], color=BLACK, stroke_width=2)
        txt_2 = Tex(r"$r$", font_size=24, color=BLACK).next_to(line_2.get_center(), UP, buff=0.05)
        self.play(
            Create(line_2),
            Write(txt_2)
        )

        line_3 = Line([-0.65, 0, 0], [-0.65, 1, 0], color=BLACK, stroke_width=2)
        txt_3 = Tex(r"$1$", font_size=24, color=BLACK).next_to(line_3.get_center(), LEFT, buff=0.05)
        self.play(
            Create(line_3),
            Write(txt_3)
        )

        line_4 = Line([-0.65, 1, 0], [0.1, 1, 0], color=BLACK, stroke_width=2)
        txt_4 = Tex(r"$r^2$", font_size=24, color=BLACK).next_to(line_4.get_center(), UP, buff=0.05)
        self.play(
            Create(line_4),
            Write(txt_4)
        )

        line_5 = Line([0.1, 1, 0], [0.1, 2, 0], color=BLACK, stroke_width=2)
        txt_5 = Tex(r"$1$", font_size=24, color=BLACK).next_to(line_5.get_center(), LEFT, buff=0.05)
        self.play(
            Create(line_5),
            Write(txt_5)
        )

        line_6 = Line([0.1, 2, 0], [0.7, 2, 0], color=BLACK, stroke_width=2)
        txt_6 = Tex(r"$r^3$", font_size=24, color=BLACK).next_to(line_6.get_center(), UP, buff=0.05)
        self.play(
            Create(line_6),
            Write(txt_6)
        )

        arrow = Arrow(
            start=[0.7, 2, 0], end=[0.7, 3, 0], buff=0,
            color=BLACK, stroke_width=2, max_tip_length_to_length_ratio=0.1
        )
        self.play(Create(arrow))

        # Dashed lines
        dashed_line_1 = DashedLine([-0.65, -1, 0], [-0.65, 0, 0], color=BLACK, stroke_width=2)
        dashed_line_2 = DashedLine([0.1, -1, 0], [0.1, 1, 0], color=BLACK, stroke_width=2)
        dashed_line_3 = DashedLine([0.7, -1, 0], [0.7, 2, 0], color=BLACK, stroke_width=2)
        txt_dots = Tex(r"$\cdots$", font_size=24, color=BLACK).move_to([1.25, 1, 0])

        txt_sum = Tex(r"$\sum_{k=1}^{\infty} kr^k$", font_size=28, color=BLACK).move_to([-1, -2, 0])
        self.play(
            Create(dashed_line_1),
            Create(dashed_line_2),
            Create(dashed_line_3),
            Write(txt_dots),
            Write(txt_sum)
        )
        self.wait(1)
        self.play(
            Uncreate(dashed_line_1),
            Uncreate(dashed_line_2),
            Uncreate(dashed_line_3),
            Uncreate(txt_dots),
        )


        dashed_line_4 = DashedLine([-0.65, 0, 0], [1.75, 0, 0], color=BLACK, stroke_width=2)
        dashed_line_5 = DashedLine([0.1, 1, 0], [1.75, 1, 0], color=BLACK, stroke_width=2)
        dashed_line_6 = DashedLine([0.7, 2, 0], [1.75, 2, 0], color=BLACK, stroke_width=2)
        txt_dots_2 = Tex(r"$\vdots$", font_size=24, color=BLACK).move_to([1.25, 2.5, 0])

        txt_sum_2 = Tex(r"$ = \sum_{k = 1}^{\infty} \sum_{i=k}^{\infty} r^i$", font_size=28, color=BLACK).next_to(txt_sum, RIGHT, buff=0.1)
        self.play(
            Create(dashed_line_4),
            Create(dashed_line_5),
            Create(dashed_line_6),
            Write(txt_dots_2),
            Write(txt_sum_2)
        )
        self.wait(1)
        txt_sum_3 = Tex(r"$= \frac{r}{(1-r)^2}$", font_size=28, color=BLACK).next_to(txt_sum, RIGHT, buff=0.1)
        self.play(Transform(txt_sum_2, txt_sum_3))


        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine, vol. 67,", font_size=30, color=BLACK),
            Tex(r"no. 3 (June 1994), p.209.", font_size=30, color=BLACK),
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
