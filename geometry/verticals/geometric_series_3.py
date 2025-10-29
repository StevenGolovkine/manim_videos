"""
Visual proof of the Geometric Series
Proofs without Words II. Roger B. Nelsen. p. 111.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, TransformFromCopy
from manim import VGroup, FadeIn, FadeOut, FunctionGraph, RoundedRectangle
from manim import RegularPolygon, Line, Polygon
from manim import Text, Tex

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
            Tex(r"Séries géométriques", font_size=48, color=BLACK),
            Tex(r"$\frac{1}{4} + \frac{1}{4^2} + \frac{1}{4^3} + \cdots = \frac{1}{3}$", font_size=24, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Rick Mabry", font_size=28, color=BLACK)
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

        # Triangles
        AB = Line([-2, -1, 0], [2, -1, 0], color=BLACK)
        AC = Line([-2, -1, 0], [0, -1 + 2 * np.sqrt(3), 0], color=BLACK)
        BC = Line([2, -1, 0], [0, -1 + 2 * np.sqrt(3), 0], color=BLACK)
        triangle = Polygon(
            [-2, -1, 0],
            [2, -1, 0],
            [0, -1 + 2 * np.sqrt(3), 0],
            color=BLACK,
            fill_color=BLUE,
            fill_opacity=1,
            stroke_width=2
        )
        
        self.play(
            Create(triangle),
        )

        # Subtriangles
        subtriangle_1 = Polygon(
            AB.get_midpoint(),
            BC.get_midpoint(),
            AC.get_midpoint(),
            color=BLACK,
            fill_color=RED,
            fill_opacity=1,
            stroke_width=2
        )
        txt_base = Tex(r"$1 / 4$", font_size=24, color=BLACK).\
            move_to(subtriangle_1.get_center_of_mass())
        txt_base.z_index = 1
        self.play(
            Create(subtriangle_1),
            Write(txt_base)
        )

        DC = Line(BC.get_midpoint(), [0, -1 + 2 * np.sqrt(3), 0], color=BLACK)
        EC = Line(AC.get_midpoint(), [0, -1 + 2 * np.sqrt(3), 0], color=BLACK)
        DE = Line(BC.get_midpoint(), AC.get_midpoint(), color=BLACK)
        subtriangle_2 = Polygon(
            DC.get_midpoint(),
            EC.get_midpoint(),
            DE.get_midpoint(),
            color=BLACK,
            fill_color=RED,
            fill_opacity=1,
            stroke_width=2
        )
        txt_1 = Tex(r"$1 / 4^2$", font_size=21, color=BLACK).\
            move_to(subtriangle_2.get_center_of_mass())
        self.play(
            Create(subtriangle_2),
            Write(txt_1)
        )

        FC = Line(DC.get_midpoint(), [0, -1 + 2 * np.sqrt(3), 0], color=BLACK)
        GC = Line(EC.get_midpoint(), [0, -1 + 2 * np.sqrt(3), 0], color=BLACK)
        FG = Line(DC.get_midpoint(), EC.get_midpoint(), color=BLACK)
        subtriangle_3 = Polygon(
            FC.get_midpoint(),
            GC.get_midpoint(),
            FG.get_midpoint(),
            color=BLACK,
            fill_color=RED,
            fill_opacity=1,
            stroke_width=2
        )
        txt_2 = Tex(r"$1 / 4^3$", font_size=18, color=BLACK).\
            move_to(subtriangle_3.get_center_of_mass())
        self.play(
            Create(subtriangle_3),
            Write(txt_2)
        )

        txt_top = Tex(r"$\vdots$", font_size=36, color=BLACK).\
            next_to(subtriangle_3, UP, buff=0.1)
        self.play(Write(txt_top))

        # Write equations
        equations = Tex(
            r"$\frac{1}{4} + \frac{1}{4^2} + \frac{1}{4^3} + \cdots = \frac{1}{3}$",
            font_size=36, color=BLACK
        ).to_edge(DOWN, buff=2)
        self.play(Write(equations))

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine, vol. 72,", font_size=26, color=BLACK),
            Tex(r"no. 1 (Feb. 1999), p.63.", font_size=26, color=BLACK)
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