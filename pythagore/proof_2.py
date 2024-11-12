"""
Visual proof of the Pythagorean theorem.
Proofs without Words I. Roger B. Nelsen. p. 4.
"""
from manim import MovingCameraScene, Mobject
from manim import Point, Square, Polygon
from manim import Create, Rotate, Transform, Uncreate, Write
from manim import TransformFromCopy
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
            Point(location=[4.5, 2.5, 0]),
            Point(location=[4.5, 1.5, 0])
        ]

        # Introduction text
        txt = [
            Tex(r"Démonstration II", font_size=72, color=BLACK),
            Tex(r"de Bhāskara (12e siècle)", font_size=48, color=BLACK)
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

        # Create the square
        self.play(
            self.camera.frame.animate.move_to(points[0])
        )

        triangle_r = triangle_b.copy()
        self.play(
            RotateAndColor(triangle_r, PI / 2, RED)
        )
        self.play(
            triangle_r.animate.move_to(triangle_b, RIGHT + DOWN)
        )

        triangle_l = triangle_b.copy()
        self.play(
            RotateAndColor(triangle_l, -PI / 2, RED)
        )
        self.play(
            triangle_l.animate.move_to(triangle_b, LEFT + DOWN)
        )

        triangle_u = triangle_b.copy()
        self.play(
            Rotate(triangle_u, PI)
        )
        self.play(
            triangle_u.animate.move_to(triangle_l, LEFT + UP)
        )

        txt_c = Tex(r"$c$", font_size=48, color=BLACK)\
            .next_to(triangle_u, UP)
        txt_c2 = Tex(r"$c$", font_size=48, color=BLACK)\
            .next_to(triangle_l, LEFT)
        self.play(
            Write(txt_c),
            Write(txt_c2)
        )
        self.play(
            self.camera.frame.animate.move_to(points[1]).set(width=18)
        )

        triangle_r2 = triangle_r.copy()
        triangle_l2 = triangle_l.copy()
        self.play(
            triangle_r2.animate.move_to([9, 2.5, 0]),
            triangle_l2.animate.move_to([9 + 12 / 5, 2.5, 0]),
            run_time=0.5
        )
        triangle_g1 = VGroup(triangle_l2, triangle_r2)
        self.play(
            Rotate(triangle_g1, 37 * DEGREES),
            run_time=0.5
        )
        self.play(
            triangle_g1.animate.move_to([10, 2.5, 0]),
            run_time=0.5
        )
        txt_a = Tex(r"$a$", font_size=48, color=BLACK)\
            .next_to(triangle_g1, DOWN)
        txt_b = Tex(r"$b$", font_size=48, color=BLACK)\
            .next_to(triangle_g1, RIGHT)
        self.play(
            Write(txt_a),
            Write(txt_b),
            run_time=0.1
        )


        triangle_u2 = triangle_u.copy()
        triangle_b2 = triangle_b.copy()
        self.play(
            triangle_u2.animate.move_to([6.5, 2.5, 0]),
            triangle_b2.animate.move_to([6.5, 2.5 + 12 / 5, 0]),
            run_time=0.5
        )
        triangle_g2 = VGroup(triangle_u2, triangle_b2)
        self.play(
            Rotate(triangle_g2, 37 * DEGREES),
            run_time=0.5
        )
        self.play(
            triangle_g2.animate.move_to([6.5, 2, 0]),
            run_time=0.5
        )
        txt_a2 = Tex(r"$a$", font_size=48, color=BLACK)\
            .next_to(triangle_g2, LEFT)
        txt_b2 = Tex(r"$b$", font_size=48, color=BLACK)\
            .next_to(triangle_g2, DOWN)
        self.play(
            Write(txt_a2),
            Write(txt_b2),
            run_time=0.1
        )

        square_ab  = Square(side_length=1, stroke_width=4, stroke_color=BLACK)\
            .rotate(PI / 4, about_point=[0, 0, 0])\
            .move_to([0, 2.5, 0])
        self.play(
            square_ab.animate.move_to([8, 4, 0]),
            run_time=0.5
        )
        self.play(
            Rotate(square_ab, -PI / 4),
            run_time=0.25
        )
        txt_ab = Tex(r"$b - a$", font_size=48, color=BLACK)\
            .next_to(square_ab, LEFT)
        txt_ab2 = Tex(r"$b - a$", font_size=48, color=BLACK)\
            .next_to(square_ab, UP)
        self.play(
            Write(txt_ab),
            Write(txt_ab2),
            run_time=0.1
        )

        # Areas
        square_c2 = Square(
            side_length=5, stroke_width=4, stroke_color=BLACK,
            fill_color=WHITE, fill_opacity=0.8
        ).move_to([0, 2.5, 0])
        txt_c2 = Tex(r"$c^2$", font_size=96, color=BLACK)\
            .move_to(square_c2.get_center_of_mass())
        self.play(
            Create(square_c2),
            Write(txt_c2)
        )
        
        square_a2 = Square(
            side_length=3, stroke_width=4, stroke_color=BLACK,
            fill_color=WHITE, fill_opacity=0.8
        ).move_to([6, 2, 0])
        txt_a2 = Tex(r"$a^2$", font_size=96, color=BLACK)\
            .move_to(square_a2.get_center_of_mass())
        self.play(
            Create(square_a2),
            Write(txt_a2)
        )

        square_b2 = Square(
            side_length=4, stroke_width=4, stroke_color=BLACK,
            fill_color=WHITE, fill_opacity=0.8
        ).move_to([9.5, 2.5, 0])
        txt_b2 = Tex(r"$b^2$", font_size=96, color=BLACK)\
            .move_to(square_b2.get_center_of_mass())
        self.play(
            Create(square_b2),
            Write(txt_b2)
        )

        # Finish the animation
        self.play(
            self.camera.frame.animate.move_to(points[2])
        )

        txt = Tex(
            r"$c^2$", r"$~=~$", r"$a^2$", r"$~+~$", r"$b^2$",
            font_size=96, color=BLACK
        ).move_to([4.5, -2, 0])

        self.play(
            TransformFromCopy(txt_c2[0], txt[0]),
            Write(txt[1]),
            TransformFromCopy(txt_a2[0], txt[2]),
            Write(txt[3]),
            TransformFromCopy(txt_b2[0], txt[4])
        )
        
        self.wait(1)
