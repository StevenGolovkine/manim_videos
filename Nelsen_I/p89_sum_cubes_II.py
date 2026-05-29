"""
Visual proof of the sum of cubes VI.
Proofs without Words. Roger B. Nelsen. p. 89.
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
            Tex(r"Somme des cubes", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Farhood Pouryoussefi", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        results = [
            Tex(
                r"$\sum_{k = 1}^n k^3 = \left(\sum_{k = 1}^n k\right)^2$",
                font_size=24, color=BLACK
            ),
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
                ["1", "2", "3", "\cdot", "\cdot", "\cdot", "n"],
                ["2", "4", "6", "\cdot", "\cdot", "\cdot", "2n"],
                ["3", "6", "9", "\cdot", "\cdot", "\cdot", "3n"],
                ["\cdot", "\cdot", "\cdot", "\cdot", "\cdot", "\cdot", "\cdot"],
                ["\cdot", "\cdot", "\cdot", "\cdot", "\cdot", "\cdot", "\cdot"],
                ["\cdot", "\cdot", "\cdot", "\cdot", "\cdot", "\cdot", "\cdot"],
                ["n", "2n", "3n", "\cdot", "\cdot", "\cdot", "n^2"],
            ],
            h_buff=0.5, v_buff=0.4
        ).scale(0.75).move_to([0, 1, 0])
        table.get_horizontal_lines().set_color(WHITE)
        table.get_vertical_lines().set_color(WHITE)
        table.get_entries().set_color(BLACK)

        self.play(
            Create(table),
        )

        # Color by rows
        txts = []
        txt = Tex(
            r"$\sum k$",
            font_size=24,
            color=BLACK
        ).move_to([-1.5, -1, 0])
        txts.append(txt)
        self.play(
            table.get_rows()[0].animate.set_color(RED),
            Write(txts[0])
        )

        txt = Tex(
            r"$ + 2\sum k$",
            font_size=24,
            color=BLACK
        ).next_to(txts[0], RIGHT, buff=0)
        txts.append(txt)
        self.play(
            table.get_rows()[1].animate.set_color(RED),
            Write(txts[1])
        )

        txt = Tex(
            r"$ + 3\sum k$",
            font_size=24,
            color=BLACK
        ).next_to(txts[1], RIGHT, buff=0)
        txts.append(txt)
        self.play(
            table.get_rows()[2].animate.set_color(RED),
            Write(txts[2])
        )

        txt = Tex(
            r"$ + \cdots$",
            font_size=24,
            color=BLACK
        ).next_to(txts[2], RIGHT, buff=0)
        txts.append(txt)
        self.play(
            table.get_rows()[3:6].animate.set_color(RED),
            Write(txts[3])
        )

        txt = Tex(
            r"$ + n\sum k$",
            font_size=24,
            color=BLACK
        ).next_to(txts[3], RIGHT, buff=0)
        txts.append(txt)
        self.play(
            table.get_rows()[6].animate.set_color(RED),
            Write(txts[4])
        )

        txt = Tex(
            r"$(\sum k)^2$",
            font_size=24,
            color=RED
        ).move_to(VGroup(*txts).get_center())
        self.play(
            Transform(VGroup(*txts), txt)
        )

        self.wait(1)

        # Color another way
        txts = []
        txt = Tex(
            r"$1(1)^2$",
            font_size=24,
            color=BLACK
        ).move_to([-1.5, -1.5, 0])
        txts.append(txt)
        self.play(
            table.get_entries((1, 1)).animate.set_color(BLUE),
            Write(txts[0])
        )

        txt = Tex(
            r"$ + 2(2)^2$",
            font_size=24,
            color=BLACK
        ).next_to(txts[0], RIGHT, buff=0)
        txts.append(txt)
        self.play(
            table.get_entries((1, 2)).animate.set_color(BLUE),
            table.get_entries((2, 1)).animate.set_color(BLUE),
            table.get_entries((2, 2)).animate.set_color(BLUE),
            Write(txts[1])
        )

        txt = Tex(
            r"$ + 3(3)^2$",
            font_size=24,
            color=BLACK
        ).next_to(txts[1], RIGHT, buff=0)
        txts.append(txt)
        self.play(
            table.get_entries((1, 3)).animate.set_color(BLUE),
            table.get_entries((2, 3)).animate.set_color(BLUE),
            table.get_entries((3, 1)).animate.set_color(BLUE),
            table.get_entries((3, 2)).animate.set_color(BLUE),
            table.get_entries((3, 3)).animate.set_color(BLUE),
            Write(txts[2])
        )

        txt = Tex(
            r"$ + \cdots$",
            font_size=24,
            color=BLACK
        ).next_to(txts[2], RIGHT, buff=0)
        txts.append(txt)
        self.play(
            table.get_entries((4, 4)).animate.set_color(BLUE),
            table.get_entries((5, 5)).animate.set_color(BLUE),
            table.get_entries((6, 6)).animate.set_color(BLUE),
            table.get_entries((4, 5)).animate.set_color(BLUE),
            table.get_entries((4, 6)).animate.set_color(BLUE),
            table.get_entries((5, 4)).animate.set_color(BLUE),
            table.get_entries((5, 6)).animate.set_color(BLUE),
            table.get_entries((6, 4)).animate.set_color(BLUE),
            table.get_entries((6, 5)).animate.set_color(BLUE),
            table.get_entries((1, 4)).animate.set_color(BLUE),
            table.get_entries((1, 5)).animate.set_color(BLUE),
            table.get_entries((1, 6)).animate.set_color(BLUE),
            table.get_entries((2, 4)).animate.set_color(BLUE),
            table.get_entries((2, 5)).animate.set_color(BLUE),
            table.get_entries((2, 6)).animate.set_color(BLUE),
            table.get_entries((3, 4)).animate.set_color(BLUE),
            table.get_entries((3, 5)).animate.set_color(BLUE),
            table.get_entries((3, 6)).animate.set_color(BLUE),
            table.get_entries((4, 1)).animate.set_color(BLUE),
            table.get_entries((5, 1)).animate.set_color(BLUE),
            table.get_entries((6, 1)).animate.set_color(BLUE),
            table.get_entries((4, 2)).animate.set_color(BLUE),
            table.get_entries((5, 2)).animate.set_color(BLUE),
            table.get_entries((6, 2)).animate.set_color(BLUE),
            table.get_entries((4, 3)).animate.set_color(BLUE),
            table.get_entries((5, 3)).animate.set_color(BLUE),
            table.get_entries((6, 3)).animate.set_color(BLUE),
            Write(txts[3])
        )

        txt = Tex(
            r"$ + n(n)^2$",
            font_size=24,
            color=BLACK
        ).next_to(txts[3], RIGHT, buff=0)
        txts.append(txt)
        self.play(
            table.get_entries((1, 7)).animate.set_color(BLUE),
            table.get_entries((2, 7)).animate.set_color(BLUE),
            table.get_entries((3, 7)).animate.set_color(BLUE),
            table.get_entries((4, 7)).animate.set_color(BLUE),
            table.get_entries((5, 7)).animate.set_color(BLUE),
            table.get_entries((6, 7)).animate.set_color(BLUE),
            table.get_entries((7, 1)).animate.set_color(BLUE),
            table.get_entries((7, 2)).animate.set_color(BLUE),
            table.get_entries((7, 3)).animate.set_color(BLUE),
            table.get_entries((7, 4)).animate.set_color(BLUE),
            table.get_entries((7, 5)).animate.set_color(BLUE),
            table.get_entries((7, 6)).animate.set_color(BLUE),
            table.get_entries((7, 7)).animate.set_color(BLUE),
            Write(txts[4])
        )

        txt = Tex(
            r"$\sum k^3$",
            font_size=24,
            color=BLUE
        ).move_to(VGroup(*txts).get_center())
        self.play(
            Transform(VGroup(*txts), txt)
        )


        # Write equation
        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, -2.5, 0])
        txt = Tex(
            r"$\sum_{k = 1}^n k^3 = \left(\sum_{k = 1}^n k\right)^2$",
            font_size=28, color=BLACK
        ).move_to([0, -2.5, 0])

        self.play(
            Create(rect),
            Write(txt)
        )


        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine,", font_size=30, color=BLACK),
            Tex(r"vol. 62, no. 5,", font_size=30, color=BLACK),
            Tex(r"(dec. 1989), p. 323.", font_size=30, color=BLACK),
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