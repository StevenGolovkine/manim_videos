"""
Visual proof of the Pythagorean theorem.
Proofs without Words I. Roger B. Nelsen. p. 3.
"""
from manim import MovingCameraScene, Mobject
from manim import BraceBetweenPoints, Point, Square, Line, Polygon
from manim import Create, Rotate, Transform, Uncreate, Write
from manim import FadeOut, FadeTransform, TransformFromCopy
from manim import VGroup
from manim import Tex

from manim import LEFT, RIGHT, UP, DOWN, PI, DR, DL, UR, UL


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
            Point(location=[2, 2, 0]),
            Point(location=[5.5, 2, 0]),
            Point(location=[5.5, 1, 0])
        ]

        # Introduction text
        txt = [
            Tex(r"Démonstration I", font_size=72, color=BLACK),
            Tex(r"adapté de \textit{Zhoubi Suanjing} (auteur inconnu, 200 av. J.C.$?$)", font_size=48, color=BLACK)
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

        # Second triangle
        triangle_r = triangle_b.copy()
        txt_a_r = Tex(r"$a$", font_size=48, color=BLACK)\
            .next_to(triangle_r, UP)
        txt_b_r = Tex(r"$b$", font_size=48, color=BLACK)\
            .next_to(triangle_r, LEFT)

        self.play(
            FadeOut(txt_c),
            RotateAndColor(triangle_r, PI, RED),
            Write(txt_a_r),
            Write(txt_b_r)
        )

        # Expand squares
        line_a = Line([-2, 1.5, 0], [2, 1.5, 0])
        square_a  = Square(side_length=4, stroke_width=4, stroke_color=BLACK)
        square_a.next_to(triangle_r, 0.1 * UP)
        txt_a2  = Tex(r"$a^2$", font_size=72, color=BLACK)\
            .move_to(square_a.get_center_of_mass())

        self.play(
            self.camera.frame.animate.move_to(points[0]).set(width=18),
            FadeOut(txt_a_r),
            FadeTransform(line_a, square_a, stretch=True),
            Write(txt_a2)
        )

        line_b = Line([2, -1.5, 0], [2, 1.5, 0])
        square_b = Square(side_length=3, stroke_width=4, color=BLACK)
        square_b.next_to(triangle_r, 0.1 * RIGHT)
        txt_b2  = Tex(r"$b^2$", font_size=72, color=BLACK)\
            .move_to(square_b.get_center_of_mass())
        self.play(
            FadeOut(txt_b),
            FadeTransform(line_b, square_b, stretch=True),
            Write(txt_b2)
        )

        # Complete the square
        triangle_y = triangle_r.copy()
        triangle_v = triangle_b.copy()

        self.play(
            RotateAndColor(triangle_v, -PI / 2, VIOLET),
            RotateAndColor(triangle_y, -PI / 2, YELLOW)
        )
        self.play(
            triangle_v.animate.next_to(square_b, 0.1 * UP),
            triangle_y.animate.next_to(square_b, 0.1 * UP)
        )

        # Create braces
        brace_r = BraceBetweenPoints(
            [-2.5, -1.5, 0], [-2.5, 5.5, 0], direction=[-1, 0, 0], color=BLACK
        )
        brace_t = BraceBetweenPoints(
            [-2, 5.6, 0], [5, 5.6, 0], direction=[0, 1, 0], color=BLACK
        )
        txt_ab_r = Tex(r"$a + b$", font_size=48, color=BLACK)\
            .next_to(brace_r, LEFT)
        txt_ab_t = Tex(r"$a + b$", font_size=48, color=BLACK)\
            .next_to(brace_t, UP)

        self.play(
            Create(brace_r),
            Create(brace_t),
            Write(txt_ab_r),
            Write(txt_ab_t)
        )

        # Create text
        txt_area = Tex(r"Aire", font_size=72, color=BLACK)
        txt_area_f = Tex(r"$(a + b)^2$", font_size=72, color=BLACK)
        txt_area = VGroup(txt_area, txt_area_f)\
            .arrange(DOWN)\
            .move_to([8, 2, 0])

        self.play(
            Create(txt_area)
        )

        # Delete objects
        self.play(
            self.camera.frame.animate.move_to(points[1]).set(width=18),
            Uncreate(txt_area),
            Uncreate(brace_r),
            Uncreate(txt_ab_r)
        )

        # Create second square
        square_ab = Square(
            side_length=7, stroke_width=4, color=BLACK, fill_color=WHITE
        )
        square_ab.move_to([10, 2, 0])
        brace_tt = BraceBetweenPoints(
            [6.5, 5.6, 0], [13.5, 5.6, 0], direction=[0, 1, 0], color=BLACK
        )
        txt_ab_tt = txt_ab_t.copy().next_to(brace_tt, UP)

        self.play(
            Create(square_ab),
            Create(brace_tt),
            Write(txt_ab_tt)
        )

        # Move the triangles
        triangle_br = triangle_b.copy()
        self.play(
            triangle_br.animate.move_to(square_ab, DR),
            run_time=0.5
        )

        triangle_rr = triangle_r.copy()
        self.play(
            triangle_rr.animate.move_to(square_ab, UL),
            run_time=0.5
        )
        
        triangle_yr = triangle_y.copy()
        self.play(
            triangle_yr.animate.move_to(square_ab, UR),
            run_time=0.5
        )
        
        triangle_vr = triangle_v.copy()
        self.play(
            triangle_vr.animate.move_to(square_ab, DL),
            run_time=0.5
        )

        txt_c2  = Tex(r"$c^2$", font_size=72, color=BLACK)\
            .move_to(square_ab.get_center_of_mass())
        self.play(
            Write(txt_c2)
        )

        # Finish the animation
        self.play(
            self.camera.frame.animate.move_to(points[2]).set(width=24)
        )

        txt = Tex(
            r"$a^2$", r"$~+~$", r"$b^2$", r"$~=~$", r"$c^2$",
            font_size=96, color=BLACK
        ).move_to([5.5, -3, 0])

        self.play(
            TransformFromCopy(txt_a2[0], txt[0]),
            Write(txt[1]),
            TransformFromCopy(txt_b2[0], txt[2]),
            Write(txt[3]),
            TransformFromCopy(txt_c2[0], txt[4])
        )

        self.wait(1)
