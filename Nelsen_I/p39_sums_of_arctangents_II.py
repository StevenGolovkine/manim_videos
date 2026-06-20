"""
Visual proof of Sums of Arctangents.
Proofs without Words III. Roger B. Nelsen. p. 74.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Angle, Arc
from manim import Text, Tex, Polygon, Rectangle, Line, RightAngle, Dot
from manim import TransformFromCopy, Transform

from manim import config
from manim import LEFT, RIGHT, DOWN, LIGHT, UP, PI

# COLORS
BLUE = "#B0E1FA"
VIOLET = "#E8C9FA"
RED = "#F79BC5"
GREEN = "#DBF9E7"
YELLOW = "#EFE9B7"
ORANGE = "#F6CCB0"
BLACK = "#000000"
GREY = "#D3D3D3"
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


class Arctangent(MovingCameraScene):
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
            Tex(r"Une égalité sur", font_size=48, color=BLACK),
            Tex(r"les arctangentes", font_size=48, color=BLACK),
            Tex(r"Partie II", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Edward M. Harris", font_size=28, color=BLACK)
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

        # Proof figure
        unit = 0.58
        origin = np.array([-1.75, -1.45, 0])

        def p(x, y):
            return origin + unit * np.array([x, y, 0])

        cells = []
        cells += [(x, y) for x in range(2) for y in range(4)]
        cells += [(x, y) for x in range(2, 4) for y in range(2, 5)]
        cells += [(x, y) for x in range(4, 6) for y in range(4, 6)]

        edges = set()
        for x, y in cells:
            cell_edges = [
                ((x, y), (x + 1, y)),
                ((x + 1, y), (x + 1, y + 1)),
                ((x, y + 1), (x + 1, y + 1)),
                ((x, y), (x, y + 1)),
            ]
            for start, end in cell_edges:
                edges.add(tuple(sorted((start, end))))

        grid = VGroup(*[
            Line(p(*start), p(*end), color=BLACK, stroke_width=1.7)
            for start, end in sorted(edges)
        ])

        shaded_vertices = [(0, 0), (0, 3), (6, 6), (1, 1)]
        shaded_region = Polygon(
            *[p(x, y) for x, y in shaded_vertices],
            stroke_width=0,
            fill_color=GREY,
            fill_opacity=0.1
        )

        # Triangle 1
        vertices_1 = [(0, 0), (1, 1), (0, 1)]
        shaded_region_1 = Polygon(
            *[p(x, y) for x, y in vertices_1],
            stroke_width=0,
            fill_color=RED,
            fill_opacity=0.5
        )

        # Triangle 2
        vertices_2 = [(0, 1), (0, 3), (1, 1)]
        shaded_region_2 = Polygon(
            *[p(x, y) for x, y in vertices_2],
            stroke_width=0,
            fill_color=BLUE,
            fill_opacity=0.5
        )

        # Triangle 3
        vertices_3 = [(1, 1), (0, 3), (6, 6)]
        shaded_region_3 = Polygon(
            *[p(x, y) for x, y in vertices_3],
            stroke_width=0,
            fill_color=ORANGE,
            fill_opacity=0.5
        )

        def is_inside_shaded(x, y):
            inside = False
            vertices = shaded_vertices
            j = len(vertices) - 1
            for i in range(len(vertices)):
                xi, yi = vertices[i]
                xj, yj = vertices[j]
                crosses = (yi > y) != (yj > y)
                if crosses:
                    x_intersection = (xj - xi) * (y - yi) / (yj - yi) + xi
                    if x < x_intersection:
                        inside = not inside
                j = i
            return inside

        stipple = VGroup()
        row = 0
        for y in np.arange(0.08, 6, 0.13):
            x_start = 0.08 + 0.06 * (row % 2)
            for x in np.arange(x_start, 6, 0.13):
                if is_inside_shaded(x, y):
                    stipple.add(
                        Dot(
                            p(x, y),
                            radius=0.007,
                            color=BLACK,
                            fill_opacity=0.42,
                            stroke_width=0
                        )
                    )
            row += 1

        main_diagonal = Line(
            p(0, 0), p(6, 6),
            color=BLACK, stroke_width=4.2
        )
        upper_ray = Line(
            p(0, 3), p(6, 6),
            color=BLACK, stroke_width=4.2
        )
        left_ray = Line(
            p(0, 3), p(0, 0),
            color=BLACK, stroke_width=4.2
        )
        heavy_lines = VGroup(main_diagonal, upper_ray, left_ray)

        angle_arc = Arc(
            radius=0.78 * unit,
            start_angle=5 * PI / 4,
            angle=-PI,
            arc_center=p(1, 1),
            color=BLACK,
            stroke_width=2.2
        )

        formula = Tex(
            r"$\arctan 1$",
            r"$\;+\;$",
            r"$\arctan 2$",
            r"$\;+\;$",
            r"$\arctan 3$",
            r"$\;=\;$",
            r"$\pi$",
            font_size=34,
            color=BLACK
        ).move_to([0, 2.5, 0])
        formula[0].set_color(RED)
        formula[2].set_color(BLUE)
        formula[4].set_color(ORANGE)
        formula.scale_to_fit_width(config.frame_width - 0.55)

        self.play(
            Create(grid),
            run_time=2
        )

        self.play(
            FadeIn(shaded_region_1)
        )
        self.play(
            FadeIn(shaded_region_2)
        )
        self.play(
            FadeIn(shaded_region_3)
        )

        self.play(
            Create(heavy_lines),
            FadeIn(shaded_region),
            FadeIn(stipple),
            Create(angle_arc),
            run_time=1
        )

        self.play(Write(formula))

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"College Mathematics Journal,", font_size=26, color=BLACK),
            Tex(r"vol. 18, no. 2", font_size=26, color=BLACK),
            Tex(r"(march 1987), pp. 141.", font_size=26, color=BLACK)
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
