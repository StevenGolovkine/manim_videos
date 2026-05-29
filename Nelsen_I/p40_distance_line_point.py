"""
Visual proof of The distance between a point and a line segment.
Proofs without Words I. Roger B. Nelsen. p. 40.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, Group, RightAngle
from manim import Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Dot, Line, Polygon
from manim import Text, Tex, DashedVMobject, DashedLine, RoundedRectangle

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


class Distance(MovingCameraScene):
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
            Tex(r"Distance entre", font_size=48, color=BLACK),
            Tex(r"une ligne et", font_size=48, color=BLACK),
            Tex(r"un point", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"R. L. Eisenman", font_size=28, color=BLACK)
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


        # Graphs
        ax = Axes(
            x_range=[-0.1, 1, 0.1],
            y_range=[-0.1, 2, 0.1],
            x_length=7,
            y_length=10,
            tips=False,
            x_axis_config={
                "color": BLACK,
            },
            y_axis_config={
                "color": BLACK
            }
        ).scale(0.5).move_to([0, 0, 0])

        self.play(Create(ax))

        graph = ax.plot(
            lambda x: 3*x - 0.15,
            x_range=[-0.1, 0.9],
            use_smoothing=False,
            color=BLACK
        )
        txt_line = Tex(
            r"$y = mx + c$",
            font_size=20, color=BLACK
        ).next_to(ax.c2p(-0.05, -3*0.05 - 0.15), RIGHT, buff=0.2)
        self.play(
            Create(graph),
            Create(txt_line)
        )

        # Point
        point = Dot(ax.c2p(0.8, 0.5), color=RED, stroke_width=3)
        txt_point = Tex(
            r"$(a, b)$",
            font_size=16, color=BLACK
        ).next_to(point.get_center(), DOWN + RIGHT, buff=0.1)
        self.play(
            Create(point),
            Write(txt_point)
        )

        # Line point to line
        line = Line(
            start=ax.c2p(0.8, 3*0.8 - 0.15),
            end=ax.c2p(0.2, 3*0.2 - 0.15),
            color=BLACK
        )
        line_perp = Line(
            start=ax.c2p(0.8, 0.5),
            end=ax.c2p(0.325, 0.825),
            color=BLACK
        )
        txt_d = Tex(
            r"$d$",
            font_size=20, color=BLACK
        ).next_to(line_perp.get_center(), LEFT + DOWN, buff=0.1)
        r_angle = RightAngle(
            line_perp,
            line,
            length=0.2,
            quadrant=(-1, 1),
            stroke_width=1,
            color=BLACK
        )
        self.play(
            Create(line_perp),
            Create(txt_d),
            Create(r_angle)
        )

        # Vertical line from point to line
        line_vert = DashedLine(
            start=ax.c2p(0.8, 0.5),
            end=ax.c2p(0.8, 3*0.8 - 0.15),
            color=BLACK
        )
        point_proj = Dot(ax.c2p(0.8, 3*0.8 - 0.15), color=BLACK, stroke_width=1)
        txt_point_proj = Tex(
            r"$(a, ma + c)$",
            font_size=16, color=BLACK
        ).next_to(point_proj.get_center(), LEFT, buff=0.3)
        self.play(
            Create(line_vert),
            Write(txt_point_proj),
        )

        # Distance
        txt_v = Tex(
            r"$| ma +c - b |$",
            font_size=24, color=BLACK
        ).rotate(-PI / 2).next_to(line_vert.get_center(), RIGHT, buff=0.2)
        self.play(
            Create(txt_v)
        )

        # Smaller triangle
        point_base = Dot(ax.c2p(0.6, 1), color=BLACK, stroke_width=1)
        line_ver = DashedLine(
            start=ax.c2p(0.6, 1),
            end=ax.c2p((1 + 0.15) / 3, 1),
            color=BLACK
        )
        line_hor = DashedLine(
            start=ax.c2p(0.6, 3*0.6 - 0.15),
            end=ax.c2p(0.6, 1),
            color=BLACK
        )
        r_angle_2 = RightAngle(
            line_hor,
            line_ver,
            length=0.2,
            quadrant=(-1, 1),
            stroke_width=1,
            color=BLACK
        )
        txt_1 = Tex(
            r"$1$",
            font_size=16, color=BLACK
        ).next_to(line_ver.get_center(), DOWN, buff=0.1)
        txt_m = Tex(
            r"$m$",
            font_size=16, color=BLACK
        ).next_to(line_hor, RIGHT, buff=0.1)
        self.play(
            Create(point_base),
            Create(line_ver),
            Create(line_hor),
            Create(r_angle_2),
            Write(txt_m),
            Write(txt_1)
        )

        # Distance formula
        txt_dist_formula = Tex(
            r"$\sqrt{1 + m^2}$",
            font_size=24, color=BLACK
        ).next_to(ax.c2p(0.5, 3*0.5 - 0.15), LEFT, buff=0.3)
        self.play(
            Create(txt_dist_formula)
        )

        # Write distance formula
        rect = RoundedRectangle(
            height=1, width=2.5,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0.5, -2, 0])
        txt_final = Tex(
            r"$\frac{d}{1} = \frac{| ma + c - b |}{\sqrt{1 + m^2}}$",
            font_size=32, color=BLACK
        ).move_to([0.5, -2, 0])
        self.play(
            Create(rect),
            Write(txt_final)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine,", font_size=26, color=BLACK),
            Tex(r"vol. 42, no. 1 (Jan. 1969), pp. 40-41.", font_size=26, color=BLACK)
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