"""
Visual proof of a Euler's Arctangent Identity.
Proofs without Words III. Roger B. Nelsen. p. 77.
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


class Euler(MovingCameraScene):
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
            Tex(r"Des identités", font_size=48, color=BLACK),
            Tex(r"d'arctangentes", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Rex H. Wu", font_size=28, color=BLACK)
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
            r"$\frac{\pi}{4} = \arctan \frac{1}{2} + \arctan \frac{1}{3}$",
            font_size=32, color=BLACK
        ).next_to(squares, DOWN, buff=1)
        self.play(
            Create(angle1),
            Write(txt_1)
        )

        self.wait(1)

        # Second identity
        self.play(
            Uncreate(angle1),
            Uncreate(txt_1)
        )
        angle2 = Angle(
            Line(
                squares[2].get_corner(UP + RIGHT),
                squares[0].get_corner(DOWN + LEFT)
            ),
            Line(
                squares[2].get_corner(UP + RIGHT),
                squares[5].get_corner(DOWN + RIGHT)
            ),
            radius=0.3,
            quadrant=(1, 1),
            other_angle=False,
            stroke_color=BLACK,
            stroke_width=2
        )
        txt_2 = Tex(
            r"$\frac{\pi}{4} = \arctan 3 - \arctan \frac{1}{2}$",
            font_size=32, color=BLACK
        ).next_to(squares, DOWN, buff=1)
        self.play(
            Create(angle2),
            Write(txt_2)
        )

        self.wait(1)

        # Third identity
        self.play(
            Uncreate(angle2),
            Uncreate(txt_2)
        )
        angle3 = Angle(
            Line(
                squares[2].get_corner(UP + RIGHT),
                squares[0].get_corner(UP + LEFT)
            ),
            Line(
                squares[2].get_corner(UP + RIGHT),
                squares[5].get_corner(DOWN + LEFT)
            ),
            radius=0.3,
            quadrant=(1, 1),
            other_angle=False,
            stroke_color=BLACK,
            stroke_width=2
        )
        txt_3 = Tex(
            r"$\frac{\pi}{4} = \arctan 2 - \arctan \frac{1}{3}$",
            font_size=32, color=BLACK
        ).next_to(squares, DOWN, buff=1)
        self.play(
            Create(angle3),
            Write(txt_3)
        )

        self.wait(1)
        
        # Fourth identity
        self.play(
            Uncreate(angle3),
            Uncreate(txt_3)
        )
        angle4 = Angle(
            Line(
                squares[2].get_corner(UP + RIGHT),
                squares[0].get_corner(UP + LEFT)
            ),
            Line(
                squares[2].get_corner(UP + RIGHT),
                squares[5].get_corner(DOWN + RIGHT),
            ),
            radius=0.3,
            quadrant=(1, 1),
            other_angle=False,
            stroke_color=BLACK,
            stroke_width=2
        )
        txt_4 = Tex(
            r"$\frac{\pi}{2} = \arctan 1 + \arctan \frac{1}{2} + \arctan \frac{1}{3}$",
            font_size=24, color=BLACK
        ).next_to(squares, DOWN, buff=1)
        self.play(
            Create(angle4),
            Write(txt_4)
        )

        self.wait(1)

        # Fifth identity
        self.play(
            Uncreate(angle4),
            Uncreate(txt_4)
        )
        angle5 = Arc(
            angle=PI, start_angle=-PI / 2,
            stroke_color=BLACK, stroke_width=2, radius=0.3
        ).move_arc_center_to(squares[3].get_corner(UP + LEFT))
        txt_5 = Tex(
            r"$\pi = \arctan 1 + \arctan 2 + \arctan 3$",
            font_size=24, color=BLACK
        ).next_to(squares, DOWN, buff=1)
        self.play(
            Create(angle5),
            Write(txt_5)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"College Mathematics Journal,", font_size=26, color=BLACK),
            Tex(r"vol. 34, no. 2", font_size=26, color=BLACK),
            Tex(r"(march 2003), pp. 115-138.", font_size=26, color=BLACK)
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