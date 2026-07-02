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
            for column in range(n):
                for height in range(column + 1):
                    cubes.add(
                        cube_at(
                            column * side, 0, height * side, side
                        )
                    )
            cubes.\
                move_to(np.array([0, 0, 0])).\
                rotate(PI / 2, axis=[0, 0, 1])
            return cubes

        def triangular_array_sequence(n, side, spacing):
            arrays = VGroup()
            for size in range(1, n + 1):
                arrays.add(triangular_array(size, side))
            arrays.arrange(RIGHT, buff=spacing)
            arrays.move_to(np.array([0, 0, 0]))
            return arrays

        C = triangular_array_sequence(5, 0.18, 0.12)
        self.play(FadeIn(C), run_time=0.5)

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
