"""
Visual proof of the problem of the Calissons
Proofs without Words I. Roger B. Nelsen. p. 142.
"""
import numpy as np

from manim import MovingCameraScene, Mobject
from manim import Brace, Line, Polygon
from manim import RoundedRectangle, Square
from manim import Create, Rotate, Transform, Uncreate, Write, Angle
from manim import FadeIn, FadeOut, FadeTransform, TransformFromCopy
from manim import FunctionGraph, VGroup
from manim import Text, Tex, MathTex

from manim import config

from manim import LEFT, RIGHT, UP, DOWN, PI, DR, DL, UR, UL, LIGHT

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


class Calissons(MovingCameraScene):
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
            Tex(r"Problème des", font_size=48, color=BLACK),
            Tex(r"Calissons", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Guy David \& Carlos Tomei", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        self.add(
            txt_title,
            txt,
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt),
        )

        def calisson(center, angle, side=0.34, color=BLUE):
            half_long = np.sqrt(3) * side / 2
            half_short = side / 2
            points = [
                center + np.array([-half_long, 0, 0]),
                center + np.array([0, half_short, 0]),
                center + np.array([half_long, 0, 0]),
                center + np.array([0, -half_short, 0]),
            ]
            return Polygon(
                *points,
                color=BLACK,
                stroke_width=1.7,
                fill_color=color,
                fill_opacity=0.9,
            ).rotate(angle, about_point=center)

        def lozenge_tiling_data(n, seed=12):
            """Create a perfect matching of the triangular hexagonal grid."""
            root_three = np.sqrt(3)

            def lattice_point(i, j):
                return np.array([i + j / 2, root_three * j / 2, 0])

            boundary = [
                lattice_point(0, 0),
                lattice_point(n, 0),
                lattice_point(n, n),
                lattice_point(0, 2 * n),
                lattice_point(-n, 2 * n),
                lattice_point(-n, n),
            ]

            def inside_hexagon(point):
                cross_products = []
                for start, end in zip(
                    boundary, boundary[1:] + boundary[:1]
                ):
                    edge = end - start
                    offset = point - start
                    cross_products.append(
                        edge[0] * offset[1] - edge[1] * offset[0]
                    )
                return (
                    min(cross_products) >= -1e-8
                    or max(cross_products) <= 1e-8
                )

            triangles = []
            for i in range(-n - 2, n + 2):
                for j in range(-2, 2 * n + 2):
                    candidates = [
                        (
                            "up",
                            [
                                lattice_point(i, j),
                                lattice_point(i + 1, j),
                                lattice_point(i, j + 1),
                            ],
                        ),
                        (
                            "down",
                            [
                                lattice_point(i + 1, j + 1),
                                lattice_point(i, j + 1),
                                lattice_point(i + 1, j),
                            ],
                        ),
                    ]
                    for orientation, points in candidates:
                        if inside_hexagon(sum(points) / 3):
                            triangles.append((orientation, points))

            edge_map = {}
            for index, (_, points) in enumerate(triangles):
                for start, end in zip(points, points[1:] + points[:1]):
                    edge = tuple(sorted((
                        tuple(np.round(start[:2], 6)),
                        tuple(np.round(end[:2], 6)),
                    )))
                    edge_map.setdefault(edge, []).append(index)

            adjacency = {
                index: []
                for index, (orientation, _) in enumerate(triangles)
                if orientation == "up"
            }
            for edge, indices in edge_map.items():
                if len(indices) != 2:
                    continue
                first, second = indices
                if triangles[first][0] == "up":
                    adjacency[first].append((second, edge))
                else:
                    adjacency[second].append((first, edge))

            generator = np.random.default_rng(seed)
            for neighbors in adjacency.values():
                generator.shuffle(neighbors)

            matched_down = {}

            def augment(up_index, visited):
                for down_index, _ in adjacency[up_index]:
                    if down_index in visited:
                        continue
                    visited.add(down_index)
                    if (
                        down_index not in matched_down
                        or augment(matched_down[down_index], visited)
                    ):
                        matched_down[down_index] = up_index
                        return True
                return False

            for up_index in adjacency:
                if not augment(up_index, set()):
                    raise ValueError("The triangular region was not tileable.")

            lozenges = []
            for down_index, up_index in matched_down.items():
                up_points = triangles[up_index][1]
                down_points = triangles[down_index][1]
                unique_points = {}
                for point in up_points + down_points:
                    unique_points[tuple(np.round(point[:2], 6))] = point

                center = sum(unique_points.values()) / 4
                ordered_points = sorted(
                    unique_points.values(),
                    key=lambda point: np.arctan2(
                        point[1] - center[1], point[0] - center[0]
                    ),
                )

                up_keys = {
                    tuple(np.round(point[:2], 6)) for point in up_points
                }
                down_keys = {
                    tuple(np.round(point[:2], 6)) for point in down_points
                }
                shared_keys = list(up_keys & down_keys)
                shared_edge = (
                    np.array(shared_keys[1]) - np.array(shared_keys[0])
                )
                shared_angle = np.arctan2(
                    shared_edge[1], shared_edge[0]
                ) % PI
                directions = [0, PI / 3, 2 * PI / 3]
                orientation = min(
                    range(3),
                    key=lambda index: abs(
                        shared_angle - directions[index]
                    ),
                )
                lozenges.append((ordered_points, orientation))

            return lozenges

        orientation_colors = ["#5DADE2", "#F0A35E", "#75C68B"]

        def make_tiling(
            tiling_data,
            colored,
            width,
            center,
            stroke_width=1.1,
        ):
            polygons = VGroup()
            for points, orientation in tiling_data:
                fill_color = (
                    orientation_colors[orientation] if colored else WHITE
                )
                polygon = Polygon(
                    *points,
                    color=BLACK,
                    stroke_width=stroke_width,
                    fill_color=fill_color,
                    fill_opacity=0.88 if colored else 0.18,
                )
                polygons.add(polygon)
            polygons.rotate(PI / 6)
            polygons.scale_to_fit_width(width)
            polygons.move_to(center)
            return polygons

        definition = VGroup(
            Tex(
                r"Un calisson est formé de deux triangles",
                font_size=23,
                color=BLACK,
            ),
            Tex(
                r"équilatéraux accolés par un côté.",
                font_size=23,
                color=BLACK,
            ),
        ).arrange(DOWN, buff=0.05).move_to([0, 3.45, 0])
        box_description = VGroup(
            Tex(
                r"Les calissons sont rangés dans une boîte",
                font_size=21,
                color=BLACK,
            ),
            Tex(
                r"en forme d'hexagone régulier.",
                font_size=21,
                color=BLACK,
            ),
        ).arrange(DOWN, buff=0.04).move_to([0, 2.75, 0])

        box_radius = 1.80
        box_center = np.array([0, -0.10, 0])
        box_vertices = [
            box_center
            + box_radius * np.array([
                np.cos(PI / 2 + index * PI / 3),
                np.sin(PI / 2 + index * PI / 3),
                0,
            ])
            for index in range(6)
        ]
        box = Polygon(
            *box_vertices,
            color=BLACK,
            stroke_width=2.2,
        )
        side_pairs = VGroup(
            VGroup(
                Line(
                    box_vertices[1], box_vertices[2],
                    color=orientation_colors[0], stroke_width=4.2,
                ),
                Line(
                    box_vertices[4], box_vertices[5],
                    color=orientation_colors[0], stroke_width=4.2,
                ),
            ),
            VGroup(
                Line(
                    box_vertices[2], box_vertices[3],
                    color=orientation_colors[1], stroke_width=4.2,
                ),
                Line(
                    box_vertices[5], box_vertices[0],
                    color=orientation_colors[1], stroke_width=4.2,
                ),
            ),
            VGroup(
                Line(
                    box_vertices[0], box_vertices[1],
                    color=orientation_colors[2], stroke_width=4.2,
                ),
                Line(
                    box_vertices[3], box_vertices[4],
                    color=orientation_colors[2], stroke_width=4.2,
                ),
            ),
        )

        sample_calissons = VGroup(
            calisson(
                np.array([-0.58, 0.88, 0]),
                0,
                color=orientation_colors[0],
            ),
            calisson(
                np.array([0, 1.18, 0]),
                PI / 3,
                color=orientation_colors[1],
            ),
            calisson(
                np.array([0.58, 0.88, 0]),
                2 * PI / 3,
                color=orientation_colors[2],
            ),
        )
        orientation_caption = Tex(
            r"trois orientations possibles",
            font_size=22,
            color=BLACK,
        ).move_to([0, 0.42, 0])
        side_label = MathTex(
            r"n", font_size=24, color=BLACK
        ).next_to(box, RIGHT, buff=0.14)
        orientation_explanation = VGroup(
            Tex(
                r"La petite diagonale doit être parallèle à une",
                font_size=19,
                color=BLACK,
            ),
            Tex(
                r"paire de côtés opposés de l'hexagone.",
                font_size=19,
                color=BLACK,
            ),
            Tex(
                r"$3$ directions de côtés $\Longrightarrow$ "
                r"$3$ orientations.",
                font_size=21,
                color=BLACK,
            ),
        ).arrange(DOWN, buff=0.06).move_to([0, -2.78, 0])

        self.play(
            Write(definition),
            Write(box_description),
            Create(box),
            run_time=1.6,
        )
        self.play(
            Create(side_pairs),
            FadeIn(sample_calissons),
            Write(orientation_caption),
            Write(side_label),
            Write(orientation_explanation),
            run_time=1.6,
        )
        self.wait(2)

        self.play(
            FadeOut(definition),
            FadeOut(box_description),
            FadeOut(box),
            FadeOut(side_pairs),
            FadeOut(sample_calissons),
            FadeOut(orientation_caption),
            FadeOut(side_label),
            FadeOut(orientation_explanation),
        )

        theorem = VGroup(
            Tex(
                r"Dans tout pavage hexagonal, chaque",
                font_size=22,
                color=BLACK,
            ),
            Tex(
                r"orientation représente un tiers",
                font_size=22,
                color=BLACK,
            ),
            Tex(
                r"des calissons.",
                font_size=22,
                color=BLACK,
            ),
        ).arrange(DOWN, buff=0.06).move_to([0, 3.25, 0])
        proof_caption = VGroup(
            Tex(
                r"Colorons un même pavage hexagonal",
                font_size=20,
                color=BLACK,
            ),
            Tex(
                r"selon l'orientation.",
                font_size=20,
                color=BLACK,
            )
        ).arrange(DOWN, buff=0.06).move_to([0, 2, 0])

        tiling_data = lozenge_tiling_data(4)
        uncolored_tiling = make_tiling(
            tiling_data,
            colored=False,
            width=1.88,
            center=np.array([-1.08, 0.40, 0]),
        )
        colored_tiling = make_tiling(
            tiling_data,
            colored=True,
            width=1.88,
            center=np.array([1.08, 0.40, 0]),
        )
        tiling_labels = VGroup(
            Tex(r"hexagone", font_size=20, color=BLACK).next_to(
                uncolored_tiling, DOWN, buff=0.14
            ),
            Tex(r"orientations", font_size=20, color=BLACK).next_to(
                colored_tiling, DOWN, buff=0.14
            ),
        )

        legend = VGroup()
        for index, color in enumerate(orientation_colors):
            sample = calisson(
                np.zeros(3),
                index * PI / 3,
                side=0.20,
                color=color,
            )
            count = MathTex(r"n^2", font_size=20, color=BLACK)
            legend.add(VGroup(sample, count).arrange(RIGHT, buff=0.08))
        legend.arrange(RIGHT, buff=0.22).move_to([0, -1.70, 0])

        conclusion = VGroup(
            MathTex(
                r"N_1=N_2=N_3=n^2,",
                r"\qquad N=3n^2",
                font_size=23,
                color=BLACK,
            ),
            MathTex(
                r"N_1=N_2=N_3=\frac{N}{3}",
                font_size=25,
                color=BLACK,
            ),
        ).arrange(DOWN, buff=0.18).move_to([0, -2.40, 0])

        self.play(Write(theorem), Write(proof_caption), run_time=1.4)
        self.wait(1)
        self.play(Create(uncolored_tiling), Write(tiling_labels[0]), run_time=2)
        self.play(
            TransformFromCopy(uncolored_tiling, colored_tiling),
            Write(tiling_labels[1]),
            run_time=2,
        )
        self.play(FadeIn(legend), Write(conclusion), run_time=1.6)
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"American Mathematical", font_size=30, color=BLACK),
            Tex(r"Monthly, vol. 96, no. 5", font_size=30, color=BLACK),
            Tex(r"(May 1989), p.152.", font_size=30, color=BLACK),
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

        
