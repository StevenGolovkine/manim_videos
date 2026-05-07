"""
Visual proof of the Pythagorean-like theorem IV.
Proofs without Words III. Roger B. Nelsen. p. 9.
"""
import numpy as np

from manim import DEGREES, MovingCameraScene, Mobject
from manim import Brace, Line, Polygon
from manim import RoundedRectangle, Square
from manim import Create, Rotate, Transform, Uncreate, Write
from manim import FadeIn, FadeOut, Angle
from manim import FunctionGraph, VGroup
from manim import Text, Tex

from manim import config

from manim import LEFT, RIGHT, UP, DOWN, PI, DR, DL, UR, UL, LIGHT

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


class RotateAndColor(Rotate, Transform):
    def __init__(
        self,
        mobject: Mobject,            
        angle: float,
        new_color,
        **kwargs,
    ) -> None:
        self.new_color = new_color
        super().__init__(mobject, angle=angle, **kwargs)

    def create_target(self) -> Mobject:
        target = self.mobject.copy()
        target.set_fill(self.new_color)
        target.rotate(
            self.angle,
            axis=self.axis,
            about_point=self.about_point,
            about_edge=self.about_edge,
        )
        return target


class Pythagorean(MovingCameraScene):
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
            Tex(r"Un théorème", font_size=48, color=BLACK),
            Tex(r"Pythagore-like", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration IV", font_size=36, color=BLACK),
            Tex(r"Larry Hoehn", font_size=28, color=BLACK),
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
            run_time=0.5
        )
        self.wait(0.5)

        # Create an isosceles triangle
        A = [-1.5, 0, 0]
        B = [1.5, 0, 0]
        C = [0, 2, 0]
        D = [-0.5, 0, 0]
        triangle = Polygon(
            A, B, C,
            color=BLACK, fill_color=WHITE, fill_opacity=1, stroke_width=2
        )
        line = Line(D, C, color=BLACK, stroke_width=2)

        side_c_left = np.array(C) - np.array(A)
        side_c_left_normal = np.array([-side_c_left[1], side_c_left[0], 0])
        square_c_left = Polygon(
            A,
            C,
            np.array(C) + side_c_left_normal,
            np.array(A) + side_c_left_normal,
            color=BLACK,
            fill_color=GREEN,
            fill_opacity=1,
            stroke_width=2,
        )

        txt_a = Tex(r"$a$", font_size=24, color=BLACK).move_to([0, 1, 0])
        txt_b = Tex(r"$b$", font_size=24, color=BLACK).move_to([-1, -0.2, 0])
        txt_c = Tex(r"$c$", font_size=24, color=BLACK).move_to([-1, 1, 0])
        txt_c2 = Tex(r"$c$", font_size=24, color=BLACK).move_to([1, 1, 0])
        txt_d = Tex(r"$d$", font_size=24, color=BLACK).move_to([0.5, -0.2, 0])
        txt_c_square = Tex(r"$c^2$", font_size=24, color=BLACK)\
            .move_to(square_c_left.get_center_of_mass())

        diagram = VGroup(
            square_c_left,
            triangle,
            line,
            txt_a,
            txt_b,
            txt_c,
            txt_c2,
            txt_d,
            txt_c_square,
        ).scale(0.78).move_to([0, 0.25, 0])

        self.play(
            Create(square_c_left),
            Create(triangle),
            Create(line),
            Write(txt_a),
            Write(txt_b),
            Write(txt_c),
            Write(txt_c2),
            Write(txt_d),
            Write(txt_c_square),
        )


        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"The Changing Shape of", font_size=30, color=BLACK),
            Tex(r"Geometry, MAA,", font_size=30, color=BLACK),
            Tex(r"2003, pp.228-231.", font_size=30, color=BLACK),
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

        
