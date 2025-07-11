"""
Visual proof of the Pythagorean theorem.
Proofs without Words I. Roger B. Nelsen. p. 3.
"""
import numpy as np

from manim import MovingCameraScene, Mobject
from manim import Brace, Line, Polygon
from manim import RoundedRectangle, Square
from manim import Create, Rotate, Transform, Uncreate, Write
from manim import FadeIn, FadeOut, FadeTransform, TransformFromCopy
from manim import FunctionGraph, VGroup
from manim import Text, Tex

from manim import config

from manim import LEFT, RIGHT, UP, DOWN, PI, DR, DL, UR, UL, LIGHT

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

        txt_copy = Text(
            r"@chill.maths", font_size=12,
            font="CMU Typewriter Text", weight=LIGHT, color=BLACK
        ).to_edge(RIGHT + DOWN, buff=0.1)
        self.add(txt_copy)

        # Introduction text
        txt_title = [
            Tex(r"Théorème de", font_size=48, color=BLACK),
            Tex(r"Pythagore", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt_dem = Tex(r"Démonstration I", font_size=48, color=BLACK)\
            .next_to(txt_title, DOWN, buff=0.7)

        txt_desc = [
            Tex(r"adapté de \textit{Zhoubi Suanjing", font_size=28, color=BLACK),
            Tex(r"(auteur inconnu, 200 av. J.C.$?$)", font_size=28, color=BLACK)
        ]
        txt_desc = VGroup(*txt_desc).arrange(DOWN)\
            .next_to(txt_dem, DOWN, buff=0.5)

        self.play(
            Write(txt_title), Write(txt_dem), Write(txt_desc),
            run_time=3
        )
        self.wait(3)
        self.play(Uncreate(txt_title), Uncreate(txt_dem), Uncreate(txt_desc))
        self.wait(1)
        
        # First triangle and text
        triangle_b = Polygon(
            [-1, -0.75, 0], [1, -0.75, 0], [1, 0.75, 0],
            stroke_width=2,
            color=BLACK, fill_color=BLUE, fill_opacity=1
        )
        txt_a = Tex(r"$a$", font_size=36, color=BLACK)\
            .next_to(triangle_b, DOWN)
        txt_b = Tex(r"$b$", font_size=36, color=BLACK)\
            .next_to(triangle_b, RIGHT)
        txt_c = Tex(r"$c$", font_size=36, color=BLACK)\
            .next_to(triangle_b.get_center(), UP + LEFT)

        self.play(
            Create(triangle_b),
            Write(txt_a),
            Write(txt_b),
            Write(txt_c)
        )

        # Second triangle
        triangle_r = triangle_b.copy()
        txt_a_r = Tex(r"$a$", font_size=36, color=BLACK)\
            .next_to(triangle_r, UP)
        txt_b_r = Tex(r"$b$", font_size=36, color=BLACK)\
            .next_to(triangle_r, LEFT)

        self.play(
            FadeOut(txt_c),
            RotateAndColor(triangle_r, PI, RED),
            Write(txt_a_r),
            Write(txt_b_r)
        )
        self.wait(0.5)

        # Expand squares
        line_a = Line(
            [-1, 0.75, 0], [1, 0.75, 0],
            stroke_width=2, stroke_color=BLACK
        )
        square_a  = Square(side_length=2, stroke_width=2, stroke_color=BLACK)
        square_a.next_to(triangle_r, 0.1 * UP)
        txt_a2  = Tex(r"$a^2$", font_size=48, color=BLACK)\
            .move_to(square_a.get_center_of_mass())

        self.play(
            FadeOut(txt_a_r),
            txt_a.animate.next_to(triangle_b, DOWN, buff=-0.25),
            FadeTransform(line_a, square_a, stretch=True),
            Write(txt_a2),
            run_time=1.5
        )

        self.play(
            triangle_b.animate.move_to(triangle_b.get_center() + LEFT / 2),
            triangle_r.animate.move_to(triangle_r.get_center() + LEFT / 2),
            txt_a.animate.move_to(txt_a.get_center_of_mass() + LEFT / 2),
            txt_b_r.animate.move_to(txt_b_r.get_center_of_mass() + LEFT / 2),
            square_a.animate.move_to(square_a.get_center_of_mass() + LEFT / 2),
            txt_a2.animate.move_to(txt_a2.get_center_of_mass() + LEFT / 2),
            FadeOut(txt_b),
        )

        line_b = Line(
            [0.5, -0.75, 0], [0.5, 0.75, 0],
            stroke_width=2, stroke_color=BLACK
        )
        square_b = Square(side_length=1.5, stroke_width=2, color=BLACK)
        square_b.next_to(triangle_r, 0.1 * RIGHT)
        txt_b2  = Tex(r"$b^2$", font_size=48, color=BLACK)\
            .move_to(square_b.get_center_of_mass())
        self.play(
            txt_b_r.animate.next_to(triangle_r, LEFT, buff=-0.25),
            FadeTransform(line_b, square_b, stretch=True),
            Write(txt_b2),
            run_time=1.5
        )
        self.wait(0.5)

        # Complete the square
        triangle_y = triangle_r.copy()
        triangle_v = triangle_b.copy()

        self.play(
            RotateAndColor(triangle_v, -PI / 2, VIOLET),
            RotateAndColor(triangle_y, -PI / 2, YELLOW)
        )
        self.play(
            triangle_v.animate.next_to(square_b, 0.1 * UP),
            triangle_y.animate.next_to(square_b, 0.1 * UP),
            run_time=1.5
        )

        # Create a group for everything
        big_square = VGroup(
            triangle_b, triangle_r, triangle_y, triangle_v,
            square_a, square_b,
            txt_a2, txt_b2, txt_a, txt_b_r
        )
        self.play(
            big_square.animate.scale(0.8)
        )

        # Create braces
        brace_r = Brace(big_square, direction=[-1, 0, 0], color=BLACK)
        brace_t = Brace(big_square, direction=[0, 1, 0], color=BLACK)
        txt_ab_r = Tex(r"$a + b$", font_size=48, color=BLACK)\
            .rotate(PI / 2)\
            .next_to(brace_r, 0.2 * LEFT)
        txt_ab_t = Tex(r"$a + b$", font_size=48, color=BLACK)\
            .next_to(brace_t, 0.2 * UP)

        self.play(
            Create(brace_r),
            Create(brace_t),
            Write(txt_ab_r),
            Write(txt_ab_t),
            run_time=1.5
        )

        # Create text
        txt_area = Tex(r"Aire: $(a + b)^2$", font_size=52, color=BLACK)\
            .next_to(big_square, 1.5 * DOWN)

        self.play(
            Create(txt_area)
        )
        self.wait(1)

        # Delete objects and move square
        square_brace = VGroup(big_square, brace_t, txt_ab_t)
        self.play(
            Uncreate(txt_area),
            Uncreate(brace_r),
            Uncreate(txt_ab_r),
            square_brace.animate.move_to([0, 2, 0])
        )

        # Create second square
        square_ab = Square(
            side_length=3.5, stroke_width=2, color=BLACK, fill_color=WHITE
        ).scale(0.8)
        square_ab.next_to(big_square, DOWN)
        brace_tt = Brace(square_ab, direction=[0, -1, 0], color=BLACK)
        txt_ab_tt = txt_ab_t.copy().next_to(brace_tt, 0.2 * DOWN)

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

        txt_c2  = Tex(r"$c^2$", font_size=48, color=BLACK)\
            .move_to(square_ab.get_center_of_mass())
        self.play(
            Write(txt_c2)
        )

        # Finish the animation
        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        )
        txt = Tex(
            r"$a^2$", r"$~+~$", r"$b^2$", r"$~=~$", r"$c^2$",
            font_size=52, color=BLACK
        )

        rect.z_index = 0
        txt.z_index = 1
        self.play(
            Create(rect),
            run_time=0.1
        )
        self.play(
            TransformFromCopy(txt_a2[0], txt[0]),
            Write(txt[1]),
            TransformFromCopy(txt_b2[0], txt[2]),
            Write(txt[3]),
            TransformFromCopy(txt_c2[0], txt[4])
        )

        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Proofs without words:", font_size=30, color=BLACK),
            Tex(r"Exercises in visual thinking", font_size=30, color=BLACK),
            Tex(r"Roger B. Nelsen (1993), p. 3", font_size=30, color=BLACK)
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

        