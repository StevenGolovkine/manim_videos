"""
Visual proof of the triangle of medians has three-fourth the area of the original
triangle.
Proofs without Words II. Roger B. Nelsen. p. 16.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import VGroup, FadeIn, FadeOut , FunctionGraph
from manim import Line, Point
from manim import Text, Tex

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


class Triangle(MovingCameraScene):
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
            Tex(r"L'aire du triangle", font_size=40, color=BLACK),
            Tex(r"des médianes est égale", font_size=40, color=BLACK),
            Tex(r"aux trois-quarts", font_size=40, color=BLACK),
            Tex(r"du triangle original", font_size=40, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Norbert Hungerbühler", font_size=28, color=BLACK)
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

        # Triangle
        pA = Point([-2, -1, 0], color=BLACK)
        pB = Point([2, -1, 0], color=BLACK)
        pC = Point([-1, 2, 0], color=BLACK)
        AB = Line(pA, pB, color=BLACK)
        BC = Line(pB, pC, color=BLACK)
        CA = Line(pC, pA, color=BLACK)
        AMb = Line(pA, BC.get_center_of_mass(), color=BLUE)
        BMc = Line(pB, CA.get_center_of_mass(), color=VIOLET)
        CMa = Line(pC, AB.get_center_of_mass(), color=RED)
        A = Tex(r"$A$", font_size=36, color=BLACK).next_to(pA, DOWN, buff=0.1)
        B = Tex(r"$B$", font_size=36, color=BLACK).next_to(pB, DOWN, buff=0.1)
        C = Tex(r"$C$", font_size=36, color=BLACK).next_to(pC, UP, buff=0.1)
        Ma = Tex(r"$M_a$", font_size=36, color=BLUE).\
            next_to(BC.get_center_of_mass(), RIGHT, buff=0.1)
        Mb = Tex(r"$M_b$", font_size=36, color=VIOLET).\
            next_to(CA.get_center_of_mass(), LEFT, buff=0.1)
        Mc = Tex(r"$M_c$", font_size=36, color=RED).\
            next_to(AB.get_center_of_mass(), DOWN, buff=0.1)
        self.play(
            Create(AB),
            Create(BC),
            Create(CA),
            Create(AMb),
            Create(BMc),
            Create(CMa),
            Create(A),
            Create(B),
            Create(C),
            Create(Ma),
            Create(Mb),
            Create(Mc)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine, vol. 72,", font_size=30, color=BLACK),
            Tex(r"no. 2 (April 1999), p. 142", font_size=30, color=BLACK),
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