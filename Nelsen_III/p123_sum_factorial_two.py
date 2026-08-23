"""
Visual proof of the sum of factorials of order two.
Proofs without Words III. Roger B. Nelsen. p. 123.
"""
import numpy as np

from manim import ThreeDScene
from manim import Create, Uncreate, Write
from manim import Brace, VGroup, FadeIn, FadeOut, FunctionGraph
from manim import LaggedStart
from manim import Cube, MathTex, Text, Tex

from manim import config
from manim import DEGREES, LEFT, RIGHT, DOWN, LIGHT, ORIGIN, OUT, UP

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


class SumFactorialTwo(ThreeDScene):
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
            Tex(r"La somme des", font_size=48, color=BLACK),
            Tex(r"factorielles d'ordre", font_size=48, color=BLACK),
            Tex(r"deux", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Giorgio Goldoni", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        results = [
            Tex(r"$\displaystyle\sum_{k=1}^n k(k +1) = \dfrac{n(n+1)(n+2)}{3}$", font_size=24, color=BLACK),
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

        phi = 66 * DEGREES
        theta = -52 * DEGREES
        self.set_camera_orientation(phi=phi, theta=theta, zoom=1)

        # Camera-plane basis vectors let the 3D solids use page-like positions.
        view_right = np.array([-np.sin(theta), np.cos(theta), 0])
        view_up = np.array([
            -np.cos(phi) * np.cos(theta),
            -np.cos(phi) * np.sin(theta),
            np.sin(phi),
        ])

        def screen_point(x, y):
            return x * view_right + y * view_up

        def cube_at(x, y, z, side, color=None):
            cube = Cube(
                side_length=side,
                fill_color=color or "#F4F4F4",
                fill_opacity=1,
                stroke_color=BLACK,
                stroke_width=0.55,
            )
            cube.move_to(side * np.array([x, y, z]))
            face_colors = [color] * 6 if color else [
                "#D0D0D0", "#FAFAFA", "#F5F5F5",
                "#D8D8D8", "#E6E6E6", "#FFFFFF",
            ]
            for face, face_color in zip(cube, face_colors):
                face.set_fill(face_color, opacity=1)
                face.set_stroke(BLACK, width=0.55)
            return cube

        def voxel_solid(coords, side, color=None, center=True):
            solid = VGroup(*[
                cube_at(x, y, z, side, color) for x, y, z in coords
            ])
            if center:
                solid.move_to(ORIGIN)
            return solid

        def factorial_staircase(n):
            coords = []
            for z in range(n):
                layer_size = n - z
                for x in range(layer_size + 1):
                    for y in range(layer_size):
                        coords.append((x, y, z))
            return coords

        def factorial_staircase_2(n):
            coords = []
            for z in range(n):
                layer_size = n - z
                for x in range(layer_size):
                    for y in range(layer_size + 1):
                        coords.append((x, y, z))
            return coords

        def place_on_screen(mobject, x, y):
            return mobject.move_to(screen_point(x, y))

        n = 5
        staircase_coords = factorial_staircase(n)
        staircase_coords_2 = factorial_staircase_2(n)
        piece_colors = [BLUE, GREEN, ORANGE]
        piece_label_colors = ["#3F91BB", "#438B5C", "#BC7042"]

        definition = MathTex(
            r"S=1\cdot2+2\cdot3+3\cdot4+\cdots+n(n+1)",
            font_size=27,
            color=BLACK,
        ).move_to([0, 3.35, 0])
        definition.scale_to_fit_width(4.05)

        first_staircase = voxel_solid(
            staircase_coords, side=0.17, color=piece_colors[0]
        )
        first_staircase.apply_matrix(
            np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        )

        second_staircase = voxel_solid(
            staircase_coords_2, side=0.17, color=piece_colors[1]
        )
        second_staircase.apply_matrix(
            np.array([[0, 1, 0], [0, 0, -1], [-1, 0, 0]])
        )

        third_staircase = voxel_solid(
            staircase_coords, side=0.17, color=piece_colors[2]
        )
        third_staircase.apply_matrix(
            np.array([[0, 0, -1], [1, 0, 0], [0, -1, 0]])
        )

        stage_one = VGroup(
            first_staircase,
            second_staircase,
            third_staircase,
        )
        for solid, (x, y) in zip(
            stage_one,
            [(-0.7, 0.72), (0, 2), (0.7, 0.72)],
        ):
            place_on_screen(solid, x, y)

        three_sum = MathTex(
            r"S", r"+", r"S", r"+", r"S", r"=", r"3S",
            font_size=32,
            color=BLACK,
        ).move_to([0, -2.35, 0])
        three_sum[0].set_color(piece_label_colors[0])
        three_sum[2].set_color(piece_label_colors[1])
        three_sum[4].set_color(piece_label_colors[2])

        final_side = 0.17
        assembly_center = screen_point(0, 0.05)
        box_dimensions = np.array([n + 2, n + 1, n])
        box_center = (box_dimensions - 1) / 2

        # These offsets pack the three already-oriented staircases exactly into
        # the (n + 2) x (n + 1) x n cuboid. Only translations are required.
        piece_dimensions = [
            np.array([n + 1, n, n]),
            np.array([n + 1, n, n]),
            np.array([n, n + 1, n]),
        ]
        lattice_offsets = [
            np.array([0, 0, 0]),
            np.array([0, 1, 0]),
            np.array([2, 0, 0]),
        ]
        target_centers = [
            assembly_center + final_side * (
                offset + (dimensions - 1) / 2 - box_center
            )
            for dimensions, offset in zip(piece_dimensions, lattice_offsets)
        ]

        product_formula = MathTex(
            r"3S=n(n+1)(n+2)",
            font_size=31,
            color=BLACK,
        ).move_to(three_sum)
        conclusion = MathTex(
            r"S=\frac{n(n+1)(n+2)}{3}",
            font_size=31,
            color=BLACK,
        ).move_to(three_sum)
        product_formula.set_opacity(0)
        conclusion.set_opacity(0)

        self.add_fixed_in_frame_mobjects(definition)
        self.play(Write(definition), run_time=0.7)
        self.play(
            LaggedStart(*[FadeIn(solid) for solid in stage_one], lag_ratio=0.18),
            run_time=1.2,
        )

        self.add_fixed_in_frame_mobjects(three_sum)
        self.add_fixed_in_frame_mobjects(product_formula, conclusion)
        self.play(Write(three_sum), run_time=0.6)
        self.wait(0.4)

        self.play(
            stage_one[0].animate.move_to(target_centers[0]),
            run_time=1.4,
        )
        self.play(
            stage_one[1].animate.move_to(target_centers[1]),
            run_time=1.4,
        )
        self.play(
            stage_one[2].animate.move_to(target_centers[2]),
            run_time=1.4,
        )
        self.play(
            three_sum.animate.set_opacity(0),
            product_formula.animate.set_opacity(1),
            run_time=0.9,
        )
        self.wait(0.5)
        self.play(
            product_formula.animate.set_opacity(0),
            conclusion.animate.set_opacity(1),
            run_time=0.8,
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        self.move_camera(
            phi=0,
            theta=-90 * DEGREES,
            gamma=0,
            zoom=1,
            run_time=0.5,
        )

        # Logo
        ref = [
            Tex(r"Mathematical Intelligencer,", font_size=30, color=BLACK),
            Tex(r"vol. 24, no. 4 (Fall 2002),", font_size=30, color=BLACK),
            Tex(r" pp. 67-69.", font_size=30, color=BLACK)
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
