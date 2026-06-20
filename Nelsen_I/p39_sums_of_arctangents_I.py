"""
Visual proof of Sums of Arctangents.
Proofs without Words III. Roger B. Nelsen. p. 74.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Angle, Arc
from manim import Text, Tex, Polygon, Rectangle, Line, RightAngle
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

        # Create 6 small squares in one rectangle
        squares = VGroup()
        for i in range(6):
            square = Rectangle(
                height=1, width=1,
                fill_color=WHITE, fill_opacity=1,
                stroke_color=BLACK, stroke_width=1
            )
            squares.add(square)
        squares.arrange_in_grid(rows=2, cols=3, buff=0)
        squares.move_to([0, 1, 0])
        self.play(Create(squares, run_time=2))


        # Triangle up
        triangle_up = Polygon(
            squares[0].get_corner(DOWN + LEFT),
            squares[2].get_corner(UP + RIGHT),
            squares[2].get_corner(DOWN + RIGHT),
            fill_color=RED, fill_opacity=0.5,
            stroke_color=BLACK, stroke_width=1
        )

        self.play(Create(triangle_up))

        # Triangle down
        triangle_down = Polygon(
            squares[3].get_corner(UP + LEFT),
            squares[4].get_corner(UP + RIGHT),
            squares[4].get_corner(DOWN + RIGHT),
            fill_color=BLUE, fill_opacity=0.5,
            stroke_color=BLACK, stroke_width=1
        )
        self.play(Create(triangle_down))

        # Triangle
        triangle = Polygon(
            squares[2].get_corner(UP + RIGHT),
            squares[0].get_corner(DOWN + LEFT),
            squares[5].get_corner(DOWN + LEFT),
            fill_color=GREY, fill_opacity=0.5,
            stroke_color=BLACK, stroke_width=1
        )
        r_angle = RightAngle(
            Line(
                squares[2].get_corner(UP + RIGHT),
                squares[5].get_corner(DOWN + LEFT)
            ),
            Line(
                squares[5].get_corner(DOWN + LEFT),
                squares[0].get_corner(DOWN + LEFT)
            ),
            length=0.2,
            quadrant=(-1, 1),
            stroke_color=BLACK,
            stroke_width=1
        )
        self.play(
            Create(triangle),
            Create(r_angle)
        )

        # First identity
        angle1 = Angle(
            Line(
                squares[0].get_corner(DOWN + LEFT),
                squares[2].get_corner(UP + RIGHT)
            ),
            Line(
                squares[0].get_corner(DOWN + LEFT),
                squares[5].get_corner(DOWN + LEFT)
            ),
            radius=0.3,
            quadrant=(1, 1),
            other_angle=True,
            stroke_color=BLACK,
            stroke_width=2
        )
        txt_1 = Tex(
            r"$\frac{\pi}{4} = $",
            r"$\arctan \frac{1}{2}$",
            r"$+$",
            r"$\arctan \frac{1}{3}$",
            font_size=32, color=BLACK
        ).next_to(squares, DOWN, buff=1)
        txt_1[1].set_color(BLUE)
        txt_1[3].set_color(RED)
        self.play(
            Create(angle1),
            Write(txt_1)
        )

        self.wait(1)


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