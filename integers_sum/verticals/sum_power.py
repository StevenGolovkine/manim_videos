"""
Visual proof of 1 + 2r +3r^2 + ... = (1 / (1 - r))^2.
Proofs without Words I. Roger B. Nelsen. p. 125.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import Brace, VGroup, FadeIn, FadeOut, FunctionGraph, Rotate
from manim import Text, Tex, Rectangle, RoundedRectangle, Transform

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


class Sums(MovingCameraScene):
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
            Tex(r"Sur la somme des", font_size=48, color=BLACK),
            Tex(r"puissances", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Roger B. Nelsen", font_size=28, color=BLACK),
        ]
        txt = VGroup(*txt).arrange(DOWN)

        results = [
            Tex(r"$\sum_{k = 1}^\infty k \times r^{k - 1} = \frac{1}{(1 - r)^2}$",
            font_size=20, color=BLACK),
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

        # Rectangle
        rect = Rectangle(
            width=3, height=3, color=BLACK, fill_color=WHITE, fill_opacity=1,
            stroke_width=2
        )
        txt_1 = Tex(
            r"$\frac{1}{1 - r}$", font_size=20, color=BLACK
        ).next_to(rect, DOWN, buff=0.1)

        self.play(
            Create(rect),
            Write(txt_1),
            run_time=1
        )


        # Aire 1
        inside_rect1 = Rectangle(
            width=1.5, height=1.5, color=BLACK, fill_color=BLUE, fill_opacity=0.5,
            stroke_width=0.1
        ).align_to(rect, DOWN + LEFT)
        txt_inside1 = Tex(
            r"$1$", font_size=15, color=BLACK
        ).move_to(inside_rect1.get_center_of_mass())
        txt_outside1 = Tex(
            r"$1$", font_size=15, color=BLACK
        ).next_to(inside_rect1, LEFT, buff=0.1)

        self.play(
            Create(inside_rect1),
            Write(txt_inside1),
            Write(txt_outside1)
        )

        # Aires r
        inside_rect2 = Rectangle(
            width=1.5, height=0.75, color=BLACK, fill_color=RED, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect1, RIGHT, buff=0).align_to(inside_rect1, DOWN)
        txt_inside2 = Tex(
            r"$r$", font_size=15, color=BLACK
        ).move_to(inside_rect2.get_center_of_mass())
        self.play(
            Create(inside_rect2),
            Write(txt_inside2),
        )

        inside_rect3 = Rectangle(
            width=0.75, height=1.5, color=BLACK, fill_color=RED, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect1, UP, buff=0).align_to(inside_rect1, LEFT)
        txt_inside3 = Tex(
            r"$r$", font_size=15, color=BLACK
        ).move_to(inside_rect3.get_center_of_mass())
        txt_outside3 = Tex(
            r"$\frac{r}{1 - r}$", font_size=15, color=BLACK
        ).next_to(inside_rect3, LEFT, buff=0.1)
        self.play(
            Create(inside_rect3),
            Write(txt_inside3),
            Write(txt_outside3)
        )

        # Aires r^2
        inside_rect4 = Rectangle(
            width=0.75, height=0.75, color=BLACK, fill_color=BLUE, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect2, UP, buff=0).align_to(inside_rect2, LEFT)
        txt_inside4 = Tex(
            r"$r^2$", font_size=15, color=BLACK
        ).move_to(inside_rect4.get_center_of_mass())
        self.play(
            Create(inside_rect4),
            Write(txt_inside4),
        )

        inside_rect5 = Rectangle(
            width=0.75, height=0.75, color=BLACK, fill_color=BLUE, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect3, RIGHT, buff=0).align_to(inside_rect3, DOWN)
        txt_inside5 = Tex(
            r"$r^2$", font_size=15, color=BLACK
        ).move_to(inside_rect5.get_center_of_mass())
        txt_outside5 = Tex(
            r"$r$", font_size=15, color=BLACK
        ).next_to(inside_rect5, LEFT, buff=0.1)
        self.play(
            Create(inside_rect5),
            Write(txt_inside5),
            Write(txt_outside5)
        )

        inside_rect6 = Rectangle(
            width=0.75, height=0.75, color=BLACK, fill_color=BLUE, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect1, RIGHT + UP, buff=0)
        txt_inside6 = Tex(
            r"$r^2$", font_size=15, color=BLACK
        ).move_to(inside_rect6.get_center_of_mass())
        self.play(
            Create(inside_rect6),
            Write(txt_inside6)
        )

        # Aire r^3
        inside_rect7 = Rectangle(
            width=0.75, height=0.25, color=BLACK, fill_color=RED, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect4, RIGHT, buff=0).align_to(inside_rect4, DOWN)
        txt_inside7 = Tex(
            r"$r^3$", font_size=15, color=BLACK
        ).move_to(inside_rect7.get_center_of_mass())
        self.play(
            Create(inside_rect7),
            Write(txt_inside7)
        )

        inside_rect8 = Rectangle(
            width=0.75, height=0.25, color=BLACK, fill_color=RED, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect7, UP, buff=0).align_to(inside_rect7, LEFT)
        txt_inside8 = Tex(
            r"$r^3$", font_size=15, color=BLACK
        ).move_to(inside_rect8.get_center_of_mass())
        self.play(
            Create(inside_rect8),
            Write(txt_inside8)
        )

        inside_rect9 = Rectangle(
            width=0.25, height=0.75, color=BLACK, fill_color=RED, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect5, UP, buff=0).align_to(inside_rect5, LEFT)
        txt_inside9 = Tex(
            r"$r^3$", font_size=15, color=BLACK
        ).move_to(inside_rect9.get_center_of_mass())
        txt_outside9 = Tex(
            r"$\frac{r^2}{1 - r}$", font_size=15, color=BLACK
        ).next_to(inside_rect9, LEFT, buff=0.1)
        self.play(
            Create(inside_rect9),
            Write(txt_inside9),
            Write(txt_outside9)
        )

        inside_rect10 = Rectangle(
            width=0.25, height=0.75, color=BLACK, fill_color=RED, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect9, RIGHT, buff=0).align_to(inside_rect9, DOWN)
        txt_inside10 = Tex(
            r"$r^3$", font_size=15, color=BLACK
        ).move_to(inside_rect10.get_center_of_mass())
        self.play(
            Create(inside_rect10),
            Write(txt_inside10)
        )

        # Aire r^4
        inside_rect11 = Rectangle(
            width=0.5, height=0.5, color=BLACK, fill_color=BLUE, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect8, UP, buff=0).align_to(inside_rect8, LEFT)
        txt_inside11 = Tex(
            r"$r^4$", font_size=15, color=BLACK
        ).move_to(inside_rect11.get_center_of_mass())
        self.play(
            Create(inside_rect11),
            Write(txt_inside11)
        )

        inside_rect12 = Rectangle(
            width=0.5, height=0.5, color=BLACK, fill_color=BLUE, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect11, UP, buff=0).align_to(inside_rect11, LEFT)
        txt_inside12 = Tex(
            r"$r^4$", font_size=15, color=BLACK
        ).move_to(inside_rect12.get_center_of_mass())
        self.play(
            Create(inside_rect12),
            Write(txt_inside12)
        )

        inside_rect_13 = Rectangle(
            width=0.5, height=0.5, color=BLACK, fill_color=BLUE, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect10, RIGHT, buff=0).align_to(inside_rect10, DOWN)
        txt_inside13 = Tex(
            r"$r^4$", font_size=15, color=BLACK
        ).move_to(inside_rect_13.get_center_of_mass())
        self.play(
            Create(inside_rect_13),
            Write(txt_inside13)
        )

        inside_rect_14 = Rectangle(
            width=0.5, height=0.5, color=BLACK, fill_color=BLUE, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect_13, RIGHT, buff=0).align_to(inside_rect_13, DOWN)
        txt_inside14 = Tex(
            r"$r^4$", font_size=15, color=BLACK
        ).move_to(inside_rect_14.get_center_of_mass())
        self.play(
            Create(inside_rect_14),
            Write(txt_inside14)
        )

        inside_rect15 = Rectangle(
            width=0.5, height=0.5, color=BLACK, fill_color=BLUE, fill_opacity=0.5,
            stroke_width=0.1
        ).next_to(inside_rect_14, RIGHT, buff=0).align_to(inside_rect_14, DOWN)
        txt_inside15 = Tex(
            r"$r^4$", font_size=15, color=BLACK
        ).move_to(inside_rect15.get_center_of_mass())
        self.play(
            Create(inside_rect15),
            Write(txt_inside15)
        )

        # Dots
        inside_rect_dots = Rectangle(
            width=0.24, height=0.24, color=BLACK, fill_color=WHITE, fill_opacity=1,
            stroke_width=0
        ).next_to(inside_rect15, RIGHT + UP, buff=0)
        txt_inside_dots = Tex(
            r"$\mathstrut^{.^{.^{.}}}$", font_size=15, color=BLACK
        ).move_to(inside_rect_dots.get_center_of_mass())
        self.play(
            Create(inside_rect_dots),
            Write(txt_inside_dots)
        )


        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Proofs without words,", font_size=30, color=BLACK),
            Tex(r"Roger B. Nelsen (1993)", font_size=30, color=BLACK),
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
