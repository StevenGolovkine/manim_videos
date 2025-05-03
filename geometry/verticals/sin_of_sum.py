"""
Visual proof of the sine of the sum formula
Proofs without Words III. Roger B. Nelsen. p. 39.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, FadeTransform, TransformFromCopy
from manim import VGroup, FadeIn, FadeOut , FunctionGraph, Rotate
from manim import Line, Point, Polygon, RoundedRectangle, Square, Angle
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


class Sum(MovingCameraScene):
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
            Tex(r"Le sinus de la somme", font_size=32, color=BLACK),
            Tex(r"de deux angles", font_size=32, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Christopher Brueningsen", font_size=28, color=BLACK)
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
        shift_y = 2.5
        point_A = Point([-1.5, -0.75 + shift_y, 0])
        point_B = Point([1.5, -0.75 + shift_y, 0])
        point_C = Point([0, 0.75 + shift_y, 0])
        AB = Line(point_A, point_B)
        BC = Line(point_B, point_C)
        CA = Line(point_C, point_A)
        triangle_b = Polygon(
            point_A.get_center(),
            point_B.get_center(),
            point_C.get_center(),
            stroke_width=2,
            color=BLACK, fill_color=BLUE, fill_opacity=1
        )

        txt_a = Tex(r"$a$", font_size=36, color=BLACK)\
            .next_to(CA.get_center_of_mass(), LEFT, buff=0.25)
        txt_b = Tex(r"$b$", font_size=36, color=BLACK)\
            .next_to(BC.get_center_of_mass(), RIGHT, buff=0.25)
        self.play(
            Create(triangle_b),
            Write(txt_a),
            Write(txt_b)
        )

        # Triangle altitude
        point_H = Point([0, -0.75 + shift_y, 0])
        CH = Line(point_C, point_H, color=BLACK)
        txt_y = Tex(r"$y$", font_size=28, color=BLACK)\
            .next_to(CH.get_center_of_mass(), LEFT, buff=0.1)
        angle_alpha = Angle(
            CH, CA, radius=0.3, other_angle=True, quadrant=(1, 1),
            color=BLACK, stroke_width=2
        )
        txt_alpha = Tex(r"$\alpha$", font_size=20, color=BLACK)\
            .next_to(angle_alpha.get_center_of_mass(), DOWN + LEFT, buff=0.1)
        angle_beta = Angle(
            CH, BC, radius=0.25, other_angle=False, quadrant=(1, -1),
            color=BLACK, stroke_width=2
        )
        txt_beta = Tex(r"$\beta$", font_size=20, color=BLACK)\
            .next_to(angle_beta.get_center_of_mass(), DOWN + RIGHT, buff=0.1)
        self.play(
            Create(CH),
            Write(txt_y),
            Create(angle_alpha),
            Create(angle_beta),
            Write(txt_alpha),
            Write(txt_beta)
        )

        # Text trigogonometric functions
        txt = Tex(
            r"$y = a\cos \alpha = b \cos \beta$", font_size=36, color=BLACK
        ).next_to(triangle_b, DOWN, buff=0.5)

        self.play(
            Write(txt),
        )

        # Text area
        triangle_red = Polygon(
            point_A.get_center(),
            point_H.get_center(),
            point_C.get_center(),
            stroke_width=2,
            color=BLACK, fill_color=RED, fill_opacity=0.5
        )
        triangle_green = Polygon(
            point_B.get_center(),
            point_C.get_center(),
            point_H.get_center(),
            stroke_width=2,
            color=BLACK, fill_color=GREEN, fill_opacity=0.5
        )
        self.play(
            Create(triangle_red),
            Create(triangle_green)
        )

        txt_area = Tex(
            r"Aire ", r"$\blacksquare$", r" $=$ ",
            r"Aire ", r"$\blacksquare$", r" $+$ ",
            r"Aire ", r"$\blacksquare$",
            font_size=30, color=BLACK,
        )
        txt_area[1].set_color(BLUE).set_opacity(0.5)
        txt_area[4].set_color(RED).set_opacity(0.5)
        txt_area[7].set_color(GREEN).set_opacity(0.5)

        self.play(
            Write(txt_area),
        )

        txt_formula = Tex(
            r"$\frac{1}{2}ab\sin(\alpha + \beta) = \frac{1}{2}ay\sin\alpha + \frac{1}{2}by\sin\beta$",
            font_size=20, color=BLACK
        ).next_to(txt_area, DOWN)

        self.play(
            Write(txt_formula)
        )

        txt_formula2 = Tex(
            r"$ab\sin(\alpha + \beta) = ab\sin\alpha\cos\beta + ab\sin\beta\cos\alpha$",
            font_size=20, color=BLACK
        ).next_to(txt_formula, DOWN)

        self.play(
            Write(txt_formula2)
        )

        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, -2, 0])
        txt_formula3 = Tex(
            r"$\sin(\alpha + \beta) = \sin\alpha\cos\beta + \sin\beta\cos\alpha$",
            font_size=20, color=BLACK
        ).move_to([0, -2, 0])

        self.play(
            Create(rect),
            Write(txt_formula3)
        )
        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine,", font_size=30, color=BLACK),
            Tex(r"vol. 66, no. 2 (April 1993),", font_size=30, color=BLACK),
            Tex(r"p. 135", font_size=30, color=BLACK),
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