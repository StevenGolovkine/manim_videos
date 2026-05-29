"""
Visual proof of the alternating harmonic series.
Proofs without Words I. Roger B. Nelsen. p. 128.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Line, Polygon
from manim import Text, Tex, RoundedRectangle
from manim import NumberPlane, always_redraw

from manim import config
from manim import LEFT, RIGHT, DOWN, LIGHT, UP, BLUE, GREEN

# COLORS
# BLUE = "#B0E1FA"
VIOLET = "#E8C9FA"
RED = "#F79BC5"
# GREEN = "#DBF9E7"
YELLOW = "#EFE9B7"
ORANGE = "#F6CCB0"
BLACK = "#000000"
GREY = "#D0D0D0"
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


class Series(MovingCameraScene):
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
            Tex(r"La série harmonique", font_size=48, color=BLACK),
            Tex(r"alternée", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Mark Finkelstein", font_size=28, color=BLACK)
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

        # Create the graph
        ax = NumberPlane(
            x_range = (0.8, 2.1, 0.1),
            y_range = (0, 1.1, 0.1),
            x_length = 7,
            y_length = 5,
            axis_config={
                "include_numbers": True,
                "color": BLACK,
            },
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        ).scale(0.5).move_to([0, 2, 0])

        graph = ax.plot(
            lambda x: 1 / x,
            x_range=[0.9, 2.1],
            color=BLACK,
            stroke_width = 4,
        )

        txt_f = Tex(r"$f(x) = \frac{1}{x}$", font_size=24, color=BLACK)\
            .next_to(ax.c2p(1.5, 0.8), UP)
        
        self.play(
            Create(ax),
            Create(txt_f),
            Create(graph)
        )

        # ln 2 = integral from 1 to 2 of 1/x
        point_a = ax.c2p(1, 1)
        line_a = ax.get_vertical_line(point_a, line_func=Line, color=BLACK)
        point_b = ax.c2p(2, 1 / 2)
        line_b = ax.get_vertical_line(point_b, line_func=Line, color=BLACK)
        txt_1 = Tex(r"$1$", font_size=18, color=BLACK)\
            .next_to(ax.c2p(1, 0), DOWN, buff=0.1)
        txt_11 = Tex(r"$1$", font_size=18, color=BLACK)\
            .next_to(ax.c2p(1, 1), UP, buff=0.1)
        txt_2 = Tex(r"$2$", font_size=18, color=BLACK)\
            .next_to(ax.c2p(2, 0), DOWN, buff=0.1)
        txt_12 = Tex(r"$\frac{1}{2}$", font_size=18, color=BLACK)\
            .next_to(ax.c2p(2, 1 / 2), UP, buff=0.1)
        self.play(
            Create(line_a),
            Create(line_b),
            Create(txt_1),
            Create(txt_11),
            Create(txt_2),
            Create(txt_12)
        )

        txt_ln2 = Tex(
            r"$\ln(2)$", font_size=24, color=BLACK
        ).move_to([-1.5, 0, 0])
        txt_int = Tex(
            r"$= \int_1^2 \frac{1}{x} \, dx$", font_size=24, color=BLACK
        ).next_to(txt_ln2, RIGHT, buff=0.1)
        self.play(
            Write(txt_ln2),
            Write(txt_int)
        )

        # 1 - 1/2
        point_a = ax.c2p(1, 1 / 2)
        point_b = ax.c2p(2, 1 / 2) 
        line_h = Line(point_a, point_b, color=BLACK, stroke_width=2)
        txt = Tex(r"$1 - \frac{1}{2}$", font_size=24, color=BLACK).\
            move_to(ax.c2p(1.5, 0.25))
        txt_2 = Tex(r"$= 1 - \frac{1}{2}$", font_size=24, color=BLACK).\
            next_to(txt_int, DOWN, aligned_edge=LEFT)
        self.play(
            Create(line_h),
            Write(txt),
            Write(txt_2),
        )

        # 1/3 - 1/4
        point_a = ax.c2p(3 / 2, 1 / 2)
        point_b = ax.c2p(3 / 2, 2 / 3)
        point_c = ax.c2p(1, 2 / 3)
        line_v = Line(point_a, point_b, color=BLACK, stroke_width=2)
        line_h = Line(point_b, point_c, color=BLACK, stroke_width=2)
        txt = Tex(r"$\frac{1}{3} - \frac{1}{4}$", font_size=24, color=BLACK).\
            move_to(ax.c2p(1.25, 7 / 12))
        txt_3 = Tex(r"$+ \frac{1}{3} - \frac{1}{4}$", font_size=24, color=BLACK).\
            next_to(txt_2, RIGHT, buff=0.1)
        txt_32 = Tex(
            r"$\frac{3}{2}$", font_size=18, color=BLACK
        ).next_to(ax.c2p(3 / 2, 0), DOWN, buff=0.1)
        txt_23 = Tex(
            r"$\frac{2}{3}$", font_size=18, color=BLACK
        ).next_to(ax.c2p(3 / 2, 2 / 3), UP, buff=0.1)
        self.play(
            Create(line_v),
            Create(line_h),
            Write(txt),
            Write(txt_3),
            Create(txt_32),
            Create(txt_23),
        )

        # 1/5 - 1/6
        point_a = ax.c2p(5 / 4, 2 / 3)
        point_b = ax.c2p(5 / 4, 4 / 5)
        point_c = ax.c2p(1, 4 / 5)
        line_v = Line(point_a, point_b, color=BLACK, stroke_width=2)
        line_h = Line(point_b, point_c, color=BLACK, stroke_width=2)
        txt = Tex(r"$\frac{1}{5} - \frac{1}{6}$", font_size=16, color=BLACK).\
            move_to(ax.c2p(9 / 8, 22 / 30))
        txt_4 = Tex(r"$+ \frac{1}{5} - \frac{1}{6}$", font_size=24, color=BLACK).\
            next_to(txt_2, DOWN, aligned_edge=RIGHT)
        txt_54 = Tex(
            r"$\frac{5}{4}$", font_size=18, color=BLACK
        ).next_to(ax.c2p(5 / 4, 0), DOWN, buff=0.1)
        txt_45 = Tex(
            r"$\frac{4}{5}$", font_size=18, color=BLACK
        ).next_to(ax.c2p(5 / 4, 4 / 5), UP, buff=0.1)
        self.play(
            Create(line_v),
            Create(line_h),
            Write(txt),
            Write(txt_4),
            Create(txt_54),
            Create(txt_45),
        )

        # 1 / 7 - 1 / 8
        point_a = ax.c2p(7 / 4, 1 / 2)
        point_b = ax.c2p(7 / 4, 4 / 7)
        point_c = ax.c2p(3 / 2, 4 / 7)
        line_v = Line(point_a, point_b, color=BLACK, stroke_width=2)
        line_h = Line(point_b, point_c, color=BLACK, stroke_width=2)
        txt = Tex(r"$\frac{1}{7} - \frac{1}{8}$", font_size=12, color=BLACK).\
            move_to(ax.c2p(13 / 8, 15 / 28))
        txt_5 = Tex(
            r"$+ \frac{1}{7} - \frac{1}{8} + \cdots$", font_size=24, color=BLACK
        ).next_to(txt_4, RIGHT, buff=0.1)
        txt_74 = Tex(
            r"$\frac{7}{4}$", font_size=18, color=BLACK
        ).next_to(ax.c2p(7 / 4, 0), DOWN, buff=0.1)
        txt_47 = Tex(
            r"$\frac{4}{7}$", font_size=18, color=BLACK
        ).next_to(ax.c2p(7 / 4, 4 / 7), UP, buff=0.1)
        self.play(
            Create(line_v),
            Create(line_h),
            Write(txt),
            Write(txt_5),
            Create(txt_74),
            Create(txt_47),
        )

        # Write equation
        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, -2.5, 0])
        txt = Tex(
            r"$1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots = \ln{2}$",
            font_size=26, color=BLACK
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
            Tex(r"American Mathematical Monthly,", font_size=26, color=BLACK),
            Tex(r"vol. 94, no. 6 (June-July 1988)", font_size=26, color=BLACK),
            Tex(r"pp. 541-542.", font_size=26, color=BLACK)
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