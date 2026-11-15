"""
Visual proof of the arithmetic mean - geometric mean inequality VIII.
Proofs without Words III. Roger B. Nelsen. p. 94.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, TransformFromCopy
from manim import TransformMatchingTex
from manim import VGroup, FadeIn, FadeOut, FunctionGraph, Polygon
from manim import (
    Text, Tex, MathTex, Line, Arc, Circle, Angle, DoubleArrow, Dot,
    DashedLine,
)

from manim import config
from manim import LEFT, RIGHT, DOWN, LIGHT, BOLD, UP, PI, DEGREES

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


class Cauchy(MovingCameraScene):
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
            Tex(r"de Cauchy-Schwarz", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Sidney H. Kung", font_size=28, color=BLACK)
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

        panel_bottom = -0.55
        panel_top = 1.95
        panel_width = 1.65
        panel_height = panel_top - panel_bottom
        gray = "#D1D3D4"

        # Left panel: (|x| + |b|)(|a| + |y|).
        left_x = -2.05
        right_x = left_x + panel_width
        split_x = left_x + 0.43 * panel_width
        split_y = panel_bottom + 0.43 * panel_height

        left_top_right_fill = Polygon(
            [split_x, split_y, 0],
            [right_x, split_y, 0],
            [right_x, panel_top, 0],
            [split_x, panel_top, 0],
            stroke_width=0,
            fill_color=gray,
            fill_opacity=0.82,
        )
        left_bottom_left_fill = Polygon(
            [left_x, panel_bottom, 0],
            [split_x, panel_bottom, 0],
            [split_x, split_y, 0],
            [left_x, split_y, 0],
            stroke_width=0,
            fill_color=gray,
            fill_opacity=0.82,
        )
        left_outline = Polygon(
            [left_x, panel_bottom, 0],
            [right_x, panel_bottom, 0],
            [right_x, panel_top, 0],
            [left_x, panel_top, 0],
            color=BLACK,
            stroke_width=1.35,
            fill_opacity=0,
        )
        left_vertical = Line(
            [split_x, panel_bottom, 0],
            [split_x, panel_top, 0],
            color=BLACK,
            stroke_width=1.25,
        )
        left_horizontal = Line(
            [left_x, split_y, 0],
            [right_x, split_y, 0],
            color=BLACK,
            stroke_width=1.25,
        )
        left_upper_diagonal = Line(
            [split_x, split_y, 0],
            [right_x, panel_top, 0],
            color=BLACK,
            stroke_width=1.25,
        )
        left_lower_diagonal = Line(
            [left_x, split_y, 0],
            [split_x, panel_bottom, 0],
            color=BLACK,
            stroke_width=1.25,
        )
        left_lines = VGroup(
            left_outline,
            left_vertical,
            left_horizontal,
            left_upper_diagonal,
            left_lower_diagonal,
        )
        left_fills = VGroup(
            left_top_right_fill,
            left_bottom_left_fill,
        )

        label_x = MathTex(r"|x|", font_size=23, color=BLACK).move_to(
            [(left_x + split_x) / 2, panel_top + 0.2, 0]
        )
        label_b = MathTex(r"|b|", font_size=23, color=BLACK).move_to(
            [(split_x + right_x) / 2, panel_top + 0.2, 0]
        )
        label_a = MathTex(r"|a|", font_size=23, color=BLACK).move_to(
            [left_x - 0.25, (split_y + panel_top) / 2, 0]
        )
        label_y = MathTex(r"|y|", font_size=23, color=BLACK).move_to(
            [left_x - 0.25, (panel_bottom + split_y) / 2, 0]
        )
        left_labels = VGroup(label_x, label_b, label_a, label_y)

        # Right panel: the same area rearranged around a parallelogram.
        r_left = 0.40
        r_right = r_left + panel_width
        top_point = np.array([
            r_left + 0.57 * panel_width, panel_top, 0
        ])
        right_point = np.array([
            r_right, panel_bottom + 0.57 * panel_height, 0
        ])
        bottom_point = np.array([
            r_left + 0.43 * panel_width, panel_bottom, 0
        ])
        left_point = np.array([
            r_left, panel_bottom + 0.43 * panel_height, 0
        ])

        right_background = Polygon(
            [r_left, panel_bottom, 0],
            [r_right, panel_bottom, 0],
            [r_right, panel_top, 0],
            [r_left, panel_top, 0],
            stroke_width=0,
            fill_color=gray,
            fill_opacity=0.82,
        )
        inner_parallelogram = Polygon(
            top_point,
            right_point,
            bottom_point,
            left_point,
            color=BLACK,
            stroke_width=1.35,
            fill_color=WHITE,
            fill_opacity=1,
        )
        right_outline = Polygon(
            [r_left, panel_bottom, 0],
            [r_right, panel_bottom, 0],
            [r_right, panel_top, 0],
            [r_left, panel_top, 0],
            color=BLACK,
            stroke_width=1.35,
            fill_opacity=0,
        )

        base_vector = right_point - bottom_point
        base_unit = base_vector / np.linalg.norm(base_vector)
        projection_parameter = np.dot(
            left_point - bottom_point, base_vector
        ) / np.dot(base_vector, base_vector)
        altitude_foot = bottom_point + projection_parameter * base_vector
        altitude = DashedLine(
            left_point,
            altitude_foot,
            dash_length=0.10,
            dashed_ratio=0.55,
            color=BLACK,
            stroke_width=1.3,
        )

        altitude_unit = (
            left_point - altitude_foot
        ) / np.linalg.norm(left_point - altitude_foot)
        marker_size = 0.085
        marker_along = altitude_foot - marker_size * base_unit
        marker_corner = marker_along + marker_size * altitude_unit
        right_angle_marker = VGroup(
            Line(
                marker_along,
                marker_corner,
                color=BLACK,
                stroke_width=1.2,
            ),
            Line(
                marker_corner,
                altitude_foot + marker_size * altitude_unit,
                color=BLACK,
                stroke_width=1.2,
            ),
        )

        side_angle = np.arctan2(base_vector[1], base_vector[0])
        side_normal = np.array([-base_unit[1], base_unit[0], 0])
        side_label = MathTex(
            r"\sqrt{a^2+b^2}", font_size=16, color=BLACK
        )
        side_label.rotate(side_angle).move_to(
            bottom_point
            + 0.7 * (right_point - bottom_point)
            + 0.15 * side_normal
        )

        altitude_vector = altitude_foot - left_point
        altitude_angle = np.arctan2(
            altitude_vector[1], altitude_vector[0]
        )
        if altitude_angle > PI / 2:
            altitude_angle -= PI
        altitude_normal = np.array([
            -np.sin(altitude_angle), np.cos(altitude_angle), 0
        ])
        altitude_label = MathTex(
            r"\sqrt{x^2+y^2}\sin z", font_size=15, color=BLACK
        )
        altitude_label.rotate(altitude_angle).move_to(
            left_point
            + 0.5 * (altitude_foot - left_point)
            + 0.1 * altitude_normal
        )

        angle_z = Angle(
            Line(bottom_point, right_point),
            Line(bottom_point, left_point),
            radius=0.16,
            color=BLACK,
            stroke_width=1.25,
        )
        direction_right = (right_point - bottom_point) / np.linalg.norm(
            right_point - bottom_point
        )
        direction_left = (left_point - bottom_point) / np.linalg.norm(
            left_point - bottom_point
        )
        angle_bisector = direction_right + direction_left
        angle_bisector /= np.linalg.norm(angle_bisector)
        label_z = MathTex(r"z", font_size=18, color=BLACK).move_to(
            bottom_point + 0.24 * angle_bisector
        )

        # Rotate both constructions and stack them vertically.
        left_center = left_outline.get_center()
        left_figure = VGroup(left_fills, left_lines, left_labels)
        left_figure.rotate(PI / 2, about_point=left_center)
        for label in left_labels:
            label.rotate(-PI / 2)
        left_figure.scale(1.08, about_point=left_center)
        left_figure.shift(
            np.array([0, 2.5, 0]) - left_outline.get_center()
        )

        right_center = right_outline.get_center()
        right_figure = VGroup(
            right_background,
            inner_parallelogram,
            right_outline,
            altitude,
            right_angle_marker,
            side_label,
            altitude_label,
            angle_z,
            label_z,
        )
        right_figure.rotate(PI / 2, about_point=right_center)
        side_label.rotate(-PI)
        label_z.rotate(-PI / 2)
        right_figure.scale(1.08, about_point=right_center)
        right_figure.shift(
            np.array([0, 0, 0]) - right_outline.get_center()
        )

        first_identity = MathTex(
            r"|a|\,|x|+|b|\,|y|",
            r"=",
            r"\sqrt{a^2+b^2}\sqrt{x^2+y^2}\sin z",
            font_size=23,
            color=BLACK,
        ).move_to([0, -2, 0])
        first_identity.scale_to_fit_width(4.05)

        conclusion = MathTex(
            r"\Longrightarrow",
            r"\left|\langle a,b\rangle\cdot\langle x,y\rangle\right|",
            r"\leq",
            r"\left\|\langle a,b\rangle\right\|"
            r"\left\|\langle x,y\rangle\right\|.",
            font_size=22,
            color=BLACK,
        ).move_to([0, -2.5, 0])
        conclusion.scale_to_fit_width(4.05)

        self.play(
            FadeIn(left_fills),
            Create(left_lines),
            run_time=1.5,
        )
        self.play(Write(left_labels), run_time=0.9)
        self.play(
            FadeIn(right_background),
            FadeIn(inner_parallelogram),
            Create(right_outline),
            run_time=1.5,
        )
        self.play(
            Create(altitude),
            FadeIn(right_angle_marker),
            Create(angle_z),
            Write(label_z),
            run_time=1.1,
        )
        self.wait(0.5)
        self.play(
            Write(side_label),
            Write(altitude_label),
            run_time=1.0,
        )
        self.play(Write(first_identity), run_time=1.2)
        self.play(Write(conclusion), run_time=1.2)
        self.wait(2)

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine,", font_size=26, color=BLACK),
            Tex(r"vol. 81, no. 1 (Feb. 2008), p.69", font_size=26, color=BLACK)
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
