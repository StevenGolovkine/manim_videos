"""
Visual proof of nonnegative integer solutions and triangular numbers
Proofs without Words III. Roger B. Nelsen. p. 166.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, TransformFromCopy
from manim import VGroup, FadeIn, FadeOut , FunctionGraph, Rotate
from manim import Line, Point, Polygon, RoundedRectangle, Circle, Angle
from manim import line_intersection, DashedLine, RightAngle
from manim import Text, Tex, Intersection

from manim import config
from manim import ORIGIN, LEFT, RIGHT, DOWN, LIGHT, UP, PI, DEGREES

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
            Tex(r"Les solutions de", font_size=48, color=BLACK),
            Tex(r"$x + y + z = n$", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"M. Haines \& M. Jones", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        self.add(
            txt_title,
            txt
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt)
        )

        # Write theorem
        theorem_1 = Tex(
            r"Soit $i, j$ et $k$ des entiers compris entre $0$ et $n$.",
            font_size=20, color=BLACK
        )
        theorem_1.to_edge(UP)
        theorem_2 = Tex(
            r"Le nombre de solutions non négatives et",
            font_size=20, color=BLACK
        )
        theorem_2.next_to(theorem_1, DOWN, aligned_edge=LEFT, buff=0.1)
        theorem_3 = Tex(
            r"entières de $x + y + z = n$ avec $x \leq i$,",
            font_size=20, color=BLACK
        )
        theorem_3.next_to(theorem_2, DOWN, aligned_edge=LEFT, buff=0.1)
        theorem_4 = Tex(
            r"$y \leq j$, $z \leq k$, est donné par",
            font_size=20, color=BLACK
        )
        theorem_4.next_to(theorem_3, DOWN, aligned_edge=LEFT, buff=0.1)
        theorem_5 = Tex(
            r"$T_{i + j + k - n + 1} - T_{i + j - n} - T_{i + k - n}$",
            r"$- T_{j + k - n}$,",
            font_size=20, color=BLACK
        )
        theorem_5.next_to(theorem_4, DOWN, aligned_edge=LEFT, buff=0.1)
        theorem_6 = Tex(
            r"où $T_n$ est le $n^{\text{e}}$ nombre triangulaire.",
            font_size=20, color=BLACK
        )
        theorem_6.next_to(theorem_5, DOWN, aligned_edge=LEFT, buff=0.1)
        self.play(
            Write(theorem_1),
            Write(theorem_2),
            Write(theorem_3),
            Write(theorem_4),
            Write(theorem_5),
            Write(theorem_6)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine,", font_size=30, color=BLACK),
            Tex(r"vol. 75, no. 5 (Dec. 2002),", font_size=30, color=BLACK),
            Tex(r"p. 388", font_size=30, color=BLACK),
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