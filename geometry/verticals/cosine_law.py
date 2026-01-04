"""
Visual proof of The Law of Cosines.
Proofs without Words I. Roger B. Nelsen. p. 32.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, Group
from manim import Polygon, VGroup, FadeIn, FadeOut, FunctionGraph
from manim import Text, Tex, Triangle, RoundedRectangle, Circle, Line, Dot, Angle

from manim import line_intersection

from manim import config
from manim import LEFT, RIGHT, DOWN, LIGHT, UP, SMALL_BUFF, PI

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


class Cosine(MovingCameraScene):
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
            Tex(r"La loi", font_size=48, color=BLACK),
            Tex(r"des cosinus", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Sidney H. Kung", font_size=28, color=BLACK)
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

        # Create circle
        circle = Circle(radius=2, color=BLACK, stroke_width=2)
        circle.move_to([0, 1, 0])
        self.play(Create(circle))

        # Create right triangle inside circle
        A = np.array([-2, 1, 0])
        B = np.array([2, 1, 0])
        C = np.array(
            [
                2 - 4 * np.cos(np.pi / 6)**2,
                1 + 4 * np.cos(np.pi / 6) * np.sin(np. pi / 6),
                0
            ]
        )
        # Angle theta
        angle = Angle(
            Line(B, A), Line(B, C), other_angle=True,   
            radius=0.4, color=BLACK, stroke_width=2
        )
        theta = Tex(r"$\theta$", font_size=24, color=BLACK)
        theta.next_to(angle, RIGHT + UP, buff=SMALL_BUFF)

        triangle = Polygon(A, B, C, color=BLACK, stroke_width=2)
        self.play(
            Create(triangle),
            Create(angle),
            Write(theta)
        )

        # Line that correspond to diameter
        D = np.array(
            [
                2 * np.cos(np.pi / 4),
                1 + 2 * np.sin(np.pi / 4),
                0
            ]
        )
        E = np.array(
            [
                2 * np.cos(5 * np.pi / 4),
                1 + 2 * np.sin(5 * np.pi / 4),
                0
            ]
        )

        diameter = Line(D, E, color=BLACK, stroke_width=2)
        self.play(
            Create(diameter)
        )

        # Write the different lengths
        O = np.array([0, 1, 0])
        F = line_intersection([D, E], [B, C])

        line_AO = Line(A, O, color=BLACK, stroke_width=0)
        line_EO = Line(E, O, color=BLACK, stroke_width=0)
        line_BO = Line(B, O, color=BLACK, stroke_width=0)
        line_FO = Line(F, O, color=BLACK, stroke_width=0)
        line_FD = Line(F, D, color=BLACK, stroke_width=0)
        line_BF = Line(B, F, color=BLACK, stroke_width=0)
        line_FC = Line(F, C, color=BLACK, stroke_width=0)

        txt_a = Tex(r"$a$", font_size=24, color=BLACK)
        txt_a.next_to(line_AO.get_center(), DOWN, buff=SMALL_BUFF)
        txt_a2 = Tex(r"$a$", font_size=24, color=BLACK)
        txt_a2.next_to(line_EO.get_center(), DOWN + RIGHT, buff=SMALL_BUFF)
        txt_a3 = Tex(r"$a$", font_size=24, color=BLACK)
        txt_a3.next_to(line_BO.get_center(), DOWN, buff=SMALL_BUFF)

        self.play(
            Write(txt_a),
            Write(txt_a2),
            Write(txt_a3)
        )

        txt_b = Tex(r"$b$", font_size=24, color=BLACK)
        txt_b.next_to(line_BF.get_center(), UP + RIGHT, buff=SMALL_BUFF)
        txt_b2 = Tex(r"$2a\cos(\theta) - b$", font_size=24, color=BLACK).rotate(-PI/6)
        txt_b2.move_to(line_FC.get_center()+ [0.1, 0.1, 0])

        self.play(
            Write(txt_b),
            Write(txt_b2)
        )

        txt_c = Tex(r"$c$", font_size=24, color=BLACK)
        txt_c.next_to(line_FO.get_center(), UP + LEFT, buff=SMALL_BUFF)
        txt_c2 = Tex(r"$a - c$", font_size=24, color=BLACK).rotate(PI/4)
        txt_c2.move_to(line_FD.get_center() + [-0.1, 0.1, 0])

        self.play(
            Write(txt_c),
            Write(txt_c2)
        )

        # Color small triangle
        small_triangle = Polygon(O, B, F, color=RED, fill_opacity=0.5, stroke_width=2)
        self.play(Create(small_triangle))

        # Write text
        txt = Tex(
            r"$(2a \cos(\theta) - b)b = (a - c)(a + c)$", font_size=28, color=BLACK
        )
        txt.move_to([0, -1.5, 0])
        self.play(Write(txt))
        self.wait(1)

        txt2 = Tex(
            r"$c^2 = a^2 + b^2 - 2 a b \cos(\theta)$", font_size=28, color=BLACK   
        )
        txt2.next_to(txt, DOWN, buff=0.5)
        self.play(Write(txt2))


        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine, vol. 63,", font_size=26, color=BLACK),
            Tex(r"no. 5 (Dec. 1990), p.342", font_size=26, color=BLACK)
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