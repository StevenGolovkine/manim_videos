"""
Visual proof of a Product of Tangents.
Proofs without Words III. Roger B. Nelsen. p. 72.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Angle, Polygon
from manim import Text, Tex, RoundedRectangle, Rectangle, Line, RightAngle, Dot
from manim import Brace, line_intersection
from manim import TransformFromCopy, Transform

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


class Tangents(MovingCameraScene):
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
            Tex(r"Un produit de", font_size=48, color=BLACK),
            Tex(r"tangentes", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Roger B. Nelsen", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        formula = Tex(
            r"$\tan(\frac{\pi}{4} + \alpha)  \tan(\frac{\pi}{4} - \alpha) = 1$",
            font_size=20, color=BLACK
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

        # Rectangle and square
        A = Dot([-1.5, -1.5, 0], color=BLACK)
        B = Dot([1.5, -1.5, 0], color=BLACK)
        C = Dot([1.5, 1.5, 0], color=BLACK)
        D = Dot([-1.5, 1.5, 0], color=BLACK)
        E = Dot([1.5, 3, 0], color=BLACK)
        F = Dot([-0.5, 3, 0], color=BLACK)
        G = Dot([-0.5, -1.5, 0], color=BLACK)

        square = Polygon(
            A.get_center(), B.get_center(),
            C.get_center(), D.get_center(),
            stroke_width=1,
            stroke_color=BLACK,
            fill_color=WHITE,
            fill_opacity=1
        )
        brace_1 = Brace(
            square, DOWN, buff=0.1, color=BLACK
        )
        txt_1 = Tex(r"$1$", font_size=24, color=BLACK)\
            .next_to(brace_1, DOWN, buff=0.1)
        brace_2 = Brace(
            square, LEFT, buff=0.1, color=BLACK
        )
        txt_2 = Tex(r"$1$", font_size=24, color=BLACK)\
            .next_to(brace_2, LEFT, buff=0.1)
        self.play(
            Create(square),
            Create(brace_1),
            Write(txt_1),
            Create(brace_2),
            Write(txt_2)
        )

        rect = Polygon(
            G.get_center(), B.get_center(),
            E.get_center(), F.get_center(),
            stroke_width=1,
            fill_color=BLUE,
            fill_opacity=0.5
        )
        self.play(
            Create(rect),
        )

        # Lines and angles
        AC = Line(
            A.get_center(), C.get_center(),
            stroke_width=1, color=BLACK
        )
        angle_CAB = Angle(
            AC, Line(B.get_center(), A.get_center()),
            quadrant=(1, -1), other_angle=True,
            radius=0.2, color=BLACK, stroke_width=1
        )
        txt_angle_CAB = Tex(r"$\frac{\pi}{4}$", font_size=22, color=BLACK)\
            .next_to(angle_CAB, RIGHT, buff=0.1)

        angle_ACB = Angle(
            AC, Line(C.get_center(), B.get_center()),
            quadrant=(-1, 1),
            radius=0.2, color=BLACK, stroke_width=1
        )
        txt_angle_ACB = Tex(r"$\frac{\pi}{4}$", font_size=22, color=BLACK)\
            .next_to(angle_ACB, DOWN, buff=0.1)

        self.play(
            Create(AC),
            Create(angle_CAB),
            Write(txt_angle_CAB),
            Create(angle_ACB),
            Write(txt_angle_ACB)
        )

        AE = Line(
            A.get_center(), E.get_center(),
            stroke_width=1, color=BLACK
        )
        angle_EAC = Angle(
            AE, Line(A.get_center(), C.get_center()),
            quadrant=(1, 1), other_angle=True,
            radius=0.8, color=BLACK, stroke_width=1
        )
        txt_angle_EAC = Tex(r"$\alpha$", font_size=22, color=BLACK)\
            .next_to(angle_EAC, UP + 0.1 * RIGHT, buff=0.1)
        self.play(
            Create(AE),
            Create(angle_EAC),
            Write(txt_angle_EAC)
        )

        txt_BE = Tex(r"$\tan(\frac{\pi}{4} + \alpha)$", font_size=22, color=BLACK)\
            .rotate(-PI / 2).next_to(rect, RIGHT, buff=0.1)
        self.play(
            Write(txt_BE)
        )

        GC = Line(
            G.get_center(), C.get_center(),
            stroke_width=1, color=BLACK
        )
        angle_CGA = Angle(
            GC, AC,
            quadrant=(-1, -1), other_angle=True,
            radius=0.8, color=BLACK, stroke_width=1
        )
        txt_angle_CGA = Tex(r"$\alpha$", font_size=22, color=BLACK)\
            .next_to(angle_CGA, DOWN + 0.2 * LEFT, buff=0.1)
        self.play(
            Create(GC),
            Create(angle_CGA),
            Write(txt_angle_CGA)
        )

        txt_GB = Tex(r"$\tan(\frac{\pi}{4} - \alpha)$", font_size=22, color=BLACK)\
            .next_to(Line(G, B), UP, buff=0.1)
        self.play(
            Write(txt_GB)
        )

        # Triangle
        intersection_point = line_intersection(
            line1=[A.get_center(), E.get_center()],
            line2=[G.get_center(), F.get_center()]
        )
        H = Dot(intersection_point, color=BLACK)

        intersection_point = line_intersection(
            line1=[A.get_center(), E.get_center()],
            line2=[D.get_center(), C.get_center()]
        )
        I = Dot(intersection_point, color=BLACK)
        
        triangle_ICE = Polygon(
            I.get_center(), C.get_center(), E.get_center(),
            stroke_width=1,
            fill_color=RED,
            fill_opacity=0.5
        )
        self.play(
            Create(triangle_ICE),
        )

        triangle_AGH = Polygon(
            A.get_center(), G.get_center(), H.get_center(),
            stroke_width=1,
            fill_color=RED,
            fill_opacity=0.5
        )
        self.play(
            Transform(triangle_ICE, triangle_AGH),
        )

        triangle_FHE = Polygon(
            F.get_center(), H.get_center(), E.get_center(),
            stroke_width=1,
            fill_color=GREEN,
            fill_opacity=0.5
        )
        self.play(
            Create(triangle_FHE),
        )

        triangle_DAI = Polygon(
            D.get_center(), A.get_center(), I.get_center(),
            stroke_width=1,
            fill_color=GREEN,
            fill_opacity=0.5
        )
        self.play(
            Transform(triangle_FHE, triangle_DAI),
        )

        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, -2.5, 0])
        txt_formula3 = Tex(
            r"$\tan(\frac{\pi}{4} + \alpha)  \tan(\frac{\pi}{4} - \alpha) = 1$",
            font_size=20, color=BLACK
        ).move_to([0, -2.5, 0])

        self.play(
            Create(rect),
            Write(txt_formula3)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"College Mathematics Journal,", font_size=26, color=BLACK),
            Tex(r"vol. 34, no. 3, ", font_size=26, color=BLACK),
            Tex(r"(May 2003), p. 193.", font_size=26, color=BLACK)
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