"""
Visual proof of the Chebyshev inequality.
Proofs without Words II. Roger B. Nelsen. p. 80.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Line, Polygon
from manim import Arrow, DashedLine, Rectangle, Text, Tex

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
GREY = "#D3D3D3"
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


class Chebyshev(MovingCameraScene):
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
            Tex(r"L'inégalité", font_size=48, color=BLACK),
            Tex(r"de Chebyshev", font_size=48, color=BLACK)
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

        # Proof figure
        sx = 0.40
        sy = 0.36
        origin = np.array([-1.85, -1.0, 0])

        def p(x, y):
            return origin + np.array([sx * x, sy * y, 0])

        def rectangle_from_bounds(
            x0, x1, y0, y1,
            fill_color=WHITE,
            fill_opacity=0,
            stroke_color=BLACK,
            stroke_width=1.4
        ):
            return Rectangle(
                width=(x1 - x0) * sx,
                height=(y1 - y0) * sy,
                fill_color=fill_color,
                fill_opacity=fill_opacity,
                stroke_color=stroke_color,
                stroke_width=stroke_width
            ).move_to(p((x0 + x1) / 2, (y0 + y1) / 2))

        def hatched_rectangle(x0, x1, y0, y1):
            rect = rectangle_from_bounds(
                x0, x1, y0, y1,
                fill_color=WHITE,
                fill_opacity=0.75,
                stroke_width=1.5
            )
            hatches = VGroup()
            spacing = 0.23
            for x_start in np.arange(x0 - (y1 - y0), x1, spacing):
                start_x = max(x0, x_start)
                end_x = min(x1, x_start + (y1 - y0))
                if start_x < end_x:
                    hatches.add(
                        Line(
                            p(start_x, y0 + start_x - x_start),
                            p(end_x, y0 + end_x - x_start),
                            color=BLACK,
                            stroke_width=1.15
                        )
                    )
            return VGroup(rect, hatches)

        top_formula = Tex(
            r"$\sum_{i=1}^{n}x_i\sum_{i=1}^{n}y_i"
            r"\leq n\sum_{i=1}^{n}x_iy_i$",
            font_size=34,
            color=BLACK
        ).move_to([0, 3.15, 0])
        top_formula.scale_to_fit_width(config.frame_width - 0.45)

        outer_box = rectangle_from_bounds(
            0, 10, 0, 7,
            stroke_width=2.2
        )

        verticals = [0.55, 1.35, 3.0, 5.1, 7.3]
        horizontals = [0.4, 1.05, 2.05, 3.2, 5.0]
        grid = VGroup()
        for x in verticals:
            grid.add(
                DashedLine(
                    p(x, 0), p(x, 7),
                    color=BLACK,
                    stroke_width=1.35,
                    dash_length=0.07
                ).set_opacity(0.55)
            )
        for y in horizontals:
            grid.add(
                DashedLine(
                    p(0, y), p(10, y),
                    color=BLACK,
                    stroke_width=1.35,
                    dash_length=0.07
                ).set_opacity(0.55)
            )

        source_left = rectangle_from_bounds(
            1.35, 3.0, 3.2, 5.0,
            fill_color=GREY,
            fill_opacity=0.28,
            stroke_width=1.35,
            stroke_color="#666666"
        )
        source_right = rectangle_from_bounds(
            5.1, 7.3, 1.05, 2.05,
            fill_color=GREY,
            fill_opacity=0.16,
            stroke_width=1.35,
            stroke_color="#777777"
        )

        lower_left = hatched_rectangle(1.35, 3.0, 1.05, 2.05)
        lower_right = hatched_rectangle(5.1, 7.3, 3.2, 4.25)
        upper_right = hatched_rectangle(5.1, 6.55, 4.25, 5.0)

        arrows = VGroup(
            Arrow(
                p(2.1, 4.55), p(4.9, 4.55),
                buff=0,
                color=BLACK,
                stroke_width=2.0,
                max_tip_length_to_length_ratio=0.09
            ),
            Arrow(
                p(2.1, 3.85), p(2.1, 2.35),
                buff=0,
                color=BLACK,
                stroke_width=2.0,
                max_tip_length_to_length_ratio=0.12
            ),
            Arrow(
                p(6.2, 1.45), p(6.2, 3.0),
                buff=0,
                color=BLACK,
                stroke_width=2.0,
                max_tip_length_to_length_ratio=0.12
            ),
        )

        x_labels = VGroup(
            Tex(r"$x_1$", font_size=26, color=BLACK).next_to(p(0.55, 0), DOWN, buff=0.08),
            Tex(r"$x_i$", font_size=26, color=BLACK).next_to(p(2.05, 0), DOWN, buff=0.08),
            Tex(r"$x_j$", font_size=26, color=BLACK).next_to(p(6.2, 0), DOWN, buff=0.08),
            Tex(r"$x_n$", font_size=26, color=BLACK).next_to(p(8.5, 0), DOWN, buff=0.08),
        )
        y_labels = VGroup(
            Tex(r"$y_1$", font_size=26, color=BLACK).next_to(p(0, 0.4), LEFT, buff=0.08),
            Tex(r"$y_i$", font_size=26, color=BLACK).next_to(p(0, 1.45), LEFT, buff=0.08),
            Tex(r"$y_j$", font_size=26, color=BLACK).next_to(p(0, 4.1), LEFT, buff=0.08),
            Tex(r"$y_n$", font_size=26, color=BLACK).next_to(p(0, 6.0), LEFT, buff=0.08),
        )

        bottom_formula_1 = Tex(
            r"$x_i < x_j \ \&\ y_i < y_j"
            r"\Rightarrow x_i y_j + x_j y_i \leq x_i y_i + x_j y_j$",
            font_size=23,
            color=BLACK
        ).move_to([0, -2.75, 0])
        bottom_formula_1.scale_to_fit_width(config.frame_width - 0.35)

        bottom_formula_2 = Tex(
            r"$\therefore (x_1+x_2+\cdots+x_n)(y_1+y_2+\cdots+y_n)"
            r"\leq n(x_1y_1+x_2y_2+\cdots+x_ny_n)$",
            font_size=23,
            color=BLACK
        ).move_to([0, -3.25, 0])
        bottom_formula_2.scale_to_fit_width(config.frame_width - 0.25)

        self.play(Write(top_formula))
        self.play(
            Create(outer_box),
            Create(grid),
            Write(x_labels),
            Write(y_labels),
            run_time=2
        )
        self.play(FadeIn(source_left), FadeIn(source_right))
        self.play(
            FadeIn(lower_left),
            FadeIn(lower_right),
            FadeIn(upper_right),
            Create(arrows),
            run_time=2
        )
        self.play(Write(bottom_formula_1), Write(bottom_formula_2))

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"College Mathematics Journal,", font_size=26, color=BLACK),
            Tex(r"vol. 25, no. 3 (May 1994)", font_size=26, color=BLACK),
            Tex(r"p. 192.", font_size=26, color=BLACK),
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
