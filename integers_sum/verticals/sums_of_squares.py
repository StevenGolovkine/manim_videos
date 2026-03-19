"""
Visual proof of the sums of squares.
Proofs without Words II. Roger B. Nelsen. p. 88.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import VGroup, FadeIn, FadeOut, FunctionGraph, Transform
from manim import MathTable, Brace, RoundedRectangle
from manim import Text, Tex

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
            Tex(r"Somme des carrés", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
        ]
        txt = VGroup(*txt).arrange(DOWN)

        results = [
            Tex(r"$k^2 = 1 + 3 + \dots + (2k-1)$", font_size=24, color=BLACK),
            Tex(r"$\Downarrow$", font_size=24, color=BLACK),
            Tex(r"$\sum_{k = 1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$", font_size=24, color=BLACK),
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

        # First table
        table = MathTable(
            [
                ["1", "", "", "", "", "", ""],
                ["1", "3", "", "", "", "", ""],
                ["1", "3", "5", "", "", "", ""],
                ["\cdot", "\cdot", "\cdot", "\cdot", "", "", ""],
                ["\cdot", "\cdot", "\cdot", "\cdot", "\cdot", "", ""],
                ["1", "3", "\cdot", "\cdot", "\cdot", "2n-3", ""],
                ["1", "3", "\cdot", "\cdot", "\cdot", "2n-3", "2n-1"],
            ],
            h_buff=0.5, v_buff=0.4
        ).scale(0.4)
        table.get_horizontal_lines().set_color(WHITE)
        table.get_vertical_lines().set_color(WHITE)
        table.get_entries().set_color(BLACK)

        self.play(
            Create(table),
        )
        self.wait(1)
        table_c = table.copy()
        table_c.scale(0.5).move_to([-1.5, 3, 0])
        self.play(
            Transform(table, table_c),
        )

        # Second table
        table2 = MathTable(
            [
                ["1", "", "", "", "", "", ""],
                ["3", "1", "", "", "", "", ""],
                ["5", "3", "1", "", "", "", ""],
                ["\cdot", "\cdot", "\cdot", "\cdot", "", "", ""],
                ["\cdot", "\cdot", "\cdot", "\cdot", "\cdot", "", ""],
                ["2n-3", "2n-5", "\cdot", "\cdot", "\cdot", "1", ""],
                ["2n-1", "2n-3", "\cdot", "\cdot", "\cdot", "2", "1"],
            ],
            h_buff=0.5, v_buff=0.4
        ).scale(0.4)
        table2.get_horizontal_lines().set_color(WHITE)
        table2.get_vertical_lines().set_color(WHITE)
        table2.get_entries().set_color(BLACK)

        self.play(
            Create(table2),
        )
        self.wait(1)
        table2_c = table2.copy()
        table2_c.scale(0.5).move_to([0, 3, 0])
        self.play(
            Transform(table2, table2_c),
        )

        # Third table
        table3 = MathTable(
            [
                ["2n-1", "", "", "", "", "", ""],
                ["2n-3", "2n-3", "", "", "", "", ""],
                ["2n-5", "2n-5", "2n-5", "", "", "", ""],
                ["\cdot", "\cdot", "\cdot", "\cdot", "", "", ""],
                ["\cdot", "\cdot", "\cdot", "\cdot", "\cdot", "", ""],
                ["3", "3", "\cdot", "\cdot", "\cdot", "3", ""],
                ["1", "1", "\cdot", "\cdot", "\cdot", "1", "1"],
            ],
            h_buff=0.5, v_buff=0.4
        ).scale(0.4)
        table3.get_horizontal_lines().set_color(WHITE)
        table3.get_vertical_lines().set_color(WHITE)
        table3.get_entries().set_color(BLACK)

        self.play(
            Create(table3),
        )
        self.wait(1)
        table3_c = table3.copy()
        table3_c.scale(0.5).move_to([1.5, 3, 0])
        self.play(
            Transform(table3, table3_c),
        )

        # Plus signs and equal sign
        plus_1 = Tex(r"$+$", font_size=18, color=BLACK).move_to([-0.85, 3, 0])
        plus_2 = Tex(r"$+$", font_size=18, color=BLACK).move_to([0.6, 3, 0])
        equal = Tex(r"$=$", font_size=36, color=BLACK).move_to([0, 1.5, 0])

        self.play(
            Create(plus_1),
            Create(plus_2),
            Create(equal)
        )

        # Fourth table
        table4 = MathTable(
            [
                ["2n + 1", "", "", "", "", "", ""],
                ["2n + 1", "2n + 1", "", "", "", "", ""],
                ["2n + 1", "2n + 1", "2n + 1", "", "", "", ""],
                ["\cdot", "\cdot", "\cdot", "\cdot", "", "", ""],
                ["\cdot", "\cdot", "\cdot", "\cdot", "\cdot", "", ""],
                ["2n + 1", "2n + 1", "\cdot", "\cdot", "\cdot", "2n + 1", ""],
                ["2n + 1", "2n + 1", "\cdot", "\cdot", "\cdot", "2n + 1", "2n + 1"],
            ],
            h_buff=0.5, v_buff=0.4
        ).scale(0.4)
        table4.get_horizontal_lines().set_color(WHITE)
        table4.get_vertical_lines().set_color(WHITE)
        table4.get_entries().set_color(BLACK)
        self.play(
            Create(table4),
        )

        brace = Brace(table4.get_rows()[6], sharpness=1, color=BLACK)
        txt_n = Tex(r"$n$", font_size=30, color=BLACK).next_to(brace, 0.5 * DOWN)
        
        self.play(
            Create(brace),
            Write(txt_n)
        )
        self.wait(1)

        # Write equation
        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, -2.5, 0])
        txt = Tex(
            r"$3 \sum_{k = 1}^n k^2 = (2n+1)\sum_{k = 1}^n k$",
            font_size=28, color=BLACK
        ).move_to([0, -2.5, 0])

        self.play(
            Create(rect),
            Write(txt)
        )

        txt2 = Tex(
            r"$\sum_{k = 1}^n k^2 = \frac{2n+1}{3}\cdot\frac{n(n+1)}{2}$",
            font_size=28, color=BLACK
        ).move_to([0, -2.5, 0])
        self.play(
            Transform(txt, txt2)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Proofs without words II:", font_size=30, color=BLACK),
            Tex(r"More exercises in visual thinking", font_size=30, color=BLACK),
            Tex(r"Roger B. Nelsen (2000), p. 88", font_size=30, color=BLACK)
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