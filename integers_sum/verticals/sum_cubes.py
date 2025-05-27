"""
Visual proof of the sums of cubes.
Proofs without Words I. Roger B. Nelsen. p. 87.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Dot, Brace, RoundedRectangle, Square, MobjectTable
from manim import Create, Uncreate, Write
from manim import VGroup, Transform, FadeIn, FadeOut, FunctionGraph
from manim import Text, Tex

from manim import config

from manim import LEFT, RIGHT, DOWN, LIGHT, UP, PI

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
            Tex(r"Démonstration I", font_size=36, color=BLACK),
            Tex(r"Cupillari and Lushbaugh", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        txt_formula = Tex(r"$1^3 + 2^3 + \cdots + n = \frac{1}{4}n^2(n + 1)^2$", font_size=28, color=BLACK)\
            .next_to(txt, 2 * DOWN)

        self.add(
            txt_title,
            txt,
            txt_formula
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt),
            Uncreate(txt_formula),
            run_time=0.5
        )
        self.wait(0.5)

        # Create small squares
        s = Square(
            side_length=0.1, stroke_width=1,
            color=WHITE, stroke_color=WHITE, fill_opacity=1
        )
        t5 = MobjectTable(
            [
                [s.copy(), s.copy(), s.copy(), s.copy(), s.copy()],
                [s.copy(), s.copy(), s.copy(), s.copy(), s.copy()],
                [s.copy(), s.copy(), s.copy(), s.copy(), s.copy()],
                [s.copy(), s.copy(), s.copy(), s.copy(), s.copy()],
                [s.copy(), s.copy(), s.copy(), s.copy(), s.copy()]
            ],
            h_buff=0, v_buff=0,
            line_config={
                "stroke_color": BLACK,
                "stroke_width": 1,
            },
            include_outer_lines=True,
        )
        t5.get_vertical_lines()[0].set_color(RED)
        t5.get_horizontal_lines()[0].set_color(RED)
        t5.get_vertical_lines()[1].set_color(RED)
        t5.get_horizontal_lines()[1].set_color(RED)
        t5_c = t5.copy().next_to(t5, RIGHT, buff=0)
        t5_cc = t5.copy().next_to(t5_c, RIGHT, buff=0)
        t5_ccc = t5.copy().next_to(t5, LEFT, buff=0)
        t5_cccc = t5.copy().next_to(t5_ccc, LEFT, buff=0)

        t4 = MobjectTable(
            [
                [s.copy(), s.copy(), s.copy(), s.copy()],
                [s.copy(), s.copy(), s.copy(), s.copy()],
                [s.copy(), s.copy(), s.copy(), s.copy()],
                [s.copy(), s.copy(), s.copy(), s.copy()]
            ],
            h_buff=0, v_buff=0,
            line_config={
                "stroke_color": BLACK,
                "stroke_width": 1,
            },
            include_outer_lines=True,
        ).next_to(t5, UP, buff=0).shift(0.25 * RIGHT)
        t4.get_vertical_lines()[0].set_color(RED)
        t4.get_horizontal_lines()[0].set_color(RED)
        t4.get_vertical_lines()[1].set_color(RED)
        t4.get_horizontal_lines()[1].set_color(RED)
        t4_c = t4.copy().next_to(t4, RIGHT, buff=0)
        t4_cc = t4.copy().next_to(t4, LEFT, buff=0)
        t4_ccc = t4.copy().next_to(t4_cc, LEFT, buff=0)

        t3 = MobjectTable(
            [
                [s.copy(), s.copy(), s.copy()],
                [s.copy(), s.copy(), s.copy()],
                [s.copy(), s.copy(), s.copy()]
            ],
            h_buff=0, v_buff=0,
            line_config={
                "stroke_color": BLACK,
                "stroke_width": 1,
            },
            include_outer_lines=True,
        ).next_to(t4, UP, buff=0).shift(0.15 * RIGHT)
        t3.get_vertical_lines()[0].set_color(RED)
        t3.get_horizontal_lines()[0].set_color(RED)
        t3.get_vertical_lines()[1].set_color(RED)
        t3.get_horizontal_lines()[1].set_color(RED)
        t3_c = t3.copy().next_to(t3, LEFT, buff=0)
        t3_cc = t3.copy().next_to(t3_c, LEFT, buff=0)

        t2 = MobjectTable(
            [
                [s.copy(), s.copy()],
                [s.copy(), s.copy()],
            ],
            h_buff=0, v_buff=0,
            line_config={
                "stroke_color": BLACK,
                "stroke_width": 1,
            },
            include_outer_lines=True,
        ).next_to(t3, UP, buff=0).shift(0.15 * LEFT)
        t2.get_vertical_lines()[0].set_color(RED)
        t2.get_horizontal_lines()[0].set_color(RED)
        t2.get_vertical_lines()[1].set_color(RED)
        t2.get_horizontal_lines()[1].set_color(RED)
        t2_c = t2.copy().next_to(t2, LEFT, buff=0)

        t1 = s.copy().set_stroke(RED).next_to(t2, UP, buff=0).shift(0.05 * LEFT)
        
        self.play(
            Create(t5),
            Create(t5_c),
            Create(t5_cc),
            Create(t5_ccc),
            Create(t5_cccc),
        )

        self.play(
            Create(t4),
            Create(t4_c),
            Create(t4_cc),
            Create(t4_ccc),
        )

        self.play(
            Create(t3),
            Create(t3_c),
            Create(t3_cc),
        )

        self.play(
            Create(t2),
            Create(t2_c)
        )

        self.play(
            Create(t1),
        )

        g = VGroup(
            t5, t5_c, t5_cc, t5_ccc, t5_cccc,
            t4, t4_c, t4_cc, t4_ccc,
            t3, t3_c, t3_cc,
            t2, t2_c,
            t1
        )
        g_c = g.copy().set_stroke(BLUE, width=1)
        self.play(
            g_c.animate.rotate(PI / 2).\
                next_to(g, RIGHT, aligned_edge=DOWN, buff=-0.99),
        )

        g_cc = g_c.copy().set_stroke(ORANGE, width=1)
        self.play(
            g_cc.animate.rotate(PI / 2).\
                next_to(g_c, UP, aligned_edge=RIGHT, buff=-0.99),
        )

        g_ccc = g_cc.copy().set_stroke(VIOLET, width=1)
        self.play(
            g_ccc.animate.rotate(PI / 2).\
                next_to(g_cc, LEFT, aligned_edge=UP, buff=-0.99),
        )

        b = Brace(g, DOWN, color=BLACK)
        txt_n2 = Tex(
            r"$n^2$", font_size=36, color=BLACK
        ).next_to(b, DOWN, buff=0.1)
        self.play(
            Create(b),
            Write(txt_n2)
        )

        b1 = Brace(g_c[4], DOWN, color=BLACK)
        txt_n = Tex(
            r"$n$", font_size=36, color=BLACK
        ).next_to(b1, DOWN, buff=0.1)
        self.play(
            Create(b1),
            Write(txt_n)
        )

        self.wait(1)

        # Write equation
        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, -2, 0])
        txt = Tex(
            r"$1^3 + 2^3 + \cdots + n^3 = $",
            r"$\frac{1}{4}(n^2 + n)^2$",
            font_size=26, color=BLACK
        ).move_to([0, -2, 0])

        self.play(
            Create(rect),
            Write(txt)
        )

        txt_c = Tex(
            r"$1^3 + 2^3 + \cdots + n^3 = $",
            r"$\frac{1}{4}n^2(n + 1)^2$",
            font_size=26, color=BLACK
        ).move_to([0, -2, 0])
        self.play(
            Transform(txt, txt_c)
        )


        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine, vol. 62,", font_size=30, color=BLACK),
            Tex(r"no. 4 (Oct. 1989), p.259.", font_size=30, color=BLACK),
            Tex(r"Mathematical Gazette, vol. 49", font_size=30, color=BLACK),
            Tex(r"no. 368 (May 1965), p.200", font_size=30, color=BLACK),
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
