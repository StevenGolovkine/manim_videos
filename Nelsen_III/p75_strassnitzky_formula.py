"""
Visual proof of The Formulas of Strassnitzky.
Proofs without Words III. Roger B. Nelsen. p. 75.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, RightAngle, Square, Angle
from manim import Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Line, Polygon
from manim import Text, Tex, DashedVMobject, DashedLine, RoundedRectangle

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


class Formula(MovingCameraScene):
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
            Tex(r"La formule de", font_size=48, color=BLACK),
            Tex(r"Strassnitzky", font_size=48, color=BLACK),
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

        # Formula
        txt_formula = Tex(r"$\frac{\pi}{4} = \arctan \frac{1}{2} + \arctan \frac{1}{5} + \arctan \frac{1}{8}$", font_size=22, color=BLACK)\
            .move_to([0, 3, 0])
        self.play(Write(txt_formula))

        # Create 7 by 5 squares
        squares = VGroup()
        squares.add(Square(side_length=0.4, color=BLACK, stroke_width=1))
        for idx in range(9):
            new_square = Square(side_length=0.4, color=BLACK, stroke_width=1).\
                next_to(squares[idx], direction=RIGHT, buff=0)
            squares.add(new_square)
        for idx in range(70):
            new_square = Square(side_length=0.4, color=BLACK, stroke_width=1).\
                next_to(squares[idx], direction=DOWN, buff=0)
            squares.add(new_square)
        squares.move_to([0, 0, 0])
        self.play(
            Create(squares)
        )

        # First triangle
        triangle_1 = Polygon(
            squares[70].get_boundary_point(DOWN),
            squares[69].get_boundary_point(RIGHT + UP),
            squares[79].get_boundary_point(RIGHT + DOWN),
            color=RED, fill_color=RED, fill_opacity=0.5, stroke_width=1
        )
        right_angle_1 = RightAngle(
            Line(
                squares[79].get_boundary_point(RIGHT + DOWN),
                squares[69].get_boundary_point(RIGHT + UP)
            ),
            Line(
                squares[79].get_boundary_point(RIGHT + DOWN),
                squares[70].get_boundary_point(DOWN)
            ),
            length=0.2, color=BLACK, stroke_width=1
        )
        self.play(
            Create(triangle_1),
            Create(right_angle_1)
        )

        # Second triangle
        triangle_2 = Polygon(
            squares[70].get_boundary_point(DOWN),
            squares[19].get_boundary_point(LEFT),
            squares[69].get_boundary_point(RIGHT + UP),
            color=BLUE, fill_color=BLUE, fill_opacity=0.5, stroke_width=1
        )
        right_angle_2 = RightAngle(
            Line(
                squares[69].get_boundary_point(RIGHT + UP),
                squares[70].get_boundary_point(LEFT)
            ),
            Line(
                squares[69].get_boundary_point(RIGHT + UP),
                squares[19].get_boundary_point(LEFT)
            ),
            length=0.2, color=BLACK, stroke_width=1
        )
        self.play(
            Create(triangle_2),
            Create(right_angle_2)
        )

        # Third triangle
        triangle_3 = Polygon(
            squares[70].get_boundary_point(DOWN),
            squares[8].get_boundary_point(LEFT),
            squares[19].get_boundary_point(LEFT),
            color=RED, fill_color=RED, fill_opacity=0.5, stroke_width=1
        )
        right_angle_3 = RightAngle(
            Line(
                squares[8].get_boundary_point(LEFT),
                squares[70].get_boundary_point(LEFT)
            ),
            Line(
                squares[8].get_boundary_point(LEFT),
                squares[19].get_boundary_point(LEFT)
            ),
            length=0.2, color=BLACK, stroke_width=1
        )
        self.play(
            Create(triangle_3),
            Create(right_angle_3)
        )

        # Fourth triangle
        triangle_4 = Polygon(
            squares[70].get_boundary_point(DOWN),
            squares[8].get_boundary_point(LEFT),
            squares[78].get_boundary_point(DOWN + LEFT),
            color=BLACK, fill_color=BLACK, fill_opacity=0.5, stroke_width=1
        )
        right_angle_4 = RightAngle(
            Line(
                squares[78].get_boundary_point(DOWN + LEFT),
                squares[8].get_boundary_point(LEFT)
            ),
            Line(
                squares[78].get_boundary_point(DOWN + LEFT),
                squares[70].get_boundary_point(DOWN)
            ),
            length=0.2, color=BLACK, stroke_width=1
        )
        self.play(
            Create(triangle_4),
            Create(right_angle_4)
        )

        # Last angle
        angle = Angle(
            Line(
                squares[70].get_boundary_point(DOWN),
                squares[78].get_boundary_point(LEFT + DOWN)
            ),
            Line(
                squares[70].get_boundary_point(DOWN),
                squares[8].get_boundary_point(LEFT)
            ),
            radius=0.3, color=WHITE, stroke_width=4
        )
        txt_pi4 = Tex(r"$\pi / 4$", font_size=24, color=WHITE).next_to(angle, RIGHT, buff=0.1)
        self.play(
            Create(angle),
            Write(txt_pi4)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine,", font_size=26, color=BLACK),
            Tex(r"vol. 86, no. 5 (Dec. 2013), p. 350.", font_size=26, color=BLACK)
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