"""
Visual proof of Geometric Series II.
Proofs without Words I. Roger B. Nelsen. p. 120.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import Brace, VGroup, FadeIn, FadeOut, FunctionGraph, Line
from manim import Text, Tex, Rectangle, Transform, Polygon

from manim import line_intersection

from manim import config
from manim import LEFT, RIGHT, DOWN, LIGHT, UP, PI

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


class Series(MovingCameraScene):
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
            Tex(r"Une série", font_size=48, color=BLACK),
            Tex(r"géométrique", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"B. G. Klein et I. C. Bivens", font_size=28, color=BLACK),
        ]
        txt = VGroup(*txt).arrange(DOWN)

        results = [
            Tex(r"$\sum_{k=1}^{\infty} r^{k-1} = \frac{1}{1-r}$",
            font_size=18, color=BLACK),
        ]
        results = VGroup(*results).arrange(DOWN).move_to([0, -1, 0])


        self.add(
            txt_title,
            txt,
            results
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt),
            Uncreate(results),
            run_time=0.5
        )
        self.wait(0.5)


        # Create a square of size 1
        square = Rectangle(
            height=2.5, width=2.5,
            stroke_width=2,
            color=BLUE,
            fill_color=BLUE, fill_opacity=1
        ).move_to([0, 2, 0])
        txt_square = Tex(r"$1$", font_size=25, color=BLACK).\
            next_to(square, UP, buff=0.1)
        txt_square_2 = Tex(r"$1$", font_size=25, color=BLACK).\
            next_to(square, LEFT, buff=0.1)

        self.play(
            Create(square),
            Write(txt_square),
            Write(txt_square_2)
        )

        # Name the edges of the squares S, P, Q
        txt_S = Tex(r"$S$", font_size=25, color=BLACK).\
            next_to(square, UP + LEFT, buff=0)
        txt_P = Tex(r"$P$", font_size=25, color=BLACK).\
            next_to(square, UP + RIGHT, buff=0)
        txt_Q = Tex(r"$Q$", font_size=25, color=BLACK).\
            next_to(square, DOWN + RIGHT, buff=0)
        self.play(
            Write(txt_S),
            Write(txt_P),
            Write(txt_Q)
        )

        # Create a triangle TSP
        triangle = Polygon(
            square.get_corner(UP + LEFT),
            square.get_corner(UP + RIGHT),
            [square.get_corner(UP + LEFT)[0], -2, 0],
            stroke_width=2,
            color=RED,
            fill_color=RED, fill_opacity=0.5
        )
        txt_T = Tex(r"$T$", font_size=25, color=BLACK).\
            next_to(triangle, DOWN + LEFT, buff=0)

        self.play(
            Create(triangle),
            Write(txt_T)
        )

        # Note R the intersection of the side of the square and the line PT
        line_PT = [
            square.get_corner(UP + RIGHT),
            [square.get_corner(UP + LEFT)[0], -2, 0],
        ]
        line_side = [
            square.get_corner(DOWN + RIGHT),
            square.get_corner(DOWN + LEFT),
        ]
        intersection = line_intersection(line_side, line_PT)
        txt_R = Tex(r"$R$", font_size=25, color=BLACK).\
            next_to(intersection, DOWN + RIGHT, buff=0.)
        txt_r = Tex(r"$r$", font_size=25, color=BLACK).\
            move_to(txt_R.get_center() - [0.7, 0, 0])
        txt_1r = Tex(r"$1 - r$", font_size=25, color=BLACK).\
            move_to(txt_R.get_center() + [0.6, 0, 0])
        self.play(
            Write(txt_R),
            Write(txt_r),
            Write(txt_1r)
        )

        # Add line for r^2
        line_temp = Line(
            [square.get_corner(DOWN + LEFT)[0], -0.5, 0],
            [square.get_corner(DOWN + RIGHT)[0], -0.5, 0],
            stroke_width=2,
            color=GREEN
        )
        line_r2 = Line(
            [square.get_corner(DOWN + LEFT)[0], -0.5, 0],
            line_intersection(
                line_PT,
                [line_temp.get_start(), line_temp.get_end()]
            ),
            stroke_width=2,
            color=BLACK
        )
        txt_r = Tex(r"$r$", font_size=25, color=BLACK).\
            move_to([square.get_corner(DOWN + LEFT)[0] - 0.1, 0.1, 0])
        txt_r2 = Tex(r"$r^2$", font_size=25, color=BLACK).\
            next_to(line_r2, DOWN, buff=0.1)
        self.play(
            Create(line_r2),
            Write(txt_r),
            Write(txt_r2)
        )

        # Add line for r^3
        line_temp = Line(
            [square.get_corner(DOWN + LEFT)[0], -1.2, 0],
            [square.get_corner(DOWN + RIGHT)[0], -1.2, 0],
            stroke_width=2,
            color=GREEN
        )
        line_r3 = Line(
            [square.get_corner(DOWN + LEFT)[0], -1.2, 0],
            line_intersection(
                line_PT,
                [line_temp.get_start(), line_temp.get_end()]
            ),
            stroke_width=2,
            color=BLACK
        )
        txt_r2_1 = Tex(r"$r^2$", font_size=25, color=BLACK).\
            move_to([square.get_corner(DOWN + LEFT)[0] - 0.2, -0.8, 0])
        self.play(
            Create(line_r3),
            Write(txt_r2_1)
        )

        # Add dots
        txt_dots = Tex(r"\vdots", font_size=25, color=BLACK).\
            next_to(txt_r2_1, DOWN, buff=0.5)
        self.play(Write(txt_dots))

        # Write triangle PQR and triangle TQR are similar
        txt_similar = Tex(
            r"$\triangle PQR \sim \triangle TQR$",
            font_size=25, color=BLACK
        ).move_to([0.5, -1, 0])
        self.play(Write(txt_similar))

        txt_donc = Tex(r"$\Downarrow$", font_size=25, color=BLACK).\
            next_to(txt_similar, DOWN, buff=0.2)
        self.play(Write(txt_donc))

        # Final formula
        txt_formula3 = Tex(r"$\frac{1 + r + r^2 + \cdots}{1} = \frac{1}{1-r}$",
            font_size=30, color=BLACK).next_to(txt_donc, DOWN, buff=0.5)

        self.play(
            Write(txt_formula3)
        )

        self.wait(1)
        txt_formula4 = Tex(r"$\displaystyle\sum_{k=1}^{\infty} r^{k-1} = \frac{1}{1-r}$",
            font_size=30, color=BLACK).next_to(txt_donc, DOWN, buff=0.5)
        self.play(
            Transform(txt_formula3, txt_formula4)
        )


        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine,", font_size=30, color=BLACK),
            Tex(r"vol. 61, no. 4,", font_size=30, color=BLACK),
            Tex(r"(Oct. 1988), p. 219.", font_size=30, color=BLACK)
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