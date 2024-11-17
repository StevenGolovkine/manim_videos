"""
Visual proof of the sums of odd integers.
Proofs without Words I. Roger B. Nelsen. p. 71.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Point, Dot, BraceBetweenPoints
from manim import Create, Uncreate, Write
from manim import VGroup, TransformFromCopy
from manim import Tex

from manim import LEFT, RIGHT, UP, DOWN, PI, DEGREES

# COLORS
BLUE = "#648FFF"
VIOLET = "#785EF0"
RED = "#DC267F"
ORANGE = "#FE6100"
YELLOW = "#FFB000"
BLACK = "#000000"
WHITE = "#FFFFFF"


class Sums(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame.save_state()

        # Camera set
        points = [
            Point(location=[6, -1, 0]),
            Point(location=[6, -1.5, 0]),
            Point(location=[6, -2, 0]),
            Point(location=[6, -2.5, 0]),
            Point(location=[6, -3, 0]),
            Point(location=[6, -3.5, 0]),
            Point(location=[6, -4, 0]),
            Point(location=[10 + 1 / 9, -4.5, 0]),
        ]

        # Introduction text
        txt = [
            Tex(r"Démonstration I", font_size=72, color=BLACK),
            Tex(r"Nicomaque de Gérase (vers 100)", font_size=48, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        txt_formula = Tex(r"$1 + 3 + \cdots + (2n - 1) = n^2$", font_size=48, color=BLACK)\
            .next_to(txt, 2 * DOWN)

        self.play(
            Write(txt),
            Write(txt_formula)
        )
        self.wait(1)
        self.play(
            Uncreate(txt),
            Uncreate(txt_formula)
        )
        self.wait(1)

        # Dots
        self.play(
            self.camera.frame.animate.move_to(points[0]).set(height=12)
        )

        dot_1 = Dot([0, 0, 0], color=RED, radius=0.5)
        txt_1 = Tex(r"$k = 1$", font_size=72, color=BLACK).next_to(dot_1, 2 * LEFT)
        self.play(
            Create(dot_1),
            Write(txt_1)
        )

        dots_3 = [Dot([i, -1.25, 0], color=BLUE, radius=0.5) for i in np.arange(3)]
        txt_3 = Tex(r"$k = 3$", font_size=72, color=BLACK).next_to(dots_3[0], 2 * LEFT)
        self.play(
            self.camera.frame.animate.move_to(points[1]),
            [Create(dots_3[i]) for i in range(len(dots_3))],
            Write(txt_3)
        )

        dots_5 = [Dot([i, -2.5, 0], color=RED, radius=0.5) for i in np.arange(5)]
        txt_5 = Tex(r"$k = 5$", font_size=72, color=BLACK).next_to(dots_5[0], 2 * LEFT)
        self.play(
            self.camera.frame.animate.move_to(points[2]),
            [Create(dots_5[i]) for i in range(len(dots_5))],
            Write(txt_5)
        )
        
        dots_7 = [Dot([i, -3.75, 0], color=BLUE, radius=0.5) for i in np.arange(7)]
        txt_7 = Tex(r"$k = 7$", font_size=72, color=BLACK).next_to(dots_7[0], 2 * LEFT)
        self.play(
            self.camera.frame.animate.move_to(points[3]),
            [Create(dots_7[i]) for i in range(len(dots_7))],
            Write(txt_7)
        )

        dots_9 = [Dot([i, -5, 0], color=RED, radius=0.5) for i in np.arange(9)]
        txt_9 = Tex(r"$\cdots$", font_size=72, color=BLACK).next_to(dots_9[0], 2 * LEFT)
        self.play(
            self.camera.frame.animate.move_to(points[4]),
            [Create(dots_9[i]) for i in range(len(dots_9))],
            Write(txt_9)
        )

        dots_11 = [Dot([i, -6.25, 0], color=BLUE, radius=0.5) for i in np.arange(11)]
        txt_11 = Tex(r"$k = 2n - 3$", font_size=72, color=BLACK).next_to(dots_11[0], 2 * LEFT)
        self.play(
            self.camera.frame.animate.move_to(points[5]),
            [Create(dots_11[i]) for i in range(len(dots_11))],
            Write(txt_11)
        )
        
        dots_13 = [Dot([i, -7.5, 0], color=RED, radius=0.5) for i in np.arange(13)]
        txt_13 = Tex(r"$k = 2n - 1$", font_size=72, color=BLACK).next_to(dots_13[0], 2 * LEFT)
        self.play(
            self.camera.frame.animate.move_to(points[6]),
            [Create(dots_13[i]) for i in range(len(dots_13))],
            Write(txt_13)
        )

        self.play(
            self.camera.frame.animate.move_to(points[7]).set(width=2.25 * (14 + 2 / 9))
        )

        dot_1_c = dot_1.copy()
        self.play(
            dot_1_c.animate.move_to([14 + 1 / 9, 0, 0])
        )

        dots_3_c = [d.copy() for d in dots_3]
        pos = [RIGHT, RIGHT + DOWN, DOWN]
        self.play(
            [d.animate.next_to(dot_1_c, p) for (d, p) in zip(dots_3_c, pos)]
        )

        dots_5_c = [d.copy() for d in dots_5]
        self.play(
            *[dots_5_c[i].animate.next_to(dots_3_c[i], RIGHT) for i in range(2)],
            dots_5_c[2].animate.next_to(dots_3_c[1], RIGHT + DOWN),
            *[dots_5_c[i].animate.next_to(dots_3_c[j], DOWN) for i, j in zip(range(3, 5), range(1, 3))]
        )

        dots_7_c = [d.copy() for d in dots_7]
        self.play(
            *[dots_7_c[i].animate.next_to(dots_5_c[i], RIGHT) for i in range(3)],
            dots_7_c[3].animate.next_to(dots_5_c[2], RIGHT + DOWN),
            *[dots_7_c[i].animate.next_to(dots_5_c[j], DOWN) for i, j in zip(range(4, 7), range(2, 5))]
        )

        dots_9_c = [d.copy() for d in dots_9]
        self.play(
            *[dots_9_c[i].animate.next_to(dots_7_c[i], RIGHT) for i in range(4)],
            dots_9_c[4].animate.next_to(dots_7_c[3], RIGHT + DOWN),
            *[dots_9_c[i].animate.next_to(dots_7_c[j], DOWN) for i, j in zip(range(5, 9), range(3, 7))]
        )

        dots_11_c = [d.copy() for d in dots_11]
        self.play(
            *[dots_11_c[i].animate.next_to(dots_9_c[i], RIGHT) for i in range(5)],
            dots_11_c[5].animate.next_to(dots_9_c[4], RIGHT + DOWN),
            *[dots_11_c[i].animate.next_to(dots_9_c[j], DOWN) for i, j in zip(range(6, 11), range(4, 9))]
        )

        dots_13_c = [d.copy() for d in dots_13]
        self.play(
            *[dots_13_c[i].animate.next_to(dots_11_c[i], RIGHT) for i in range(6)],
            dots_13_c[6].animate.next_to(dots_11_c[5], RIGHT + DOWN),
            *[dots_13_c[i].animate.next_to(dots_11_c[j], DOWN) for i, j in zip(range(7, 13), range(5, 11))]
        )

        brace_bt = BraceBetweenPoints(
            dots_13_c[12].get_center() + [-0.5, -0.5, 0],
            dots_13_c[6].get_center() + [0.5, -0.5, 0],
            direction=[0, -1, 0], color=BLACK
        )
        brace_rt = BraceBetweenPoints(
            dots_13_c[0].get_center() + [0.5, 0.5, 0],
            dots_13_c[6].get_center() + [0.5, -0.5, 0],
            direction=[1, 0, 0], color=BLACK
        )
        txt_n = Tex(r"$n$", font_size=72, color=BLACK).next_to(brace_rt, RIGHT)
        txt_n_c = txt_n.copy().next_to(brace_bt, DOWN)
        self.play(
            Create(brace_bt),
            Create(brace_rt),
            Write(txt_n),
            Write(txt_n_c)
        )

        txt = Tex(
            r"$1$", r"$~+~$", r"$3$", r"$~+~$", r"$5$", r"$~+~$", r"$7$",
            r"$~+ \cdots +~$", r"$(2n - 3)$", r"$~+~$", r"$(2n - 1)$",
            r"$~=~$", r"$n^2$", r"$A$",
            font_size=72, color=BLACK
         ).move_to([10 + 1/ 9, -10, 0])

        # self.play(Write(txt))

        self.play(
            TransformFromCopy(txt_1[0], txt[0]),
            Write(txt[1]),
            TransformFromCopy(txt_3[0], txt[2]),
            Write(txt[3]),
            TransformFromCopy(txt_5[0], txt[4]),
            Write(txt[5]),
            TransformFromCopy(txt_7[0], txt[6]),
            Write(txt[7]),
            TransformFromCopy(txt_11[0], txt[8]),
            Write(txt[9]),
            TransformFromCopy(txt_13[0], txt[10]),
            Write(txt[11]),
            TransformFromCopy(txt_n[0], txt[12]),
            TransformFromCopy(txt_n_c[0], txt[13])
        )


        self.wait(1)
