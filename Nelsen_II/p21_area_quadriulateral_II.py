"""
Visual proof of The Area of aa Quadrilateral II.
Proofs without Words II. Roger B. Nelsen. p. 21.
"""
import numpy as np

from manim import MovingCameraScene
from manim import (
    Create, Uncreate, Write, Transform, TransformFromCopy, LaggedStart, Group,
)
from manim import Polygon, VGroup, FadeIn, FadeOut, FunctionGraph
from manim import (
    Text, Tex, MathTex, Triangle, RoundedRectangle, Circle, Line, Dot, Angle,
    DashedLine,
)

from manim import config
from manim import LEFT, RIGHT, DOWN, LIGHT, UP, SMALL_BUFF, PI

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


class Quadri(MovingCameraScene):
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
            Tex(r"L'aire d'un", font_size=48, color=BLACK),
            Tex(r"quadrilatère", font_size=48, color=BLACK),
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

        def make_quadrilateral(
            center,
            diagonal_1,
            diagonal_2,
            color,
            concave=False,
            fill_opacity=0.52,
            stroke_width=1.8,
            diagonal_opacity=0.75,
        ):
            center = np.array(center, dtype=float)
            diagonal_1 = np.array(diagonal_1, dtype=float)
            diagonal_2 = np.array(diagonal_2, dtype=float)

            point_a = center - diagonal_1 / 2
            point_c = center + diagonal_1 / 2
            if concave:
                point_b = center + 1.15 * diagonal_2
                point_d = center + 0.15 * diagonal_2
            else:
                point_b = center + 0.62 * diagonal_2
                point_d = center - 0.38 * diagonal_2

            quadrilateral = Polygon(
                point_a,
                point_b,
                point_c,
                point_d,
                color=BLACK,
                stroke_width=stroke_width,
                fill_color=color,
                fill_opacity=fill_opacity,
            )
            diagonals = VGroup(
                DashedLine(
                    point_a,
                    point_c,
                    dash_length=0.07,
                    dashed_ratio=0.55,
                    color=BLACK,
                    stroke_width=1.25,
                ),
                DashedLine(
                    point_b,
                    point_d,
                    dash_length=0.07,
                    dashed_ratio=0.55,
                    color=BLACK,
                    stroke_width=1.25,
                ),
            ).set_stroke(opacity=diagonal_opacity)
            return VGroup(quadrilateral, diagonals)

        def parallelogram_corners(center, side_1, side_2):
            center = np.array(center, dtype=float)
            side_1 = np.array(side_1, dtype=float)
            side_2 = np.array(side_2, dtype=float)
            return [
                center - side_1 / 2 - side_2 / 2,
                center + side_1 / 2 - side_2 / 2,
                center + side_1 / 2 + side_2 / 2,
                center - side_1 / 2 + side_2 / 2,
            ]

        def make_parallelogram(
            center,
            side_1,
            side_2,
            color,
            shade=True,
            stroke_opacity=0.90,
        ):
            center = np.array(center, dtype=float)
            corners = parallelogram_corners(center, side_1, side_2)
            outline = VGroup(*[
                DashedLine(
                    corners[index],
                    corners[(index + 1) % 4],
                    dash_length=0.07,
                    dashed_ratio=0.55,
                    color=BLACK,
                    stroke_width=1.4,
                )
                for index in range(4)
            ]).set_stroke(opacity=stroke_opacity)

            shaded_half = VGroup()
            if shade:
                shaded_half.add(
                    Polygon(
                        corners[0], corners[1], center,
                        stroke_width=0,
                        fill_color=color,
                        fill_opacity=0.50,
                    ),
                    Polygon(
                        corners[2], corners[3], center,
                        stroke_width=0,
                        fill_color=color,
                        fill_opacity=0.50,
                    ),
                )
            return VGroup(shaded_half, outline)

        def make_lattice(
            center,
            side_1,
            side_2,
            color,
            concave=False,
        ):
            outlines = VGroup()
            quadrilaterals = VGroup()
            center = np.array(center, dtype=float)
            side_1 = np.array(side_1, dtype=float)
            side_2 = np.array(side_2, dtype=float)

            for row in range(-1, 2):
                for column in range(-1, 2):
                    cell_center = center + column * side_1 + row * side_2
                    outlines.add(
                        make_parallelogram(
                            cell_center,
                            side_1,
                            side_2,
                            color,
                            shade=False,
                            stroke_opacity=0.38,
                        )[1]
                    )
                    quadrilaterals.add(
                        make_quadrilateral(
                            cell_center,
                            side_1,
                            side_2,
                            color,
                            concave=concave,
                            fill_opacity=0.36,
                            stroke_width=1.15,
                            diagonal_opacity=0.42,
                        )
                    )
            return VGroup(outlines, quadrilaterals)

        statement = VGroup(
            Tex(
                r"Les côtés de $P$ sont parallèles et égaux",
                font_size=23,
                color=BLACK,
            ),
            Tex(
                r"aux diagonales de $Q$.",
                font_size=23,
                color=BLACK,
            ),
        ).arrange(DOWN, buff=0.06).move_to([0, 3.28, 0])

        formula = MathTex(
            r"\operatorname{aire}(Q)",
            r"=",
            r"\frac{1}{2}\operatorname{aire}(P)",
            font_size=28,
            color=BLACK,
        ).move_to([0, -1.85, 0])

        self.play(Write(statement))

        # I. Convex quadrilateral
        convex_label = Tex(
            r"Si $Q$ est convexe", font_size=26, color=BLACK
        ).move_to([-1, 2.52, 0])

        convex_demo_u = np.array([0.72, -0.20, 0])
        convex_demo_v = np.array([0.45, 0.58, 0])
        def make_convex_copy(center, diagonal):
            center = np.array(center, dtype=float)
            point_a = center - 0.82 * convex_demo_u
            point_b = center + 0.50 * convex_demo_v
            point_c = center + 0.18 * convex_demo_u
            point_d = center - 0.50 * convex_demo_v
            if diagonal == "vertical":
                diagonal_start, diagonal_end = point_b, point_d
            else:
                diagonal_start, diagonal_end = point_a, point_c
            quadrilateral = VGroup(
                Polygon(
                    point_a,
                    point_b,
                    point_c,
                    point_d,
                    color=BLACK,
                    stroke_width=1.8,
                    fill_opacity=0,
                ),
                DashedLine(
                    diagonal_start,
                    diagonal_end,
                    dash_length=0.07,
                    dashed_ratio=0.55,
                    color=BLACK,
                    stroke_width=1.25,
                ).set_stroke(opacity=0.75),
            )
            return quadrilateral, (point_a, point_b, point_c, point_d)

        convex_q_vertical, vertical_points = make_convex_copy(
            [-1.25, 1.65, 0], "vertical"
        )
        convex_q_horizontal, horizontal_points = make_convex_copy(
            [-0.15, 1.65, 0], "horizontal"
        )
        vertical_a, vertical_b, vertical_c, vertical_d = vertical_points
        horizontal_a, horizontal_b, horizontal_c, horizontal_d = (
            horizontal_points
        )

        convex_q_vertical_pieces = VGroup(
            Polygon(
                vertical_a,
                vertical_b,
                vertical_d,
                color=BLACK,
                stroke_width=0.7,
                fill_color=VIOLET,
                fill_opacity=0.72,
            ),
            Polygon(
                vertical_c,
                vertical_b,
                vertical_d,
                color=BLACK,
                stroke_width=0.7,
                fill_color=GREEN,
                fill_opacity=0.72,
            ),
        )
        convex_q_horizontal_pieces = VGroup(
            Polygon(
                horizontal_a,
                horizontal_b,
                horizontal_c,
                color=BLACK,
                stroke_width=0.7,
                fill_color=BLUE,
                fill_opacity=0.72,
            ),
            Polygon(
                horizontal_a,
                horizontal_d,
                horizontal_c,
                color=BLACK,
                stroke_width=0.7,
                fill_color=ORANGE,
                fill_opacity=0.72,
            ),
        )
        convex_source_pieces = VGroup(
            *convex_q_vertical_pieces,
            *convex_q_horizontal_pieces,
        )

        convex_p_center = np.array([1.15, 1.65, 0])
        convex_p = make_parallelogram(
            convex_p_center,
            convex_demo_u,
            convex_demo_v,
            BLUE,
            shade=False,
        )
        convex_p_corners = parallelogram_corners(
            convex_p_center, convex_demo_u, convex_demo_v
        )
        convex_p_split = (
            convex_p_corners[0]
            + 0.82 * convex_demo_u
            + 0.50 * convex_demo_v
        )
        convex_p_pieces = VGroup(*[
            Polygon(
                *vertices,
                color=BLACK,
                stroke_width=0.7,
                fill_color=color,
                fill_opacity=0.72,
            )
            for vertices, color in zip(
                [
                    [
                        convex_p_split,
                        convex_p_corners[0],
                        convex_p_corners[3],
                    ],
                    [
                        convex_p_split,
                        convex_p_corners[1],
                        convex_p_corners[2],
                    ],
                    [
                        convex_p_corners[0],
                        convex_p_split,
                        convex_p_corners[1],
                    ],
                    [
                        convex_p_corners[3],
                        convex_p_split,
                        convex_p_corners[2],
                    ],
                ],
                [VIOLET, GREEN, BLUE, ORANGE],
            )
        ])

        convex_q_vertical[0].set_z_index(2)
        convex_q_vertical[1].set_z_index(3)
        convex_q_horizontal[0].set_z_index(2)
        convex_q_horizontal[1].set_z_index(3)
        convex_source_pieces.set_z_index(1)
        convex_p[1].set_z_index(3)
        convex_p_pieces.set_z_index(1)
        convex_q_vertical_label = Tex(
            r"$Q_1$", font_size=20, color=BLACK
        ).next_to(convex_q_vertical, DOWN, buff=0.08)
        convex_q_horizontal_label = Tex(
            r"$Q_2$", font_size=20, color=BLACK
        ).next_to(convex_q_horizontal, DOWN, buff=0.08)
        convex_p_label = Tex(
            r"$P$", font_size=20, color=BLACK
        ).next_to(convex_p, DOWN, buff=0.08)

        convex_lattice_center = np.array([0, -0.30, 0])
        convex_lattice_u = convex_demo_u.copy()
        convex_lattice_v = convex_demo_v.copy()
        convex_lattice_outlines = VGroup()
        convex_lattice_pieces = VGroup()
        for row in range(-1, 2):
            for column in range(-1, 2):
                cell_center = (
                    convex_lattice_center
                    + column * convex_lattice_u
                    + row * convex_lattice_v
                )
                cell = make_parallelogram(
                    cell_center,
                    convex_lattice_u,
                    convex_lattice_v,
                    BLUE,
                    shade=False,
                    stroke_opacity=0.48,
                )
                cell_corners = parallelogram_corners(
                    cell_center,
                    convex_lattice_u,
                    convex_lattice_v,
                )
                cell_split = (
                    cell_corners[0]
                    + 0.82 * convex_lattice_u
                    + 0.50 * convex_lattice_v
                )
                convex_lattice_outlines.add(cell[1])
                convex_lattice_pieces.add(
                    Polygon(
                        cell_split,
                        cell_corners[0],
                        cell_corners[3],
                        color=BLACK,
                        stroke_width=0.55,
                        fill_color=VIOLET,
                        fill_opacity=0.40,
                    ),
                    Polygon(
                        cell_split,
                        cell_corners[1],
                        cell_corners[2],
                        color=BLACK,
                        stroke_width=0.55,
                        fill_color=GREEN,
                        fill_opacity=0.40,
                    ),
                    Polygon(
                        cell_corners[0],
                        cell_split,
                        cell_corners[1],
                        color=BLACK,
                        stroke_width=0.55,
                        fill_color=BLUE,
                        fill_opacity=0.40,
                    ),
                    Polygon(
                        cell_corners[3],
                        cell_split,
                        cell_corners[2],
                        color=BLACK,
                        stroke_width=0.55,
                        fill_color=ORANGE,
                        fill_opacity=0.40,
                    ),
                )
        convex_lattice_outlines.set_z_index(2)
        convex_lattice_pieces.set_z_index(1)
        convex_lattice = VGroup(
            convex_lattice_outlines,
            convex_lattice_pieces,
        )

        self.play(Write(convex_label))
        self.play(
            Create(convex_q_vertical[0]),
            FadeIn(convex_q_vertical_pieces),
            Create(convex_q_vertical[1]),
            Write(convex_q_vertical_label),
        )
        self.play(
            Create(convex_q_horizontal[0]),
            FadeIn(convex_q_horizontal_pieces),
            Create(convex_q_horizontal[1]),
            Write(convex_q_horizontal_label),
        )
        self.play(
            Create(convex_p[1]),
            Write(convex_p_label),
        )
        self.play(
            LaggedStart(*[
                TransformFromCopy(source, target)
                for source, target in zip(
                    convex_source_pieces, convex_p_pieces
                )
            ], lag_ratio=0.18),
            run_time=2.4,
        )
        self.play(Create(convex_lattice[0]), run_time=1.4)
        self.play(FadeIn(convex_lattice[1]), run_time=1.5)
        self.play(Write(formula))
        self.wait(2)

        convex_objects = VGroup(
            convex_q_vertical,
            convex_q_vertical_pieces,
            convex_q_horizontal,
            convex_q_horizontal_pieces,
            convex_p,
            convex_p_pieces,
            convex_q_vertical_label,
            convex_q_horizontal_label,
            convex_p_label,
            convex_lattice,
        )
        concave_label = Tex(
            r"Si $Q$ est concave", font_size=26, color=BLACK
        ).move_to([-1, 2.52, 0])
        self.play(
            FadeOut(convex_objects),
            Transform(convex_label, concave_label),
        )

        # II. Concave quadrilateral
        concave_demo_u = np.array([0.78, -0.05, 0])
        concave_demo_v = np.array([0.05, 0.70, 0])

        def make_concave_copy(center, diagonal):
            center = np.array(center, dtype=float)
            point_a = center - concave_demo_u / 2
            point_b = center + 1.35 * concave_demo_v
            point_c = center + concave_demo_u / 2
            point_d = center + 0.35 * concave_demo_v

            outline = Polygon(
                point_a,
                point_b,
                point_c,
                point_d,
                color=BLACK,
                stroke_width=1.6,
                fill_opacity=0,
            )
            if diagonal == "vertical":
                cut = DashedLine(
                    point_b,
                    point_d,
                    dash_length=0.07,
                    dashed_ratio=0.55,
                    color=BLACK,
                    stroke_width=1.25,
                )
            else:
                cut = DashedLine(
                    point_a,
                    point_c,
                    dash_length=0.07,
                    dashed_ratio=0.55,
                    color=BLACK,
                    stroke_width=1.25,
                )
            return VGroup(outline, cut), (
                point_a,
                point_b,
                point_c,
                point_d,
            )

        concave_q_vertical, concave_vertical_points = make_concave_copy(
            [-1.25, 1.35, 0], "vertical"
        )
        concave_q_horizontal, concave_horizontal_points = make_concave_copy(
            [-0.15, 1.35, 0], "horizontal"
        )

        vertical_a, vertical_b, vertical_c, vertical_d = (
            concave_vertical_points
        )
        concave_q_vertical_pieces = VGroup(
            Polygon(
                vertical_a,
                vertical_b,
                vertical_d,
                color=BLACK,
                stroke_width=0.7,
                fill_color=VIOLET,
                fill_opacity=0.72,
            ),
            Polygon(
                vertical_c,
                vertical_b,
                vertical_d,
                color=BLACK,
                stroke_width=0.7,
                fill_color=GREEN,
                fill_opacity=0.72,
            ),
        )

        horizontal_a, horizontal_b, horizontal_c, horizontal_d = (
            concave_horizontal_points
        )
        concave_q_horizontal_pieces = VGroup(
            Polygon(
                horizontal_a,
                horizontal_b,
                horizontal_c,
                horizontal_d,
                color=BLACK,
                stroke_width=0.7,
                fill_color=BLUE,
                fill_opacity=0.72,
            ),
        )
        concave_q_vertical_pieces.set_z_index(1)
        concave_q_horizontal_pieces.set_z_index(1)
        concave_q_vertical.set_z_index(2)
        concave_q_horizontal.set_z_index(2)
        concave_source_pieces = VGroup(
            concave_q_vertical_pieces[0],
            concave_q_vertical_pieces[1],
            concave_q_horizontal_pieces[0],
        )

        concave_p = make_parallelogram(
            [1.15, 1.55, 0],
            concave_demo_u,
            concave_demo_v,
            VIOLET,
            shade=False,
        )
        concave_p_corners = parallelogram_corners(
            [1.15, 1.55, 0], concave_demo_u, concave_demo_v
        )
        concave_p_split = (
            concave_p_corners[0]
            + 0.50 * concave_demo_u
            + 1.35 * concave_demo_v
        )
        concave_p_notch = (
            concave_p_corners[0]
            + 0.50 * concave_demo_u
            + 0.35 * concave_demo_v
        )
        concave_p_blue_quadrilateral = (
            concave_q_horizontal_pieces[0]
            .copy()
            .shift(concave_p_corners[0] - horizontal_a)
        )
        concave_transfer_triangle = Polygon(
            concave_p_corners[3],
            concave_p_split,
            concave_p_corners[2],
            color=BLACK,
            stroke_width=0.7,
            fill_color=ORANGE,
            fill_opacity=0.82,
        ).set_z_index(4)
        concave_p_pieces = VGroup(
            Polygon(
                concave_p_split,
                concave_p_corners[0],
                concave_p_corners[3],
                color=BLACK,
                stroke_width=0.7,
                fill_color=VIOLET,
                fill_opacity=0.72,
            ),
            Polygon(
                concave_p_split,
                concave_p_corners[1],
                concave_p_corners[2],
                color=BLACK,
                stroke_width=0.7,
                fill_color=GREEN,
                fill_opacity=0.72,
            ),
            concave_p_blue_quadrilateral,
        )
        concave_p_mask = Polygon(
            concave_p_corners[3],
            concave_p_split,
            concave_p_corners[2],
            color=WHITE,
            stroke_width=2,
            fill_color=WHITE,
            fill_opacity=1,
        )
        concave_p_pieces.set_z_index(1)
        concave_p_mask.set_z_index(2)
        concave_p.set_z_index(3)

        concave_q_vertical_label = Tex(
            r"$Q_1$", font_size=20, color=BLACK
        ).next_to(concave_q_vertical, DOWN, buff=0.10)
        concave_q_horizontal_label = Tex(
            r"$Q_2$", font_size=20, color=BLACK
        ).next_to(concave_q_horizontal, DOWN, buff=0.10)
        concave_p_label = Tex(
            r"$P$", font_size=20, color=BLACK
        ).next_to(concave_p, DOWN, buff=0.10)

        concave_lattice_outlines = VGroup()
        concave_lattice_pieces = VGroup()
        concave_lattice_center = np.array([0, -0.30, 0])
        for row in range(3):
            for column in range(3):
                cell_center = (
                    concave_lattice_center
                    + (column - 1) * concave_demo_u
                    + (row - 1) * concave_demo_v
                )
                cell = make_parallelogram(
                    cell_center,
                    concave_demo_u,
                    concave_demo_v,
                    VIOLET,
                    shade=False,
                )
                cell_corners = parallelogram_corners(
                    cell_center, concave_demo_u, concave_demo_v
                )
                cell_notch = (
                    cell_corners[0]
                    + 0.50 * concave_demo_u
                    + 0.35 * concave_demo_v
                )
                cell_top_left = (
                    cell_corners[0]
                    + (0.50 / 1.35) * concave_demo_u
                    + concave_demo_v
                )
                cell_top_right = (
                    cell_corners[1]
                    - (0.50 / 1.35) * concave_demo_u
                    + concave_demo_v
                )
                concave_lattice_outlines.add(cell[1])
                concave_lattice_pieces.add(
                    Polygon(
                        cell_corners[0],
                        cell_corners[3],
                        cell_top_left,
                        color=BLACK,
                        stroke_width=0.55,
                        fill_color=VIOLET,
                        fill_opacity=0.40,
                    ),
                    Polygon(
                        cell_corners[1],
                        cell_top_right,
                        cell_corners[2],
                        color=BLACK,
                        stroke_width=0.55,
                        fill_color=GREEN,
                        fill_opacity=0.40,
                    ),
                    Polygon(
                        cell_corners[0],
                        cell_top_left,
                        cell_top_right,
                        cell_corners[1],
                        cell_notch,
                        color=BLACK,
                        stroke_width=0.55,
                        fill_color=BLUE,
                        fill_opacity=0.40,
                    ),
                    Polygon(
                        cell_corners[0],
                        cell_notch,
                        cell_corners[1],
                        color=BLACK,
                        stroke_width=0.55,
                        fill_color=ORANGE,
                        fill_opacity=0.48,
                    ),
                )
        concave_lattice_pieces.set_z_index(1)
        concave_lattice_outlines.set_z_index(3)
        concave_lattice = VGroup(
            concave_lattice_outlines,
            concave_lattice_pieces,
        )

        self.play(
            Create(concave_q_vertical[0]),
            FadeIn(concave_q_vertical_pieces),
            Create(concave_q_vertical[1]),
            Write(concave_q_vertical_label),
        )
        self.play(
            Create(concave_q_horizontal[0]),
            FadeIn(concave_q_horizontal_pieces),
            Create(concave_q_horizontal[1]),
            Write(concave_q_horizontal_label),
        )
        self.play(
            Create(concave_p[1]),
            Write(concave_p_label),
        )
        self.play(
            LaggedStart(*[
                TransformFromCopy(source, target)
                for source, target in zip(
                    concave_source_pieces, concave_p_pieces
                )
            ], lag_ratio=0.18),
            run_time=2.4,
        )
        self.play(
            FadeIn(concave_transfer_triangle),
            run_time=0.5,
        )
        self.play(
            concave_transfer_triangle.animate.shift(
                concave_p_notch - concave_p_split
            ),
            FadeIn(concave_p_mask),
            run_time=1.2,
        )
        concave_transfer_triangle.set_z_index(1)
        self.play(Create(concave_lattice[0]), run_time=1.4)
        self.play(
            FadeIn(concave_lattice[1]),
            run_time=1.5,
        )
        self.wait(2)

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Proofs without words II:", font_size=30, color=BLACK),
            Tex(r"More exercises in", font_size=30, color=BLACK),
            Tex(r"visual thinking", font_size=30, color=BLACK),
            Tex(r"Roger B. Nelsen (2000), p. 21", font_size=30, color=BLACK)
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
