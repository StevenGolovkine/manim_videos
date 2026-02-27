"""
Visual proof of the Pythagorean-like theorem.
Proofs without Words II. Roger B. Nelsen. p. 10.
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
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Manuel Moran Cabre", font_size=28, color=BLACK),
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

        # Create a triangle with one angle equal pi/3.
        A = [-1, 0, 0]
        B = [1, 0, 0]
        C = [-0.48, 0.91, 0]
        triangle = Polygon(A, B, C, color=BLACK, fill_color=BLUE, fill_opacity=1, stroke_width=2)
        txt_triangle = Tex(r"$T$", font_size=24, color=BLACK).\
            move_to(triangle.get_center_of_mass())
        angle = Angle(Line(A, B), Line(A, C), radius=0.3, color=BLACK, other_angle=False)
        txt_angle = Tex(r"$\pi/3$", font_size=18, color=BLACK).\
            next_to(angle, RIGHT, buff=0.1)
        self.play(
            Create(triangle),
            Write(txt_triangle),
            Create(angle),
            Write(txt_angle),
        )

        # Create equilateral triangles on each side of the triangle.
        D = [-1.53, 0.91, 0]
        E = [1.05, 1.74, 0]
        F = [0, -1.73, 0]

        triangle_ACD = Polygon(A, C, D, color=BLACK, fill_color=RED, fill_opacity=1, stroke_width=2)
        txt_ACD = Tex(r"$T_\alpha$", font_size=18, color=BLACK).\
            move_to(triangle_ACD.get_center_of_mass())
        self.play(
            Create(triangle_ACD),
            Write(txt_ACD),
        )
        
        triangle_BCE = Polygon(B, C, E, color=BLACK, fill_color=RED, fill_opacity=1, stroke_width=2)
        txt_BCE = Tex(r"$T_\beta$", font_size=18, color=BLACK).\
            move_to(triangle_BCE.get_center_of_mass())
        self.play(
            Create(triangle_BCE),
            Write(txt_BCE),
        )

        triangle_ABF = Polygon(A, B, F, color=BLACK, fill_color=RED, fill_opacity=1, stroke_width=2)
        txt_ABF = Tex(r"$T_\gamma$", font_size=18, color=BLACK).\
            move_to(triangle_ABF.get_center_of_mass())
        self.play(
            Create(triangle_ABF),
            Write(txt_ABF),
        )

        all_object = VGroup(
            triangle, triangle_ACD, triangle_BCE, triangle_ABF,
            txt_triangle, txt_ACD, txt_BCE, txt_ABF,
            angle, txt_angle
        )

        # Write formula
        formula = Tex(
            r"$T + T_\beta = T_\alpha + T_\gamma$", font_size=30, color=BLACK
        ).move_to([0, 2, 0])
        self.play(Write(formula))

        # Move everything to the top
        self.play(
            all_object.animate.move_to([0, 2.5, 0]),
            formula.animate.move_to([0, 0.5, 0])
        )

        # Copy main triangle and move it to BCE
        triangle_copy_1 = triangle.copy()
        triangle_copy_2 = triangle.copy()
        triangle_copy_3 = triangle.copy()
        triangle_BCE_copy = triangle_BCE.copy()
        txt_BCE_copy = txt_BCE.copy()

        self.play(
            triangle_BCE_copy.animate.move_to([0, -2, 0]),
            run_time=0.5
        )

        txt_BCE_copy.move_to(triangle_BCE_copy.get_center_of_mass())
        self.play(
            triangle_BCE_copy.animate.rotate(31 * DEGREES),
            Write(txt_BCE_copy),
            run_time=0.5
        )

        self.play(
            triangle_copy_1.animate.rotate(31 * DEGREES),
            run_time=0.5
        )
        self.play(
            triangle_copy_1.animate.next_to(triangle_BCE_copy, DOWN, buff=0),
            run_time=0.5
        )

        self.play(
            triangle_copy_2.animate.rotate(-89 * DEGREES),
            run_time=0.5
        )
        self.play(
            triangle_copy_2.animate.move_to(triangle_BCE_copy.get_center_of_mass() + [-0.45, 0.5, 0]),
            run_time=0.5
        )

        self.play(
            triangle_copy_3.animate.rotate(149 * DEGREES),
            run_time=0.5
        )
        self.play(
            triangle_copy_3.animate.move_to(triangle_BCE_copy.get_center_of_mass() + [0.88, 0.22, 0]),
            run_time=0.5
        )

        txt_triangle_copy_1 = txt_triangle.copy().move_to(triangle_copy_1.get_center_of_mass())
        txt_triangle_copy_2 = txt_triangle.copy().move_to(triangle_copy_2.get_center_of_mass())
        txt_triangle_copy_3 = txt_triangle.copy().move_to(triangle_copy_3.get_center_of_mass())
        self.play(
            Write(txt_triangle_copy_1),
            Write(txt_triangle_copy_2),
            Write(txt_triangle_copy_3),
            run_time=0.5
        )

        # Finish the proof by showing that the 4 triangles are exactly the same, so the formula is true.
        triangle_ABF_copy = triangle_ABF.copy().set_opacity(0.5)
        triangle_ACD_copy = triangle_ACD.copy().set_opacity(0.5)
        triangle_copy_4 = triangle.copy().set_opacity(0.5)

        self.play(
            triangle_ABF_copy.animate.rotate(-(60 - 30.5) * DEGREES),
            run_time=0.5
        )
        self.play(
            triangle_ABF_copy.animate.move_to(triangle_BCE_copy.get_center_of_mass() + [0.9, -0.04, 0]),
            run_time=0.5
        )
        txt_ABF_copy = txt_ABF.copy().move_to(triangle_ABF_copy.get_center_of_mass())
        self.play(
            Write(txt_ABF_copy),
            run_time=0.5
        )

        self.play(
            triangle_ACD_copy.animate.rotate(91 * DEGREES),
            run_time=0.5
        )
        self.play(
            triangle_ACD_copy.animate.move_to(triangle_BCE_copy.get_center_of_mass() + [-0.4, -1.05, 0]),
            run_time=0.5
        )
        txt_ACD_copy = txt_ACD.copy().move_to(triangle_ACD_copy.get_center_of_mass())
        self.play(
            Write(txt_ACD_copy),
            run_time=0.5
        )

        self.play(
            triangle_copy_4.animate.rotate(91 * DEGREES),
            run_time=0.5
        )
        self.play(
            triangle_copy_4.animate.move_to(triangle_BCE_copy.get_center_of_mass() + [-0.42, 0, 0]),
            run_time=0.5
        )
        txt_triangle_copy_4 = txt_triangle.copy().move_to(triangle_copy_4.get_center_of_mass())
        self.play(
            Write(txt_triangle_copy_4),
            run_time=0.5
        )


        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"College Mathematics Journal,", font_size=30, color=BLACK),
            Tex(r"vol. 34, no. 2,", font_size=30, color=BLACK),
            Tex(r"(March 2003), p. 172.", font_size=30, color=BLACK)
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

        