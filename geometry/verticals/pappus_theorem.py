"""
Visual proof of the Pappus' Generalization of the Pythagorean Theorem.
Proofs without Words III. Roger B. Nelsen. p. 7.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, TransformFromCopy
from manim import VGroup, FadeIn, FadeOut , FunctionGraph
from manim import DashedVMobject, Line, Point, Polygon, RoundedRectangle
from manim import Text, Tex

from manim import line_intersection

from manim import config
from manim import ORIGIN, LEFT, RIGHT, DOWN, LIGHT, UP, PI

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
            Tex(r"Théorème de", font_size=48, color=BLACK),
            Tex(r"Pappus", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Pappus d'Alexandrie", font_size=28, color=BLACK)
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
        A = np.array([-1.5, -1, 0])
        B = np.array([1.5, -1, 0])
        C = np.array([-0.25, 1.5, 0])
        triangle_ABC = Polygon(
            A, B, C,
            color=BLACK, stroke_width=2,
            fill_color=BLUE, fill_opacity=1, 
        )
        
        self.play(
            Create(triangle_ABC)
        )

        # Parallelograms on each side
        D = A + [-0.75, 0.25, 0]
        E = C + [-0.75, 0.25, 0]
        parallelogram_ACED = Polygon(
            A, C, E, D,
            color=BLACK, stroke_width=2,
            fill_color=VIOLET, fill_opacity=1, 
        )

        self.play(
            Create(parallelogram_ACED)
        )

        F = B + [0.4, 0.15, 0]
        G = C + [0.4, 0.15, 0]
        parallelogram_BCGF = Polygon(
            B, C, G, F,
            color=BLACK, stroke_width=2,
            fill_color=VIOLET, fill_opacity=1, 
        )

        self.play(
            Create(parallelogram_BCGF)
        )
        
        # Extend lines
        f_x = lambda x: 2 * x + 3.75
        g_x = lambda x: -1.429 * x + 1.865

        new_E = [1, f_x(1), 0]
        new_G = [-1, g_x(-1), 0]

        line_EE = Line(E, new_E, color=BLACK, stroke_width=2)
        line_GG = Line(G, new_G, color=BLACK, stroke_width=2)
        self.play(
            Create(line_EE),
            Create(line_GG),
        )

        # Intersection of lines
        H = line_intersection([E, new_E], [G, new_G])
        line_CH = Line(C, H, color=BLACK, stroke_width=2)
        self.play(
            Create(line_CH)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Great Moments in Mathematics,", font_size=30, color=BLACK),
            Tex(r"MAA, 1980, pp. 37-38.", font_size=30, color=BLACK),
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