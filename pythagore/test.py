"""
Visual proof of the Pythagorean theorem.
Proofs without Words I. Roger B. Nelsen. p. 4.
"""
import numpy as np

from manim import MovingCameraScene, Mobject
from manim import BraceBetweenPoints, Point, Square, Polygon, Line, Circle
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
        
        # First triangle and text
        triangle_b = Polygon(
            [-2, -1.5, 0], [2, -1.5, 0], [2, 1.5, 0],
            color=BLACK, fill_color=BLUE, fill_opacity=1
        )
        self.play(
            Create(triangle_b)
        )

        self.play(
            Rotate(triangle_b, 143 * DEGREES, about_point=[0, 0, 0]),
        )

        vertices = triangle_b.get_vertices()
        coords_vertices = []
        for i in range(len(vertices)):
            if i < len(vertices)-1:
                p1, p2 = [vertices[i],vertices[i+1]]
            else:
                p1, p2 = [vertices[-1],vertices[0]]
            guide_line = Line(p1, p2)
            coords_vertices.append(guide_line)

        self.play(
            Create(coords_vertices[0]),
            Create(coords_vertices[1]),
            Create(coords_vertices[2])
        )

        sq = Square(side_length=3, stroke_color=BLACK)\
            .rotate(PI / 2 - np.arcsin(0.6))\
            .move_to(coords_vertices[1], DOWN + RIGHT)
        self.play(
            FadeTransform(coords_vertices[1], sq, stretch=True)
        )

        sq = Square(side_length=4, stroke_color=BLACK)\
            .rotate(np.arcsin(0.8))\
            .move_to(coords_vertices[0], DOWN + LEFT)
        self.play(
            FadeTransform(coords_vertices[0], sq, stretch=True)
        )

        sq = Square(side_length=5, stroke_color=BLACK)\
            .move_to(coords_vertices[2], UP)

        self.play(
            FadeTransform(coords_vertices[2], sq, stretch=True)
        )

        # # Expand the squares
        # line_c = Line([-2.5, 0, 0], [2.5, 0, 0])
        # square_c  = Square(side_length=5, stroke_width=4, stroke_color=BLACK)
        # square_c.next_to(triangle_b, 0.1 * DOWN)
        # txt_c2  = Tex(r"$c^2$", font_size=72, color=BLACK)\
        #     .move_to(square_c.get_center_of_mass())
        
        # self.play(
        #     FadeTransform(line_c, square_c, stretch=True),
        #     Write(txt_c2)
        # )
        
        # c = Circle(radius=0.1).move_to(
        #     [-4.3 + 1.9 - (3 * np.sqrt(2) / 2), (3 * np.sqrt(2) / 2) - 0.05, 0]
        # )
        # line_a = Line(triangle_b.get_anchors()[3], triangle_b.get_anchors()[1])
        # square_a  = Square(side_length=3, stroke_width=4, stroke_color=BLACK)\
        #     .next_to([-4.3 + 1.9 - (3 * np.sqrt(2) / 2), (3 * np.sqrt(2) / 2) - 0.05, 0])\
        #     .rotate(np.arcsin(0.8))
        # txt_a2  = Tex(r"$a^2$", font_size=72, color=BLACK)\
        #     .move_to(square_a.get_center_of_mass())

        # self.play(
        #     Create(c),
        #     #self.camera.frame.animate.move_to(points[0]).set(width=18),
        #     #FadeOut(txt_a_r),
        #     FadeTransform(line_a, square_a, stretch=True),
        #     Write(txt_a2)
        # )
