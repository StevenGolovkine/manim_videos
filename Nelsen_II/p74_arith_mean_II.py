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
PINK = "#FFC5CB"
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
            Tex(r"Partie II", font_size=24, color=BLACK),
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


        # First Rectangles
        rect_a = Rectangle(
            width=1.5, height=1.5**2, color=BLUE, fill_opacity=0.75, stroke_width=0
        ).\
            move_to([-0.75, 0, 0])

        txt_a = Tex(r"$a$", font_size=30, color=BLACK).\
            next_to(rect_a, UP, buff=0.1)
        txt_a2 = Tex(r"$a^2$", font_size=30, color=BLACK).\
            next_to(rect_a, LEFT, buff=0.1)

        self.play(
            FadeIn(rect_a),
            Write(txt_a),
            Write(txt_a2)
        )
        
        txt_a3 = Tex(r"$a^3$", font_size=30, color=BLACK).\
            move_to(rect_a.get_center_of_mass())
        self.play(
            Transform(txt_a, txt_a3),
            Transform(txt_a2, txt_a3)
        )

        rect_ba = Rectangle(
            width=1.5, height=1, color=PINK, fill_opacity=0.75, stroke_width=0
        ).\
            next_to(rect_a, DOWN, buff=0).\
            align_to(rect_a, LEFT)
        rect_ab = Rectangle(
            width=1, height=1.5**2, color=RED, fill_opacity=0.75, stroke_width=0
        ).\
            next_to(rect_a, RIGHT, buff=0).\
            align_to(rect_a, UP)
        rect_b2 = Rectangle(
            width=1, height=1, color=BLUE, fill_opacity=0.75, stroke_width=0
        ).\
            next_to(rect_ab, DOWN, buff=0).\
            align_to(rect_ab, LEFT)

        txt_b = Tex(r"$b$", font_size=30, color=BLACK).\
            next_to(rect_ab, UP, buff=0.1)
        txt_b2 = Tex(r"$b^2$", font_size=30, color=BLACK).\
            next_to(rect_ba, LEFT, buff=0.1)

        self.play(
            FadeIn(rect_ba),
            FadeIn(rect_ab),
            FadeIn(rect_b2),
            Write(txt_b),
            Write(txt_b2)
        )

        txt_b3 = Tex(r"$b^3$", font_size=30, color=BLACK).\
            move_to(rect_b2.get_center_of_mass())
        self.play(
            Transform(txt_b, txt_b3),
            Transform(txt_b2, txt_b3)
        )

        rect_ca = Rectangle(
            width=1.5, height=0.5**2, color=GREEN, fill_opacity=0.75, stroke_width=0
        ).\
            next_to(rect_ba, DOWN, buff=0).\
            align_to(rect_ba, LEFT)
        rect_cb = Rectangle(
            width=1, height=0.5**2, color=YELLOW, fill_opacity=0.75, stroke_width=0
        ).\
            next_to(rect_b2, DOWN, buff=0).\
            align_to(rect_b2, LEFT)
        rect_ac = Rectangle(
            width=0.5, height=1.5**2, color=ORANGE, fill_opacity=0.75, stroke_width=0
        ).\
            next_to(rect_ab, RIGHT, buff=0).\
            align_to(rect_a, UP)
        rect_bc = Rectangle(
            width=0.5, height=1, color=VIOLET, fill_opacity=0.75, stroke_width=0
        ).\
            next_to(rect_b2, RIGHT, buff=0).\
            align_to(rect_b2, UP)
        rect_c2 = Rectangle(
            width=0.5, height=0.5**2, color=BLUE, fill_opacity=0.75, stroke_width=0
        ).\
            next_to(rect_bc, DOWN, buff=0).\
            align_to(rect_bc, LEFT)
        
        txt_c = Tex(r"$c$", font_size=30, color=BLACK).\
            next_to(rect_ac, UP, buff=0.1)
        txt_c2 = Tex(r"$c^2$", font_size=30, color=BLACK).\
            next_to(rect_ca, LEFT, buff=0.1)

        self.play(
            FadeIn(rect_ca),
            FadeIn(rect_cb),
            FadeIn(rect_ac),
            FadeIn(rect_bc),
            FadeIn(rect_c2),
            Write(txt_c),
            Write(txt_c2)
        )

        txt_c3 = Tex(r"$c^3$", font_size=30, color=BLACK).\
            move_to(rect_c2.get_center_of_mass())
        self.play(
            Transform(txt_c, txt_c3),
            Transform(txt_c2, txt_c3)
        )
        
        # Second rectangles
        rect_bca = Rectangle(
            width=1.5, height=1 * 0.5, color=BLUE, fill_opacity=0.5,
            stroke_width=1, stroke_color=BLACK
        ).\
            align_to(rect_a, UP + LEFT)
        
        txt_a = Tex(r"$a$", font_size=30, color=BLACK).\
            next_to(rect_bca, UP, buff=0.1)
        txt_bc = Tex(r"$bc$", font_size=30, color=BLACK).\
            next_to(rect_bca, LEFT, buff=0.1)
        
        self.play(
            FadeIn(rect_bca),
            Write(txt_a),
            Write(txt_bc)
        )

        txt_abc = Tex(r"$abc$", font_size=30, color=BLACK).\
            move_to(rect_bca.get_center_of_mass())
        self.play(
            Transform(txt_a, txt_abc),
            Transform(txt_bc, txt_abc)
        )

        rect_aca = Rectangle(
            width=1.5, height=1.5 * 0.5, color=ORANGE, fill_opacity=0.5,
            stroke_width=1, stroke_color=BLACK
        ).\
            next_to(rect_bca, DOWN, buff=0).\
            align_to(rect_bca, LEFT)
        rect_bcb = Rectangle(
            width=1, height=1 * 0.5, color=VIOLET, fill_opacity=0.5,
            stroke_width=1, stroke_color=BLACK
        ).\
            next_to(rect_bca, RIGHT, buff=0).\
            align_to(rect_bca, UP)
        rect_acb = Rectangle(
            width=1, height=1.5 * 0.5, color=BLUE, fill_opacity=0.5,
            stroke_width=1, stroke_color=BLACK
        ).\
            next_to(rect_aca, RIGHT, buff=0).\
            align_to(rect_aca, UP)
        
        txt_b = Tex(r"$b$", font_size=30, color=BLACK).\
            next_to(rect_bcb, UP, buff=0.1)
        txt_ac = Tex(r"$ac$", font_size=30, color=BLACK).\
            next_to(rect_aca, LEFT, buff=0.1)

        self.play(
            FadeIn(rect_aca),
            FadeIn(rect_bcb),
            FadeIn(rect_acb),
            Write(txt_b),
            Write(txt_ac)
        )

        txt_abc_2 = Tex(r"$abc$", font_size=30, color=BLACK).\
            move_to(rect_acb.get_center_of_mass())
        self.play(
            Transform(txt_b, txt_abc_2),
            Transform(txt_ac, txt_abc_2)
        )

        rect_aba = Rectangle(
            width=1.5, height=1.5 * 1, color=RED, fill_opacity=0.5,
            stroke_width=1, stroke_color=BLACK
        ).\
            next_to(rect_aca, DOWN, buff=0).\
            align_to(rect_aca, LEFT)
        rect_abb = Rectangle(
            width=1, height=1.5 * 1, color=PINK, fill_opacity=0.5,
            stroke_width=1, stroke_color=BLACK
        ).\
            next_to(rect_aba, RIGHT, buff=0).\
            align_to(rect_aba, UP)
        rect_bcc = Rectangle(
            width=0.5, height=1 * 0.5, color=YELLOW, fill_opacity=0.5,
            stroke_width=1, stroke_color=BLACK
        ).\
            next_to(rect_bcb, RIGHT, buff=0).\
            align_to(rect_bcb, UP)
        rect_acc = Rectangle(
            width=0.5, height=1.5 * 0.5, color=GREEN, fill_opacity=0.5,
            stroke_width=1, stroke_color=BLACK
        ).\
            next_to(rect_acb, RIGHT, buff=0).\
            align_to(rect_acb, UP)
        rect_abc = Rectangle(
            width=0.5, height=1.5 * 1, color=BLUE, fill_opacity=0.5,
            stroke_width=1, stroke_color=BLACK
        ).\
            next_to(rect_abb, RIGHT, buff=0).\
            align_to(rect_abb, UP)

        txt_c = Tex(r"$c$", font_size=30, color=BLACK).\
            next_to(rect_bcc, UP, buff=0.1)
        txt_ab = Tex(r"$ab$", font_size=30, color=BLACK).\
            next_to(rect_aba, LEFT, buff=0.1)

        self.play(
            FadeIn(rect_aba),
            FadeIn(rect_abb),
            FadeIn(rect_bcc),
            FadeIn(rect_acc),
            FadeIn(rect_abc),
            Write(txt_c),
            Write(txt_ab)
        )

        txt_abc_3 = Tex(r"$abc$", font_size=30, color=BLACK).\
            move_to(rect_abc.get_center_of_mass())
        self.play(
            Transform(txt_c, txt_abc_3),
            Transform(txt_ab, txt_abc_3)
        )
        

        # Write the inequalities
        inequalities = [
            Tex(r"$3abc$", font_size=30, color=BLACK),
            Tex(r"$ \leq $", font_size=30, color=BLACK),
            Tex(r"$a^3 + b^3 + c^3$", font_size=30, color=BLACK)
        ]
        inequalities = VGroup(*inequalities).arrange(RIGHT).move_to([0, 2, 0])

        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, 2, 0])
        txt = txt = Tex(
            r"$3abc$",
            r" $ \leq $ ",
            r"$a^3$", r"$~+~$", r"$b^3$", r"$~+~$", r"$c^3$",
            font_size=32, color=BLACK
         ).move_to([0, 2, 0])

        rect.z_index = 0
        txt.z_index = 1
        self.play(
            Create(rect),
            run_time=0.5
        )
        self.play(
            TransformFromCopy(txt_abc[0], txt[0]),
            TransformFromCopy(txt_abc_2[0], txt[0].copy()),
            TransformFromCopy(txt_abc_3[0], txt[0].copy()),
            Write(txt[1]),
            TransformFromCopy(txt_a3[0], txt[2]),
            Write(txt[3]),
            TransformFromCopy(txt_b3[0], txt[4]),
            Write(txt[5]),
            TransformFromCopy(txt_c3[0], txt[6]),
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