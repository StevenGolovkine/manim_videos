"""
Visual proof of the transpose of a product of matrices.
Proofs without Words II. Roger B. Nelsen. p. 117.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, TransformFromCopy, FadeTransform
from manim import VGroup, FadeIn, FadeOut , FunctionGraph, Rotate
from manim import RoundedRectangle, Rectangle, Line
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


class Matrix(MovingCameraScene):
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
            Tex(r"La transposée du", font_size=48, color=BLACK),
            Tex(r"produit de matrices", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"James G. Simmonds", font_size=28, color=BLACK)
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

        # Matrix A and B
        A = Rectangle(
            width=1.25, height=0.75, color=BLUE, fill_color=BLUE, fill_opacity=0.5
        ).move_to([0.6, 1.5, 0])
        A_label = Tex(r"$A$", font_size=20, color=BLACK).move_to(A.get_center())

        B = Rectangle(
            width=0.75, height=1.25, color=RED, fill_color=RED, fill_opacity=0.5
        ).next_to(A, RIGHT + UP, buff=0)
        B_label = Tex(r"$B$", font_size=20, color=BLACK).move_to(B.get_center())

        self.play(
            Create(A),
            Write(A_label),
            Create(B),
            Write(B_label)
        )

        # Product AB
        AB = Rectangle(
            width=0.75, height=0.75, color=GREEN, fill_color=GREEN, fill_opacity=0.5
        ).next_to(A, RIGHT, buff=0)
        AB_label = Tex(r"$AB$", font_size=20, color=BLACK).move_to(AB.get_center())
        self.play(
            Create(AB),
            Write(AB_label)
        )

        # Diagonal line
        diagonal_line = Line(
            [-5 + 1.1, 5, 0],
            [5 + 1.1, -5, 0],
            color=BLACK, stroke_width=2
        )
        self.play(
            Create(diagonal_line)
        )

        # Transpose of A and B
        AT = Rectangle(
            width=0.75, height=1.25, color=BLUE, fill_color=BLUE, fill_opacity=0.5
        ).next_to(A, DOWN + LEFT, buff=0)
        AT_label = Tex(r"$A^T$", font_size=20, color=BLACK).move_to(AT.get_center())
        self.play(
            TransformFromCopy(A, AT),
            Write(AT_label)
        )

        BT = Rectangle(
            width=1.25, height=0.75, color=RED, fill_color=RED, fill_opacity=0.5
        ).next_to(AT, DOWN + LEFT, buff=0)
        BT_label = Tex(r"$B^T$", font_size=20, color=BLACK).move_to(BT.get_center())
        self.play(
            TransformFromCopy(B, BT),
            Write(BT_label)
        )

        # Transpose of AB
        ABT = Rectangle(    
            width=0.75, height=0.75, color=GREEN, fill_color=GREEN, fill_opacity=0.5
        ).next_to(BT, RIGHT, buff=0)
        ABT_label = Tex(r"$(AB)^T$", font_size=20, color=BLACK).\
            move_to(ABT.get_center())
        self.play(
            TransformFromCopy(AB, ABT),
            Write(ABT_label)
        )

        # Write equation
        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, -2, 0])
        txt = Tex(
            r"$(AB)^T = B^T A^T$", font_size=36, color=BLACK
        ).move_to(rect.get_center())

        rect.z_index = 0
        txt.z_index = 1
        self.play(
            Create(rect),
            Write(txt),
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"College Mathematics Journal,", font_size=30, color=BLACK),
            Tex(r"vol. 26, no. 3,", font_size=30, color=BLACK),
            Tex(r"(May 1995), p. 250.", font_size=30, color=BLACK),
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