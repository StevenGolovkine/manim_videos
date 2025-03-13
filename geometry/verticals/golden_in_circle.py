"""
Visual proof of A Golden Section Problem from the Monthly
Proofs without Words II. Roger B. Nelsen. p. 18.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, Group
from manim import Brace, VGroup, FadeIn, FadeOut, FunctionGraph
from manim import Text, Tex, Triangle, RoundedRectangle, Circle

from manim import config
from manim import LEFT, RIGHT, DOWN, LIGHT, UP

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


class Golden(MovingCameraScene):
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
            Tex(r"Une construction", font_size=40, color=BLACK),
            Tex(r"du nombre d'or $\varphi$", font_size=40, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Jan van de Craats", font_size=28, color=BLACK)
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

        # Create the triangle
        triangle = Triangle(color=BLACK, stroke_width=2).scale(2)
        points = triangle.get_vertices()

        p_A = Tex(r"$A$", font_size=28, color=BLACK).\
            next_to(points[0], 0.5 * UP)
        p_B = Tex(r"$B$", font_size=28, color=BLACK).\
            next_to(points[1], 0.5 * (DOWN + LEFT))
        p_C = Tex(r"$C$", font_size=28, color=BLACK).\
            next_to(points[2], 0.5 * (DOWN + RIGHT))

        self.play(
            Create(triangle),
            Write(p_A),
            Write(p_B),
            Write(p_C)
        )

        # Create the middle points
        origin = triangle.get_center_of_mass()

        circle = Circle(radius=2, color=BLACK, stroke_width=2).move_to(origin)
        self.play(
            Create(circle)
        )


        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Proofs without words II:", font_size=30, color=BLACK),
            Tex(r"More exercises in", font_size=30, color=BLACK),
            Tex(r"visual thinking", font_size=30, color=BLACK),
            Tex(r"Roger B. Nelsen (2000), p. 18", font_size=30, color=BLACK)
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