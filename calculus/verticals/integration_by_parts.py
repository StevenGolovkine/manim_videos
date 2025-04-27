"""
Visual proof of The Midpoint Rule is better than the trapezoidal rule for concave f.
Proofs without Words I. Roger B. Nelsen. p. 41.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, Group
from manim import Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Dot, Line, Polygon
from manim import Text, Tex, DashedVMobject, DashedLine, RoundedRectangle

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


class Part(MovingCameraScene):
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
            Tex(r"L'intégration", font_size=40, color=BLACK),
            Tex(r"par parties", font_size=40, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Richard Courant", font_size=28, color=BLACK)
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

        # Graphs
        ax = Axes(
            x_range=[0, 1, 0.1],
            y_range=[-0.1, 1, 0.1],
            x_length=7,
            y_length=7,
            tips=False,
            x_axis_config={
                "color": BLACK,
            },
            y_axis_config={
                "color": BLACK
            }
        ).scale(0.5).move_to([0, -1.25, 0])

        graph = ax.plot(
            lambda x: x**2 + 0.15,
            x_range=[0.1, 0.9],
            use_smoothing=False,
            color=BLACK
        )
        # Write u
        txt_u = Tex(
            r"$u$",
            font_size=20, color=BLACK
        ).next_to(ax.c2p(1, 0), UP, buff=0.1)
        # Write v
        txt_v = Tex(
            r"$v$",
            font_size=20, color=BLACK
        ).next_to(ax.c2p(0, 1), LEFT, buff=0.1)

        txt_curve = Tex(
            r"$\begin{cases} u = f(x) \\ v = g(x) \end{cases}$",
            font_size=16, color=BLACK
        ).next_to(ax.c2p(0.9, 1), LEFT)
        self.play(
            Create(ax),
            Create(graph),
            Create(txt_u),
            Create(txt_v),
            Create(txt_curve)
        )

        # For f(x)
        txt_a = Tex(r"$p = f(a)$", font_size=16, color=BLACK)\
            .next_to(ax.c2p(0.2, 0), DOWN)
        txt_b = Tex(r"$q = f(b)$", font_size=16, color=BLACK)\
            .next_to(ax.c2p(0.8, 0), DOWN)

        self.play(
            Write(txt_a),
            Write(txt_b),
        )

        point_a = ax.c2p(0.2, 0.2**2 + 0.15)
        line_a = ax.get_vertical_line(point_a, line_func=Line, color=BLACK)
        point_b = ax.c2p(0.8, 0.8**2 + 0.15)
        line_b = ax.get_vertical_line(point_b, line_func=Line, color=BLACK)

        x_vals = np.arange(0.2, 0.8, 0.01)
        points = [
            graph.get_point_from_function(x) for x in x_vals
        ]
        region_under = Polygon(
            *[ax.c2p(0.2, 0), *points, ax.c2p(0.8, 0)],
            stroke_width=0,
            fill_color=RED,
            fill_opacity=0.5
        )
        self.play(
            Create(line_a),
            Create(line_b),
            Create(region_under)
        )

        # For g(x)
        txt_r = Tex(r"$r = g(a)$", font_size=16, color=BLACK)\
            .next_to(ax.c2p(0, 0.2**2 + 0.15), RIGHT + UP, buff=0.1)
        txt_s = Tex(r"$s = g(b)$", font_size=16, color=BLACK)\
            .next_to(ax.c2p(0, 0.8**2 + 0.15), RIGHT + UP, buff=0.1)

        self.play(
            Write(txt_r),
            Write(txt_s),
        )

        point_a = ax.c2p(0.2, 0.2**2 + 0.15)
        line_a = ax.get_horizontal_line(point_a, line_func=Line, color=BLACK)
        point_b = ax.c2p(0.8, 0.8**2 + 0.15)
        line_b = ax.get_horizontal_line(point_b, line_func=Line, color=BLACK)

        x_vals = np.arange(0.2, 0.8, 0.01)
        points = [
            graph.get_point_from_function(x) for x in x_vals
        ]
        region_above = Polygon(
            *[ax.c2p(0, 0.2**2 + 0.15), *points, ax.c2p(0, 0.8**2 + 0.15)],
            stroke_width=0,
            fill_color=BLUE,
            fill_opacity=0.5
        )
        self.play(
            Create(line_a),
            Create(line_b),
            Create(region_above)
        )

        # Add text on top
        txt_area = Tex(
            r"Aire + Aire = sq - rp",
            font_size=28, color=BLACK
        ).move_to([0, 2.5, 0])
        txt_area2 = Tex(
            r"$\int_{a}^{b} f(x)dx + \int_{r}^{s} g(x)dx = (b-a)(q-r)$",
            font_size=28, color=BLACK
        ).move_to([0, 1.5, 0])
        self.play(
            Write(txt_area),
            Write(txt_area2)
        )


        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Richard Courant, Differential", font_size=26, color=BLACK),
            Tex(r"and Integral Calculus, 1937", font_size=26, color=BLACK),
            Tex(r"p. 219", font_size=26, color=BLACK)
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