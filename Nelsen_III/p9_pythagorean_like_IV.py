"""
Visual proof of the Pythagorean-like theorem IV.
Proofs without Words III. Roger B. Nelsen. p. 9.
"""
import numpy as np

from manim import DEGREES, MovingCameraScene, Mobject
from manim import Brace, DashedLine, Line, Polygon
from manim import RoundedRectangle, Square
from manim import Create, Rotate, Transform, Uncreate, Write
from manim import FadeIn, FadeOut, Angle
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
            Tex(r"Un théorème", font_size=48, color=BLACK),
            Tex(r"Pythagore-like", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration IV", font_size=36, color=BLACK),
            Tex(r"Larry Hoehn", font_size=28, color=BLACK),
        ]
        txt = VGroup(*txt).arrange(DOWN)

        self.add(
            txt_title,
            txt,
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt),
            run_time=0.5
        )
        self.wait(0.5)

        # Create an isosceles triangle
        A = [-1.5, 0, 0]
        B = [1.5, 0, 0]
        C = [0, 2, 0]
        D = [-0.5, 0, 0]
        triangle = Polygon(
            A, B, C,
            color=BLACK, fill_color=WHITE, fill_opacity=1, stroke_width=2
        )
        line = Line(D, C, color=BLACK, stroke_width=2)

        txt_a = Tex(r"$a$", font_size=24, color=BLACK).move_to([-0.2, 0.5, 0])
        txt_b = Tex(r"$b$", font_size=24, color=BLACK).move_to([-1, 0.2, 0])
        txt_c = Tex(r"$c$", font_size=24, color=BLACK).move_to([-1, 1, 0])
        txt_c2 = Tex(r"$c$", font_size=24, color=BLACK).move_to([1, 1, 0])
        txt_d = Tex(r"$d$", font_size=24, color=BLACK).move_to([0.5, 0.2, 0])
        self.play(
            Create(triangle),
            Create(line),
            Write(txt_a),
            Write(txt_b),
            Write(txt_c),
            Write(txt_c2),
            Write(txt_d),
        )

        self.wait(0.5)

        # Create the square on the left side of the triangle
        side_c_left = np.array(C) - np.array(A)
        side_c_left_normal = np.array([-side_c_left[1], side_c_left[0], 0])
        square_c_left = Polygon(
            A,
            C,
            np.array(C) + side_c_left_normal,
            np.array(A) + side_c_left_normal,
            color=BLACK,
            fill_color=GREEN,
            fill_opacity=1,
            stroke_width=2,
        )
        txt_c_square = Tex(r"$c^2$", font_size=24, color=BLACK)\
            .move_to(square_c_left.get_center_of_mass())

        self.play(
            Create(square_c_left),
            Write(txt_c_square),
        )

        self.wait(0.5)

        # Create the square on the left side of CD.
        side_a = np.array(C) - np.array(D)
        side_a_left_normal = np.array([-side_a[1], side_a[0], 0])
        square_a_left = Polygon(
            D,
            C,
            np.array(C) + side_a_left_normal,
            np.array(D) + side_a_left_normal,
            color=BLACK,
            fill_color=BLUE,
            fill_opacity=0.65,
            stroke_width=2,
        )
        txt_a_square = Tex(r"$a^2$", font_size=24, color=BLACK)\
            .move_to(square_a_left.get_center_of_mass())

        self.play(
            Create(square_a_left),
            Write(txt_a_square),
        )

        # Create line H
        H = [0, 0, 0]
        line_H = DashedLine(H, C, color=BLACK, stroke_width=2)
        txt_H = Tex(r"$h$", font_size=24, color=BLACK).\
            next_to(line_H, RIGHT, buff=0.1)
        txt_x = Tex(r"$x$", font_size=24, color=BLACK).move_to([0.75, -0.2, 0])
        txt_y = Tex(r"$y$", font_size=24, color=BLACK).move_to([-0.25, -0.2, 0])

        txt_relations = VGroup(
            Tex(r"$x + y = d$", font_size=24, color=BLACK),
            Tex(r"$x - y = b$", font_size=24, color=BLACK),
        ).arrange(DOWN, buff=0.1).move_to([0, -2.2, 0])

        self.play(
            Create(line_H),
            Write(txt_H),
            Write(txt_x),
            Write(txt_y),
            Write(txt_relations),
        )

        self.wait(0.5)

        side_h = np.array(C) - np.array(H)
        side_h_right_normal = np.array([side_h[1], -side_h[0], 0])
        square_h_right = Polygon(
            H,
            C,
            np.array(C) + side_h_right_normal,
            np.array(H) + side_h_right_normal,
            color=BLACK,
            fill_color=YELLOW,
            fill_opacity=0.65,
            stroke_width=0,
        )
        square_h_right_outline = VGroup(
            Line(C, np.array(C) + side_h_right_normal, color=BLACK, stroke_width=2),
            Line(
                np.array(C) + side_h_right_normal,
                np.array(H) + side_h_right_normal,
                color=BLACK,
                stroke_width=2,
            ),
            Line(np.array(H) + side_h_right_normal, H, color=BLACK, stroke_width=2),
        )
        txt_h_square = Tex(r"$h^2$", font_size=24, color=BLACK)\
            .move_to(square_h_right.get_center_of_mass())

        side_x = np.array(H) - np.array(A)
        side_x_down_normal = np.array([side_x[1], -side_x[0], 0])
        square_x_below = Polygon(
            H,
            A,
            np.array(A) + side_x_down_normal,
            np.array(H) + side_x_down_normal,
            color=BLACK,
            fill_color=ORANGE,
            fill_opacity=0.65,
            stroke_width=2,
        )
        txt_x_square = Tex(r"$x^2$", font_size=24, color=BLACK)\
            .move_to(square_x_below.get_center_of_mass())

        self.play(
            Create(square_h_right),
            Create(square_h_right_outline),
            Write(txt_h_square),
            Create(square_x_below),
            Write(txt_x_square),
        )

        self.wait(0.5)

        y_length = np.linalg.norm(np.array(H) - np.array(D))
        square_y_cutout = Square(
            side_length=y_length,
            color=BLACK,
            fill_color=WHITE,
            fill_opacity=1,
            stroke_width=2,
        ).move_to(
            (np.array(H) + np.array(D)) / 2 + [0, -y_length / 2, 0]
        )
        txt_y_square = Tex(r"$y^2$", font_size=18, color=BLACK)\
            .move_to(square_y_cutout.get_center())
        txt_x_minus_y_square = Tex(r"$x^2-y^2$", font_size=24, color=BLACK)\
            .move_to(square_x_below.get_center())
        txt_difference_formula = Tex(
            r"$x^2-y^2=bd$", font_size=28, color=BLACK
        ).move_to([0, -3.0, 0])

        self.play(
            FadeOut(txt_x_square),
            Create(square_y_cutout),
            Write(txt_y_square),
            Write(txt_x_minus_y_square),
            Write(txt_difference_formula),
        )

        self.wait(0.5)

        x_length = np.linalg.norm(side_x)
        b_length = x_length - y_length
        d_length = x_length + y_length
        split_line = Line(
            np.array(D) + [0, -y_length, 0],
            np.array(A) + side_x_down_normal,
            color=BLACK,
            stroke_width=2,
        )
        x_minus_y_upper_piece = Polygon(
            A,
            D,
            np.array(D) + [0, -y_length, 0],
            np.array(A) + side_x_down_normal,
            color=BLACK,
            fill_color=ORANGE,
            fill_opacity=0.65,
            stroke_width=2,
        )
        x_minus_y_lower_piece = Polygon(
            np.array(D) + [0, -y_length, 0],
            np.array(H) + [0, -y_length, 0],
            np.array(H) + side_x_down_normal,
            np.array(A) + side_x_down_normal,
            color=BLACK,
            fill_color=ORANGE,
            fill_opacity=0.65,
            stroke_width=2,
        )
        diagonal_label = Tex(r"$x^2-y^2$", font_size=24, color=BLACK)\
            .move_to(square_x_below.get_center())

        self.play(
            Create(split_line),
            Transform(txt_x_minus_y_square, diagonal_label),
        )
        self.play(
            FadeOut(square_x_below),
            FadeOut(square_y_cutout),
            FadeOut(txt_y_square),
            FadeOut(txt_x_minus_y_square),
            FadeOut(split_line),
            FadeIn(x_minus_y_upper_piece),
            FadeIn(x_minus_y_lower_piece),
        )

        self.wait(0.5)

        self.play(
            Rotate(
                x_minus_y_upper_piece,
                PI,
                axis=UP,
                about_point=x_minus_y_upper_piece.get_center(),
            ),
            run_time=1,
        )
        self.play(
            Rotate(
                x_minus_y_upper_piece,
                PI / 2,
                about_point=x_minus_y_upper_piece.get_center(),
            ),
            run_time=1,
        )

        line_DB = Line(D, B, color=BLACK, stroke_width=2)
        x_minus_y_upper_piece_target = x_minus_y_upper_piece.copy()
        x_minus_y_lower_piece_target = x_minus_y_lower_piece.copy()

        x_minus_y_upper_piece_target.next_to(
            line_DB,
            direction=DOWN,
            aligned_edge=LEFT,
            buff=0,
        )
        x_minus_y_lower_piece_target.next_to(
            line_DB,
            direction=DOWN,
            aligned_edge=RIGHT,
            buff=0,
        )
        bd_target = VGroup(
            x_minus_y_upper_piece_target,
            x_minus_y_lower_piece_target,
        )
        txt_bd = Tex(r"$bd$", font_size=24, color=BLACK)\
            .move_to(bd_target.get_center() - [0.5, 0, 0])

        self.play(
            Transform(x_minus_y_upper_piece, x_minus_y_upper_piece_target),
            Transform(x_minus_y_lower_piece, x_minus_y_lower_piece_target),
            Write(txt_bd),
            run_time=1,
        )

        txt_final_formula = Tex(
            r"$c^2=a^2+bd$", font_size=32, color=BLACK
        ).move_to([0, -1.5, 0])
        self.play(
            Write(txt_final_formula),
            Uncreate(txt_relations),
            Uncreate(txt_difference_formula),
        )

        

        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"The Changing Shape of", font_size=30, color=BLACK),
            Tex(r"Geometry, MAA,", font_size=30, color=BLACK),
            Tex(r"2003, pp.228-231.", font_size=30, color=BLACK),
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

        
