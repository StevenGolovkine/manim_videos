"""
Visual proof of the gaussian quadrature as the area of either trapezoid
Proofs without Words I. Roger B. Nelsen. p. 136.
"""
import numpy as np

from manim import MovingCameraScene
from manim import (
    Dot, RoundedRectangle, Polygon, RightAngle, Line, Arc,
    Arrow, DashedLine, ParametricFunction,
)
from manim import Create, Uncreate, Write
from manim import VGroup, Transform, FadeIn, FadeOut, FunctionGraph
from manim import Text, Tex, MathTex

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

class Quadrature(MovingCameraScene):
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
            Tex(r"Quadrature de", font_size=48, color=BLACK),
            Tex(r"Gauss comme aire", font_size=48, color=BLACK),
            Tex(r"de trapèzes", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Mike Akerman", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        self.add(
            txt_title,
            txt            
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt),
            run_time=0.5
        )
        self.wait(0.5)

        axis_y = -1.20
        a = -1.35
        b = 1.40
        midpoint = (a + b) / 2
        node_offset = (b - a) / (2 * np.sqrt(3))
        a_bar = midpoint - node_offset
        b_bar = midpoint + node_offset

        def h(x):
            return 1.00 - 0.45 * (x - midpoint)

        def f_inside(x):
            return h(x) + 0.65 * (
                (x - a_bar) * (x - b_bar) * (x - midpoint)
            )

        f_a = f_inside(a)
        f_b = f_inside(b)

        def f(x):
            if x < a:
                return f_a + 1.50 * (x - a)
            if x > b:
                return f_b + 1.80 * (x - b)
            return f_inside(x)

        f_a_bar = f(a_bar)
        f_b_bar = f(b_bar)

        def trapezoid_top(x):
            return f_a_bar + (
                (f_b_bar - f_a_bar) * (x - a) / (b - a)
            )

        formula = MathTex(
            r"\frac12(b-a)\bigl(f(\bar a)+f(\bar b)\bigr)",
            r"=",
            r"\frac12(b-a)\bigl(h(a)+h(b)\bigr)",
            font_size=25,
            color=BLACK,
        ).move_to([0, -2.35, 0])
        formula.scale_to_fit_width(4.05)

        x_axis = Arrow(
            [-2.02, axis_y, 0],
            [2.05, axis_y, 0],
            buff=0,
            tip_length=0.15,
            stroke_width=2.1,
            color=BLACK,
        )
        y_axis = Arrow(
            [-1.83, axis_y - 0.14, 0],
            [-1.83, 2.35, 0],
            buff=0,
            tip_length=0.15,
            stroke_width=2.1,
            color=BLACK,
        )
        x_axis_label = MathTex(
            "x", font_size=24, color=BLACK
        ).next_to(x_axis.get_end(), RIGHT, buff=0.07)
        y_axis_label = MathTex(
            "y", font_size=24, color=BLACK
        ).next_to(y_axis.get_end(), UP, buff=0.05)

        function_curve = ParametricFunction(
            lambda t: np.array([t, f(t), 0]),
            t_range=[a - 0.18, b + 0.18],
            color=BLACK,
            stroke_width=2.5,
        )
        h_line = Line(
            [a - 0.18, h(a - 0.18), 0],
            [b + 0.18, h(b + 0.18), 0],
            color=RED,
            stroke_width=2.0,
        )
        trapezoid_line = Line(
            [a, trapezoid_top(a), 0],
            [b, trapezoid_top(b), 0],
            color=BLACK,
            stroke_width=1.8,
        )

        node_height_lines = VGroup(
            Line(
                [a, f_a_bar, 0],
                [a_bar, f_a_bar, 0],
                color=BLACK,
                stroke_width=1.4,
            ),
            Line(
                [b_bar, f_b_bar, 0],
                [b, f_b_bar, 0],
                color=BLACK,
                stroke_width=1.4,
            ),
        )

        endpoint_lines = VGroup(
            Line(
                [a, axis_y, 0],
                [a, max(h(a), f(a), trapezoid_top(a)), 0],
                color=BLACK,
                stroke_width=1.6,
            ),
            Line(
                [b, axis_y, 0],
                [b, max(h(b), f(b), trapezoid_top(b)), 0],
                color=BLACK,
                stroke_width=1.6,
            ),
        )
        node_lines = VGroup(
            DashedLine(
                [a_bar, axis_y, 0],
                [a_bar, f_a_bar, 0],
                dash_length=0.09,
                dashed_ratio=0.58,
                color=BLACK,
                stroke_width=1.7,
            ),
            DashedLine(
                [b_bar, axis_y, 0],
                [b_bar, f_b_bar, 0],
                dash_length=0.09,
                dashed_ratio=0.58,
                color=BLACK,
                stroke_width=1.7,
            ),
        )

        def colored_polygon(vertices, fill_color=BLUE):
            return Polygon(
                *vertices,
                color=BLACK,
                stroke_width=0,
                fill_color=fill_color,
                fill_opacity=0.55,
            )

        left_wedge = colored_polygon([
            np.array([a, h(a), 0]),
            np.array([a, f_a_bar, 0]),
            np.array([a_bar, f_a_bar, 0]),
        ])
        right_wedge = colored_polygon([
            np.array([b, h(b), 0]),
            np.array([b, f_b_bar, 0]),
            np.array([b_bar, f_b_bar, 0]),
        ])
        middle_region = colored_polygon([
            np.array([a, f_a_bar, 0]),
            np.array([a_bar, f_a_bar, 0]),
            np.array([b_bar, f_b_bar, 0]),
            np.array([b, f_b_bar, 0]),
        ], fill_color=VIOLET)

        tick_marks = VGroup()
        for tick_center in ((a + a_bar) / 2, (b_bar + b) / 2):
            tick_marks.add(
                Line(
                    [tick_center - 0.035, axis_y - 0.08, 0],
                    [tick_center + 0.035, axis_y + 0.08, 0],
                    color=BLACK,
                    stroke_width=1.7,
                ),
                Line(
                    [tick_center + 0.035, axis_y - 0.08, 0],
                    [tick_center + 0.105, axis_y + 0.08, 0],
                    color=BLACK,
                    stroke_width=1.7,
                ),
            )

        x_labels = VGroup(
            MathTex("a", font_size=20, color=BLACK).move_to([
                a, axis_y - 0.23, 0
            ]),
            MathTex(r"\bar a", font_size=20, color=BLACK).move_to([
                a_bar, axis_y - 0.23, 0
            ]),
            MathTex(r"\bar b", font_size=20, color=BLACK).move_to([
                b_bar, axis_y - 0.23, 0
            ]),
            MathTex("b", font_size=20, color=BLACK).move_to([
                b, axis_y - 0.23, 0
            ]),
        )

        function_label = MathTex(
            r"y=f(x)", font_size=20, color=BLACK
        ).move_to([1.28, f(1.28) + 0.8, 0])
        h_label = MathTex(
            r"y=h(x)", font_size=20, color=RED
        ).move_to([0.5, h(0.5) + 0.4, 0])

        point_labels = VGroup(
            MathTex(
                r"(a,h(a))", font_size=15, color=BLACK
            ).move_to([a + 0.20, h(a) + 0.30, 0]),
            MathTex(
                r"(a,f(\bar a))", font_size=15, color=BLACK
            ).move_to([a - 0.32, f_a_bar + 0.02, 0]),
            MathTex(
                r"(\bar a,f(\bar a))", font_size=15, color=BLACK
            ).move_to([a_bar + 0.23, f_a_bar + 0.28, 0]),
            MathTex(
                r"(\bar b,f(\bar b))", font_size=15, color=BLACK
            ).move_to([b_bar - 0.24, f_b_bar - 0.35, 0]),
            MathTex(
                r"(b,f(\bar b))", font_size=15, color=BLACK
            ).move_to([b + 0.25, f_b_bar + 0.25, 0]),
            MathTex(
                r"(b,h(b))", font_size=15, color=BLACK
            ).move_to([b + 0.28, h(b) - 0.03, 0]),
        )
        for label in point_labels:
            label.add_background_rectangle(
                color=WHITE, opacity=0.90, buff=0.025
            )

        self.play(
            Create(x_axis),
            Create(y_axis),
            Write(x_axis_label),
            Write(y_axis_label),
        )
        self.play(
            Create(function_curve),
            Write(function_label),
            run_time=1.5,
        )
        self.play(
            Create(h_line),
            Write(h_label),
        )
        self.wait(0.5)
        self.play(
            Create(endpoint_lines),
            Write(x_labels[0]),
            Write(x_labels[2]),
            Write(point_labels[0]),
            Write(point_labels[5])
        )
        self.wait(0.5)
        self.play(
            Create(tick_marks),
            Create(node_lines),
            Write(x_labels[1]),
            Write(x_labels[3]),
            Write(point_labels[2]),
            Write(point_labels[3])
        )
        self.wait(0.5)
        self.play(
            Create(node_height_lines),
            Write(point_labels[1]),
            Write(point_labels[4])
        )
        self.wait(0.5)
        self.play(
            FadeIn(left_wedge),
            FadeIn(right_wedge),
        )
        self.wait(0.5)
        self.play(
            Create(trapezoid_line),
        )
        self.play(
            FadeIn(middle_region),
        )
        self.play(Write(formula))


        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine, vol. 52,", font_size=30, color=BLACK),
            Tex(r"no. 4 (Sept. 1979), p.206.", font_size=30, color=BLACK),
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
