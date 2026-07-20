"""
Visual proof of every hexagonal number is a triangular number.
Proofs without Words. Roger B. Nelsen. p. 106.
"""
import numpy as np

from manim import ThreeDScene
from manim import Create, Uncreate, Write
from manim import Circle, LaggedStart, VGroup
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


class HexagonalTriangular(ThreeDScene):
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
            Tex(r"Tout nombre", font_size=48, color=BLACK),
            Tex(r"hexagonal", font_size=48, color=BLACK),
            Tex(r"est un nombre", font_size=48, color=BLACK),
            Tex(r"triangulaire.", font_size=48, color=BLACK),
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


        definitions = VGroup(
            Tex(
                r"$H_n=1+5+\cdots+(4n-3)$",
                font_size=20,
                color=BLACK
            ),
            Tex(
                r"$T_n=1+2+\cdots+n$",
                font_size=20,
                color=BLACK
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.05)
        implication = Tex(
            r"$\Longrightarrow$",
            font_size=20,
            color=BLACK
        )

        identity = Tex(
            r"$H_n=3T_{n-1}+T_n=T_{2n-1}=n(2n-1)$",
            font_size=20,
            color=BLACK
        )
        identity_line = VGroup(implication, identity).arrange(
            RIGHT,
            buff=0.08
        )
        identity_line.scale_to_fit_width(3.9)
        formula_block = VGroup(definitions, identity_line).arrange(
            DOWN,
            buff=0.1
        )
        formula_block.move_to([0, 2.35, 0])

        self.play(
            Write(definitions),
            run_time=1
        )
        self.play(Write(identity_line), run_time=1)
        self.wait(1)

        dot_colors = (BLACK, RED, BLUE, GREEN)
        dot_radius = 0.073
        spacing = 0.22

        def make_dot(point, color):
            return Circle(
                radius=dot_radius,
                stroke_width=1.1,
                stroke_color=BLACK,
                fill_color=color,
                fill_opacity=1
            ).move_to(point)

        def colored_dot_group(points_by_color):
            return VGroup(*[
                VGroup(*[
                    make_dot(point, dot_colors[color_index])
                    for point in points
                ])
                for color_index, points in enumerate(points_by_color)
            ])

        def hexagonal_points(n):
            """Four triangular sectors on the open hexagonal lattice."""
            points = [[] for _ in range(4)]
            order = n - 1

            def lattice_point(q, r):
                return np.array([
                    0.93 * spacing * q,
                    -spacing * (q / 2 + r),
                    0
                ])

            # T_n: the large upper-right sector.
            for q in range(order + 1):
                for r in range(-order, q - order + 1):
                    points[0].append(lattice_point(q, r))

            # Three copies of T_{n-1} around the other sides.
            for q in range(-order, 0):
                start = -order - q
                for r in range(start, start - q):
                    points[1].append(lattice_point(q, r))

            for q in range(-order, 0):
                for r in range(-2 * q - order, order + 1, 2):
                    points[2].append(lattice_point(q, r))

            for q in range(order):
                for r in range(q - order + 2, order - q + 1, 2):
                    points[3].append(lattice_point(q, r))
            return points

        def triangular_points(rows):
            points = [[] for _ in range(4)]
            vertical_step = spacing * np.sqrt(3) / 2

            for row in range(rows):
                for column in range(row + 1):
                    point = np.array([
                        (column - row / 2) * spacing,
                        (rows - 1 - row) * vertical_step,
                        0
                    ])
                    if row < 4:
                        color_index = 1
                    elif column < row - 4:
                        color_index = 2
                    elif column <= 4:
                        color_index = 0
                    else:
                        color_index = 3
                    points[color_index].append(point)
            return points

        def rectangular_points(rows, columns):
            points = [[] for _ in range(4)]
            for row in range(rows):
                for column in range(columns):
                    point = np.array([
                        (column - (columns - 1) / 2) * spacing,
                        ((rows - 1) / 2 - row) * spacing,
                        0
                    ])
                    if column <= row:
                        color_index = 0
                    elif column >= 5 + row:
                        color_index = 1
                    elif column <= 4:
                        color_index = 2
                    else:
                        color_index = 3
                    points[color_index].append(point)
            return points

        hexagon = colored_dot_group(hexagonal_points(5))
        hexagon.move_to([-1.12, 0.45, 0])
        hexagon_label = Tex(r"$H_5$", font_size=20, color=BLACK)
        hexagon_label.next_to(hexagon, DOWN, buff=0.12)

        triangle_target = colored_dot_group(triangular_points(9))
        triangle_target.move_to([1.12, 0.45, 0])
        triangle_label = Tex(r"$T_9$", font_size=20, color=BLACK)
        triangle_label.next_to(triangle_target, DOWN, buff=0.12)

        rectangle_target = colored_dot_group(rectangular_points(5, 9))
        rectangle_target.move_to([0, -2.35, 0])
        rectangle_label = Tex(r"$5\cdot9$", font_size=20, color=BLACK)
        rectangle_label.next_to(rectangle_target, DOWN, buff=0.14)

        self.play(
            LaggedStart(
                *[
                    FadeIn(dot, scale=0.5)
                    for color_group in hexagon
                    for dot in color_group
                ],
                lag_ratio=0.1
            ),
            Write(hexagon_label),
            run_time=2
        )
        self.wait(1)

        triangle = hexagon.copy()
        self.add(triangle)
        self.play(
            Transform(triangle, triangle_target),
            FadeIn(triangle_label),
            run_time=2
        )
        self.wait(1)

        rectangle = triangle.copy()
        self.add(rectangle)
        self.play(
            Transform(rectangle, rectangle_target),
            FadeIn(rectangle_label),
            run_time=2
        )


        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Richard K. Guy,", font_size=26, color=BLACK),
            Tex(r"written communication.", font_size=26, color=BLACK),
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
