"""
Visual proof of the alternating series test.
Proofs without Words I. Roger B. Nelsen. p. 135.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Dot, RoundedRectangle, Polygon, RightAngle, Line, Arc
from manim import Create, Uncreate, Write
from manim import VGroup, Transform, FadeIn, FadeOut, FunctionGraph, BraceBetweenPoints
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

class Proof(MovingCameraScene):
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
            Tex(r"Les séries", font_size=48, color=BLACK),
            Tex(r"alternées", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"R. Hammack \& D. Lyons", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        self.add(
            txt_title,
            txt            
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt),
            run_time=0.5
        )
        self.wait(0.5)

        txt_th_1 = Tex(
            r"La série $\sum (-1)^{n+1} a_n$ converge vers $S$",
            font_size=20, color=BLACK
        )
        txt_th_2 = Tex(
            r"si $\forall n, a_n \geq 0$ et $a_n \longrightarrow 0$.",
            font_size=20, color=BLACK
        )
        txt_th = VGroup(txt_th_1, txt_th_2).arrange(DOWN).to_edge(UP, buff=0.5)
        self.play(Write(txt_th))
        self.wait(0.5)

        txt_th_3 = Tex(
            r"De plus, si $s_{n} = a_1 - a_2 + \dots + (-1)^{n+1}a_{n}$",
            font_size=20, color=BLACK
        )
        txt_th_4 = Tex(
            r"alors $s_{2n} < S < s_{2n+1}$.",
            font_size=20, color=BLACK
        )
        txt_th_3_4 = VGroup(txt_th_3, txt_th_4).arrange(DOWN).next_to(txt_th, DOWN, buff=0.25)
        self.play(Write(txt_th_3_4))
        self.wait(0.5)

        # Graph
        axe_x = Line([-3, -2, 0], [3, -2, 0], color=BLACK, stroke_width=2)
        axe_y = Line([-1, -3, 0], [-1, 1.8, 0], color=BLACK, stroke_width=2)
        txt_0 = Tex(r"$0$", font_size=20, color=BLACK).move_to([-0.9, -2.2, 0])
        txt_1 = Tex(r"$1$", font_size=20, color=BLACK).move_to([0.5, -2.2, 0])
        self.play(
            Create(axe_x),
            Create(axe_y),
            Write(txt_0),
            Write(txt_1)
        )

        # Create the sequence of points along axe_y
        a_1 = Tex(r"$a_1$", font_size=20, color=BLACK).move_to([-1.15, 1.6, 0])
        self.play(Write(a_1), run_time=0.2)

        a_2 = Tex(r"$a_2$", font_size=20, color=BLACK).move_to([-1.15, 0.9, 0])
        self.play(Write(a_2), run_time=0.2)

        a_3 = Tex(r"$a_3$", font_size=20, color=BLACK).move_to([-1.15, 0.5, 0])
        self.play(Write(a_3), run_time=0.2)

        a_4 = Tex(r"$a_4$", font_size=20, color=BLACK).move_to([-1.15, -0.1, 0])
        self.play(Write(a_4), run_time=0.2)

        a_5 = Tex(r"$a_5$", font_size=20, color=BLACK).move_to([-1.15, -0.4, 0])
        self.play(Write(a_5), run_time=0.2)

        a_6 = Tex(r"$a_6$", font_size=20, color=BLACK).move_to([-1.15, -0.7, 0])
        self.play(Write(a_6), run_time=0.2)

        a_dots = Tex(r"\vdots", font_size=20, color=BLACK).move_to([-1.15, -1, 0])
        self.play(Write(a_dots), run_time=0.2)

        a_n_1 = Tex(r"$a_{2n-1}$", font_size=20, color=BLACK).move_to([-1.3, -1.2, 0])
        self.play(Write(a_n_1), run_time=0.2)

        a_n = Tex(r"$a_{2n}$", font_size=20, color=BLACK).move_to([-1.3, -1.4, 0])
        self.play(Write(a_n), run_time=0.2)

        a_n1 = Tex(r"$a_{2n+1}$", font_size=20, color=BLACK).move_to([-1.3, -1.6, 0])
        self.play(Write(a_n1), run_time=0.2)

        a_dots2 = Tex(r"\vdots", font_size=20, color=BLACK).move_to([-1.15, -1.8, 0])
        self.play(Write(a_dots2), run_time=0.2)

        # Polygons
        poly_1 = Polygon(
            [-1, 1.6, 0], [-1, 0.9, 0], [0.5, 0.9, 0], [0.5, 1.6, 0],
            color=RED, fill_opacity=0.5, stroke_width=2
        )
        txt_a1a2 = Tex(r"$a_1 - a_2$", font_size=20, color=BLACK).move_to(poly_1.get_center())
        self.play(Create(poly_1), Write(txt_a1a2), run_time=0.5)

        poly_2 = Polygon(
            [-1, 0.5, 0], [-1, -0.1, 0], [0.5, -0.1, 0], [0.5, 0.5, 0],
            color=RED, fill_opacity=0.5, stroke_width=2
        )
        txt_a3a4 = Tex(r"$a_3 - a_4$", font_size=20, color=BLACK).move_to(poly_2.get_center())
        self.play(Create(poly_2), Write(txt_a3a4), run_time=0.5)

        poly_3 = Polygon(
            [-1, -0.4, 0], [-1, -0.7, 0], [0.5, -0.7, 0], [0.5, -0.4, 0],
            color=RED, fill_opacity=0.5, stroke_width=2
        )
        txt_a5a6 = Tex(r"$a_5 - a_6$", font_size=20, color=BLACK).move_to(poly_3.get_center())
        self.play(Create(poly_3), Write(txt_a5a6), run_time=0.5)

        poly_4 = Polygon(
            [-1, -1.2, 0], [-1, -1.4, 0], [0.5, -1.4, 0], [0.5, -1.2, 0],
            color=RED, fill_opacity=0.5, stroke_width=2
        )
        txt_a7a8 = Tex(r"$a_{2n-1} - a_{2n}$", font_size=20, color=BLACK).move_to(poly_4.get_center())
        self.play(Create(poly_4), Write(txt_a7a8), run_time=0.5)

        # Brace
        brace_1 = BraceBetweenPoints(
            [0.5, 1.6, 0], [0.5, -1.4, 0],
            direction=RIGHT, color=BLACK, sharpness=0.5, buff=0.1
        )
        txt_sn = Tex(r"$s_{2n}$", font_size=20, color=RED).next_to(brace_1, RIGHT, buff=0.1)
        self.play(Create(brace_1), Write(txt_sn))

        # Polygons
        poly_5 = Polygon(
            [-1, -1.6, 0], [-1, -1.7, 0], [0.5, -1.7, 0], [0.5, -1.6, 0],
            color=RED, fill_opacity=0.5, stroke_width=2
        )
        self.play(Create(poly_5), run_time=0.5)

        poly_6 = Polygon(
            [-1, -1.8, 0], [-1, -1.875, 0], [0.5, -1.875, 0], [0.5, -1.8, 0],
            color=RED, fill_opacity=0.5, stroke_width=2
        )
        self.play(Create(poly_6), run_time=0.5)

        poly_7 = Polygon(
            [-1, -1.95, 0], [-1, -2, 0], [0.5, -2, 0], [0.5, -1.95, 0],
            color=RED, fill_opacity=0.5, stroke_width=2
        )
        self.play(Create(poly_7), run_time=0.5)

        # Brace
        brace_2 = BraceBetweenPoints(
            [-1.25, 1.6, 0], [-1.25, -2, 0],
            direction=LEFT, color=BLACK, sharpness=0.5
        )
        txt_S = Tex(r"$S$", font_size=20, color=RED).next_to(brace_2, LEFT, buff=0.1)
        self.play(Create(brace_2), Write(txt_S))

        # Polygons
        poly_8 = Polygon(
            [-1, -1.7, 0], [-1, -1.8, 0], [0.5, -1.8, 0], [0.5, -1.7, 0],
            color=BLUE, fill_opacity=0.5, stroke_width=2
        )
        self.play(Create(poly_8), run_time=0.5)

        poly_9 = Polygon(
            [-1, -1.875, 0], [-1, -1.95, 0], [0.5, -1.95, 0], [0.5, -1.875, 0],
            color=BLUE, fill_opacity=0.5, stroke_width=2
        )
        self.play(Create(poly_9), run_time=0.5)

        # Brace
        brace_3 = BraceBetweenPoints(
            [1, 1.6, 0], [1, -2, 0],
            direction=RIGHT, color=BLACK, sharpness=0.5
        )
        txt_snn = Tex(r"$s_{2n+1}$", font_size=20, color=BLUE).next_to(brace_3, RIGHT, buff=0.1)
        self.play(Create(brace_3), Write(txt_snn))



        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"College Mathematics Journal,", font_size=30, color=BLACK),
            Tex(r"vol. 36, no. 1, (Jan. 2005)", font_size=30, color=BLACK),
            Tex(r"p.72.", font_size=30, color=BLACK),
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
