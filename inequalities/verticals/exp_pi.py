"""
Visual proof of e^pi > pi^e.
Proofs without Words I. Roger B. Nelsen. p. 58.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Line, Polygon
from manim import Text, Tex, Transform, ValueTracker, ApplyMethod
from manim import NumberPlane, always_redraw

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

        # Equation
        txt_eq = [
            Tex(r"$e^\pi > \pi^e$", font_size=32, color=BLACK),
            Tex(r"$\Longleftrightarrow$", font_size=32, color=BLACK),
            Tex(r"$\frac{\log e}{e} > \frac{\log \pi}{\pi}$", font_size=32, color=BLACK),
        ]
        txt_eq = VGroup(*txt_eq).arrange(DOWN).move_to([0, 2.5, 0])
        self.play(Write(txt_eq))


        # Create the graph
        
        ax = NumberPlane(
            x_range = (1, 5),
            y_range = (-0.6, 0.6, 0.2),
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
        ).scale(0.5).move_to([0, -0.5, 0])

        ax_x = ax.get_x_axis()
        ax_x.numbers.set_color(BLACK)
        ax_y = ax.get_y_axis()
        ax_y.numbers.set_color(BLACK)

        graph = ax.plot(
            lambda x: np.log(x) / x,
            x_range=[1, 5],
            color=BLACK,
            stroke_width = 4,
        )

        txt_f = Tex(r"$f(x) = \frac{\log x}{x}$", font_size=28, color=BLACK)\
            .next_to(ax.c2p(4, 0.4), UP)
        
        self.play(
            Create(ax),
            Create(txt_f),
            Create(graph)
        )

        
        ax_2 = NumberPlane(
            x_range = (2.5, 3.5, 0.1),
            y_range = (0.36, 0.37, 0.001),
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
        ).scale(0.5).move_to([0, -0.5, 0])

        ax_x = ax_2.get_x_axis()
        ax_x.numbers.set_color(BLACK)
        ax_y = ax_2.get_y_axis()
        ax_y.numbers.set_color(BLACK)

        
        graph_2 = ax_2.plot(
            lambda x: np.log(x) / x,
            x_range=[2.5, 3.5],
            color=BLACK,
            stroke_width = 4,
        )

        self.play(
            Transform(ax, ax_2),
            Transform(graph, graph_2)
        )

        # Add points
        point_e = ax_2.c2p(2.718281828459045, 0.36)
        txt_e = Tex(r"$e$", font_size=28, color=BLACK).next_to(point_e, DOWN)  
        point = ax_2.c2p(2.718281828459045, 1 / 2.718281828459045)
        line_e = ax_2.get_vertical_line(point, line_func=Line, color=BLACK)

        point_fe = ax_2.c2p(2.5, 1 / 2.718281828459045)
        txt_fe = Tex(r"$\frac{\log e}{e}$", font_size=18, color=BLACK).\
            next_to(point_fe, 0.1 * LEFT)  
        line_fe = ax_2.get_horizontal_line(point, line_func=Line, color=BLACK)
        self.play(
            Write(txt_e),
            Write(txt_fe),
            Write(line_e),
            Create(line_fe)
        )

        point_pi = ax_2.c2p(3.141592653589793, 0.36)
        txt_pi = Tex(r"$\pi$", font_size=28, color=BLACK).next_to(point_pi, DOWN)  
        point = ax_2.c2p(3.141592653589793, np.log(3.141592653589793) / 3.141592653589793)
        line_pi = ax_2.get_vertical_line(point, line_func=Line, color=BLACK)

        point_fpi = ax_2.c2p(2.5, np.log(3.141592653589793) / 3.141592653589793)
        txt_fpi = Tex(r"$\frac{\log \pi}{\pi}$", font_size=18, color=BLACK).\
            next_to(point_fpi, 0.1 * LEFT)  
        line_fpi = ax_2.get_horizontal_line(point, line_func=Line, color=BLACK)
        self.play(
            Write(txt_pi),
            Write(txt_fpi),
            Create(line_pi),
            Create(line_fpi)
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