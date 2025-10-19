"""
Visual proof of the Pythagorean triples via double angle formulas.
Proofs without Words I. Roger B. Nelsen. p. 141.
"""
import numpy as np

from manim import MovingCameraScene, Mobject
from manim import Brace, Line, Polygon
from manim import RoundedRectangle, Square
from manim import Create, Rotate, Transform, Uncreate, Write, Angle
from manim import FadeIn, FadeOut, FadeTransform, TransformFromCopy
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
            Tex(r"Triplés de", font_size=48, color=BLACK),
            Tex(r"Pythagore", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"David Houston", font_size=28, color=BLACK)
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

        # Second triangle
        triangle2 = Polygon(
            [0, 0, 0],
            [3, 0, 0],
            [3, 4, 0],
            color=BLACK,
            fill_color=RED,
            fill_opacity=1,
            stroke_width=2,
        )
        triangle2.move_to([0, -1, 0])

        # First triangle
        triangle1 = Polygon(
            [0, 0, 0],
            [2, 0, 0],
            [2, 1, 0],
            color=BLACK,
            fill_color=BLUE,
            fill_opacity=1,
            stroke_width=2,
        )
        triangle1.next_to(triangle2, UP, buff=1, aligned_edge=RIGHT)

        angle1 = Angle(
            line1=Line(triangle1.get_vertices()[0], triangle1.get_vertices()[1]),
            line2=Line(triangle1.get_vertices()[0], triangle1.get_vertices()[2]),
            radius=0.3,
            stroke_width=2,
            other_angle=False,
            color=BLACK,
        )
        txt_theta = Tex(r"$\theta$", font_size=24, color=BLACK)
        txt_theta.move_to(angle1.get_center() + 0.2 * RIGHT + 0.05 * UP)
        txt_m = Tex(r"$m$", font_size=24, color=BLACK)
        txt_m.next_to(triangle1, DOWN, buff=0.1)
        txt_n = Tex(r"$n$", font_size=24, color=BLACK)
        txt_n.next_to(triangle1, RIGHT, buff=0.1)

        self.play(
            Create(triangle1),
            Create(angle1),
            Write(txt_theta),
            Write(txt_m),
            Write(txt_n)
        )

        # Formulas sin and cosinus
        txt_sin = Tex(
            r"$\sin(\theta) = \frac{n}{\sqrt{m^2 + n^2}}$", font_size=28, color=BLACK
        )
        txt_sin.move_to([-1, 3.25, 0])

        txt_cos = Tex(
            r"$\cos(\theta) = \frac{m}{\sqrt{m^2 + n^2}}$", font_size=28, color=BLACK
        )
        txt_cos.next_to(txt_sin, DOWN, buff=0.2)

        self.play(
            Write(txt_sin),
            Write(txt_cos),
        )

        self.wait(2)

        angle2 = Angle(
            line1=Line(triangle2.get_vertices()[0], triangle2.get_vertices()[1]),
            line2=Line(triangle2.get_vertices()[0], triangle2.get_vertices()[2]),
            radius=0.5,
            stroke_width=2,
            other_angle=False,
            color=BLACK,
        )
        ttx_theta2 = Tex(r"$2\theta$", font_size=24, color=BLACK)
        ttx_theta2.move_to(angle2.get_center() + 0.3 * RIGHT + 0.1 * UP)
        txt_m2 = Tex(r"$m^2 - n^2$", font_size=24, color=BLACK)
        txt_m2.next_to(triangle2, DOWN, buff=0.1)
        txt_n2 = Tex(r"$2mn$", font_size=24, color=BLACK)
        txt_n2.next_to(triangle2, RIGHT, buff=0.1)
        txt_mn = Tex(r"$m^2 + n^2$", font_size=24, color=BLACK)
        txt_mn.rotate(PI/4).next_to(triangle2.get_center(), UL, buff=-0.15)

        self.play(
            Create(triangle2),
            Create(angle2),
            Write(ttx_theta2),
            Write(txt_m2),
            Write(txt_n2),
            Write(txt_mn)
        )

        # Formulas sin and cosinus
        txt_sin2 = Tex(
            r"$\sin(2\theta) = \frac{2mn}{m^2 + n^2}$", font_size=28, color=BLACK
        )
        txt_sin2.move_to([-1, 1, 0])

        txt_cos2 = Tex(
            r"$\cos(2\theta) = \frac{m^2 - n^2}{m^2 + n^2}$", font_size=28, color=BLACK
        )
        txt_cos2.next_to(txt_sin2, DOWN, buff=0.2)

        self.play(
            Write(txt_sin2),
            Write(txt_cos2),
        )
        
        
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine, vol. 67,", font_size=30, color=BLACK),
            Tex(r"no. 3 (June 1994), p.187.", font_size=30, color=BLACK),
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

        