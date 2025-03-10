"""
Visual proof of Every Fourth Power Greater than One is the Sum of Two Non-consecutive
Triangular Numbers.
Proofs without Words III. Roger B. Nelsen. p. 137.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, Group
from manim import Brace, VGroup, FadeIn, FadeOut, FunctionGraph
from manim import Text, Tex, Square, RoundedRectangle

from manim import config
from manim import LEFT, RIGHT, DOWN, LIGHT, UP

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


class FourthPower(MovingCameraScene):
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
            Tex(r"Les puissances 4", font_size=48, color=BLACK),
            Tex(r"sont la somme de", font_size=48, color=BLACK),
            Tex(r"triangulaires", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
        ]
        txt = VGroup(*txt).arrange(DOWN)

        results = [
            Tex(r"Si $T_k = 1 + 2 + \cdots + k$,", font_size=24, color=BLACK),
            Tex(r"alors $n^4 = T_{n^2 + n - 1} + T_{n^2 - n - 1}$", font_size=24, color=BLACK),
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

        # Create the table
        squares = VGroup()
        squares.add(Square(side_length=0.15, color=BLACK, stroke_width=1))
        for idx in range(3):
            new_square = Square(side_length=0.15, color=BLACK, stroke_width=1).\
                next_to(squares[idx], direction=RIGHT, buff=0)
            squares.add(new_square)
        for idx in range(12):
            new_square = Square(side_length=0.15, color=BLACK, stroke_width=1).\
                next_to(squares[idx], direction=DOWN, buff=0)
            squares.add(new_square)

        big_squares = VGroup()
        big_squares.add(squares)
        for idx in range(3):
            new_square = squares.copy().\
                next_to(big_squares[idx], direction=RIGHT, buff=0.1)
            big_squares.add(new_square)
        for idx in range(12):
            new_square = squares.copy().\
                next_to(big_squares[idx], direction=DOWN, buff=0.1)
            big_squares.add(new_square)
        big_squares.move_to([0, 0, 0])
        self.play(
            Create(big_squares)
        )

        brace = Brace(big_squares, direction=[0, 1, 0], sharpness=1, color=BLACK)
        txt_n = Tex(r"$n^2$", font_size=30, color=BLACK).next_to(brace, 0.5 * UP)
        
        self.play(
            Create(brace),
            Write(txt_n)
        )

        upper = [0, 1, 2, 4, 5, 8]
        lower = [7, 10, 11, 13, 14, 15]
        diag = [3, 6, 9, 12]

        upper_group = VGroup(
            big_squares[0],
            big_squares[1],
            big_squares[4],
            *[big_squares[2][i] for i in upper],
            *[big_squares[5][i] for i in upper],
            *[big_squares[8][i] for i in upper],
        )
        diag_group = VGroup(
            *[big_squares[2][i] for i in diag],
            *[big_squares[5][i] for i in diag],
            *[big_squares[8][i] for i in diag],
        )
        lower_group = VGroup(
            big_squares[3],
            big_squares[6],
            big_squares[7],
            big_squares[9:16],
            *[big_squares[2][i] for i in lower],
            *[big_squares[5][i] for i in lower],
            *[big_squares[8][i] for i in lower],
        )
        self.play(
            # Upper
            upper_group.animate.set_fill(RED, 1),
            # Diagonal
            diag_group.animate.set_fill(BLUE, 1),
            # Lower
            lower_group.animate.set_fill(GREEN, 1)
        )

        self.play(
            FadeOut(brace),
            FadeOut(txt_n),
            upper_group.animate.move_to([0, 1.5, 0]),
            diag_group.animate.move_to([-0.5, 0, 0]),
            lower_group.animate.move_to([0, -1, 0])
        )

        # Transform diag into small triangle
        self.play(
            diag_group[1].animate.next_to(diag_group[0], DOWN, buff=0),
            diag_group[10].animate.next_to(diag_group[11], UP, buff=0),
            run_time=0.1
        )
        self.play(
            diag_group[2].animate.next_to(diag_group[1], DOWN, buff=0),
            diag_group[9].animate.next_to(diag_group[10], UP, buff=0),
            run_time=0.1
        )
        self.play(
            diag_group[3].animate.next_to(diag_group[1], LEFT, buff=0),
            diag_group[8].animate.next_to(diag_group[10], LEFT, buff=0),
            run_time=0.1
        )
        self.play(
            diag_group[4].animate.next_to(diag_group[2], LEFT, buff=0),
            diag_group[7].animate.next_to(diag_group[11], LEFT, buff=0),
            run_time=0.1
        )
        self.play(
            diag_group[5].animate.next_to(diag_group[4], LEFT, buff=0),
            diag_group[6].animate.next_to(diag_group[7], LEFT, buff=0),
            run_time=0.1
        )

        little_tri_up = VGroup(
            *[diag_group[i] for i in range(6)]
        )
        little_tri_down = VGroup(
            *[diag_group[i] for i in range(6, 12)]
        )
        self.play(
            little_tri_up.animate.\
                next_to(lower_group, UP, buff=0.1).\
                align_to(lower_group, RIGHT),
            little_tri_down.animate.\
                next_to(lower_group, LEFT + 0.01 * DOWN, buff=0.1).\
                align_to(lower_group, DOWN)
        )

        new_lower_group = VGroup(
            lower_group, little_tri_up, little_tri_down
        )

        brace_up = Brace(upper_group, direction=[0, 1, 0], sharpness=1, color=BLACK)
        txt_up = Tex(r"$n^2 - n - 1$", font_size=30, color=BLACK).\
            next_to(brace_up, 0.5 * UP)
        
        brace_low = Brace(
            new_lower_group, direction=[0, -1, 0], sharpness=1, color=BLACK
        )
        txt_low = Tex(r"$n^2 + n - 1$", font_size=30, color=BLACK).\
            next_to(brace_low, 0.5 * DOWN)
        

        self.play(
            Create(brace_up),
            Write(txt_up),
            Create(brace_low),
            Write(txt_low)
        )

        self.wait(1)

        # Write equation
        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, 0, 0])
        txt = Tex(
            r"$n^4 = T_{n^2 + n - 1} + T_{n^2 - n - 1}$",
            font_size=28, color=BLACK
        ).move_to([0, 0, 0])

        self.play(
            Create(rect),
            Write(txt)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Proofs without words III:", font_size=30, color=BLACK),
            Tex(r"Further exercises in", font_size=30, color=BLACK),
            Tex(r"visual thinking", font_size=30, color=BLACK),
            Tex(r"Roger B. Nelsen (2015), p. 137", font_size=30, color=BLACK)
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