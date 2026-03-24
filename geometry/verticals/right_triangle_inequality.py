"""
Visual proof of a right triangle inequality.
Proofs without Words II. Roger B. Nelsen. p. 12.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, FadeTransform, TransformFromCopy
from manim import VGroup, FadeIn, FadeOut , FunctionGraph, Rotate
from manim import Line, Point, Polygon, RoundedRectangle, Square, Angle
from manim import Text, Tex, Intersection, Transform

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
            Tex(r"Une inégalité", font_size=48, color=BLACK),
            Tex(r"pour les triangles", font_size=48, color=BLACK),
            Tex(r"rectangles", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Roger B. Nelsen", font_size=28, color=BLACK)
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

        txt_prob = [
            Tex(
                r"Soit $c$ l'hypothénuse d'un triangle rectangle,",
                font_size=20, color=BLACK
            ),
            Tex(
                r"et soit $a$ et $b$, les deux autres côtés.",
                font_size=20, color=BLACK
            ),
            Tex(
                r"Alors, $a + b \leq c\sqrt{2}$.",
                font_size=20, color=BLACK
            )
        ]
        txt_prob = VGroup(*txt_prob).arrange(DOWN).move_to([0, 2.5, 0])
        self.play(Write(txt_prob))

        # Make a square
        square = Square(
            side_length=3,
            color=RED, fill_color=RED,
            fill_opacity=1, stroke_width=0
        )
        square.move_to(ORIGIN)
        self.play(Create(square))

        # Make a square of length c inside the first square
        square_2 = Square(
            side_length=np.sqrt(5),
            color=BLUE, fill_color=BLUE,
            fill_opacity=1, stroke_width=0
        )
        square_2.move_to(ORIGIN).rotate(60 * DEGREES)
        self.play(Create(square_2))

        # Write txt on the sides of the square
        txt_a = Tex(r"$a$", font_size=24, color=BLACK).move_to([-1, 1.6, 0])
        txt_b = Tex(r"$b$", font_size=24, color=BLACK).move_to([-1.6, 0.7, 0])
        txt_c = Tex(r"$c$", font_size=24, color=BLACK).move_to([-0.75, 0.5, 0])
        self.play(
            Write(txt_a),
            Write(txt_b),
            Write(txt_c)
        )

        # Write second txt on the sides of the square
        txt_a2 = Tex(r"$a$", font_size=24, color=BLACK).move_to([-1.6, -1, 0])
        txt_b2 = Tex(r"$b$", font_size=24, color=BLACK).move_to([-0.7, -1.6, 0])
        txt_c2 = Tex(r"$c$", font_size=24, color=BLACK).move_to([-0.4, -0.9, 0])
        self.play(
            Write(txt_a2),
            Write(txt_b2),
            Write(txt_c2)
        )

        # Line between vertices of the blue square
        vertices = square_2.get_vertices()
        line = Line(vertices[0], vertices[2], color=BLACK)
        self.play(Create(line))

        # Text next to the line
        txt_line = Tex(r"$c\sqrt{2}$", font_size=20, color=BLACK).next_to(line.get_center(), RIGHT, buff=0.2)
        self.play(Write(txt_line))

        # Conclusion text 
        txt_conclusion = Tex(
            r"$a + b \leq c\sqrt{2}$.",
            font_size=24, color=BLACK
        ).move_to([0, -2.5, 0])
        self.play(Write(txt_conclusion))

        self.wait(1)
        
        # Rotate the inside square to show that the line is the diagonal of the square
        square_3 = Square(
            side_length=np.sqrt(1.5**2 + 1.5**2),
            color=BLUE, fill_color=BLUE,
            fill_opacity=1, stroke_width=0
        )
        square_3.move_to(ORIGIN).rotate(45 * DEGREES)

        vertices_2 = square_3.get_vertices()
        line_2 = Line(vertices_2[0], vertices_2[2], color=BLACK)

        txt_conclusion_2 = Tex(
            r"$a + b = c\sqrt{2}$.",
            font_size=24, color=BLACK
        ).move_to([0, -2.5, 0])

        self.play(
            Transform(square_2, square_3),
            Transform(line, line_2),
            Transform(txt_conclusion, txt_conclusion_2)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"The Canadian Mathematical,", font_size=30, color=BLACK),
            Tex(r"Olympiad, 1969.", font_size=30, color=BLACK),
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