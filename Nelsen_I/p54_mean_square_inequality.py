"""
Visual proof of the means inequality.
Proofs without Words I. Roger B. Nelsen. p. 54.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, Group, DoubleArrow
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


class Mean(MovingCameraScene):
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
            Tex(r"L'inégalité des", font_size=48, color=BLACK),
            Tex(r"moyennes", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Sidney H. Kung", font_size=28, color=BLACK)
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

        title_lines = VGroup(
            Tex(
                r"\textbf{The Harmonic Mean---Geometric Mean---}",
                font_size=24,
                color=BLACK
            ),
            Tex(
                r"\textbf{Arithmetic Mean---Root Mean Square}",
                font_size=24,
                color=BLACK
            ),
            Tex(
                r"\textbf{Inequality II}",
                font_size=24,
                color=BLACK
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.04)
        if title_lines.width > 4.05:
            title_lines.scale_to_fit_width(4.05)
        title_lines.to_edge(UP, buff=0.28)
        title_lines.to_edge(LEFT, buff=0.22)

        a = 1.1
        b = 2.9
        midpoint = (a + b) / 2
        difference = (b - a) / 2
        geometric = np.sqrt(a * b)
        baseline_y = -1.0

        A = np.array([-2.0, baseline_y, 0])
        B = A + np.array([a, 0, 0])
        D = A + np.array([midpoint, 0, 0])
        C = A + np.array([a + b, 0, 0])
        E = B + np.array([0, geometric, 0])

        # ED has length (a+b)/2.  EG is perpendicular to ED and has
        # length (b-a)/2.
        perpendicular_unit = np.array([
            geometric / midpoint,
            difference / midpoint,
            0
        ])
        G = E + difference * perpendicular_unit

        harmonic_ratio = a * b / midpoint ** 2
        F = B - harmonic_ratio * np.array([
            difference,
            -geometric,
            0
        ])

        baseline = Line(A, C, color=BLACK, stroke_width=2.0)
        BE = Line(B, E, color=BLACK, stroke_width=2.0)
        ED = Line(E, D, color=BLACK, stroke_width=2.0)
        DG = Line(D, G, color=BLACK, stroke_width=2.0)
        FG = Line(F, G, color=BLACK, stroke_width=2.0)
        FB = Line(F, B, color=BLACK, stroke_width=2.0)

        def right_angle_marker(vertex, ray_1, ray_2, size=0.12):
            unit_1 = (ray_1 - vertex) / np.linalg.norm(ray_1 - vertex)
            unit_2 = (ray_2 - vertex) / np.linalg.norm(ray_2 - vertex)
            corner_1 = vertex + size * unit_1
            corner_2 = corner_1 + size * unit_2
            corner_3 = vertex + size * unit_2
            return VGroup(
                Line(corner_1, corner_2, color=BLACK, stroke_width=1.5),
                Line(corner_2, corner_3, color=BLACK, stroke_width=1.5)
            )

        right_B = right_angle_marker(B, D, E)
        right_E = right_angle_marker(E, D, G)
        right_F = right_angle_marker(F, B, E)

        points = VGroup(*[
            Dot(point, radius=0.035, color=BLACK)
            for point in (A, B, D, C, E, F, G)
        ])
        point_labels = VGroup(
            Tex(r"$A$", font_size=18, color=BLACK).next_to(A, UP, buff=0.06),
            Tex(r"$B$", font_size=18, color=BLACK).next_to(B, UP + LEFT, buff=0.04),
            Tex(r"$D$", font_size=18, color=BLACK).next_to(D, UP + RIGHT, buff=0.04),
            Tex(r"$C$", font_size=18, color=BLACK).next_to(C, UP, buff=0.06),
            Tex(r"$E$", font_size=18, color=BLACK).next_to(E, UP + LEFT, buff=0.04),
            Tex(r"$F$", font_size=18, color=BLACK).next_to(F, UP + LEFT, buff=0.04),
            Tex(r"$G$", font_size=18, color=BLACK).next_to(G, UP, buff=0.05)
        )

        mean_labels = VGroup(
            Tex(
                r"$\dfrac{2ab}{a+b}$",
                font_size=17,
                color=BLACK
            ).move_to(FB.get_center() + 0.28 * LEFT),
            Tex(
                r"$\sqrt{ab}$",
                font_size=17,
                color=BLACK
            ).move_to(BE.get_center() + 0.22 * LEFT),
            Tex(
                r"$\dfrac{a+b}{2}$",
                font_size=17,
                color=BLACK
            ).move_to(ED.get_center() + np.array([-0.02, 0.24, 0])),
            Tex(
                r"$\sqrt{\dfrac{a^2+b^2}{2}}$",
                font_size=15,
                color=BLACK
            ).move_to(DG.get_center() + 0.38 * RIGHT)
        )

        equal_length_labels = VGroup(
            Tex(
                r"$\dfrac{b-a}{2}$",
                font_size=12,
                color=BLACK
            ).move_to((E + G) / 2 + 0.14 * UP),
            Tex(
                r"$\dfrac{b-a}{2}$",
                font_size=12,
                color=BLACK
            ).move_to((B + D) / 2 + 0.18 * UP)
        )

        arrow_y = baseline_y - 0.34
        lower_arrow_y = baseline_y - 0.66
        arrow_a = DoubleArrow(
            A + np.array([0, arrow_y - baseline_y, 0]),
            B + np.array([0, arrow_y - baseline_y, 0]),
            buff=0,
            tip_length=0.10,
            stroke_width=1.4,
            color=BLACK
        )
        arrow_difference = DoubleArrow(
            B + np.array([0, arrow_y - baseline_y, 0]),
            D + np.array([0, arrow_y - baseline_y, 0]),
            buff=0,
            tip_length=0.10,
            stroke_width=1.4,
            color=BLACK
        )
        arrow_midpoint = DoubleArrow(
            D + np.array([0, arrow_y - baseline_y, 0]),
            C + np.array([0, arrow_y - baseline_y, 0]),
            buff=0,
            tip_length=0.10,
            stroke_width=1.4,
            color=BLACK
        )
        arrow_b = DoubleArrow(
            B + np.array([0, lower_arrow_y - baseline_y, 0]),
            C + np.array([0, lower_arrow_y - baseline_y, 0]),
            buff=0,
            tip_length=0.10,
            stroke_width=1.4,
            color=BLACK
        )
        dimension_arrows = VGroup(
            arrow_a,
            arrow_difference,
            arrow_midpoint,
            arrow_b
        )
        dimension_labels = VGroup(
            Tex(r"$a$", font_size=17, color=BLACK).next_to(
                arrow_a, DOWN, buff=0.03
            ),
            Tex(
                r"$\dfrac{b-a}{2}$",
                font_size=16,
                color=BLACK
            ).next_to(arrow_difference, DOWN, buff=0.02),
            Tex(
                r"$\dfrac{b+a}{2}$",
                font_size=16,
                color=BLACK
            ).next_to(arrow_midpoint, DOWN, buff=0.02),
            Tex(r"$b$", font_size=17, color=BLACK).next_to(
                arrow_b, DOWN, buff=0.02
            )
        )

        construction_text = VGroup(
            Tex(r"$AB=a,\quad BC=b$", font_size=13, color=BLACK),
            Tex(
                r"$AD=DC=\dfrac{a+b}{2}$",
                font_size=13,
                color=BLACK
            ),
            Tex(r"$BE\perp AB,\quad DE=AD$", font_size=13, color=BLACK),
            Tex(r"$FE\perp ED,\quad FB\parallel ED$", font_size=13, color=BLACK),
            Tex(
                r"$EG=BD=\dfrac{b-a}{2}$",
                font_size=13,
                color=BLACK
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.13)
        construction_text.move_to([1.50, 0.08, 0])

        self.play(Write(title_lines), run_time=1)
        self.play(
            Create(baseline),
            FadeIn(points),
            Write(point_labels),
            run_time=1.1
        )
        self.play(
            Create(BE),
            Create(ED),
            Create(DG),
            Create(FG),
            Create(FB),
            run_time=1.5
        )
        self.play(
            Create(right_B),
            Create(right_E),
            Create(right_F),
            Write(mean_labels),
            Write(equal_length_labels),
            run_time=1.1
        )
        self.play(
            Create(dimension_arrows),
            Write(dimension_labels),
            run_time=1.2
        )
        self.play(Write(construction_text), run_time=1.3)


        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"College Mathematics Journal,", font_size=26, color=BLACK),
            Tex(r"vol. 21, no. 3 (May 1990),", font_size=26, color=BLACK),
            Tex(r"p. 227.", font_size=26, color=BLACK)
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
