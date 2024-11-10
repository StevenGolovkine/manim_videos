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

        # Camera set
        points = [
            Point(location=[0, 2.5, 0]),
            Point(location=[6, 2.5, 0]),
            Point(location=[6, 1, 0])
        ]

        # Introduction text
        txt = [
            Tex(r"Démonstration III", font_size=72, color=BLACK),
            Tex(r"basée sur une preuve d'Euclide (vers 300 av. J.C.)", font_size=48, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        self.play(Write(txt))
        self.wait(1)
        self.play(Uncreate(txt))
        self.wait(1)
        
        # First triangle and text
        triangle_b = Polygon(
            [-2, -1.5, 0], [2, -1.5, 0], [2, 1.5, 0],
            color=BLACK, fill_color=BLUE, fill_opacity=1
        )
        txt_a = Tex(r"$a$", font_size=48, color=BLACK)\
            .next_to(triangle_b, DOWN)
        txt_b = Tex(r"$b$", font_size=48, color=BLACK)\
            .next_to(triangle_b, RIGHT)
        txt_c = Tex(r"$c$", font_size=48, color=BLACK)\
            .next_to(triangle_b.get_center(), UP + LEFT)

        self.play(
            Create(triangle_b),
            Write(txt_a),
            Write(txt_b),
            Write(txt_c)
        )

        # Remove txt and rotate the triangle
        self.play(
            Uncreate(txt_a),
            Uncreate(txt_b),
            Uncreate(txt_c),
            Rotate(triangle_b, 143 * DEGREES, about_point=[0, 0, 0]),
        )

        # Expand the squares
        line_c = Line([-2.5, 0, 0], [2.5, 0, 0])
        square_c  = Square(side_length=5, stroke_width=4, stroke_color=BLACK)
        square_c.next_to(triangle_b, 0.1 * DOWN)
        txt_c2  = Tex(r"$c^2$", font_size=72, color=BLACK)\
            .move_to(square_c.get_center_of_mass())
        
        self.play(
            #self.camera.frame.animate.move_to(points[0]).set(width=18),
            #FadeOut(txt_a_r),
            FadeTransform(line_c, square_c, stretch=True),
            Write(txt_c2)
        )
        
        c = Circle(radius=0.1).move_to(
            [-4.3 + 1.9 - (3 * np.sqrt(2) / 2), (3 * np.sqrt(2) / 2) - 0.05, 0]
        )
        line_a = Line(triangle_b.get_anchors()[3], triangle_b.get_anchors()[1])
        square_a  = Square(side_length=3, stroke_width=4, stroke_color=BLACK)\
            .next_to([-4.3 + 1.9 - (3 * np.sqrt(2) / 2), (3 * np.sqrt(2) / 2) - 0.05, 0])\
            .rotate(np.arcsin(0.8))
        txt_a2  = Tex(r"$a^2$", font_size=72, color=BLACK)\
            .move_to(square_a.get_center_of_mass())

        self.play(
            Create(c),
            #self.camera.frame.animate.move_to(points[0]).set(width=18),
            #FadeOut(txt_a_r),
            Transform(line_a, square_a),
            Write(txt_a2)
        )

        # # Create the square
        # self.play(
        #     self.camera.frame.animate.move_to(points[0])
        # )

        # triangle_r = triangle_b.copy()
        # self.play(
        #     RotateAndColor(triangle_r, PI / 2, RED)
        # )
        # self.play(
        #     triangle_r.animate.move_to(triangle_b, RIGHT + DOWN)
        # )

        # triangle_l = triangle_b.copy()
        # self.play(
        #     RotateAndColor(triangle_l, -PI / 2, RED)
        # )
        # self.play(
        #     triangle_l.animate.move_to(triangle_b, LEFT + DOWN)
        # )

        # triangle_u = triangle_b.copy()
        # self.play(
        #     Rotate(triangle_u, PI)
        # )
        # self.play(
        #     triangle_u.animate.move_to(triangle_l, LEFT + UP)
        # )

        # txt_c = Tex(r"$c$", font_size=48, color=BLACK)\
        #     .next_to(triangle_u, UP)
        # txt_c2 = Tex(r"$c$", font_size=48, color=BLACK)\
        #     .next_to(triangle_l, LEFT)
        # self.play(
        #     Write(txt_c),
        #     Write(txt_c2)
        # )

        # # Area
        # txt_aire = Tex(r"Aire", font_size=96, color=BLACK)\
        #     .move_to([-5, 2.5, 0])
        # brace_l = BraceBetweenPoints(
        #     [-3, -0.5, 0], [-3, 5.5, 0],
        #     direction=[-1, 0, 0], color=BLACK
        # )
        # brace_r = BraceBetweenPoints(
        #     [3, -0.5, 0], [3, 5.5, 0],
        #     direction=[1, 0, 0], color=BLACK
        # )
        # self.play(
        #     Write(txt_aire),
        #     Create(brace_l),
        #     Create(brace_r)
        # )

        # # Areas equality
        # txt_eq = Tex(r"$=$", font_size=96, color=BLACK)\
        #     .move_to([4.5, 2.5, 0])
        # txt_aire = Tex(r"Aire", font_size=96, color=BLACK)\
        #     .move_to([6, 2.5, 0])
        # brace_l = BraceBetweenPoints(
        #     [8, -0.5, 0], [8, 5.5, 0],
        #     direction=[-1, 0, 0], color=BLACK
        # )
        # brace_r = BraceBetweenPoints(
        #     [17, -0.5, 0], [17, 5.5, 0],
        #     direction=[1, 0, 0], color=BLACK
        # )

        # self.play(
        #     self.camera.frame.animate.move_to(points[1]).set(width=26)
        # )
        # self.play(
        #     Write(txt_eq),
        #     Write(txt_aire),
        #     Create(brace_l),
        #     Create(brace_r)
        # )


        # triangle_r2 = triangle_r.copy()
        # triangle_l2 = triangle_l.copy()
        # self.play(
        #     triangle_r2.animate.move_to([8.5, 2.5, 0]),
        #     triangle_l2.animate.move_to([8.5 + 12 / 5, 2.5, 0]),
        #     run_time=0.5
        # )
        # triangle_g = VGroup(triangle_l2, triangle_r2)
        # self.play(
        #     Rotate(triangle_g, 37 * DEGREES),
        #     run_time=0.5
        # )
        # txt_a = Tex(r"$a$", font_size=48, color=BLACK)\
        #     .next_to(triangle_g, DOWN)
        # txt_b = Tex(r"$b$", font_size=48, color=BLACK)\
        #     .next_to(triangle_g, RIGHT)
        # self.play(
        #     Write(txt_a),
        #     Write(txt_b),
        #     run_time=0.1
        # )


        # triangle_u2 = triangle_u.copy()
        # triangle_b2 = triangle_b.copy()
        # self.play(
        #     triangle_u2.animate.move_to([14.5, 2.5, 0]),
        #     triangle_b2.animate.move_to([14.5, 2.5 + 12 / 5, 0]),
        #     run_time=0.5
        # )
        # triangle_g = VGroup(triangle_u2, triangle_b2)
        # self.play(
        #     Rotate(triangle_g, 37 * DEGREES),
        #     run_time=0.5
        # )
        # txt_a2 = Tex(r"$a$", font_size=48, color=BLACK)\
        #     .next_to(triangle_g, LEFT)
        # txt_b2 = Tex(r"$b$", font_size=48, color=BLACK)\
        #     .next_to(triangle_g, UP)
        # self.play(
        #     Write(txt_a2),
        #     Write(txt_b2),
        #     run_time=0.1
        # )


        # square_ab  = Square(side_length=1, stroke_width=4, stroke_color=BLACK)\
        #     .rotate(PI / 4, about_point=[0, 0, 0])\
        #     .move_to([0, 2.5, 0])
        # self.play(
        #     square_ab.animate.move_to([14.5, 0.5, 0]),
        #     run_time=0.5
        # )
        # self.play(
        #     Rotate(square_ab, -PI / 4),
        #     run_time=0.25
        # )
        # txt_ab = Tex(r"$b - a$", font_size=48, color=BLACK)\
        #     .next_to(square_ab, RIGHT)
        # txt_ab2 = Tex(r"$b - a$", font_size=48, color=BLACK)\
        #     .next_to(square_ab, UP)
        # self.play(
        #     Write(txt_ab),
        #     Write(txt_ab2),
        #     run_time=0.1
        # )

        # # Write equation
        # self.play(
        #     self.camera.frame.animate.move_to(points[2]).set(width=26)
        # )

        # txt = Tex(
        #     r"$c$", r"$~\times~$", r"$c$", r"$~=~$",
        #     r"$a$", r"$~\times~$", r"$b$",
        #     r"$~+~$",
        #     r"$a$", r"$~\times~$", r"$b$",
        #     r"$~+~$",
        #     r"$(b - a)$", r"$~\times~$", r"$(b - a)$",
        #     font_size=96, color=BLACK
        # ).move_to([6.5, -3, 0])

        # self.play(
        #     TransformFromCopy(txt_c2[0], txt[0]),
        #     Write(txt[1]),
        #     TransformFromCopy(txt_c[0], txt[2]),
        #     TransformFromCopy(txt_eq[0], txt[3]),
        #     TransformFromCopy(txt_a[0], txt[4]),
        #     Write(txt[5]),
        #     TransformFromCopy(txt_b[0], txt[6]),
        #     Write(txt[7]),
        #     TransformFromCopy(txt_a2[0], txt[8]),
        #     Write(txt[9]),
        #     TransformFromCopy(txt_b2[0], txt[10]),
        #     Write(txt[11]),
        #     TransformFromCopy(txt_ab2[0], txt[12]),
        #     Write(txt[13]),
        #     TransformFromCopy(txt_ab[0], txt[14])
        # )

        # txt2 = Tex(
        #     r"$c^2$", r"$~=~$", r"$2ab$", r"$~+~$", r"$(b - a)^2$",
        #     font_size=96, color=BLACK
        # ).move_to([6.5, -3, 0])
        # self.play(
        #     ReplacementTransform(txt, txt2)
        # )

        # txt3 = Tex(
        #     r"$c^2$", r"$~=~$", r"$2ab$", r"$~+~$", r"$b^2 - 2ab + a^2$",
        #     font_size=96, color=BLACK
        # ).move_to([6.5, -3, 0])
        # self.play(
        #     ReplacementTransform(txt2, txt3)
        # )

        # txt4 = Tex(
        #     r"$c^2$", r"$~=~$", r"$a^2$", r"$~+~$", r"$b^2$",
        #     font_size=96, color=BLACK
        # ).move_to([6.5, -3, 0])
        # self.play(
        #     ReplacementTransform(txt3, txt4)
        # )
        self.wait(1)
