"""
Visual proof of the sums of triangular numbers II.
Proofs without Words. Roger B. Nelsen. p. 95.
"""
import numpy as np

from manim import ThreeDScene
from manim import Create, Uncreate, Write
from manim import VGroup, FadeIn, FadeOut, FunctionGraph, Transform
from manim import MathTable, Brace, RoundedRectangle
from manim import Arrow, Cube, DoubleArrow, Line, Text, Tex

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
            Tex(r"Roger B. Nelsen", font_size=28, color=BLACK)
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


        self.set_camera_orientation(
            phi=62 * DEGREES,
            theta=-48 * DEGREES,
            zoom=1.06
        )


        def cube_at(x, y, z, side):
            cube = Cube(
                side_length=side,
                fill_color="#FFFFFF",
                fill_opacity=1,
                stroke_color=BLACK,
                stroke_width=0.55
            )
            cube.move_to(side * np.array([x, y, z]))
            face_colors = [
                "#BEBEBE", "#FFFFFF", "#FFFFFF",
                "#BEBEBE", "#D8D8D8", "#FFFFFF"
            ]
            for face, color in zip(cube, face_colors):
                face.set_fill(color, opacity=1)
                face.set_stroke(BLACK, width=0.55)
            return cube

        def block_from_coords(coords, side):
            cubes = VGroup()
            for x, y, z in sorted(
                coords,
                key=lambda c: (c[1], c[0], c[2])
            ):
                cubes.add(cube_at(x, y, z, side))
            cubes.rotate(
                1.5,
                axis=np.array([0, 0, 1]),
                about_point=cubes.get_center()
            )
            return cubes

        def triangular_stack(k, side):
            coords = []
            for x in range(k):
                for y in range(x + 1):
                    for z in range(k - x):
                        coords.append((x, y, z))
            return block_from_coords(coords, side)

        def triangular_number_sequence(n, side):
            group = VGroup()
            cursor = 0
            for k in range(1, n + 1):
                coords = []
                for x in range(k):
                    for z in range(x + 1):
                        coords.append((cursor + x, 0, z))
                group.add(block_from_coords(coords, side))
                cursor += k + 1
            return group

        def layered_triangular_stack(n, side):
            coords = []
            for y in range(n):
                for x in range(y + 1):
                    for z in range(x + 1):
                        coords.append((x, y, z))
            return block_from_coords(coords, side)

        def cuboid(nx, ny, nz, side):
            coords = [
                (x, y, z)
                for x in range(nx)
                for y in range(ny)
                for z in range(nz)
            ]
            return block_from_coords(coords, side)

        def orient(group, center, scale=1, z_rotation=0, y_rotation=0):
            group.scale(scale)
            if z_rotation:
                group.rotate(z_rotation, axis=np.array([0, 0, 1]), about_point=group.get_center())
            if y_rotation:
                group.rotate(y_rotation, axis=np.array([0, 1, 0]), about_point=group.get_center())
            group.move_to(center)
            return group

        side = 0.16
        separated = orient(
            triangular_number_sequence(5, side),
            np.array([-1.45, 0.15, 1.15]),
            scale=0.75,
            z_rotation=0,
            y_rotation=0
        )
        first_stack = orient(
            layered_triangular_stack(5, side),
            np.array([1.05, 0.15, 1.15]),
            scale=0.78,
            z_rotation=-PI / 2,
            y_rotation=0
        )

        middle_side = 0.125
        middle_pieces = VGroup(
            orient(triangular_stack(4, middle_side), np.array([-1.28, 0.12, 0.00]), 0.78, PI / 2),
            orient(triangular_stack(4, middle_side), np.array([-0.23, 0.08, 0.08]), 0.82, -0.15),
            orient(triangular_stack(4, middle_side), np.array([1.03, 0.12, 0.03]), 0.80, PI),
            orient(triangular_stack(4, middle_side), np.array([-1.22, 0.10, -0.92]), 0.90, -PI / 2),
            orient(triangular_stack(4, middle_side), np.array([-0.08, 0.08, -1.08]), 0.94, 0.18),
            orient(triangular_stack(4, middle_side), np.array([1.05, 0.10, -0.92]), 0.86, PI)
        )

        final_side = 0.142
        final_block = orient(
            cuboid(7, 6, 5, final_side),
            np.array([-0.03, 0.02, -3.22]),
            scale=1.0,
            z_rotation=0
        )

        rearrange_arrow = Arrow(
            [-0.22, 1.38, 0], [0.28, 1.38, 0],
            buff=0,
            color=BLACK,
            stroke_width=2.4,
            max_tip_length_to_length_ratio=0.18
        )
        top_height_arrow = DoubleArrow(
            [1.72, 1.08, 0], [1.72, 1.95, 0],
            buff=0,
            color=BLACK,
            stroke_width=1.5,
            max_tip_length_to_length_ratio=0.12
        )
        top_height_label = Tex(r"$n$", font_size=22, color=BLACK).next_to(
            top_height_arrow, RIGHT, buff=0.04
        )
        bottom_height_arrow = DoubleArrow(
            [1.38, -2.88, 0], [1.38, -2.02, 0],
            buff=0,
            color=BLACK,
            stroke_width=1.5,
            max_tip_length_to_length_ratio=0.1
        )
        bottom_height_label = Tex(r"$n$", font_size=22, color=BLACK).next_to(
            bottom_height_arrow, RIGHT, buff=0.04
        )
        width_arrow = DoubleArrow(
            [-1.18, -3.43, 0], [0.52, -3.66, 0],
            buff=0,
            color=BLACK,
            stroke_width=1.5,
            max_tip_length_to_length_ratio=0.08
        )
        width_label = Tex(r"$n+2$", font_size=20, color=BLACK).rotate(-0.15).move_to([-0.35, -3.60, 0])
        depth_arrow = DoubleArrow(
            [0.70, -3.62, 0], [1.28, -3.40, 0],
            buff=0,
            color=BLACK,
            stroke_width=1.5,
            max_tip_length_to_length_ratio=0.08
        )
        depth_label = Tex(r"$n+1$", font_size=20, color=BLACK).rotate(0.35).move_to([1.04, -3.66, 0])
        fixed_annotations = VGroup(
            rearrange_arrow,
            top_height_arrow,
            top_height_label,
            bottom_height_arrow,
            bottom_height_label,
            width_arrow,
            width_label,
            depth_arrow,
            depth_label,
        )
        #self.add_fixed_in_frame_mobjects(*fixed_annotations)

        self.play(FadeIn(separated), run_time=1)
        self.play(
            Transform(separated, first_stack),
            # Create(rearrange_arrow),
            # Create(top_height_arrow),
            # Write(top_height_label),
            run_time=2
        )
        # self.play(FadeIn(middle_pieces), run_time=2)
        # self.play(
        #     FadeIn(final_block),
        #     Create(bottom_height_arrow),
        #     Write(bottom_height_label),
        #     Create(width_arrow),
        #     Write(width_label),
        #     Create(depth_arrow),
        #     Write(depth_label),
        #     run_time=2
        # )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        self.move_camera(
            phi=0,
            theta=-90 * DEGREES,
            gamma=0,
            zoom=1,
            run_time=0.5
        )

        # Logo
        ref = [
            Tex(r"College Mathematics Journal,", font_size=26, color=BLACK),
            Tex(r"vol. 23, no. 5 (Nov. 1992)", font_size=26, color=BLACK),
            Tex(r"p. 417.", font_size=26, color=BLACK),
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
