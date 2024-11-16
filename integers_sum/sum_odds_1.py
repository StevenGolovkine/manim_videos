"""
Visual proof of the sums of odd integers.
Proofs without Words I. Roger B. Nelsen. p. 71.
"""
import numpy as np

from manim import MovingCameraScene, Mobject
from manim import Point, Square, Polygon, Line, Dot
from manim import Create, Rotate, Transform, Uncreate, Write
from manim import TransformFromCopy
from manim import FadeTransform
from manim import VGroup
from manim import Tex

from manim import LEFT, RIGHT, UP, DOWN, PI, DEGREES

# COLORS
BLUE = "#648FFF"
VIOLET = "#785EF0"
RED = "#DC267F"
ORANGE = "#FE6100"
YELLOW = "#FFB000"
BLACK = "#000000"
WHITE = "#FFFFFF"


class Sums(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame.save_state()

        # Camera set
        points = [
            Point(location=[0, 0, 0]),
            Point(location=[0, 1, 0]),
            Point(location=[6, 1, 0])
        ]

        # Introduction text
        txt = [
            Tex(r"Démonstration I", font_size=72, color=BLACK),
            Tex(r"Nicomaque de Gérase (vers 100)", font_size=48, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        txt_formula = Tex(r"$1 + 3 + \cdots + (2n - 1) = n^2$", font_size=48, color=BLACK)\
            .next_to(txt, 2 * DOWN)

        self.play(
            Write(txt),
            Write(txt_formula)
        )
        self.wait(1)
        self.play(
            Uncreate(txt),
            Uncreate(txt_formula)
        )
        self.wait(1)
        

        self.wait(1)
