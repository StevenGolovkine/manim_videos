"""
Visual proof of the sums of odd integers.
Proofs without Words II. Roger B. Nelsen. p. 80.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Line
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


class Young(MovingCameraScene):
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
            Tex(r"Une inégalité d'aire", font_size=48, color=BLACK),
            Tex(r"Théorème de Young", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Young (1912)", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        self.play(
            Write(txt_title),
            Write(txt)
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt)
        )
        self.wait(1)

        # Theorem
        txt_theorem = [
            Tex(r"Soit $f$ une fonction, continue,", font_size=28, color=BLACK),
            Tex(r"strictement croissante, inversible", font_size=28, color=BLACK),
            Tex(r"et tel que $f(0) = 0$ et $f^{-1}(0) = 0$.", font_size=28, color=BLACK),
            Tex(r"Pour $a, b \geq 0$, on a", font_size=28, color=BLACK),
            Tex(r"$ab \leq \int_{0}^a f(x)dx + \int_{0}^b f^{-1}(x)dx$", font_size=28, color=BLACK)
        ]
        txt_theorem = VGroup(*txt_theorem)\
            .arrange(DOWN, aligned_edge=LEFT, center=False, buff=0.1)\
                .move_to([0, 2.5, 0])

        self.play(Write(txt_theorem))

        # b > f(a)
        txt = Tex(r"Pour $b > f(a)$:", font_size=28, color=BLACK)\
            .move_to([-1.25, 1, 0])
        self.play(Write(txt))


        ax = Axes(
            x_range=[0, 1, 0.1],
            y_range=[-0.1, 2, 0.2],
            x_length=7,
            y_length=7,
            tips=False,
            x_axis_config={
                "color": BLACK,
            },
            y_axis_config={
                "color": BLACK
            }
        ).scale(0.5).move_to([0, -1.25, 0])

        graph = ax.plot(
            lambda x: x + 0.1 * x**3 + 0.5 * x**5,
            x_range=[0, 1],
            use_smoothing=False,
            color=BLACK
        )
        self.play(
            Create(ax),
            Create(graph)
        )

        point = ax.c2p(0.972669, 1.5)
        line_b = ax.get_horizontal_line(point, line_func=Line, color=BLACK)
        self.play(Create(line_b))

        point = ax.c2p(0.8, 1.5)
        line_a = ax.get_vertical_line(point, line_func=Line, color=BLACK)
        self.play(Create(line_a))

        area = ax.get_area(
            graph,
            x_range=(0, 0.8),
            color=BLUE,
            opacity=0.8,
        )
        self.add(area)

        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"On classes of summable", font_size=26, color=BLACK),
            Tex(r"functions and their Fourier series", font_size=26, color=BLACK),
            Tex(r"Proc. Royal Soc. (A), 87,", font_size=26, color=BLACK),
            Tex(r"W. H. Young (1912), pp. 225-229", font_size=26, color=BLACK)
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