"""
Visual proof of an alternating series II.
Proofs without Words III. Roger B. Nelsen. p. 160.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Dot, RoundedRectangle, Polygon, Square
from manim import Create, Uncreate, Write
from manim import VGroup, Transform, FadeIn, FadeOut, FunctionGraph, BraceBetweenPoints
from manim import Text, Tex

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

class Proof(MovingCameraScene):
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
            Tex(r"alternée", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Roger B. Nelsen", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        txt_formula = Tex(
            r"$1 - \frac{1}{2} + \frac{1}{4} - \frac{1}{8} + \cdots = \frac{2}{3}$",
            font_size=28, color=BLACK
        ).next_to(txt, 2 * DOWN)
        self.add(
            txt_title,
            txt,
            txt_formula
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt),
            Uncreate(txt_formula),
            run_time=0.5
        )
        self.wait(0.5)

        # Create L shaped figure with 3 big squares of 8x8 small squares
        square_size = 0.2
        big_squares = []
        for big in range(3):
            small_squares = []
            for i in range(8):
                for j in range(8):
                    sq = Square(
                        side_length=square_size, stroke_width=1,
                        color=RED, stroke_color=BLACK, fill_opacity=1
                    )
                    sq.move_to([j * square_size, i * square_size, 0])
                    small_squares.append(sq)
            big_sq = VGroup(*small_squares)
            big_squares.append(big_sq)

        # Position them in L shape
        big_squares[0]  # Bottom left
        big_squares[1].next_to(big_squares[0], UP, buff=0)  # Above
        big_squares[2].next_to(big_squares[0], RIGHT, buff=0)  # Right

        l_figure = VGroup(*big_squares).move_to([0, -0.5, 0])

        txt_1 = Tex(r"$1$", font_size=24, color=BLACK).move_to([0, 2.5, 0])
        self.play(
            Create(l_figure),
            Write(txt_1)
        )

        # Color some parts of the figure to show the series terms 1/2
        l_figure_2 = l_figure.copy()
        l_figure_2[0][0:64].set_fill(GREEN, opacity=1)
        for i in range(4):
            for j in range(4, 8):
                l_figure_2[1][i * 8 + j].set_fill(GREEN, opacity=1)
        for i in range(4, 8):
            for j in range(4):
                l_figure_2[2][i * 8 + j].set_fill(GREEN, opacity=1)
            

        txt_12 = Tex(
            r"$1 - \frac{1}{2}$", font_size=24, color=BLACK
        ).move_to([0, 2.5, 0])
        self.play(
            Transform(txt_1, txt_12),
            Transform(l_figure, l_figure_2)
        )

        # Color some parts of the figure to show the series terms 1/4
        l_figure_3 = l_figure_2.copy()
        for i in range(4, 8):
            for j in range(4):
                l_figure_3[2][i * 8 + j].set_fill(RED, opacity=1)
        for i in range(4):
            for j in range(4, 8):
                l_figure_3[1][i * 8 + j].set_fill(RED, opacity=1)
        for i in range(4, 8):
            for j in range(4, 8):
                l_figure_3[0][i * 8 + j].set_fill(RED, opacity=1)
        

        txt_124 = Tex(
            r"$1 - \frac{1}{2} + \frac{1}{4}$", font_size=24, color=BLACK
        ).move_to([0, 2.5, 0])
        self.play(
            Transform(txt_1, txt_124),
            Transform(l_figure, l_figure_3)
        )
        
        # Color some parts of the figure to show the series terms 1/8
        l_figure_4 = l_figure_3.copy()
        for i in range(4, 8):
            for j in range(4, 8):
                l_figure_4[0][i * 8 + j].set_fill(GREEN, opacity=1)
        for i in range(2):
            for j in range(6, 8):
                l_figure_4[1][i * 8 + j].set_fill(GREEN, opacity=1)
        for i in range(6, 8):
            for j in range(2):
                l_figure_4[2][i * 8 + j].set_fill(GREEN, opacity=1)

        txt_1248 = Tex(
            r"$1 - \frac{1}{2} + \frac{1}{4} - \frac{1}{8}$", font_size=24, color=BLACK
        ).move_to([0, 2.5, 0])
        self.play(
            Transform(txt_1, txt_1248),
            Transform(l_figure, l_figure_4)
        )

        # Color some parts of the figure to show the series terms 1/16
        l_figure_5 = l_figure_4.copy()
        for i in range(6, 8):
            for j in range(2):
                l_figure_5[2][i * 8 + j].set_fill(RED, opacity=1)
        for i in range(2):
            for j in range(6, 8):
                l_figure_5[1][i * 8 + j].set_fill(RED, opacity=1)
        for i in range(6, 8):
            for j in range(6, 8):
                l_figure_5[0][i * 8 + j].set_fill(RED, opacity=1)

        txt_124816 = Tex(
            r"$1 - \frac{1}{2} + \frac{1}{4} - \frac{1}{8} + \frac{1}{16}$",
            font_size=24, color=BLACK
        ).move_to([0, 2.5, 0])
        self.play(
            Transform(txt_1, txt_124816),
            Transform(l_figure, l_figure_5)
        )

        # Finish the figure and write the limit
        l_figure_6 = l_figure_5.copy()
        for i in range(6, 8):
            for j in range(6, 8):
                l_figure_6[0][i * 8 + j].set_fill(GREEN, opacity=1)

        txt_end = Tex(
            r"$1 - \frac{1}{2} + \frac{1}{4} - \frac{1}{8} + \cdots = \frac{2}{3}$",
            font_size=28, color=BLACK
        ).move_to([0, 2.5, 0])
        self.play(
            Transform(txt_1, txt_end),
            Transform(l_figure, l_figure_6)
        )


        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        
        # Logo
        ref = [
            Tex(r"College Mathematics Journal,", font_size=30, color=BLACK),
            Tex(r"vol. 43, no. 5, (Nov. 2012)", font_size=30, color=BLACK),
            Tex(r"p.370.", font_size=30, color=BLACK),
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
