"""
Visual proof of an algebraic inequality.
Proofs without Words III. Roger B. Nelsen. p. 103.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, TransformFromCopy
from manim import VGroup, FadeIn, FadeOut, FunctionGraph, Rectangle, RoundedRectangle
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
            Tex(r"Une inégalité", font_size=48, color=BLACK),
            Tex(r"algébrique", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Wei-Dong Jiang", font_size=28, color=BLACK)
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

        # Text
        txt = [
            Tex(r"Soit $a \geq b \geq c \geq 0$,", font_size=30, color=BLACK),
            Tex(r"et soit $a + b + c \leq 1$,", font_size=30, color=BLACK),
            Tex(r"alors $a^2 + 3b^2 + 5c^2 \leq 1$.", font_size=30, color=BLACK),
        ]
        txt = VGroup(*txt).arrange(DOWN, aligned_edge=LEFT).move_to([0, 3, 0])

        self.play(
            Write(txt),
        )

        # Rectangles
        rect = Rectangle(width=4, height=4, color=BLACK).move_to([0, -0.5, 0])

        self.play(
            Create(rect)
        )

        rect_a = Rectangle(width=2, height=2, color=BLUE, fill_opacity=0.5).\
            align_to(rect, UP + LEFT)
        txt_a = Tex(r"$a$", font_size=30, color=BLACK).\
            next_to(rect_a, UP)
        txt_a2 = Tex(r"$a^2$", font_size=30, color=BLACK).\
            move_to(rect_a.get_center())
        self.play(
            Create(rect_a),
            Create(txt_a),
            Create(txt_a2)
        )

        rect_b = Rectangle(width=1.25, height=1.25, color=VIOLET, fill_opacity=0.5).\
            next_to(rect_a, RIGHT, aligned_edge=UP, buff=0)
        txt_b = Tex(r"$b$", font_size=30, color=BLACK).\
            next_to(rect_b, UP)
        txt_b2 = Tex(r"$b^2$", font_size=30, color=BLACK).\
            move_to(rect_b.get_center())
        rect_b_c = rect_b.copy().\
            next_to(rect_a, DOWN, aligned_edge=LEFT, buff=0)
        txt_b2_c = Tex(r"$b^2$", font_size=30, color=BLACK).\
            move_to(rect_b_c.get_center())
        rect_b_cc = rect_b.copy().\
            next_to(rect_a, DOWN + RIGHT, buff=0)
        txt_b2_cc = Tex(r"$b^2$", font_size=30, color=BLACK).\
            move_to(rect_b_cc.get_center())

        self.play(
            Create(rect_b),
            Create(rect_b_c),
            Create(rect_b_cc),
            Create(txt_b),
            Create(txt_b2),
            Create(txt_b2_c),
            Create(txt_b2_cc)
        )

        rect_c = Rectangle(width=0.75, height=0.755, color=RED, fill_opacity=0.5).\
            next_to(rect_b, RIGHT, aligned_edge=UP, buff=0)
        txt_c = Tex(r"$c$", font_size=30, color=BLACK).\
            next_to(rect_c, UP)
        txt_c2 = Tex(r"$c^2$", font_size=30, color=BLACK).\
            move_to(rect_c.get_center())
        rect_c_c = rect_c.copy().\
            next_to(rect_b_cc, RIGHT, aligned_edge=UP, buff=0)
        txt_c2_c = Tex(r"$c^2$", font_size=30, color=BLACK).\
            move_to(rect_c_c.get_center())
        rect_c_cc = rect_c.copy().\
            next_to(rect_b_c, DOWN, aligned_edge=LEFT, buff=0)
        txt_c2_cc = Tex(r"$c^2$", font_size=30, color=BLACK).\
            move_to(rect_c_cc.get_center())
        rect_c_ccc = rect_c.copy().\
            next_to(rect_b_cc, DOWN, aligned_edge=LEFT, buff=0)
        txt_c2_ccc = Tex(r"$c^2$", font_size=30, color=BLACK).\
            move_to(rect_c_ccc.get_center())
        rect_c_cccc = rect_c.copy().\
            next_to(rect_b_cc, DOWN + RIGHT, buff=0)
        txt_c2_cccc = Tex(r"$c^2$", font_size=30, color=BLACK).\
            move_to(rect_c_cccc.get_center())

        self.play(
            Create(rect_c),
            Create(rect_c_c),
            Create(rect_c_cc),
            Create(rect_c_ccc),
            Create(rect_c_cccc),
            Create(txt_c),
            Create(txt_c2),
            Create(txt_c2_c),
            Create(txt_c2_cc),
            Create(txt_c2_ccc),
            Create(txt_c2_cccc)
        )
        self.wait(1)

        # Write the inequalities
        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, -3, 0])
        txt = txt = Tex(
            r"$a^2 + 3b^2 + 5c^2$",
            r" $ \leq $ ",
            r"$(a + b + c)^2$",
            font_size=28, color=BLACK
         ).move_to([0, -3, 0])

        rect.z_index = 0
        txt.z_index = 1
        self.play(
            Create(rect),
            Create(txt),
        )
        self.wait(1)

        txt_1 = Tex(
            r"$a^2 + 3b^2 + 5c^2$",
            r" $ \leq $ ",
            r"$1^2$",
            font_size=28, color=BLACK
         ).move_to([0, -3, 0])
        self.play(
            Transform(txt, txt_1),
        )

        txt_12 = Tex(
            r"$a^2 + 3b^2 + 5c^2$",
            r" $ \leq $ ",
            r"$1$",
            font_size=28, color=BLACK
         ).move_to([0, -3, 0])
        self.play(
            Transform(txt, txt_12),
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Problem 12, 1989 Leningrad", font_size=26, color=BLACK),
            Tex(r"Mathematics Olympiad, Grade 7.", font_size=26, color=BLACK),
            Tex(r"Mathematics Magazine, vol. 80,", font_size=26, color=BLACK),
            Tex(r"no. 5 (Dec. 2007), p.344", font_size=26, color=BLACK)
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