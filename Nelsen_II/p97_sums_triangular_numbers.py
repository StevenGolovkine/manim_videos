"""
Visual proof of Sums of Triangular Numbers. IV
Proofs without Words II. Roger B. Nelsen. p. 97.
"""
import numpy as np

from manim import ThreeDScene
from manim import Create, Uncreate, Write, TransformFromCopy
from manim import VGroup, FadeIn, FadeOut, FunctionGraph
from manim import Text, Tex, LaggedStart, DoubleArrow, MathTex, Sphere

from manim import config
from manim import LEFT, RIGHT, DOWN, LIGHT, UP, PI, DEGREES

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

class Tri(ThreeDScene):
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
            Tex(r"des nombres", font_size=48, color=BLACK),
            Tex(r"triangulaires", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])


        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"D. Haunsperger \& S. Kennedy", font_size=28, color=BLACK),
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
            run_time=0.5
        )
        self.wait(0.5)

        phi = 64 * DEGREES
        theta = -50 * DEGREES
        self.set_camera_orientation(phi=phi, theta=theta, zoom=1)

        # Camera-plane vectors let 3D groups be laid out like the source page.
        view_right = np.array([-np.sin(theta), np.cos(theta), 0])
        view_up = np.array([
            -np.cos(phi) * np.cos(theta),
            -np.cos(phi) * np.sin(theta),
            np.sin(phi),
        ])

        def screen_point(x, y):
            return x * view_right + y * view_up

        def cannonball(center, radius, color):
            return Sphere(
                center=center,
                radius=radius,
                resolution=(8, 8),
                fill_color=color,
                fill_opacity=1,
                checkerboard_colors=[color, color],
                stroke_color=BLACK,
                stroke_width=0.02,
            )

        def triangular_positions(size, spacing):
            positions = []
            for row in range(size):
                for column in range(size - row):
                    positions.append(np.array([
                        spacing * (column + row / 2),
                        spacing * np.sqrt(3) * row / 2,
                        0,
                    ]))
            center = np.mean(positions, axis=0)
            return [position - center for position in positions]

        def rectangular_positions(rows, columns, spacing):
            positions = [
                np.array([column * spacing, row * spacing, 0])
                for row in range(rows)
                for column in range(columns)
            ]
            center = np.mean(positions, axis=0)
            return [position - center for position in positions]

        def sphere_cloud(positions, radius, colors):
            return VGroup(*[
                cannonball(position, radius, colors[index])
                for index, position in enumerate(positions)
            ])

        n = 5
        sphere_spacing = 0.32
        sphere_radius = 0.115
        layer_height = sphere_spacing * np.sqrt(2 / 3)
        layer_colors = [
            "#4A7184", "#4F7C63", "#88783C", "#995E3E", "#8B4565"
        ]

        formula = MathTex(
            r"T_k=1+2+\cdots+k",
            r"\Longrightarrow",
            r"\sum_{k=1}^{n}T_k",
            r"=\sum_{k=1}^{n}k(n-k+1)",
            font_size=25,
            color=BLACK,
        ).move_to([0, 3.30, 0])
        formula.scale_to_fit_width(4.08)
        self.add_fixed_in_frame_mobjects(formula)

        pyramid_positions = []
        pyramid_colors = []
        for level, size in enumerate(range(n, 0, -1)):
            for position in triangular_positions(size, sphere_spacing):
                pyramid_positions.append(
                    position + np.array([0, 0, level * layer_height])
                )
                pyramid_colors.append(layer_colors[level])

        pyramid = sphere_cloud(
            pyramid_positions, sphere_radius, pyramid_colors
        ).move_to(screen_point(0, 0.68))

        height_arrow = DoubleArrow(
            [1.06, -0.02, 0],
            [1.06, 1.48, 0],
            buff=0,
            tip_length=0.10,
            stroke_width=1.6,
            color=BLACK,
        )
        height_label = MathTex(
            r"n", font_size=24, color=BLACK
        ).next_to(height_arrow, RIGHT, buff=0.10)
        #self.add_fixed_in_frame_mobjects(height_arrow, height_label)

        self.play(Write(formula), run_time=0.8)
        self.play(
            *[FadeIn(ball, scale=0.45) for ball in pyramid],
            run_time=1.8,
        )
        self.add_fixed_in_frame_mobjects(height_arrow, height_label)
        self.play(
            Create(height_arrow),
            Write(height_label)
        )
        self.wait(0.5)

        self.play(
            pyramid.animate.move_to(screen_point(-1, 0.55)),
            FadeOut(height_arrow),
            FadeOut(height_label),
            run_time=1.2,
        )
        self.wait(0.5)

        layer_screen_y = [-1.30, -0.63, 0.04, 0.71, 1.38]
        separated_positions = []
        separated_colors = []
        for level, size in enumerate(range(n, 0, -1)):
            layer_center = screen_point(0.88, layer_screen_y[level] + 0.5)
            for position in triangular_positions(size, 0.225):
                separated_positions.append(position + layer_center)
                separated_colors.append(layer_colors[level])

        separated_layers = sphere_cloud(
            separated_positions, 0.082, separated_colors
        )

        count_tex = [
            r"\frac{n(n+1)}{2}", r"\vdots", r"6", r"3", r"1"
        ]
        count_labels = VGroup()
        count_y = layer_screen_y
        for index, label in enumerate(count_tex):
            count_labels.add(
                MathTex(label, font_size=18, color=BLACK).move_to(
                    [1.77, count_y[index] + 0.5, 0]
                )
            )
        plus_labels = VGroup(*[
            MathTex(r"+", font_size=18, color=BLACK).move_to(
                [1.77, (count_y[index] + count_y[index + 1]) / 2 + 0.5, 0]
            )
            for index in range(n - 1)
        ])

        self.play(
            TransformFromCopy(pyramid, separated_layers),
            run_time=2.0,
        )
        self.add_fixed_in_frame_mobjects(count_labels, plus_labels)
        self.play(
            *[Write(label) for label in count_labels],
            *[Write(plus) for plus in plus_labels],
        )
        self.wait(0.8)

        term_colors = [
            "#8B4565", "#995E3E", "#88783C", "#4F7C63", "#4A7184"
        ]
        row_centers = [-1.70, -0.86, 0, 0.86, 1.70]
        row_positions = []
        row_colors = []
        for k in range(1, n + 1):
            group_center = screen_point(row_centers[k - 1], -2.15)
            positions = rectangular_positions(k, n - k + 1, 0.18)
            row_positions.extend([
                position + group_center for position in positions
            ])
            row_colors.extend([term_colors[k - 1]] * len(positions))

        row_arrays = sphere_cloud(row_positions, 0.068, row_colors)
        term_formula = MathTex(
            r"1(n)", r"+", r"2(n-1)", r"+", r"3(n-2)",
            r"+\cdots+", r"n(1)",
            font_size=22,
            color=BLACK,
        ).move_to([0, -2.92, 0])
        term_formula.scale_to_fit_width(4.04)
        displayed_colors = (
            term_colors[0], term_colors[1], term_colors[2], term_colors[-1]
        )
        for index, color in zip((0, 2, 4, 6), displayed_colors):
            term_formula[index].set_color(color)

        self.play(
            TransformFromCopy(pyramid, row_arrays),
            run_time=2,
        )
        self.wait(0.5)

        self.add_fixed_in_frame_mobjects(term_formula)
        self.play(Write(term_formula), run_time=1.0)

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
            Tex(r"Mathematics Magazine,", font_size=30, color=BLACK),
            Tex(r"vol. 70, no. 1 (Feb. 1997),", font_size=30, color=BLACK),
            Tex(r"p. 46.", font_size=30, color=BLACK),
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
