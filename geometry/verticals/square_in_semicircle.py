"""
Visual proof of the sqaures in circles and semicircles.
Proofs without Words III. Roger B. Nelsen. p. 38.
"""
from networkx import radius
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, TransformFromCopy
from manim import VGroup, FadeIn, FadeOut , FunctionGraph, Rotate
from manim import Line, Point, Polygon, RoundedRectangle, Circle
from manim import line_intersection, DashedLine, Arc, Sector
from manim import Text, Tex, Intersection, Square, Rectangle

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


class SquareCircle(MovingCameraScene):
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
            Tex(r"Des carrés dans", font_size=48, color=BLACK),
            Tex(r"des cercles", font_size=48, color=BLACK)
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

        # Draw semicircle
        semicircle = Sector(
            radius=0.5, start_angle=0, angle=PI, 
            color=RED, fill_opacity=0.5
        ).move_to([-1, 3, 0])
        self.play(Create(semicircle))

        side = (2 * 0.5) / np.sqrt(5) 
        square = Square(
            side_length=side, color=BLUE, fill_opacity=1,
            stroke_width=0,
        ).\
            move_to(semicircle.get_center() - [0, 0.0325, 0])
        self.play(Create(square))

        # Write equality
        eq = Tex(r"$=$", font_size=36, color=BLACK).\
            next_to(semicircle, RIGHT, buff=0.1)
        self.play(Write(eq))

        eq2 = Tex(r"$\frac{2}{5} \times $", font_size=36, color=BLACK).\
            next_to(eq, RIGHT, buff=0.1)
        self.play(Write(eq2))

        # Draw circle
        circle = Circle(
            radius=0.5, color=RED, fill_opacity=0.5,
            stroke_width=0,
        ).move_to([1, 3, 0])
        self.play(Create(circle))

        # Draw inside square
        square_circle = Square(
            side_length=0.5* 2**0.5, fill_color=BLUE,
            stroke_width=0, fill_opacity=1
        ).\
            move_to(circle.get_center())
        self.play(Create(square_circle))


        # Create a big square consisting of 6 by 6 small squares
        squares = VGroup()
        for i in range(36):
            square = Rectangle(
                height=0.5, width=0.5,
                fill_color=WHITE, fill_opacity=0.2,
                stroke_color=BLACK, stroke_width=1
            )
            squares.add(square)
        squares.arrange_in_grid(rows=6, cols=6, buff=0)
        squares.move_to([0, 0, 0])
        self.play(Create(squares, run_time=2))

        # Square in big sqaure
        square_big = Square(
            side_length=1, fill_color=BLUE,
            stroke_width=0, fill_opacity=1
        ).\
            move_to(squares.get_center() + [0, 0.5, 0])
        self.play(Create(square_big))

        # Draw diameter line
        line_diameter = Line(
            squares.get_left(),
            squares.get_right(),
            stroke_color=RED, stroke_width=4
        )
        self.play(Create(line_diameter))

        # Draw circle
        rad = 1 * np.sqrt(5) / 2
        circle2 = Circle(
            radius=rad,
            color=RED, fill_opacity=0.5,
            stroke_width=0,
        ).move_to(squares.get_center())
        self.play(Create(circle2))

        # Draw other square
        squares2 = Polygon(
            squares[7].get_corner(UP + RIGHT),
            squares[16].get_corner(UP + RIGHT),
            squares[28].get_corner(DOWN + LEFT),
            squares[19].get_corner(DOWN + LEFT),
            fill_color=BLUE, fill_opacity=0.5,
            stroke_width=0
        )
        self.play(Create(squares2))

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine,", font_size=30, color=BLACK),
            Tex(r"vol. 82, no. 5 (Dec. 2009),", font_size=30, color=BLACK),
            Tex(r"p. 359", font_size=30, color=BLACK),
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