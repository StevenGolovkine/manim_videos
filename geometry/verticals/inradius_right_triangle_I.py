"""
Visual proof of a relation between the inradius of a right triangle and the
side of the triangle.
Proofs without Words II. Roger B. Nelsen. p. 13.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, FadeTransform, TransformFromCopy
from manim import VGroup, FadeIn, FadeOut , FunctionGraph, Rotate
from manim import Line, Circle, Polygon, RoundedRectangle, Square, Angle
from manim import Text, Tex, Intersection

from manim import config
from manim import ORIGIN, LEFT, RIGHT, DOWN, LIGHT, UP, PI, DEGREES

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


def get_vertices(obj: Polygon) -> list[Line]:
    vertices = obj.get_vertices()
    coords_vertices = []
    for i in range(len(vertices)):
        if i < len(vertices)-1:
            p1, p2 = [vertices[i], vertices[i + 1]]
        else:
            p1, p2 = [vertices[-1], vertices[0]]
        guide_line = Line(p1, p2)
        coords_vertices.append(guide_line)
    return coords_vertices


class Triangle(MovingCameraScene):
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
            Tex(r"La rayon du cercle", font_size=48, color=BLACK),
            Tex(r"inscrit dans un", font_size=48, color=BLACK),
            Tex(r"triangle rectangle", font_size=48, color=BLACK),
            Tex(r"Partie I", font_size=24, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Liu Hui", font_size=28, color=BLACK)
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

        # Triangle
        A = [-1, -0.75 + 1.5, 0]
        B = [1, -0.75 + 1.5, 0]
        C = [1, 0.75 + 1.5, 0]
        triangle_b = Polygon(
            A, B, C,
            stroke_width=2,
            color=BLACK, fill_color=BLUE, fill_opacity=1
        )
        txt_a = Tex(r"$a$", font_size=28, color=BLACK).\
            next_to(triangle_b, DOWN, buff=0.1)
        txt_b = Tex(r"$b$", font_size=28, color=BLACK).\
            next_to(triangle_b, RIGHT, buff=0.1)

        self.play(
            Create(triangle_b),
            Write(txt_a),
            Write(txt_b)
        )

        # Inside circle
        a = 2
        b = 1.5
        c = np.sqrt(a**2 + b**2)
        xr = (b * -1 + c * 1 + a * 1) / (a + b + c) 
        yr = (b * -0.75 + c * -0.75 + a * 0.75) / (a + b + c) + 1.5
        R = [xr, yr, 0]
        r = (a * b) / (a + b + c)
        circle = Circle(
            radius=r, color=BLACK, fill_color=VIOLET, fill_opacity=1, stroke_width=2
        ).move_to(R)
        self.play(
            Create(circle),
        )

        # Inside triangle
        line_a = Line(
            A, R, color=BLACK, stroke_width=2
        )
        line_c = Line(
            C, R, color=BLACK, stroke_width=2
        )
        line_d = Line(
            R, [xr, A[1], 0], color=BLACK, stroke_width=2
        )
        line_e = Line(
            R, [B[0], yr, 0], color=BLACK, stroke_width=2
        )


        self.play(
            Create(line_a),
            Create(line_c),
            Create(line_d),
            Create(line_e)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine, vol. 71,", font_size=30, color=BLACK),
            Tex(r"no. 3 (June 1998)", font_size=30, color=BLACK),
            Tex(r"p. 196", font_size=30, color=BLACK),
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