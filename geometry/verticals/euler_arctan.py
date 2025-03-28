"""
Visual proof of a Euler's Arctangent Identity.
Proofs without Words III. Roger B. Nelsen. p. 77.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Angle
from manim import Text, Tex, RoundedRectangle, Rectangle, Line, RightAngle
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
            Tex(r"Une identé d'Euler", font_size=48, color=BLACK),
            Tex(r"sur les arctangentes", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Rex H. Wu", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        formula = Tex(
            r"$\arctan \frac{1}{x} = \arctan \frac{1}{x + y}+ \arctan \frac{y}{x^2 + xy + 1}$",
            font_size=20, color=BLACK
        ).move_to([0, -2, 0])

        self.add(
            txt_title,
            txt,
            formula
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt),
            Uncreate(formula)
        )

        # Create rectangle
        rect = Rectangle(
            width=3, height=7, color=BLACK, stroke_width=1
        ).scale(0.8)
        txt_xy = Tex(r"$x + y$", font_size=24, color=BLACK).next_to(rect, UP, buff=0.1)
        txt_xy1 = Tex(r"$x^2 + xy +1$", font_size=24, color=BLACK).\
            rotate(-PI/2).\
            next_to(rect, RIGHT, buff=0.1)

        self.play(
            Create(rect),
            Write(txt_xy),
            Write(txt_xy1)
        )

        # Create triangle
        print(rect.get_boundary_point(DOWN))
        l = Line(
            rect.get_boundary_point(UP),
            rect.get_boundary_point(DOWN) + [1.6, 0, 0],
            color=BLACK, stroke_width=1
        )
        l2 = Line(
            rect.get_boundary_point(DOWN) + [1.6, 0, 0],
            rect.get_boundary_point(DOWN) + [0, 0.8, 0],
            color=BLACK, stroke_width=1
        )
        l3 = Line(
            rect.get_boundary_point(DOWN) + [0, 0.8, 0],
            rect.get_boundary_point(UP),
            color=BLACK, stroke_width=1
        )
        txt_x = Tex(r"$x$", font_size=24, color=BLACK).\
            move_to(rect.get_boundary_point(DOWN) + [0.8, -0.1, 0])
        txt_y = Tex(r"$y$", font_size=24, color=BLACK).\
            move_to(rect.get_boundary_point(DOWN) + [2, -0.1, 0])
        txt_1 = Tex(r"$1$", font_size=24, color=BLACK).\
            move_to(rect.get_boundary_point(DOWN) + [-0.1, 0.4, 0])
        txt_xxy = Tex(r"$x(x + y)$", font_size=24, color=BLACK).\
            move_to(rect.get_boundary_point(DOWN) + [-0.2, 2.8, 0]).\
            rotate(PI/2)
        r_angle = RightAngle(l2, l3, length=0.2, quadrant=(-1, 1), color=BLACK)
        
        self.play(
            Create(l),
            Create(l2),
            Create(l3),
            Write(txt_x),
            Write(txt_y),
            Write(txt_1),
            Write(txt_xxy),
            Create(r_angle),
        )

        # Pythagorean theorem
        txt_sqrt1x2 = Tex(
            r"$\sqrt{1 + x^2}$", font_size=18, color=BLACK
        ).rotate_about_origin(l2.get_angle() + PI).\
            move_to(l2.get_center_of_mass() + [0.15, 0.15, 0])

        txt_xysqrt = Tex(
            r"$(x + y)\sqrt{1 + x^2}$", font_size=18, color=BLACK
        ).rotate_about_origin(l3.get_angle()).\
            move_to(l3.get_center_of_mass() + [-0.4, -0.4, 0])
        
        self.play(
            Write(txt_sqrt1x2),
            Write(txt_xysqrt)
        )


        # Angles
        l_rect = Line(
            rect.get_boundary_point(LEFT),
            rect.get_boundary_point(DOWN),
        )
        l_rect2 = Line(
            rect.get_boundary_point(RIGHT),
            rect.get_corner(DOWN + RIGHT)
        )
        angle1 = Angle(
            l3, l_rect, radius=0.5,
            quadrant=(1, -1),
            color=RED, stroke_width=6
        )
        alpha = Tex(
            r"$\alpha$", font_size=24, color=BLACK
        ).next_to(angle1, UP, buff=0.2)

        angle2 = Angle(
            l, l3, radius=1,
            quadrant=(1, -1), other_angle=True,
            color=BLUE, stroke_width=6
        )
        beta = Tex(
            r"$\beta$", font_size=24, color=BLACK
        ).next_to(angle2, DOWN, buff=0.2)

        angle3 = Angle(
            l, l_rect2, radius=1.5,
            quadrant=(1, 1),
            color=GREEN, stroke_width=6
        )
        gamma = Tex(
            r"$\gamma$", font_size=24, color=BLACK
        ).next_to(angle3, DOWN, buff=0.2)

        self.play(
            Create(angle1),
            Write(alpha),
            Create(angle2),
            Write(beta),
            Write(angle3),
            Write(gamma),
        )

        # Write equation
        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        )
        txt = Tex(
            r"$\alpha$", r" $ = $ ", r"$\beta$", r" $ + $ ", r"$\gamma$",
            font_size=28, color=BLACK
        )

        rect.z_index = 0
        txt.z_index = 1
        self.play(
            Create(rect),
            run_time=0.1
        )
        self.play(
            TransformFromCopy(alpha[0], txt[0]),
            Write(txt[1]),
            TransformFromCopy(beta[0], txt[2]),
            Write(txt[3]),
            TransformFromCopy(gamma[0], txt[4])
        )

        formula = Tex(
            r"$\arctan \frac{1}{x} = \arctan \frac{1}{x + y}$",
            r"$+ \arctan \frac{y}{x^2 + xy + 1}$",
            font_size=20, color=BLACK
        )
        
        self.play(
            Transform(txt, formula)
        )


        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine, vol. 77,", font_size=26, color=BLACK),
            Tex(r"no. 3 (June 2004 ), p.189", font_size=26, color=BLACK)
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