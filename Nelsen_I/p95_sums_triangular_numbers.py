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

        axis_origin = np.array([-1.80, 3.30, 0])
        axis_x_end = axis_origin + np.array([0.42, -0.12, 0])
        axis_y_end = axis_origin + np.array([-0.34, 0.20, 0])
        axis_z_end = axis_origin + np.array([0.00, 0.46, 0])
        axis_guide = VGroup(
            Arrow(
                axis_origin, axis_x_end,
                buff=0,
                color=BLACK,
                stroke_width=2,
                max_tip_length_to_length_ratio=0.22
            ),
            Arrow(
                axis_origin, axis_y_end,
                buff=0,
                color=BLACK,
                stroke_width=2,
                max_tip_length_to_length_ratio=0.22
            ),
            Arrow(
                axis_origin, axis_z_end,
                buff=0,
                color=BLACK,
                stroke_width=2,
                max_tip_length_to_length_ratio=0.22
            ),
            Tex(r"$x$", font_size=16, color=BLACK).next_to(
                axis_x_end, RIGHT, buff=0.02
            ),
            Tex(r"$y$", font_size=16, color=BLACK).next_to(
                axis_y_end, LEFT, buff=0.02
            ),
            Tex(r"$z$", font_size=16, color=BLACK).next_to(
                axis_z_end, UP, buff=0.02
            ),
        )
        self.add(axis_guide)
        self.add_fixed_in_frame_mobjects(axis_guide)

        def cube_at(x, y, z, side):
            cube = Cube(
                side_length=side,
                fill_color="#FFFFFF",
                fill_opacity=1,
                stroke_color=BLACK,
                stroke_width=0.55
            )
            cube.move_to(np.array([x, y, z]))
            face_colors = [
                "#BEBEBE", "#FFFFFF", "#FFFFFF",
                "#BEBEBE", "#D8D8D8", "#FFFFFF"
            ]
            for face, color in zip(cube, face_colors):
                face.set_fill(color, opacity=1)
                face.set_stroke(BLACK, width=0.55)
            return cube

        def triangular_array(n, side):
            cubes = VGroup()
            number = 1
            for column in range(n):
                for height in range(column + 1):
                    center = np.array(
                        [column * side, 0, height * side]
                    )
                    cube = cube_at(*center, side)
                    cubes.add(cube)
                    number += 1
            cubes.\
                move_to(np.array([0, 0, 0])).\
                rotate(PI / 2, axis=[0, 0, 1])
            return cubes

        def triangular_array_sequence(n, side, spacing):
            arrays = VGroup()
            x_step = side + spacing
            for index, size in enumerate(range(1, n + 1)):
                array = triangular_array(size, side)
                cube_one_center = array[0][0].get_center()
                target = np.array([index * x_step, 0, 0])
                array.shift(target - cube_one_center)
                arrays.add(array)
            arrays.move_to(np.array([0, 0, 0]))
            return arrays

        def cuboid_slab(nx, y_index, nz, side):
            slab = VGroup()
            for x in range(nx):
                for z in range(nz):
                    slab.add(cube_at(x * side, y_index * side, z * side, side))
            return slab


        split = triangular_array_sequence(5, 0.18, 0.2).\
            move_to(np.array([0, 0, 2]))
        self.play(FadeIn(split), run_time=0.5)

        no_split = triangular_array_sequence(5, 0.18, 0).\
            move_to(np.array([0, 0, 2]))
        
        no_split_other = triangular_array_sequence(5, -0.18, 0).\
            move_to(np.array([0, 0, -3]))
        
        arrow_x = no_split.get_critical_point(RIGHT)[0] + 0.28
        arrow_y = no_split.get_critical_point(
            np.array([0, 1, 0]))[1] + 0.28
        arrow_bottom_z = no_split.get_critical_point(
            np.array([0, 0, -1]))[2]
        arrow_top_z = no_split.get_critical_point(
            np.array([0, 0, 1]))[2]
        no_split_arrow = DoubleArrow(
            [arrow_x, arrow_y, arrow_bottom_z],
            [arrow_x, arrow_y, arrow_top_z],
            buff=0,
            color=BLACK,
            stroke_width=1.5,
            max_tip_length_to_length_ratio=0.12
        )
        no_split_label = Tex(r"$n$", font_size=24, color=BLACK)
        no_split_label.rotate(PI / 2, axis=[1, 0, 0])
        no_split_label.move_to(
            [
                arrow_x + 0.16,
                arrow_y,
                (arrow_bottom_z + arrow_top_z) / 2
            ]
        )

        def rotated_no_split_copy(
            to_copy,
            center, x_rotation=0, y_rotation=0, z_rotation=0
        ):
            copy = to_copy.copy()
            copy.scale(0.75, about_point=copy.get_center())
            if x_rotation:
                copy.rotate(
                    x_rotation,
                    axis=np.array([1, 0, 0]),
                    about_point=copy.get_center()
                )
            if y_rotation:
                copy.rotate(
                    y_rotation,
                    axis=np.array([0, 1, 0]),
                    about_point=copy.get_center()
                )
            if z_rotation:
                copy.rotate(
                    z_rotation,
                    axis=np.array([0, 0, 1]),
                    about_point=copy.get_center()
                )
            copy.move_to(center)
            return copy

        no_split_rotations = VGroup(
            rotated_no_split_copy(
                no_split,
                np.array([-1.5, -0.2, 0.15]),
                y_rotation=PI / 2
            ),
            rotated_no_split_copy(
                no_split_other,
                np.array([0, -0.05, 0.35]),
                x_rotation=-PI / 2,
                y_rotation=4 * PI / 2,      
                z_rotation=0,
            ),
            rotated_no_split_copy(
                no_split,
                np.array([1.15, 0.2, 0.35]),
                x_rotation=PI / 2,
                y_rotation=-PI / 2,
            ),
            rotated_no_split_copy(
                no_split,
                np.array([1.15, 0.05, -0.60]),
            ),
            rotated_no_split_copy(
                no_split_other,
                np.array([-1, 0.3, -1.6]),
                x_rotation=PI / 2,
                y_rotation=2 * PI,
                z_rotation=PI / 2,
            ),
            rotated_no_split_copy(
                no_split,
                np.array([-1.4, -0.2, -1]),
                x_rotation=PI / 2,
                y_rotation=3 * PI / 2,      
                z_rotation=PI,
            ),
        )

        combined_no_split = VGroup(*[
            cuboid_slab(7, y_index, 5, 0.135)
            for y_index in range(6)
        ])
        combined_no_split.move_to(np.array([0, 0, -1.15]))

        self.play(
            Transform(split, no_split), run_time=1
        )
        self.play(
            Create(no_split_arrow),
            Write(no_split_label),
            run_time=0.5
        )
        
        no_split_copy_0 = no_split.copy()
        no_split_copy_1 = no_split.copy()
        no_split_copy_2 = no_split.copy()
        no_split_copy_3 = no_split.copy()
        no_split_copy_4 = no_split.copy()
        no_split_copy_5 = no_split.copy()

        self.play(
            Transform(no_split_copy_0, no_split_rotations[0]),
        )
        self.play(
            Transform(no_split_copy_1, no_split_rotations[1]),
        )
        self.play(
            Transform(no_split_copy_2, no_split_rotations[2]),
        )
        self.play(
            Transform(no_split_copy_3, no_split_rotations[3]),
        )
        self.play(
            Transform(no_split_copy_4, no_split_rotations[4]),
        )
        self.play(
            Transform(no_split_copy_5, no_split_rotations[5]),
        )

        no_split_rotations_copy = no_split_rotations.copy()

        self.play(
            FadeOut(no_split_copy_0),
            FadeOut(no_split_copy_1),
            FadeOut(no_split_copy_2),
            FadeOut(no_split_copy_3),
            FadeOut(no_split_copy_4),
            FadeOut(no_split_copy_5),
            Transform(
                no_split_rotations_copy, combined_no_split
            ),
            run_time=1
        )


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
