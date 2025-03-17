"""
Visual proof of e^pi > pi^e.
Proofs without Words I. Roger B. Nelsen. p. 58.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Line, Polygon
from manim import Text, Tex, Transform

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


class ExpPi(MovingCameraScene):
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
            Tex(r"$e^\pi > \pi^e$", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Fouad Nakhli", font_size=28, color=BLACK)
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
        ax = Axes(
            x_range=[0.1, 5, 0.5],
            y_range=[-0.5, 0.5, 0.1],
            x_length=7,
            y_length=7,
            tips=False,
            x_axis_config={
                "color": BLACK,
            },
            y_axis_config={
                "color": BLACK
            }
        ).scale(0.5)

        graph = ax.plot(
            lambda x: np.log(x) / x,
            x_range=[0.75, 5],
            use_smoothing=False,
            color=BLACK
        )
        txt_f = Tex(r"$f(x) = \frac{\log x}{x}$", font_size=28, color=BLACK)\
            .next_to(ax.c2p(4, 0.4), UP)
        self.play(
            Create(ax),
            Write(txt_f)
        )
        self.play(
            Create(graph)
        )

        ax_zoom = Axes(
            x_range=[2, 4, 0.1],
            y_range=[0.3, 0.4, 0.05],
            x_length=7,
            y_length=7,
            tips=False,
            x_axis_config={
                "color": BLACK,
            },
            y_axis_config={
                "color": BLACK
            }
        ).scale(0.5)

        graph_zoom = ax.plot(
            lambda x: np.log(x) / x,
            x_range=[2, 4],
            use_smoothing=False,
            color=BLACK
        )

        self.play(
            Transform(ax, ax_zoom),
            Transform(graph, graph_zoom)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine, vol. 60,", font_size=26, color=BLACK),
            Tex(r"no. 3 (June 1987), p.165", font_size=26, color=BLACK)
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