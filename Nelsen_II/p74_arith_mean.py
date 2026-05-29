"""
Visual proof of the arithmetic mean - geometric mean inequality for three positive
numbers.
Proofs without Words II. Roger B. Nelsen. p. 74.
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


class Mean(MovingCameraScene):
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
            Tex(r"de moyennes", font_size=48, color=BLACK),
            Tex(r"pour 3 nombres", font_size=48, color=BLACK),
            Tex(r"Partie I", font_size=24, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Claudi Alsina", font_size=28, color=BLACK)
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

        # Square
        rect_a = Rectangle(width=2, height=2, color=BLUE, fill_opacity=0.5)
        rect_b = Rectangle(width=1, height=1, color=VIOLET, fill_opacity=0.5).\
            next_to(rect_a, DOWN, buff=0).\
            align_to(rect_a, LEFT)
        rect_c = Rectangle(width=0.5, height=0.5, color=RED, fill_opacity=0.5).\
            next_to(rect_b, DOWN, buff=0).\
            align_to(rect_a, LEFT)

        txt_a = Tex(r"$a$", font_size=36, color=BLACK).\
            next_to(rect_a, UP, buff=0.1)
        txt_aa = Tex(r"$a$", font_size=36, color=BLACK).\
            next_to(rect_a, LEFT, buff=0.1)
        txt_b = Tex(r"$b$", font_size=36, color=BLACK).\
            next_to(rect_b, UP, buff=0.1)
        txt_bb = Tex(r"$b$", font_size=36, color=BLACK).\
            next_to(rect_b, LEFT, buff=0.1)
        txt_c = Tex(r"$c$", font_size=36, color=BLACK).\
            next_to(rect_c, UP, buff=0.1)
        txt_cc = Tex(r"$c$", font_size=36, color=BLACK).\
            next_to(rect_c, LEFT, buff=0.1)

        self.play(
            FadeIn(rect_a),
            Write(txt_a),
            Write(txt_aa)
        )

        txt_a2 = Tex(r"$a^2$", font_size=36, color=BLACK).\
            move_to(rect_a.get_center_of_mass())
        self.play(
            Transform(txt_a, txt_a2),
            Transform(txt_aa, txt_a2)
        )

        self.play(
            FadeIn(rect_b),
            Write(txt_b),
            Write(txt_bb)
        )

        txt_b2 = Tex(r"$b^2$", font_size=36, color=BLACK).\
            move_to(rect_b.get_center_of_mass())
        self.play(
            Transform(txt_b, txt_b2),
            Transform(txt_bb, txt_b2)
        )

        self.play(
            FadeIn(rect_c),
            Write(txt_c),
            Write(txt_cc)
        )

        txt_c2 = Tex(r"$c^2$", font_size=36, color=BLACK).\
            move_to(rect_c.get_center_of_mass())
        self.play(
            Transform(txt_c, txt_c2),
            Transform(txt_cc, txt_c2)
        )

        # Rectangles
        rect_ab = Rectangle(width=2, height=1, color=GREEN, fill_opacity=0.5).\
            align_to(rect_a, UP)
        rect_bc = Rectangle(width=1, height=0.5, color=YELLOW, fill_opacity=0.5).\
            next_to(rect_ab, DOWN, buff=0).\
            align_to(rect_a, LEFT)
        rect_ac = Rectangle(width=0.5, height=2, color=ORANGE, fill_opacity=0.5).\
            next_to(rect_bc, DOWN, buff=0).\
            align_to(rect_a, LEFT)
        
        txt_a = Tex(r"$a$", font_size=36, color=BLACK).\
            next_to(rect_ab, UP, buff=0.1)
        txt_b = Tex(r"$b$", font_size=36, color=BLACK).\
            next_to(rect_ab, LEFT, buff=0.1)
        txt_bb = Tex(r"$b$", font_size=36, color=BLACK).\
            next_to(rect_bc, UP, buff=0.1)
        txt_c = Tex(r"$c$", font_size=36, color=BLACK).\
            next_to(rect_bc, LEFT, buff=0.1)
        txt_cc = Tex(r"$c$", font_size=36, color=BLACK).\
            next_to(rect_ac, UP, buff=0.1)
        txt_aa = Tex(r"$a$", font_size=36, color=BLACK).\
            next_to(rect_ac, LEFT, buff=0.1)

        self.play(
            FadeIn(rect_ab),
            Write(txt_a),
            Write(txt_b)
        )

        txt_ab = Tex(r"$ab$", font_size=36, color=BLACK).\
            move_to(rect_ab.get_center_of_mass())
        self.play(
            Transform(txt_a, txt_ab),
            Transform(txt_b, txt_ab)
        )

        self.play(
            FadeIn(rect_bc),
            Write(txt_bb),
            Write(txt_c)
        )

        txt_bc = Tex(r"$bc$", font_size=36, color=BLACK).\
            move_to(rect_bc.get_center_of_mass())
        self.play(
            Transform(txt_bb, txt_bc),
            Transform(txt_c, txt_bc)
        )

        self.play(
            FadeIn(rect_ac),
            Write(txt_cc),
            Write(txt_aa)
        )

        txt_ac = Tex(r"$ac$", font_size=36, color=BLACK).\
            move_to(rect_ac.get_center_of_mass())
        self.play(
            Transform(txt_cc, txt_ac),
            Transform(txt_aa, txt_ac)
        )

        # Write the inequalities
        inequalities = [
            Tex(r"$ab + bc + ac$", font_size=30, color=BLACK),
            Tex(r"$ \leq $", font_size=30, color=BLACK),
            Tex(r"$a^2 + b^2 + c^2$", font_size=30, color=BLACK)
        ]
        inequalities = VGroup(*inequalities).arrange(RIGHT).move_to([0, 2, 0])

        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, 2, 0])
        txt = txt = Tex(
            r"$ab$", r"$~+~$", r"$bc$", r"$~+~$", r"$ac$",
            r" $ \leq $ ",
            r"$a^2$", r"$~+~$", r"$b^2$", r"$~+~$", r"$c^2$",
            font_size=28, color=BLACK
         ).move_to([0, 2, 0])

        rect.z_index = 0
        txt.z_index = 1
        self.play(
            Create(rect),
            run_time=0.5
        )
        self.play(
            TransformFromCopy(txt_ab[0], txt[0]),
            Write(txt[1]),
            TransformFromCopy(txt_bc[0], txt[2]),
            Write(txt[3]),
            TransformFromCopy(txt_ac[0], txt[4]),
            Write(txt[5]),
            TransformFromCopy(txt_a2[0], txt[6]),
            Write(txt[7]),
            TransformFromCopy(txt_b2[0], txt[8]),
            Write(txt[9]),
            TransformFromCopy(txt_c2[0], txt[10]),
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine, vol. 73,", font_size=26, color=BLACK),
            Tex(r"no. 2 (April 2000), p.97", font_size=26, color=BLACK)
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