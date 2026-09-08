"""
Visual proof of the difference of consecutive integer cubes formula is
congruent to 1 modulo 6.
Proofs without Words III. Roger B. Nelsen. p. 123.
"""
import numpy as np

from manim import ThreeDScene
from manim import Create, Uncreate, Write, ReplacementTransform
from manim import Brace, VGroup, FadeIn, FadeOut, FunctionGraph
from manim import LaggedStart
from manim import Cube, Sphere, MathTex, Text, Tex

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


class DifferenceCubes(ThreeDScene):
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
            Tex(r"La différence des", font_size=48, color=BLACK),
            Tex(r"cubes consécutifs", font_size=48, color=BLACK),
            Tex(r"est congru à 1 ", font_size=48, color=BLACK),
            Tex(r"modulo 6", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"C. Alsina, H. Unal \& R.B. Nelsen", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        results = [
            Tex(r"$(n + 1)^3 - n^3 \equiv 1 \pmod{6}$", font_size=24, color=BLACK),
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

        # Camera-plane basis vectors allow page-like placement of 3D objects.
        view_right = np.array([-np.sin(theta), np.cos(theta), 0])
        view_up = np.array([
            -np.cos(phi) * np.cos(theta),
            -np.cos(phi) * np.sin(theta),
            np.sin(phi),
        ])

        def screen_point(x, y):
            return x * view_right + y * view_up

        def cube_at(coords, side, center, color):
            cube = Cube(
                side_length=side,
                fill_color=color,
                fill_opacity=1,
                stroke_color=BLACK,
                stroke_width=0.5,
            )
            cube.move_to(side * (np.array(coords) - center))
            for face in cube:
                face.set_fill(color, opacity=1)
                face.set_stroke(BLACK, width=0.5)
            return cube

        def voxel_group(coords, side, center, color):
            return VGroup(*[
                cube_at(point, side, center, color) for point in coords
            ])

        def sphere_at(coords, side, center, color):
            sphere = Sphere(
                center=side * (np.array(coords) - center),
                radius=side * 0.34,
                resolution=(8, 8),
                fill_color=color,
                fill_opacity=1,
                checkerboard_colors=[color, color],
                stroke_color=BLACK,
                stroke_width=0.25,
            )
            return sphere

        def sphere_group(coords, side, center, color):
            return VGroup(*[
                sphere_at(point, side, center, color) for point in coords
            ])

        n = 4
        side = 0.19
        outer_center = np.array([n / 2, n / 2, n / 2])
        inner_center = np.array([(n - 1) / 2] * 3)

        outer_coords = [
            (x, y, z)
            for x in range(n + 1)
            for y in range(n + 1)
            for z in range(n + 1)
        ]
        inner_coords = [
            (x, y, z)
            for x in range(n)
            for y in range(n)
            for z in range(n)
        ]

        # The shell is split into three n by (n + 1) rectangles and one cube.
        slab_x = [
            (0, y, z)
            for y in range(n)
            for z in range(n + 1)
        ]
        slab_y = [
            (x, n, z)
            for x in range(n + 1)
            for z in range(1, n + 1)
        ]
        slab_z = [
            (x, y, 0)
            for x in range(1, n + 1)
            for y in range(n + 1)
        ]
        corner = [(0, n, 0)]
        shell_coords = slab_x + slab_y + slab_z + corner

        assert len(shell_coords) == (n + 1) ** 3 - n ** 3
        assert len(set(shell_coords)) == len(shell_coords)
        assert len(slab_x) == len(slab_y) == len(slab_z) == n * (n + 1)

        heading = Tex(
            r"Différence de deux cubes consécutifs",
            font_size=24,
            color=BLACK,
        ).move_to([0, 3.48, 0])
        difference = MathTex(
            r"(n+1)^3", r"-", r"n^3",
            font_size=31,
            color=BLACK,
        ).move_to([0, 2.92, 0])
        self.add_fixed_in_frame_mobjects(heading, difference)
        self.play(Write(heading), Write(difference), run_time=0.8)

        outer_cube = voxel_group(
            outer_coords, side, outer_center, "#D7E5EC"
        ).move_to(screen_point(-0.9, 1.25))
        inner_cube = voxel_group(
            inner_coords, side, inner_center, "#E5DDEE"
        ).move_to(screen_point(0.9, 1.25))
        minus_sign = MathTex(r"-", font_size=42, color=BLACK).move_to(
            [0, 1.28, 0]
        )
        self.add_fixed_in_frame_mobjects(minus_sign)
        self.play(
            FadeIn(outer_cube),
            Write(minus_sign),
            FadeIn(inner_cube),
            run_time=1.5,
        )
        self.wait(0.5)

        slab_colors = [BLUE, GREEN, ORANGE]
        shell = VGroup(
            voxel_group(slab_x, side, outer_center, slab_colors[0]),
            voxel_group(slab_y, side, outer_center, slab_colors[1]),
            voxel_group(slab_z, side, outer_center, slab_colors[2]),
            voxel_group(corner, side, outer_center, RED),
        ).move_to(screen_point(0, -0.65))
        equal_sign = MathTex(r"=", font_size=38, color=BLACK).move_to(
            [0, 0.3, 0]
        )
        self.add_fixed_in_frame_mobjects(equal_sign)


        self.play(
            Write(equal_sign),
            Create(shell),
            run_time=1.3,
        )
        self.wait(0.5)

        # Checkerboard each rectangle into two equal groups of T_n spheres.
        source_coord_groups = [
            [point for point in slab_x if (point[1] + point[2]) % 2 == parity]
            for parity in (0, 1)
        ] + [
            [point for point in slab_y if (point[0] + point[2] - 1) % 2 == parity]
            for parity in (0, 1)
        ] + [
            [point for point in slab_z if (point[0] - 1 + point[1]) % 2 == parity]
            for parity in (0, 1)
        ]
        triangular_number = n * (n + 1) // 2
        assert all(len(group) == triangular_number for group in source_coord_groups)

        sector_colors = [BLUE, VIOLET, RED, GREEN, YELLOW, ORANGE]
        sphere_shell = VGroup(*[
            sphere_group(coords, side, outer_center, color)
            for coords, color in zip(source_coord_groups, sector_colors)
        ])
        sphere_center = sphere_group(
            corner, side, outer_center, "#B44978"
        )
        sphere_shell.add(sphere_center)
        sphere_shell.move_to(shell)

        self.play(
            shell.animate.set_opacity(0.2),
            *[FadeIn(group) for group in sphere_shell],
            run_time=1.4,
        )
        self.wait(0.5)
        self.play(
            FadeOut(shell),
            FadeOut(outer_cube),
            FadeOut(inner_cube),
            FadeOut(minus_sign),
            FadeOut(equal_sign),
            run_time=0.7,
        )

        # A centered hexagonal array consists of six T_n sectors and its center.
        axial_directions = [
            np.array([1, 0]),
            np.array([0, 1]),
            np.array([-1, 1]),
            np.array([-1, 0]),
            np.array([0, -1]),
            np.array([1, -1]),
        ]
        spacing = 0.205
        sphere_radius = 0.071
        hex_center = screen_point(0, 0.62)

        def axial_to_screen(axial):
            q, r = axial
            x = spacing * (q + r / 2)
            y = spacing * np.sqrt(3) * r / 2
            return hex_center + screen_point(x, y)

        target_sectors = VGroup()
        target_axial_points = []
        for index, color in enumerate(sector_colors):
            direction = axial_directions[index]
            next_direction = axial_directions[(index + 1) % 6]
            sector = VGroup()
            for a in range(1, n + 1):
                for b in range(n - a + 1):
                    axial = a * direction + b * next_direction
                    target_axial_points.append(tuple(axial))
                    sphere = Sphere(
                        center=axial_to_screen(axial),
                        radius=sphere_radius,
                        resolution=(8, 8),
                        fill_color=color,
                        fill_opacity=1,
                        checkerboard_colors=[color, color],
                        stroke_color=BLACK,
                        stroke_width=0.25,
                    )
                    sector.add(sphere)
            target_sectors.add(sector)

        assert len(target_axial_points) == 6 * triangular_number
        assert len(set(target_axial_points)) == len(target_axial_points)

        target_center = Sphere(
            center=hex_center,
            radius=sphere_radius,
            resolution=(8, 8),
            fill_color="#B44978",
            fill_opacity=1,
            checkerboard_colors=["#B44978", "#B44978"],
            stroke_color=BLACK,
            stroke_width=0.35,
        )

        self.play(
            *[
                ReplacementTransform(
                    sphere_shell[index], target_sectors[index]
                )
                for index in range(6)
            ],
            ReplacementTransform(sphere_shell[6], target_center),
            run_time=2.2,
        )
        self.wait(0.5)

        sector_note = Tex(
            r"Six groupes de $T_n$ sphères et une sphère centrale",
            font_size=18,
            color=BLACK,
        ).move_to([0, -0.68, 0])
        final_formula = MathTex(
            r"(n+1)^3-n^3",
            r"=6\frac{n(n+1)}{2}+1",
            r"\equiv 1\pmod 6",
            font_size=27,
            color=BLACK,
        ).arrange(DOWN, buff=0.2).move_to([0, -1.78, 0])
        final_formula[2].set_color("#B44978")
        self.add_fixed_in_frame_mobjects(
            sector_note, final_formula
        )
        # self.play(
        #     FadeOut(difference),
        #     #Write(sector_note),
        #     run_time=0.7,
        # )
        # self.play(
        #     Write(final_formula), run_time=1.1
        # )
        # self.wait(1)


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
            Tex(r"College Mathematics Journal,", font_size=30, color=BLACK),
            Tex(r"vol. 45, no. 2 (March 2014),", font_size=30, color=BLACK),
            Tex(r" p. 135.", font_size=30, color=BLACK)
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
