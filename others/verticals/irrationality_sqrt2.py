"""
Visual proof of the irrationality of √2.
Proofs without Words III. Roger B. Nelsen. p. 172.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Dot, RoundedRectangle, Polygon, RightAngle, Line, Arc
from manim import Create, Uncreate, Write
from manim import VGroup, Transform, FadeIn, FadeOut, FunctionGraph
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
            Tex(r"L'irrationalité de", font_size=48, color=BLACK),
            Tex(r"$\sqrt{2}$", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Tom M. Apostol", font_size=28, color=BLACK)
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

        # Text
        txt = [
            Tex(r"D'après le théorème de Pythagore, un triangle", font_size=20, color=BLACK),
            Tex(r"isocèle et rectangle de côté $1$ a une", font_size=20, color=BLACK),
            Tex(r"hypothénuse de longueur $\sqrt{2}$. Si $\sqrt{2}$ est",
                font_size=20, color=BLACK),
            Tex(r"rationnel, alors il doit exister un multiple",
                font_size=20, color=BLACK),
            Tex(r"de ce triangle avec $3$ longueurs entières.",
                font_size=20, color=BLACK),
            Tex(r"Donc, il doit exister le plus petit triangle",
                font_size=20, color=BLACK),
            Tex(r"avec ces propriétés. Mais ...",
                font_size=20, color=BLACK),
        ]
        txt = VGroup(*txt)\
            .arrange(DOWN, aligned_edge=LEFT, center=False, buff=0.1)\
            .move_to([0, 2.5, 0])

        self.play(
            Write(txt),
            run_time=2
        )

        triangle_b = Polygon(
            [-1.5, -2, 0], [1.5, -2, 0], [1.5, 1, 0],
            stroke_width=2,
            color=BLACK, fill_color=BLUE, fill_opacity=1
        )
        
        r_angle = RightAngle(
            Line(triangle_b.get_vertices()[0], triangle_b.get_vertices()[1]),
            Line(triangle_b.get_vertices()[1], triangle_b.get_vertices()[2]),
            length=0.2, quadrant=(-1,1), color=BLACK, stroke_width=2
        )
        self.play(
            Create(triangle_b),
            Create(r_angle),
        )

        arc = Arc(
            start_angle=-PI/2,
            angle=-PI/4,
            arc_center=triangle_b.get_vertices()[2],
            radius=3,
            color=BLACK, stroke_width=2
        )
        self.play(
            Create(arc),
        )

        triangle_r = Polygon(
            [-1.5, -2, 0], [1.5 - 3 * 0.414213, -2, 0], [-0.621319, -1.15, 0],
            stroke_width=2,
            color=BLACK, fill_color=RED, fill_opacity=1
        )
        self.play(
            Create(triangle_r),
        )

        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"American Mathematical", font_size=30, color=BLACK),
            Tex(r"Monthly, vol. 107, no. 9", font_size=30, color=BLACK),
            Tex(r"(Nov. 2000), p. 841.", font_size=30, color=BLACK),
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
