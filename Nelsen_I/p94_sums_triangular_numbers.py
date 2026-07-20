"""
Visual proof of the sums of triangular numbers I.
Proofs without Words. Roger B. Nelsen. p. 94.
"""
import numpy as np

from manim import ThreeDScene
from manim import Create, Uncreate, Write
from manim import LaggedStart, Polygon, Rectangle, VGroup
from manim import FadeIn, FadeOut, FunctionGraph, Transform
from manim import MathTable, Brace, RoundedRectangle
from manim import Arrow, Cube, Line, Text, Tex

from manim import config
from manim import DEGREES, LEFT, RIGHT, DOWN, LIGHT, UP, PI

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


class Sums(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE

        txt_copy = Text(
            r"@chill.maths", font_size=12,
            font="CMU Typewriter Text", weight=LIGHT, color=BLACK
        ).to_edge(RIGHT + DOWN, buff=0.1)
        self.add(txt_copy)
        self.add_fixed_in_frame_mobjects(txt_copy)

        # Introduction text
        txt_title = [
            Tex(r"Somme des nombres", font_size=48, color=BLACK),
            Tex(r"triangulaires", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Monte J. Zerger", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        results = [
            Tex(r"Si $T_k = 1 + 2 + \cdots + k$,", font_size=24, color=BLACK),
            Tex(r"alors $\sum_{k = 1}^n T_k = \frac{1}{6}n(n+1)(n+2)$", font_size=24, color=BLACK),
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

        n = 6
        unit = 0.17
        triangular_n = n * (n + 1) // 2
        diagram_width = triangular_n * unit
        diagram_height = (n + 2) * unit
        left_x = -diagram_width / 2
        bottom_y = -0.15

        top_regions = VGroup()
        lower_regions = VGroup()
        shaded_regions = VGroup()
        sections = VGroup()
        section_lefts = {}

        for k in range(1, n + 1):
            section_left = left_x + (k - 1) * k / 2 * unit
            section_width = k * unit
            lower_height = (k + 1) * unit
            section_lefts[k] = section_left

            lower = Rectangle(
                width=section_width,
                height=lower_height,
                stroke_color=BLACK,
                stroke_width=0.8,
                fill_color=GREEN,
                fill_opacity=0.38
            ).move_to([
                section_left + section_width / 2,
                bottom_y + lower_height / 2,
                0
            ])

            staircase_points = [
                np.array([section_left, bottom_y + unit, 0]),
                np.array([section_left, bottom_y + lower_height, 0]),
                np.array([
                    section_left + section_width,
                    bottom_y + lower_height,
                    0
                ])
            ]
            for level in range(k, 0, -1):
                staircase_points.extend([
                    np.array([
                        section_left + level * unit,
                        bottom_y + level * unit,
                        0
                    ]),
                    np.array([
                        section_left + (level - 1) * unit,
                        bottom_y + level * unit,
                        0
                    ])
                ])

            shaded = Polygon(
                *staircase_points,
                stroke_color=BLACK,
                stroke_width=0.9,
                fill_color=RED,
                fill_opacity=0.72
            )

            lower_regions.add(lower)
            shaded_regions.add(shaded)
            sections.add(VGroup(lower, shaded))

        # The upper region is a staircase of horizontal strips.  Its kth
        # strip has length T_k, matching the construction in the source.
        for k in range(1, n + 1):
            strip_width = k * (k + 1) / 2 * unit
            strip = Rectangle(
                width=strip_width,
                height=unit,
                stroke_color=BLACK,
                stroke_width=0.8,
                fill_color=BLUE,
                fill_opacity=0.34
            ).move_to([
                left_x + strip_width / 2,
                bottom_y + (k + 1.5) * unit,
                0
            ])
            top_regions.add(strip)

        outer = Rectangle(
            width=diagram_width,
            height=diagram_height,
            stroke_color=BLACK,
            stroke_width=1.3,
            fill_opacity=0
        ).move_to([
            0,
            bottom_y + diagram_height / 2,
            0
        ])

        top_sum_labels = VGroup()
        for k, label in (
            (1, r"$1$"),
            (2, r"$1+2$"),
            (3, r"$1+2+3$"),
            (n, r"$1+2+\cdots+n$")
        ):
            width_to_k = k * (k + 1) / 2 * unit
            sum_label = Tex(
                label,
                font_size=21 if k < n else 26,
                color=BLACK
            )
            sum_label.move_to([
                left_x + width_to_k / 2,
                bottom_y + (k + 1.5) * unit,
                0
            ])
            top_sum_labels.add(sum_label)

        width_labels = VGroup()
        for k in (1, 2, 3, n):
            label = Tex(
                rf"${k}$" if k < n else r"$n$",
                font_size=24,
                color=BLACK
            )
            label.move_to([
                section_lefts[k] + k * unit / 2,
                bottom_y - 0.13,
                0
            ])
            width_labels.add(label)
        omitted = Tex(r"$\cdots$", font_size=24, color=BLACK)
        omitted.move_to([
            (section_lefts[4] + section_lefts[n]) / 2,
            bottom_y - 0.13,
            0
        ])
        width_labels.add(omitted)

        height_label = Tex(r"$n+2$", font_size=30, color=BLACK)
        height_label.next_to(outer, RIGHT, buff=0.1)

        region_labels = VGroup()
        for k, symbol in ((2, r"$T_2$"), (3, r"$T_3$"), (n, r"$T_n$")):
            shaded_label = Tex(symbol, font_size=23, color=BLACK)
            shaded_label.move_to([
                section_lefts[k] + 0.28 * k * unit,
                bottom_y + (k + 0.35) * unit,
                0
            ])
            region_labels.add(shaded_label)

        lower_tn = Tex(r"$T_n$", font_size=26, color=BLACK)
        lower_tn.move_to([
            section_lefts[n] + 0.72 * n * unit,
            bottom_y + 0.75 * unit,
            0
        ])
        region_labels.add(lower_tn)

        diagram = VGroup(
            sections,
            top_regions,
            outer,
            top_sum_labels,
            width_labels,
            height_label,
            region_labels
        )
        diagram.rotate(PI / 2).scale(0.82).move_to([0, 0.1, 0])

        upright_labels = [*width_labels, height_label, *region_labels]
        for label in upright_labels:
            label.rotate(-PI / 2, about_point=label.get_center())

        self.play(
            LaggedStart(
                *[FadeIn(section) for section in sections],
                lag_ratio=0.15
            ),
            LaggedStart(
                *[FadeIn(strip) for strip in top_regions],
                lag_ratio=0.12
            ),
            Create(outer),
            run_time=1.8
        )
        self.play(
            FadeIn(top_sum_labels),
            FadeIn(width_labels),
            FadeIn(height_label),
            FadeIn(region_labels),
            run_time=0.8
        )

        first_identity = Tex(
            r"$3(T_1+T_2+\cdots+T_n)=(n+2)T_n$",
            font_size=22,
            color=BLACK
        )
        first_identity.move_to([0, -2.15, 0])

        conclusion = Tex(
            r"$T_1+T_2+\cdots+T_n"
            r"=\dfrac{n+2}{3}\cdot\dfrac{n(n+1)}{2}"
            r"=\dfrac{n(n+1)(n+2)}{6}$",
            font_size=20,
            color=BLACK
        )
        conclusion.scale_to_fit_width(4.05)
        conclusion.move_to([0, -2.85, 0])

        self.play(Write(first_identity), run_time=1)
        self.play(Write(conclusion), run_time=1.2)

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine,", font_size=26, color=BLACK),
            Tex(r"vol. 63, no. 5 (Dec. 1990)", font_size=26, color=BLACK),
            Tex(r"p. 314.", font_size=26, color=BLACK),
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
