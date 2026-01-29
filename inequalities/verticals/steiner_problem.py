"""
Visual proof of the Steiner's problem.
Proofs without Words III. Roger B. Nelsen. p. 108.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Line, Polygon
from manim import Text, Tex, Transform, ValueTracker, ApplyMethod, DashedLine
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


class Steiner(MovingCameraScene):
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
            Tex(r"Le problème de", font_size=48, color=BLACK),
            Tex(r"Steiner", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Roger B. Nelsen", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        results = [
            Tex(r"Pour quel $x > 0$,", font_size=24, color=BLACK),
            Tex(r"$\sqrt[x]{x}$ est-il le plus grand ?", font_size=24, color=BLACK),
        ]
        results = VGroup(*results).arrange(DOWN).move_to([0, -1, 0])

        self.add(
            txt_title,
            txt,
            results
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt),
            Uncreate(results)
        )

        # Create the graph
        
        ax = NumberPlane(
            x_range = (0, 5),
            y_range = (0, 5, 0.2),
            x_length = 7,
            y_length = 5,
            axis_config={
                "include_numbers": False,
                "color": BLACK,
            },
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        ).scale(0.6)


        graph_1 = ax.plot(
            lambda x: x,
            x_range=[0, 5],
            color=BLACK,
            stroke_width = 4,
        )

        txt_f = Tex(r"$y = x$", font_size=28, color=BLACK)\
            .next_to(ax.c2p(4, 4), DOWN + 0.5 * RIGHT)
        
        # Add point (0, 0)
        point_0 = ax.c2p(0, 0)
        txt_0 = Tex(r"0", font_size=18, color=BLACK).next_to(point_0, DOWN, buff=0.1)  

        self.play(
            Create(ax),
            Create(txt_f),
            Create(graph_1),
            Write(txt_0)
        )

        graph_2 = ax.plot(
            lambda x: np.exp(x / np.exp(1)),
            x_range=[0, 5],
            color=RED,
            stroke_width = 4,
        )

        txt_f2 = Tex(r"$y = e^{x/e}$", font_size=28, color=BLACK)\
            .next_to(ax.c2p(4, 5), UP)
        
        # Add point (0, 1)
        point_1 = ax.c2p(0, 1)
        txt_1 = Tex(r"1", font_size=18, color=BLACK).\
            next_to(point_1, DOWN + RIGHT, buff=0.1)

        self.play(
            Create(txt_f2),
            Create(graph_2),
            Write(txt_1)
        )

        # Add point (e, e)
        point_e = ax.c2p(2.718281828459045, 2.718281828459045)
        point_e0 = ax.c2p(2.718281828459045, 0)
        point_e1 = ax.c2p(0, 2.718281828459045)
        txt_e = Tex(r"$e$", font_size=28, color=BLACK).next_to(point_e0, DOWN)
        txt_e1 = Tex(r"$e$", font_size=28, color=BLACK).next_to(point_e1, UP + RIGHT)
        line_e = ax.get_vertical_line(point_e, line_func=DashedLine, color=BLACK)
        line_e1 = ax.get_horizontal_line(point_e, line_func=DashedLine, color=BLACK)
        self.play(
            Write(txt_e),
            Write(txt_e1),
            Create(line_e),
            Create(line_e1)
        )

        self.wait(2)

        txt_in = Tex(r"$x \leq \exp(x / e)$",font_size=28, color=BLACK).\
            next_to(ax, 2.5 * DOWN)
        self.play(Write(txt_in))

        self.wait(1)


        # Second graph        
        ax_2 = NumberPlane(
            x_range = (0, 5),
            y_range = (0, 2, 0.2),
            x_length = 7,
            y_length = 5,
            axis_config={
                "include_numbers": False,
                "color": BLACK,
            },
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.6
            }
        ).scale(0.6)

        
        graph_3 = ax_2.plot(
            lambda x: np.sqrt(x),
            x_range=[0, 5],
            color=BLUE,
            stroke_width = 4,
        )

        txt_f3 = Tex(r"$y = t^{1/x}$", font_size=28, color=BLACK)\
            .next_to(ax_2.c2p(4, 2), UP + LEFT)

        self.play(
            Transform(ax, ax_2),
            Transform(graph_2, graph_3),
            Uncreate(graph_1),
            Uncreate(txt_f),
            Uncreate(txt_f2),
            Uncreate(line_e1),
            Uncreate(txt_e1),
            Uncreate(line_e),
            Uncreate(txt_e),
            Uncreate(txt_1),
            Write(txt_f3)
        )

        # Add points
        point_a = ax_2.c2p(1, np.sqrt(1))
        point_a1 = ax_2.c2p(1, 0)
        point_a2 = ax_2.c2p(0, np.sqrt(1))
        txt_a = Tex(r"$x$", font_size=28, color=BLACK).next_to(point_a1, DOWN)
        txt_a1 = Tex(r"$x^{1/x}$", font_size=28, color=BLACK).next_to(point_a2, UP + RIGHT)
        line_a = ax_2.get_vertical_line(point_a, line_func=DashedLine, color=BLACK)
        line_a1 = ax_2.get_horizontal_line(point_a, line_func=DashedLine, color=BLACK)
        self.play(
            Write(txt_a),
            Write(txt_a1),
            Create(line_a),
            Create(line_a1)
        )
        
        point_b = ax_2.c2p(np.exp(2 / np.exp(1)), np.exp(1 / np.exp(1)))
        point_b1 = ax_2.c2p(np.exp(2 / np.exp(1)), 0)
        point_b2 = ax_2.c2p(0, np.exp(1 / np.exp(1)))
        txt_b = Tex(r"$e^{x / e}$", font_size=28, color=BLACK).next_to(point_b1, 0.9 * DOWN)
        txt_b1 = Tex(r"$e^{1 / e}$", font_size=28, color=BLACK).next_to(point_b2, UP + RIGHT)
        line_b = ax_2.get_vertical_line(point_b, line_func=DashedLine, color=BLACK)
        line_b1 = ax_2.get_horizontal_line(point_b, line_func=DashedLine, color=BLACK)
        self.play(
            Write(txt_b),
            Write(txt_b1),
            Create(line_b),
            Create(line_b1)
        )
        
        txt_in2 = Tex(r"$x^{1 /x} \leq \exp(1 / e)$",font_size=28, color=BLACK).\
            next_to(txt_in, DOWN)
        self.play(Write(txt_in2))

        self.wait(1)

        txt_in3 = Tex(r"$\sqrt[x]{x} \leq \sqrt[e]{e}$",font_size=28, color=BLACK).\
            next_to(txt_in, DOWN)
        self.play(Transform(txt_in2, txt_in3))


        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine, vol. 82,", font_size=26, color=BLACK),
            Tex(r"no. 2 (April 2009), p.102", font_size=26, color=BLACK)
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