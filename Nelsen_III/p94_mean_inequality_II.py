"""
Visual proof of the arithmetic mean - geometric mean inequality VIII.
Proofs without Words III. Roger B. Nelsen. p. 94.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, TransformFromCopy
from manim import TransformMatchingTex
from manim import VGroup, FadeIn, FadeOut, FunctionGraph, Polygon
from manim import Text, Tex, MathTex, Line, Arc, Circle, Angle, DoubleArrow, Dot

from manim import config
from manim import LEFT, RIGHT, DOWN, LIGHT, UP, PI, DEGREES

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
            Tex(r"par trigonométrie", font_size=48, color=BLACK),
            Tex(r"Partie II", font_size=24, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Roger B. Nelsen", font_size=28, color=BLACK)
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

        statement = MathTex(
            r"a,b>0",
            r"\Longrightarrow",
            r"\frac{a+b}{2}\geq\sqrt{ab}",
            font_size=29,
            color=BLACK,
        ).move_to([0, 3.35, 0])
        statement.scale_to_fit_width(4.05)

        base_y = 0.40
        A = np.array([-1.78, base_y, 0])
        B = np.array([1.48, base_y, 0])
        C = np.array([1.48, 2.13, 0])

        triangle_fill = Polygon(
            A, B, C,
            fill_color=BLUE,
            fill_opacity=0.22,
            stroke_width=0,
        )
        base = Line(A, B, color=BLACK, stroke_width=2.0)
        vertical_side = Line(B, C, color=BLACK, stroke_width=2.0)
        hypotenuse = Line(A, C, color=BLACK, stroke_width=2.0)

        right_size = 0.16
        right_corner = B + right_size * (LEFT + UP)
        right_angle = VGroup(
            Line(B + right_size * LEFT, right_corner,
                 color=BLACK, stroke_width=1.5),
            Line(right_corner, B + right_size * UP,
                 color=BLACK, stroke_width=1.5),
        )

        x_value = np.arctan2(C[1] - A[1], C[0] - A[0])
        angle_x = Angle(
            Line(A, B),
            Line(A, C),
            radius=0.34,
            color=BLACK,
            stroke_width=1.5,
        )
        label_x = MathTex(r"x", font_size=24, color=BLACK).move_to(
            A + 0.48 * np.array([
                np.cos(x_value / 2), np.sin(x_value / 2), 0
            ])
        )

        label_sqrt_b = MathTex(
            r"\sqrt b", font_size=27, color="#BC7042"
        ).next_to(base, DOWN, buff=0.12)
        label_sqrt_a = MathTex(
            r"\sqrt a", font_size=27, color="#3F91BB"
        ).next_to(vertical_side, RIGHT, buff=0.12)

        previous_result = MathTex(
            r"\tan x", r"+", r"\cot x", r"\geq 2",
            font_size=25,
            color=BLACK,
        ).move_to([0, -1.45, 0])
        previous_result[0].set_color("#3F91BB")
        previous_result[2].set_color("#BC7042")

        ratio_inequality = MathTex(
            r"\frac{\sqrt a}{\sqrt b}",
            r"+",
            r"\frac{\sqrt b}{\sqrt a}",
            r"\geq 2",
            font_size=25,
            color=BLACK,
        )
        ratio_inequality[0].set_color("#3F91BB")
        ratio_inequality[2].set_color("#BC7042")
        implication = MathTex(
            r"\Longrightarrow", font_size=25, color=BLACK
        )
        conclusion = MathTex(
            r"\frac{a+b}{2}\geq\sqrt{ab}",
            font_size=25,
            color=BLACK,
        )
        derivation = VGroup(
            ratio_inequality, implication, conclusion
        ).arrange(RIGHT, buff=0.20)
        derivation.scale_to_fit_width(4.05).move_to([0, -1.45, 0])

        self.play(Write(statement), run_time=1.0)
        self.wait(0.5)
        self.play(
            FadeIn(triangle_fill),
            Create(base),
            Create(vertical_side),
            Create(hypotenuse),
            run_time=1.2,
        )
        self.play(FadeIn(right_angle), run_time=0.5)
        self.play(
            Create(angle_x),
            Write(label_x),
            Write(label_sqrt_a),
            Write(label_sqrt_b),
            run_time=1.0,
        )
        self.wait(0.5)
        self.play(Write(previous_result), run_time=0.8)
        self.wait(0.5)
        self.play(
            TransformMatchingTex(
                previous_result,
                ratio_inequality,
                transform_mismatches=True,
            ),
            run_time=1.2,
        )
        self.play(
            Write(implication),
            Write(conclusion),
            run_time=1.0,
        )
        self.wait(2)

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"College Mathematics Journal,", font_size=26, color=BLACK),
            Tex(r"vol. 46, no. 1 (Jan. 2015), p.42", font_size=26, color=BLACK)
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
