"""
Visual proof of the Pythagorean theorem.
Proofs without Words I. Roger B. Nelsen. p. 4.
"""
import numpy as np

from manim import MovingCameraScene, Mobject
from manim import BraceBetweenPoints, Point, Square, Polygon, Line, Circle, Dot
from manim import Create, Rotate, Transform, Uncreate, Write
from manim import ReplacementTransform, TransformFromCopy
from manim import FadeOut, FadeTransform
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

        position_list = [
            [0, 0, 0],  
            [1, 0, 0],  
            [1, 1, 0], 
            [0, 1, 0], 
        ]
        square = Polygon(*position_list, color=BLUE)

        self.play(
            Create(square)
        )

        new_position_list = [
            [0, 0, 0],  
            [1, 0, 0],  
            [3, 1, 0], 
            [2, 1, 0], 
        ]
        parallelogram = Polygon(*new_position_list, color=RED)

        self.play(
            Transform(square, parallelogram)
        )

        self.wait(1)
