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
        ax = NumberPlane(
            x_range = (1, 2, 0.1),
            y_range = (0, 1, 0.1),
            x_length = 5,
            y_length = 5,
            axis_config={
                "include_numbers": False,
                "color": WHITE,
                "stroke_width": 0,
            },
            background_line_style={
                "stroke_color": WHITE,
                "stroke_width": 0,
                "stroke_opacity": 0
            }
        ).scale(0.5).move_to([0, 1, 0])

        # Create the square
        point_a = ax.c2p(1, 1)
        left = ax.get_vertical_line(
            point_a, line_func=Line, color=BLACK, stroke_width=2
        )

        point_b = ax.c2p(2, 1)
        right = ax.get_vertical_line(
            point_b, line_func=Line, color=BLACK, stroke_width=2
        )

        down = ax.plot(lambda x: 0, x_range=[1, 2], color=BLACK, stroke_width=2)
        up = ax.plot(lambda x: 1, x_range=[1, 2], color=BLACK, stroke_width=2)

        txt_1 = Tex(r"$1$", font_size=18, color=BLACK)\
            .next_to(ax.c2p(1, 0), DOWN, buff=0.1)
        txt_2 = Tex(r"$2$", font_size=18, color=BLACK)\
            .next_to(ax.c2p(2, 0), DOWN, buff=0.1)
        self.play(
            Create(left),
            Create(right),
            Create(down),
            Create(up),
            Write(txt_1),
            Write(txt_2),
        )

        square_1 = Polygon(
            ax.c2p(1, 0), ax.c2p(2, 0),
            ax.c2p(2, 1), ax.c2p(1, 1),
            stroke_color=BLACK, stroke_width=0,
            fill_color=RED, fill_opacity=0.8
        )
        txt_1 = Tex(r"$1$", font_size=28, color=BLACK)\
            .move_to([-1.75, -1, 0])
        self.play(
            Create(square_1),
            Write(txt_1)
        )

        # Create the 1/x
        graph = ax.plot(
            lambda x: 1 / x,
            x_range=[1, 2],
            color=BLACK,
            stroke_width = 2,
        )
        txt_fx = Tex(r"$f(x) = \frac{1}{x}$", font_size=28, color=BLACK).\
            next_to(ax.c2p(1.5, 1), UP, buff=0.1)
        graph.z_index = 1
        self.play(
            Create(graph),
            Write(txt_fx)
        )

        # For the -1/2
        txt_32 = Tex(r"$3/2$", font_size=18, color=BLACK)\
            .next_to(ax.c2p(3/2, 0), DOWN, buff=0.1)
        self.play(Write(txt_32))

        square_12 = Polygon(
            ax.c2p(1, 0), ax.c2p(3/2, 0),
            ax.c2p(3/2, 1), ax.c2p(1, 1),
            stroke_color=BLACK, stroke_width=0,
            fill_color=RED, fill_opacity=0.8
        )
        txt_12 = Tex(r"$-\frac{1}{2}$", font_size=28, color=BLACK)\
            .next_to(txt_1, RIGHT, buff=0.1)
        self.play(
            Transform(square_1, square_12),
            Write(txt_12)
        )

        # For the +1/3
        txt_23 = Tex(r"$2/3$", font_size=18, color=BLACK)\
            .next_to(ax.c2p(2, 2/3), RIGHT, buff=0.1)
        self.play(Write(txt_23))

        square_13 = Polygon(
            ax.c2p(3/2, 0), ax.c2p(2, 0),
            ax.c2p(2, 2/3), ax.c2p(3/2, 2/3),
            stroke_color=BLACK, stroke_width=0,
            fill_color=RED, fill_opacity=0.8
        )
        txt_13 = Tex(r"$+\frac{1}{3}$", font_size=28, color=BLACK)\
            .next_to(txt_12, RIGHT, buff=0.1)
        self.play(
            Create(square_13),
            Write(txt_13)
        )

        # For the -1/4
        txt_54 = Tex(r"$5/4$", font_size=18, color=BLACK)\
            .next_to(ax.c2p(5/4, 0), DOWN, buff=0.1)
        self.play(Write(txt_54))

        square_14 = Polygon(
            ax.c2p(1, 0), ax.c2p(5/4, 0),
            ax.c2p(5/4, 1), ax.c2p(1, 1),
            stroke_color=BLACK, stroke_width=0,
            fill_color=RED, fill_opacity=0.8
        )
        txt_14 = Tex(r"$-\frac{1}{4}$", font_size=28, color=BLACK)\
            .next_to(txt_13, RIGHT, buff=0.1)
        self.play(
            Transform(square_1, square_14),
            Write(txt_14)
        )

        # For the +1/5
        txt_45 = Tex(r"$4/5$", font_size=18, color=BLACK)\
            .next_to(ax.c2p(2, 4/5), RIGHT, buff=0.1)
        self.play(Write(txt_45))

        square_15 = Polygon(
            ax.c2p(5/4, 0), ax.c2p(3/2, 0),
            ax.c2p(3/2, 4/5), ax.c2p(5/4, 4/5),
            stroke_color=BLACK, stroke_width=0,
            fill_color=RED, fill_opacity=0.8
        )
        txt_15 = Tex(r"$+\frac{1}{5}$", font_size=28, color=BLACK)\
            .next_to(txt_14, RIGHT, buff=0.1)
        self.play(
            Create(square_15),
            Write(txt_15)
        )

        # For the -1/6
        txt_74 = Tex(r"$7/4$", font_size=18, color=BLACK)\
            .next_to(ax.c2p(7/4, 0), DOWN, buff=0.1)
        self.play(Write(txt_74))

        square_16 = Polygon(
            ax.c2p(3/2, 0), ax.c2p(7/4, 0),
            ax.c2p(7/4, 2/3), ax.c2p(3/2, 2/3),
            stroke_color=BLACK, stroke_width=0,
            fill_color=RED, fill_opacity=0.8
        )
        txt_16 = Tex(r"$-\frac{1}{6}$", font_size=28, color=BLACK)\
            .next_to(txt_15, RIGHT, buff=0.1)
        self.play(
            Transform(square_13, square_16),
            Write(txt_16)
        )

        # For the +1/7
        txt_47 = Tex(r"$4/7$", font_size=18, color=BLACK)\
            .next_to(ax.c2p(2, 4/7), RIGHT, buff=0.1)
        self.play(Write(txt_47))

        square_17 = Polygon(
            ax.c2p(7/4, 0), ax.c2p(2, 0),
            ax.c2p(2, 4/7), ax.c2p(7/4, 4/7),
            stroke_color=BLACK, stroke_width=0,
            fill_color=RED, fill_opacity=0.8
        )
        txt_17 = Tex(r"$+\frac{1}{7}$", font_size=28, color=BLACK)\
            .next_to(txt_16, RIGHT, buff=0.1)
        self.play(
            Create(square_17),
            Write(txt_17)
        )

        # Area under the curve
        txt_points = Tex(r"$+ \cdots$", font_size=28, color=BLACK)\
            .next_to(txt_17, RIGHT, buff=0.1)
        self.play(Write(txt_points))

        rectangles = VGroup(square_1, square_13, square_15, square_17)
        x_vals = np.arange(1, 2.01, 0.01)
        points = [
            graph.get_point_from_function(x) for x in x_vals
        ]
        region_under = Polygon(
            *[ax.c2p(1, 0), *points, ax.c2p(2, 0)],
            stroke_width=0,
            fill_color=RED,
            fill_opacity=0.8
        )
        txt_group = VGroup(
            txt_1, txt_12, txt_13, txt_14, txt_15, txt_16, txt_17
        )
        txt_area = Tex(
            r"$= \int_1^2 \frac{1}{x} dx = \ln(2)$", font_size=28, color=BLACK)\
            .next_to(txt_group.get_center(), DOWN, buff=0.5)
        self.play(
            Transform(rectangles, region_under),
            Write(txt_area)
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