"""
Visual proof of the internal bisector of the right angle of a right triangle bisects
the square of the hypotenuse.
Proofs without Words I. Roger B. Nelsen. p. 16.
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
        # La bissectrice de l'angle droit d'un triangle rectangle coupe le carré 
        # construit sur l'hypothénuse en deux moitiés identiques.
        txt_title = [
            Tex(r"La bissectrice de", font_size=48, color=BLACK),
            Tex(r"l'angle droit d'un triangle", font_size=48, color=BLACK),
            Tex(r"rectangle coupe le carré", font_size=48, color=BLACK),
            Tex(r"construit sur l'hypothénuse",font_size=48, color=BLACK),
            Tex(r"en deux moitiés identiques.",font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Roland H. Eddy", font_size=28, color=BLACK)
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
        triangle_b = Polygon(
            [-1, -0.75, 0], [1, -0.75, 0], [1, 0.75, 0],
            stroke_width=2,
            color=BLACK, fill_color=BLUE, fill_opacity=1
        ).move_to([0, 1.5, 0])

        self.play(
            Create(triangle_b)
        )

        self.play(
            Rotate(triangle_b, 143 * DEGREES, about_point=[0, 1.5, 0]),
        )

        coords_vertices_b = get_vertices(triangle_b)

        sq_c2 = Square(side_length=2.5, stroke_color=BLACK, stroke_width=2)\
            .move_to(coords_vertices_b[2], UP)
        self.play(
            FadeTransform(coords_vertices_b[2].set_color(WHITE), sq_c2, stretch=True),
        )

        # Complete other triangles
        triangle_b_c = triangle_b.copy()
        self.play(
            triangle_b_c.animate.rotate(PI).next_to(sq_c2, DOWN, buff=0),
        )

        triangle_b_c2 = triangle_b.copy()
        self.play(
            triangle_b_c2.animate.rotate(PI/2).next_to(sq_c2, LEFT, buff=0),
        )

        triangle_b_c3 = triangle_b.copy()
        self.play(
            triangle_b_c3.animate.rotate(-PI/2).next_to(sq_c2, RIGHT, buff=0),
        )

        # Bisector
        bisector = Line(
            triangle_b.get_vertices()[1], triangle_b_c.get_vertices()[1],
            stroke_width=2,
            color=RED
        )
        self.play(
            Create(bisector)
        )

        # Add angles
        angle_a = Angle(
            bisector, coords_vertices_b[1],
            color=BLACK, other_angle=True, stroke_width=1
        )
        angle_b = Angle(
            coords_vertices_b[0], bisector, quadrant=(-1, 1), radius=0.25,
            color=BLACK, other_angle=True, stroke_width=1
        )
        txt_pi = Tex(r"$\frac{\pi}{2}$", font_size=28, color=BLACK).\
            next_to(angle_a, DOWN, buff=0.1)
        txt_pi_2 = txt_pi.copy().next_to(angle_b, DOWN + 0.5 * RIGHT, buff=0.1)
        self.play(
            Create(angle_a),
            Create(angle_b),
            Write(txt_pi),
            Write(txt_pi_2),
        )

        coords_vertices_b_c = get_vertices(triangle_b_c)
        angle_c = Angle(
            bisector, coords_vertices_b_c[1],
            color=BLACK, other_angle=True, stroke_width=1,
            quadrant=(-1, 1)
        )
        angle_d = Angle(
            coords_vertices_b_c[0], bisector, quadrant=(-1, -1), radius=0.25,
            color=BLACK, other_angle=True, stroke_width=1
        )
        txt_pi_3 = txt_pi.copy().next_to(angle_c, UP, buff=0.1)
        txt_pi_4 = txt_pi.copy().next_to(angle_d, UP + 0.5 * LEFT, buff=0.1)
        self.play(
            Create(angle_c),
            Create(angle_d),
            Write(txt_pi_3),
            Write(txt_pi_4)
        )

        # Color side of the square
        A = Line(
            triangle_b.get_vertices()[0],
            [-0.18, 1.49716161, 0],
            stroke_width=8,
            color = ORANGE
        )
        B = Line(
            triangle_b_c.get_vertices()[0],
            [0.18, -0.99716161, 0],
            stroke_width=8,
            color = ORANGE
        )
        self.play( 
            Create(A),
            Create(B)
        )

        C = Line(
            triangle_b.get_vertices()[2],
            [-0.18, 1.49716161, 0],
            stroke_width=8,
            color = VIOLET
        )
        D = Line(
            triangle_b_c.get_vertices()[2],
            [0.18, -0.99716161, 0],
            stroke_width=8,
            color = VIOLET
        )
        self.play( 
            Create(C),
            Create(D)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"College Mathematics Journal,", font_size=30, color=BLACK),
            Tex(r"vol. 22, no. 5 (Nov. 1991),", font_size=30, color=BLACK),
            Tex(r"p. 420", font_size=30, color=BLACK),
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