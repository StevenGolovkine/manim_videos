"""
Visual proof of The Midpoint Rule is better than the trapezoidal rule for concave f.
Proofs without Words I. Roger B. Nelsen. p. 41.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, Group
from manim import Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Dot, Line, Polygon
from manim import Text, Tex, DashedVMobject, DashedLine, RoundedRectangle

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


class Trapz(MovingCameraScene):
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
            Tex(r"Comment intégrer", font_size=48, color=BLACK),
            Tex(r"des fonctions concaves ?", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Frank Burk", font_size=28, color=BLACK)
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

        # Theorem
        txt_theorem = [
            Tex(r"Pour une fonction concave,", font_size=28, color=BLACK),
            Tex(r"la méthode du point médian ", font_size=28, color=BLACK),
            Tex(r"est plus précise que", font_size=28, color=BLACK),
            Tex(r"la méthode des trapèzes.", font_size=28, color=BLACK),
        ]
        txt_theorem = VGroup(*txt_theorem)\
            .arrange(DOWN, aligned_edge=LEFT, center=False, buff=0.1)\
                .move_to([0, 3, 0])

        self.play(Write(txt_theorem))

        # Graph
        txt = Tex(r"Méthode du point médian:", font_size=28, color=BLACK)\
            .move_to([-0.2, 0.7, 0])
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
            lambda x: - 9 * (x - 0.5)**2 + 1.5,
            x_range=[0.2, 0.7],
            use_smoothing=False,
            color=BLACK
        )
        txt_a = Tex(r"$a$", font_size=28, color=BLACK)\
            .next_to(ax.c2p(0.2, 0), DOWN)
        txt_b = Tex(r"$b$", font_size=28, color=BLACK)\
            .next_to(ax.c2p(0.7, 0), DOWN)
        txt_ab = Tex(r"$\frac{a + b}{2}$", font_size=28, color=BLACK)\
            .next_to(ax.c2p(0.45, 0), DOWN)
        point = ax.c2p(0.45, - 9 * (0.45 - 0.5)**2 + 1.5)
        p_fab = Dot(point, color=BLACK)
        txt_fab = Tex(r"$f(\frac{a + b}{2})$", font_size=28, color=BLACK)\
            .next_to(point, UP)
        
        self.play(
            Create(ax),
            Create(graph),
            Write(txt_a),
            Write(txt_b),
            Write(txt_ab),
            Create(p_fab),
            Write(txt_fab)
        )

        point_a = ax.c2p(0.2, - 9 * (0.45 - 0.5)**2 + 1.5)
        line_a = ax.get_vertical_line(point_a, line_func=Line, color=BLACK)
        point_b = ax.c2p(0.7, - 9 * (0.45 - 0.5)**2 + 1.5)
        line_b = ax.get_vertical_line(point_b, line_func=Line, color=BLACK)
        line_ab = ax.plot(
            lambda x: - 9 * (0.45 - 0.5)**2 + 1.5,
            x_range=[0.2, 0.7],
            use_smoothing=False,
            color=BLACK,
            stroke_width=2
        )

        points = [ax.c2p(0.2, 0), point_a, point_b, ax.c2p(0.7, 0)]
        region_midpoint = Polygon(
            *points,
            stroke_width=0,
            fill_color=BLUE,
            fill_opacity=0.5
        )
        self.play(
            Create(line_a),
            Create(line_b),
            Create(line_ab),
            Create(region_midpoint)
        )

        # Transform rectangle to trapeze
        point_a2 = ax.c2p(0.2, 0.9 * 0.2 + 1.0725)
        line_a2 = ax.get_vertical_line(point_a2, line_func=Line, color=BLACK)
        point_b2 = ax.c2p(0.7, 0.9 * 0.7 + 1.0725)
        line_b2 = ax.get_vertical_line(point_b2, line_func=Line, color=BLACK)
        line_ab2 = ax.plot(
            lambda x: 0.9 * x + 1.0725,
            x_range=[0.2, 0.7],
            use_smoothing=False,
            color=BLACK,
            stroke_width=2
        )
        points2 = [ax.c2p(0.2, 0), point_a2, point_b2, ax.c2p(0.7, 0)]
        region_midpoint2 = Polygon(
            *points2,
            stroke_width=0,
            fill_color=BLUE,
            fill_opacity=0.5
        )
        self.play(
            Transform(line_a, line_a2),
            Transform(line_b, line_b2),
            Transform(line_ab, line_ab2),
            Transform(region_midpoint, region_midpoint2)
        )

        # Get the errors for the midpoint rule
        txt_2 = Tex(r"Erreur du point médian:", font_size=28, color=BLACK)\
            .move_to([-0.2, 0.7, 0])

        x_vals = np.arange(0.2, 0.45, 0.01)
        points = [
            graph.get_point_from_function(x) for x in x_vals
        ]
        region_a = Polygon(
            *[point_a2, *points],
            stroke_width=0,
            fill_color=RED,
            fill_opacity=0.5
        )
        x_vals = np.arange(0.45, 0.7, 0.01)
        points = [
            graph.get_point_from_function(x) for x in x_vals
        ]
        region_b = Polygon(
            *[point_b2, *points],
            stroke_width=0,
            fill_color=RED,
            fill_opacity=0.5
        )

        self.play(
            FadeOut(txt),
            FadeOut(region_midpoint),
            Create(txt_2),
            Create(region_a),
            Create(region_b)
        )


        g = Group(
            ax, graph, txt_a, txt_b, txt_ab, p_fab, txt_fab,
            line_a, region_a, line_b, region_b, line_ab
        )
        g_copy = g.copy()
        self.play(
            FadeOut(txt_2),
            g_copy.animate.scale(0.3).move_to([-1.5, 1.5, 0])
        )

        # Bound the errors
        line_ab3 = ax.plot(
            lambda x: 0.9 * x + 0.51,
            x_range=[0.2, 0.7],
            use_smoothing=False,
            color=BLACK,
            stroke_width=2
        )
        line_ab3 = DashedVMobject(line_ab3)
        p_fab2 = Dot(ax.c2p(0.45, 0.9 * 0.45 + 0.51), color=BLACK)
        line_vert = DashedLine(
            p_fab.get_center(), p_fab2.get_center(),
            stroke_width=2,
            color=BLACK
        )

        point_a3 = ax.c2p(0.2, 0.9 * 0.2 + 0.51)
        line_fa_fab = Line(
            p_fab.get_center(), point_a3,
            stroke_width=2, color=BLACK
        )
        point_b3 = ax.c2p(0.7, 0.9 * 0.7 + 0.51)
        line_fb_fab = Line(
            p_fab.get_center(), point_b3,
            stroke_width=2, color=BLACK
        )

        region_a2 = Polygon(
            *[point_a2, point_a3, p_fab.get_center()],
            stroke_width=0,
            fill_color=RED,
            fill_opacity=0.5
        )
        region_b2 = Polygon(
            *[point_b2, p_fab.get_center(), point_b3],
            stroke_width=0,
            fill_color=RED,
            fill_opacity=0.5
        )
        
        self.play(
            Create(line_ab3),
            Create(line_vert),
            Create(line_fa_fab),
            Create(line_fb_fab),
            Transform(region_a, region_a2),
            Transform(region_b, region_b2)
        )

        g = Group(
            ax, graph, txt_a, txt_b, txt_ab, p_fab, txt_fab,
            line_a, region_a2, line_b, region_b2, line_ab,
            line_ab3, line_vert, line_fa_fab, line_fb_fab
        )
        g_copy = g.copy()
        txt_less = Tex(r"$\leq$", font_size=28, color=BLACK)\
            .move_to([-0.8, 1.5, 0])
        self.play(
            Write(txt_less),
            g_copy.animate.scale(0.3).move_to([0, 1.5, 0])
        )

        region_a3 = Polygon(
            *[p_fab.get_center(), point_a3, p_fab2.get_center()],
            stroke_width=0,
            fill_color=RED,
            fill_opacity=0.5
        )
        region_b3 = Polygon(
            *[p_fab.get_center(), p_fab2.get_center(), point_b3],
            stroke_width=0,
            fill_color=RED,
            fill_opacity=0.5
        )
        self.play(
            Transform(region_a, region_a3),
            Transform(region_b, region_b3)
        )

        g = Group(
            ax, graph, txt_a, txt_b, txt_ab, p_fab, txt_fab,
            line_a, region_a3, line_b, region_b3, line_ab,
            line_ab3, line_vert, line_fa_fab, line_fb_fab
        )
        g_copy2 = g.copy()
        self.play(
            FadeOut(g_copy),
            g_copy2.animate.scale(0.3).move_to([0, 1.5, 0])
        )

        # Get the errors for the trapz rule
        txt_3 = Tex(r"Erreur du trapèze:", font_size=28, color=BLACK)\
            .move_to([-0.4, 0.7, 0])

        x_vals = np.arange(0.2, 0.7, 0.01)
        points = [
            graph.get_point_from_function(x) for x in x_vals
        ]
        region_c = Polygon(
            *[
                ax.c2p(0.2, - 9 * (0.2 - 0.5)**2 + 1.5),
                *points,
                ax.c2p(0.7, - 9 * (0.7 - 0.5)**2 + 1.5)
            ],
            stroke_width=0,
            fill_color=RED,
            fill_opacity=0.5
        )

        self.play(
            Write(txt_3),
            FadeOut(region_a),
            FadeOut(region_b),
            Create(region_c)
        )

        g = Group(
            ax, graph, txt_a, txt_b, txt_ab, p_fab, txt_fab,
            line_a, line_b, line_ab, region_c,
            line_ab3, line_vert, line_fa_fab, line_fb_fab
        )
        g_copy = g.copy()
        txt_less = Tex(r"$\leq$", font_size=28, color=BLACK)\
            .move_to([0.7, 1.5, 0])
        self.play(
            Write(txt_less),
            g_copy.animate.scale(0.3).move_to([1.5, 1.5, 0])
        )

        # Write conclusion
        self.play(
            FadeOut(txt_3),
            FadeOut(g)
        )
        
        rect = RoundedRectangle(
            height=1.5, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, -1, 0])
        txt = [
            Tex(r"Erreur du point médian", font_size=28, color=BLACK),
            Tex(r"$\leq$", font_size=28, color=BLACK),
            Tex(r"Erreur du trapèze ", font_size=28, color=BLACK),
        ]
        txt = VGroup(*txt)\
            .arrange(DOWN, center=True, buff=0.1)\
                .move_to([0, -1, 0])


        self.play(
            Create(rect),
            Write(txt)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"College Mathematics Journal,", font_size=26, color=BLACK),
            Tex(r"vol. 16, no. 1 (Jan. 1985), p. 56", font_size=26, color=BLACK)
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