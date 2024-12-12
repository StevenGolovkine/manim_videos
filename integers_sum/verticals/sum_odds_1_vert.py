"""
Visual proof of the sums of odd integers.
Proofs without Words I. Roger B. Nelsen. p. 71.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Dot, BraceBetweenPoints, RoundedRectangle
from manim import Create, Uncreate, Write
from manim import VGroup, TransformFromCopy, FadeIn, FadeOut, FunctionGraph
from manim import Text, Tex

from manim import config

from manim import LEFT, RIGHT, DOWN, LIGHT

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
            Tex(r"Somme des entiers", font_size=48, color=BLACK),
            Tex(r"impairs", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration I", font_size=36, color=BLACK),
            Tex(r"Nicomaque de Gérase (vers 100)", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        txt_formula = Tex(r"$1 + 3 + \cdots + (2n - 1) = n^2$", font_size=28, color=BLACK)\
            .next_to(txt, 2 * DOWN)

        self.play(
            Write(txt_title),
            Write(txt),
            Write(txt_formula)
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt),
            Uncreate(txt_formula)
        )
        self.wait(1)

        # Dots
        # self.camera.frame.move_to(points[0]).set(width=20)

        dot_1 = Dot([-1, 2.5, 0], color=RED, radius=0.1)
        txt_1 = Tex(r"$k = 1$", font_size=20, color=BLACK)\
            .next_to(dot_1, 0.5 * LEFT)
        self.play(
            Create(dot_1),
            Write(txt_1)
        )

        dots_3 = [
            Dot([-1 + 0.25 * i, 2.25, 0], color=BLUE, radius=0.1)
            for i in np.arange(3)
        ]
        txt_3 = Tex(r"$k = 3$", font_size=20, color=BLACK)\
            .next_to(dots_3[0], 0.5 * LEFT)
        self.play(
            [Create(dots_3[i]) for i in range(len(dots_3))],
            Write(txt_3)
        )

        dots_5 = [
            Dot([-1 + 0.25 * i, 2, 0], color=RED, radius=0.1)
            for i in np.arange(5)
        ]
        txt_5 = Tex(r"$k = 5$", font_size=20, color=BLACK)\
            .next_to(dots_5[0], 0.5 * LEFT)
        self.play(
            [Create(dots_5[i]) for i in range(len(dots_5))],
            Write(txt_5)
        )
        
        dots_7 = [
            Dot([-1 + 0.25 * i, 1.75, 0], color=BLUE, radius=0.1)
            for i in np.arange(7)
        ]
        txt_7 = Tex(r"$k = 7$", font_size=20, color=BLACK)\
            .next_to(dots_7[0], 0.5 * LEFT)
        self.play(
            [Create(dots_7[i]) for i in range(len(dots_7))],
            Write(txt_7)
        )

        dots_9 = [
            Dot([-1 + 0.25 * i, 1.5, 0], color=RED, radius=0.1)
            for i in np.arange(9)
        ]
        txt_9 = Tex(r"$\cdots$", font_size=20, color=BLACK)\
            .next_to(dots_9[0], 0.5 * LEFT)
        self.play(
            [Create(dots_9[i]) for i in range(len(dots_9))],
            Write(txt_9)
        )

        dots_11 = [
            Dot([-1 + 0.25 * i, 1.25, 0], color=BLUE, radius=0.1)
            for i in np.arange(11)
        ]
        txt_11 = Tex(r"$k = 2n - 3$", font_size=20, color=BLACK)\
            .next_to(dots_11[0], 0.5 * LEFT)
        self.play(
            [Create(dots_11[i]) for i in range(len(dots_11))],
            Write(txt_11)
        )
        
        dots_13 = [
            Dot([-1 + 0.25 * i, 1, 0], color=RED, radius=0.1)
            for i in np.arange(13)
        ]
        txt_13 = Tex(r"$k = 2n - 1$", font_size=20, color=BLACK)\
            .next_to(dots_13[0], 0.5 * LEFT)
        self.play(
            [Create(dots_13[i]) for i in range(len(dots_13))],
            Write(txt_13)
        )

        dot_1_c = dot_1.copy()
        self.play(
            dot_1_c.animate.move_to([-1, -1, 0])
        )

        dots_3_c = [d.copy() for d in dots_3]
        pos = [DOWN, RIGHT + DOWN, RIGHT]
        self.play([
            d.animate.next_to(dot_1_c, 0.25 * p)
            for (d, p) in zip(dots_3_c, pos)
        ])

        dots_5_c = [d.copy() for d in dots_5]
        self.play(
            *[
                dots_5_c[i].animate.next_to(dots_3_c[i], 0.25 * DOWN)
                for i in range(2)
            ],
            dots_5_c[2].animate.next_to(
                dots_3_c[1], 0.25 * RIGHT + 0.25 * DOWN
            ),
            *[
                dots_5_c[i].animate.next_to(dots_3_c[j], 0.25 * RIGHT)
                for i, j in zip(range(3, 5), range(1, 3))
            ]
        )

        dots_7_c = [d.copy() for d in dots_7]
        self.play(
            *[
                dots_7_c[i].animate.next_to(dots_5_c[i], 0.25 * DOWN)
                for i in range(3)
            ],
            dots_7_c[3].animate.next_to(
                dots_5_c[2], 0.25 * RIGHT + 0.25 * DOWN
            ),
            *[
                dots_7_c[i].animate.next_to(dots_5_c[j], 0.25 * RIGHT)
                for i, j in zip(range(4, 7), range(2, 5))
            ]
        )

        dots_9_c = [d.copy() for d in dots_9]
        self.play(
            *[
                dots_9_c[i].animate.next_to(dots_7_c[i], 0.25 * DOWN)
                for i in range(4)
            ],
            dots_9_c[4].animate.next_to(
                dots_7_c[3], 0.25 * RIGHT + 0.25 * DOWN
            ),
            *[
                dots_9_c[i].animate.next_to(dots_7_c[j], 0.25 * RIGHT)
                for i, j in zip(range(5, 9), range(3, 7))
            ]
        )

        dots_11_c = [d.copy() for d in dots_11]
        self.play(
            *[
                dots_11_c[i].animate.next_to(dots_9_c[i], 0.25 * DOWN)
                for i in range(5)
            ],
            dots_11_c[5].animate.next_to(
                dots_9_c[4], 0.25 * RIGHT + 0.25 * DOWN
            ),
            *[
                dots_11_c[i].animate.next_to(dots_9_c[j], 0.25 * RIGHT)
                for i, j in zip(range(6, 11), range(4, 9))
            ]
        )

        dots_13_c = [d.copy() for d in dots_13]
        self.play(
            *[
                dots_13_c[i].animate.next_to(dots_11_c[i], 0.25 * DOWN)
                for i in range(6)
            ],
            dots_13_c[6].animate.next_to(
                dots_11_c[5], 0.25 * RIGHT + 0.25 * DOWN
            ),
            *[
                dots_13_c[i].animate.next_to(dots_11_c[j], 0.25 * RIGHT)
                for i, j in zip(range(7, 13), range(5, 11))
            ]
        )

        brace_bt = BraceBetweenPoints(
            dots_13_c[0].get_center_of_mass(),
            dots_13_c[6].get_center_of_mass(),
            direction=[0, -1, 0], color=BLACK
        )
        brace_rt = BraceBetweenPoints(
            dots_13_c[12].get_center(),
            dots_13_c[6].get_center(),
            direction=[1, 0, 0], color=BLACK
        )
        txt_n = Tex(r"$n$", font_size=30, color=BLACK).next_to(brace_rt, 0.5 * RIGHT)
        txt_n_c = txt_n.copy().next_to(brace_bt, 0.5 * DOWN)
        self.play(
            Create(brace_bt),
            Create(brace_rt),
            Write(txt_n),
            Write(txt_n_c)
        )

        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        )
        txt = Tex(
            r"$1$", r"$~+~$", r"$3$",
            r"$~+ \cdots +~$", r"$(2n - 1)$",
            r"$~=~$", r"$n^2$",
            font_size=30, color=BLACK
         )

        # self.play(Write(txt))

        rect.z_index = 0
        txt.z_index = 1
        self.play(
            Create(rect),
            run_time=0.5
        )
        self.play(
            TransformFromCopy(txt_1[0], txt[0]),
            Write(txt[1]),
            TransformFromCopy(txt_3[0], txt[2]),
            Write(txt[3]),
            TransformFromCopy(txt_13[0], txt[4]),
            Write(txt[5]),
            TransformFromCopy(txt_n[0], txt[6]),
            TransformFromCopy(txt_n_c[0], txt[6].copy())
        )

        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Proofs without words:", font_size=30, color=BLACK),
            Tex(r"Exercises in visual thinking", font_size=30, color=BLACK),
            Tex(r"Roger B. Nelsen (1993), p. 71", font_size=30, color=BLACK)
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
