"""
Visual proof of a Graph theoric decomposition of binomial coefficients.
Proofs without Words III. Roger B. Nelsen. p. 175.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Graph
from manim import Text, Tex, MathTex

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
GREY = "#D3D3D3"
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


class Graphe(MovingCameraScene):
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
            Tex(r"Des graphs", font_size=48, color=BLACK),
            Tex(r"pour des binômes", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Joe DeMaio", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        formula = Tex(
            r"$\binom{n + m}{2} = \binom{n}{2} + \binom{m}{2} + nm$",
            font_size=36, color=BLACK
        ).move_to([0, -2, 0])

        self.add(
            txt_title,
            txt,
            formula
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt),
            Uncreate(formula)
        )

        # Create graph
        txt_ex = Tex(r"Pour $n = 5$ et $m = 3$", font_size=28, color=BLACK).\
            move_to([-0.5, 3, 0])
        self.play(Write(txt_ex))

        # k = 8
        vertices = ["1", "2", "3", "4", "5", "A", "B", "C"]
        edges = [(i, j) for i in vertices for j in vertices]
        g = Graph(
            vertices,
            edges,
            layout='circular',
            labels={
                    v: MathTex(v, color=BLACK, font_size=14) for v in vertices
                },
            vertex_config={
                idx: {"fill_color": GREY} for idx in vertices
            },
            edge_config={
                (i, j): {"color": BLACK, "stroke_width": 1}
                for i in vertices for j in vertices
            }
        )
        self.play(Create(g))
        self.remove(g)

        # k = 5
        vertices_5 = ["1", "2", "3", "4", "5"]
        edges_5 = [(i, j) for i in vertices_5 for j in vertices_5]
        g_5 = Graph(
            vertices_5,
            edges_5,
            layout='circular',
            labels={
                    v: MathTex(v, color=BLACK, font_size=14) for v in vertices_5
                },
            vertex_config={
                idx: {"fill_color": GREY} for idx in vertices_5
            },
            edge_config={
                (i, j): {"color": BLACK, "stroke_width": 1}
                for i in vertices_5 for j in vertices_5
            }
        )
        self.play(Create(g_5))
        self.remove(g_5)

        # k = 3
        vertices_3 = ["A", "B", "C"]
        edges_3 = [(i, j) for i in vertices_3 for j in vertices_3]
        g_3 = Graph(
            vertices_3,
            edges_3,
            layout='circular',
            labels={
                    v: MathTex(v, color=BLACK, font_size=14) for v in vertices_3
                },
            vertex_config={
                idx: {"fill_color": GREY} for idx in vertices_3
            },
            edge_config={
                (i, j): {"color": BLACK, "stroke_width": 1}
                for i in vertices_3 for j in vertices_3
            }
        )
        self.play(Create(g_3))
        self.remove(g_3)

        # k = 3*5
        vertices_35 = ["1", "2", "3", "4", "5", "A", "B", "C"]
        edges_35 = [(i, j) for i in vertices_35[:5] for j in vertices_35[5:]]
        g_35 = Graph(
            vertices_35,
            edges_35,
            labels={
                    v: MathTex(v, color=BLACK, font_size=14) for v in vertices_35
                },
            vertex_config={
                idx: {"fill_color": GREY} for idx in vertices_35
            },
            edge_config={
                (i, j): {"color": BLACK, "stroke_width": 1}
                for i in vertices_35[:5] for j in vertices_35[5:]
            }
        )
        self.play(Create(g_35))

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine, vol. 80,", font_size=26, color=BLACK),
            Tex(r"no. 3 (June 2007), p.226", font_size=26, color=BLACK)
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