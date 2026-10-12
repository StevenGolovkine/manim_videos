"""
Visual proof of the differentiated geometric series
Proofs without Words III. Roger B. Nelsen. p. 158.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, TransformFromCopy
from manim import VGroup, FadeIn, FadeOut, FunctionGraph, RoundedRectangle
from manim import RegularPolygon, Line, Polygon, Rectangle, DoubleArrow
from manim import Text, Tex, MathTex

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


class Series(MovingCameraScene):
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
            Tex(r"Séries géométriques", font_size=48, color=BLACK),
            Tex(r"différenciées", font_size=48, color=BLACK),
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

        x_value = 2 / 3
        total_length = 1 / (1 - x_value)
        square_side = 3.25
        unit_scale = square_side / total_length
        square_center = np.array([-0.10, 0.45, 0])
        square_left = square_center[0] - square_side / 2
        square_right = square_center[0] + square_side / 2
        square_bottom = square_center[1] - square_side / 2
        square_top = square_center[1] + square_side / 2

        shown_powers = 4
        segment_lengths = [
            unit_scale * x_value**power
            for power in range(shown_powers)
        ]
        remainder_length = square_side - sum(segment_lengths)
        all_segments = segment_lengths + [remainder_length]

        outer_square = Rectangle(
            width=square_side,
            height=square_side,
            color=BLACK,
            stroke_width=2.4,
        ).move_to(square_center)

        vertical_lines = VGroup()
        horizontal_lines = VGroup()
        running_length = 0
        for length in segment_lengths:
            running_length += length
            vertical_lines.add(Line(
                [square_left + running_length, square_bottom, 0],
                [square_left + running_length, square_top, 0],
                color=BLACK,
                stroke_width=1.15,
            ))
            horizontal_lines.add(Line(
                [square_left, square_bottom + running_length, 0],
                [square_right, square_bottom + running_length, 0],
                color=BLACK,
                stroke_width=1.15,
            ))

        power_tex = ["1", "x", "x^2", "x^3"]
        column_labels = VGroup()
        row_labels = VGroup()
        running_length = 0
        for power, length in enumerate(segment_lengths):
            column_labels.add(
                MathTex(
                    power_tex[power], font_size=20, color=BLACK
                ).move_to([
                    square_left + running_length + length / 2,
                    square_bottom - 0.18,
                    0,
                ])
            )
            row_labels.add(
                MathTex(
                    power_tex[power], font_size=20, color=BLACK
                ).move_to([
                    square_left - 0.14,
                    square_bottom + running_length + length / 2,
                    0,
                ])
            )
            running_length += length

        column_ellipsis = MathTex(
            r"\cdots", font_size=22, color=BLACK
        ).move_to([
            square_left + sum(segment_lengths) + remainder_length / 2,
            square_bottom - 0.18,
            0,
        ])

        def cell_geometry(column, row):
            width = segment_lengths[column]
            height = segment_lengths[row]
            center = np.array([
                square_left + sum(segment_lengths[:column]) + width / 2,
                square_bottom + sum(segment_lengths[:row]) + height / 2,
                0,
            ])
            return center, width, height

        def hatch_rectangle(center, width, height, spacing=0.095):
            lines = VGroup()
            half_width = width / 2
            half_height = height / 2
            minimum = -half_width - half_height
            maximum = half_width + half_height

            for offset in np.arange(minimum, maximum + spacing, spacing):
                intersections = []
                for x_coordinate in (-half_width, half_width):
                    y_coordinate = x_coordinate - offset
                    if -half_height <= y_coordinate <= half_height:
                        intersections.append((x_coordinate, y_coordinate))
                for y_coordinate in (-half_height, half_height):
                    x_coordinate = y_coordinate + offset
                    if -half_width <= x_coordinate <= half_width:
                        intersections.append((x_coordinate, y_coordinate))

                unique_points = []
                for point_coordinates in intersections:
                    if not any(
                        np.allclose(point_coordinates, existing)
                        for existing in unique_points
                    ):
                        unique_points.append(point_coordinates)

                if len(unique_points) >= 2:
                    start = center + np.array([*unique_points[0], 0])
                    end = center + np.array([*unique_points[1], 0])
                    lines.add(Line(
                        start,
                        end,
                        color=BLACK,
                        stroke_width=0.75,
                        stroke_opacity=0.50,
                    ))
            return lines

        diagonal_colors = [BLUE, GREEN, ORANGE, VIOLET]
        diagonal_groups = VGroup()
        for exponent in range(shown_powers):
            diagonal = VGroup()
            for column in range(exponent + 1):
                row = exponent - column
                center, width, height = cell_geometry(column, row)
                cell = Rectangle(
                    width=width,
                    height=height,
                    color=BLACK,
                    stroke_width=1.15,
                    fill_color=diagonal_colors[exponent],
                    fill_opacity=0.34 if exponent < 3 else 0.20,
                ).move_to(center)
                diagonal.add(cell)

                if exponent == 3:
                    diagonal.add(hatch_rectangle(center, width, height))

                label = MathTex(
                    power_tex[exponent],
                    font_size=18,
                    color=BLACK,
                ).move_to(center)
                diagonal.add(label)
            diagonal_groups.add(diagonal)

        top_remainder_center = square_top - remainder_length / 2
        continuation_marks = VGroup(
            MathTex(r"\vdots", font_size=23, color=BLACK).move_to([
                column_labels[0].get_x(), top_remainder_center, 0
            ]),
            MathTex(r"\vdots", font_size=23, color=BLACK).move_to([
                column_labels[1].get_x(), top_remainder_center, 0
            ]),
            MathTex(r"\ddots", font_size=23, color=BLACK).move_to(
                cell_geometry(2, 2)[0]
            ),
            MathTex(r"\cdots", font_size=23, color=BLACK).move_to([
                square_left + sum(segment_lengths) + remainder_length / 2,
                row_labels[0].get_y(),
                0,
            ]),
        )

        horizontal_dimension = DoubleArrow(
            [square_left, square_top + 0.24, 0],
            [square_right, square_top + 0.24, 0],
            buff=0,
            tip_length=0.10,
            stroke_width=1.4,
            color=BLACK,
        )
        horizontal_dimension_label = MathTex(
            r"\frac{1}{1-x}", font_size=22, color=BLACK
        ).move_to(horizontal_dimension.get_center())
        horizontal_dimension_label.add_background_rectangle(
            color=WHITE, opacity=1, buff=0.06
        )

        vertical_dimension = DoubleArrow(
            [square_right + 0.26, square_bottom, 0],
            [square_right + 0.26, square_top, 0],
            buff=0,
            tip_length=0.10,
            stroke_width=1.4,
            color=BLACK,
        )
        vertical_dimension_label = MathTex(
            r"\frac{1}{1-x}", font_size=22, color=BLACK
        ).move_to(vertical_dimension.get_center())
        vertical_dimension_label.add_background_rectangle(
            color=WHITE, opacity=1, buff=0.06
        )

        conclusion = VGroup(
            MathTex(
                r"x\in[0,1)\quad\Longrightarrow",
                font_size=24,
                color=BLACK,
            ),
            MathTex(
                r"1+2x+3x^2+4x^3+\cdots"
                r"=\left(\frac{1}{1-x}\right)^2",
                font_size=24,
                color=BLACK,
            ),
        ).arrange(DOWN, buff=0.14).move_to([0, -2.72, 0])

        self.play(
            Create(outer_square),
            Create(horizontal_dimension),
            Create(vertical_dimension),
            Write(horizontal_dimension_label),
            Write(vertical_dimension_label),
        )
        self.play(
            Create(vertical_lines),
            Create(horizontal_lines),
            Write(column_labels),
            Write(row_labels),
            Write(column_ellipsis),
            run_time=1.5,
        )
        for diagonal in diagonal_groups:
            self.play(FadeIn(diagonal), run_time=0.8)
        self.play(Write(continuation_marks))
        self.play(Write(conclusion))


        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"College Mathematics Journal,", font_size=26, color=BLACK),
            Tex(r"vol. 32, no. 4 (Sept. 2001), p.257.", font_size=26, color=BLACK)
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
