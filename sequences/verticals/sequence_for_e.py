"""
Visual proof of a recursively defined sequences of e.
Proofs without Words I. Roger B. Nelsen. p. 117.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Line, Polygon
from manim import Text, Tex, Transform
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
            Tex(r"Une construction", font_size=48, color=BLACK),
            Tex(r"récursive pour $e$", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Thomas P. Dence", font_size=28, color=BLACK)
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
            x_range=[0, 7, 1],
            y_range=[0, 5, 1],
            x_length=7,
            y_length=7,
            tips=False,
            x_axis_config={
                "color": BLACK,
            },
            y_axis_config={
                "color": BLACK
            }
        ).scale(0.5).move_to([0, 0, 0])

        graph = ax.plot(
            lambda x: x / np.log(x),
            x_range=[1.5, 7],
            use_smoothing=False,
            color=BLACK
        )

        txt_f = Tex(r"$f(x) = \frac{x}{\log x}$", font_size=24, color=BLACK)\
            .next_to(ax.c2p(1.5, 1.5 / np.log(1.5)), 0.5 * UP)
        
        self.play(
            Create(ax),
            Create(txt_f),
            Create(graph)
        )

        graph_xy = ax.plot(
            lambda x: x,
            x_range=[0, 7],
            use_smoothing=False,
            color=GREY
        )
        txt_fx = Tex(r"$f(x) = x$", font_size=24, color=BLACK)\
            .next_to(ax.c2p(6, 6), 0.5 * UP)
        self.play(
            Create(graph_xy),
            Create(txt_fx)
        )

        # Vertical line at x = 1
        line_x1 = always_redraw(lambda: Line(
            start=ax.c2p(1, 0), end=ax.c2p(1, 5),
            color=GREY
        ))
        txt_x1 = Tex(r"$1$", font_size=24, color=BLACK)\
            .next_to(ax.c2p(1, 0), DOWN)
        self.play(
            Create(line_x1),
            Write(txt_x1)
        )

        # x0
        x0 = 6.5
        pt_x0 = ax.c2p(x0, 0)
        pt_fx0 = ax.c2p(x0, x0 / np.log(x0))
        line_x0 = always_redraw(lambda: Line(
            start=pt_x0, end=pt_fx0,
            color=RED
        ))
        txt_x0 = Tex(r"$x_0$", font_size=24, color=RED)\
            .next_to(pt_x0, DOWN)
        self.play(
            Create(line_x0),
            Write(txt_x0)
        )

        # Line from f(x0) to x = y
        line_fx0 = always_redraw(lambda: Line(
            start=pt_fx0, end=ax.c2p(x0 / np.log(x0), x0 / np.log(x0)),
            color=BLUE
        ))
        self.play(
            Create(line_fx0),
        )

        # Line from line_fx0 to f(x1)
        x1 = x0 / np.log(x0)
        pt_x1 = ax.c2p(x1, x1)
        pt_fx1 = ax.c2p(x1, x1 / np.log(x1))
        line_x1 = always_redraw(lambda: Line(
            start=pt_x1, end=pt_fx1,
            color=RED
        ))
        ptt_x1 = ax.c2p(x1, 0)
        txt_x1 = Tex(r"$x_1$", font_size=24, color=RED)\
            .next_to(ptt_x1, DOWN)
        self.play(
            Create(line_x1),
            Write(txt_x1)
        )

        # Line from f(x1) to x = y
        line_fx1 = always_redraw(lambda: Line(
            start=pt_fx1, end=ax.c2p(x1 / np.log(x1), x1 / np.log(x1)),
            color=BLUE
        ))
        self.play(
            Create(line_fx1),
        )

        # Write e + lines to e on x and y
        line_fx1 = always_redraw(lambda: Line(
            start=ax.c2p(np.e, 0), end=ax.c2p(np.e, np.e),
            color=GREEN
        ))
        line_fx2 = always_redraw(lambda: Line(
            start=ax.c2p(0, np.e), end=ax.c2p(np.e, np.e),
            color=GREEN
        ))
        txt_e = Tex(r"$e$", font_size=36, color=GREEN)\
            .next_to(ax.c2p(np.e, 0), DOWN)
        txt_e2 = Tex(r"$e$", font_size=36, color=GREEN)\
            .next_to(ax.c2p(0, np.e), LEFT)
        self.play(
            Create(line_fx1),
            Create(line_fx2),
            Write(txt_e),
            Write(txt_e2)
        )   

        # Write final results
        txt_result = Tex(
            r"$x_1 > 1$ et $x_{n+1} = \frac{x_n}{\log(x_n)}$",
            color=BLACK, font_size=28
        ).move_to([0, -2.5, 0])
        txt_result2 = Tex(
            r"alors $\lim_{n \to +\infty} x_n = e$.",
            color=BLACK, font_size=28
        ).next_to(txt_result, DOWN, buff=0.2)
        txt_result = VGroup(txt_result, txt_result2)

        self.play(
            Write(txt_result)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine, vol. 66,", font_size=26, color=BLACK),
            Tex(r"no. 3 (June 1993), p. 179.", font_size=26, color=BLACK),
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