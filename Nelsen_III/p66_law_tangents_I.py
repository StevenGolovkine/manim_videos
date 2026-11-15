"""
Visual proof of The Law of Tangents I.
Proofs without Words III. Roger B. Nelsen. p. 66.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, FadeIn, FadeOut
from manim import VGroup, FunctionGraph
from manim import Line, DashedLine, Arc
from manim import Text, Tex, MathTex

from manim import config
from manim import RIGHT, DOWN, LIGHT, PI

# COLORS
BLUE = "#B0E1FA"
VIOLET = "#E8C9FA"
RED = "#F79BC5"
GREEN = "#DBF9E7"
YELLOW = "#EFE9B7"
ORANGE = "#F6CCB0"
BLACK = "#000000"
WHITE = "#F4EDDE"
GRAY = "#B6B8BA"
ANGLE_SUM = "#C23B6E"
ANGLE_ALPHA = "#2077B4"
ANGLE_BETA = "#D96C14"
ANGLE_HALF_SUM = "#2E8B57"
ANGLE_HALF_DIFFERENCE = "#6F4BA8"

# Make it vertical
SCALE_FACTOR = 1
tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height
config.frame_height = config.frame_height / SCALE_FACTOR
config.frame_width = config.frame_height * 9 / 16


class Tangent(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame.save_state()

        txt_copy = Text(
            r"@chill.maths",
            font_size=12,
            font="CMU Typewriter Text",
            weight=LIGHT,
            color=BLACK,
        ).to_edge(RIGHT + DOWN, buff=0.1)
        self.add(txt_copy)

        txt_title = VGroup(
            Tex(r"La loi", font_size=48, color=BLACK),
            Tex(r"des tangentes", font_size=48, color=BLACK),
        ).arrange(DOWN).move_to([0, 2, 0])
        txt = VGroup(
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Rex H. Wu", font_size=28, color=BLACK),
        ).arrange(DOWN)

        self.add(txt_title, txt)
        self.wait(1)
        self.play(Uncreate(txt_title), Uncreate(txt))

        def angle_of(start, end):
            vector = end - start
            return np.arctan2(vector[1], vector[0])

        def point_from_angle(center, radius, angle):
            return center + radius * np.array([
                np.cos(angle), np.sin(angle), 0
            ])

        def right_angle_mark(corner, point_1, point_2, size=0.12):
            side_1 = point_1 - corner
            side_2 = point_2 - corner
            side_1 /= np.linalg.norm(side_1)
            side_2 /= np.linalg.norm(side_2)
            far_corner = corner + size * (side_1 + side_2)
            return VGroup(
                Line(
                    corner + size * side_1,
                    far_corner,
                    color=BLACK,
                    stroke_width=1.25,
                ),
                Line(
                    corner + size * side_2,
                    far_corner,
                    color=BLACK,
                    stroke_width=1.25,
                ),
            )

        def side_label(
            tex, start, end, offset=0.15, side=1, t=0.5, font_size=24
        ):
            direction = end - start
            direction /= np.linalg.norm(direction)
            normal = side * np.array([
                -direction[1], direction[0], 0
            ])
            return MathTex(
                tex, font_size=font_size, color=BLACK
            ).move_to(start + t * (end - start) + offset * normal)

        # AC is a diameter, so angle ABC is a right angle.
        A = np.array([-1.75, -0.20, 0])
        B = np.array([1.35, -0.20, 0])
        C = np.array([1.35, 3.05, 0])
        P = (A + C) / 2
        radius = np.linalg.norm(C - A) / 2
        diameter_unit = (C - A) / np.linalg.norm(C - A)

        Q = P - 0.42 * radius * diameter_unit
        E = np.array([Q[0], A[1], 0])
        F = np.array([B[0], Q[1], 0])

        theta_c = angle_of(P, C)
        theta_b = angle_of(P, B)
        theta_a = angle_of(P, A)
        theta_qb = angle_of(Q, B)
        theta_bq = angle_of(B, Q)
        theta_bp = angle_of(B, P)

        circle_arcs = VGroup(
            Arc(
                radius=radius,
                start_angle=theta_c,
                angle=-np.pi,
                arc_center=P,
                color=GRAY,
                stroke_width=2.4,
            ),
            # Arc(
            #     radius=radius,
            #     start_angle=theta_a,
            #     angle=theta_b - theta_a,
            #     arc_center=P,
            #     color=GRAY,
            #     stroke_width=2.4,
            # ),
        )

        outer_lines = VGroup(
            Line(A, C, color=BLACK, stroke_width=1.8),
            Line(A, B, color=BLACK, stroke_width=1.8),
            Line(B, C, color=BLACK, stroke_width=1.8),
        )
        inner_lines = VGroup(
            Line(Q, P, color=BLACK, stroke_width=2.0),
            Line(P, B, color=BLACK, stroke_width=2.0),
            Line(Q, B, color=BLACK, stroke_width=1.9),
        )
        projections = VGroup(
            Line(E, Q, color=BLACK, stroke_width=1.45),
            DashedLine(
                Q,
                F,
                dash_length=0.10,
                dashed_ratio=0.55,
                color=BLACK,
                stroke_width=1.25,
            ),
        )
        right_marks = VGroup(
            right_angle_mark(B, A, C, size=0.13),
            right_angle_mark(E, A, Q, size=0.13),
            right_angle_mark(F, Q, C, size=0.13),
        )

        central_angle = Arc(
            radius=0.29,
            start_angle=theta_c,
            angle=theta_b - theta_c,
            arc_center=P,
            color=ANGLE_SUM,
            stroke_width=3.2,
        )
        alpha_angle = Arc(
            radius=0.28,
            start_angle=theta_qb,
            angle=theta_c - theta_qb,
            arc_center=Q,
            color=ANGLE_ALPHA,
            stroke_width=3.2,
        )
        beta_angle = Arc(
            radius=0.25,
            start_angle=theta_bp,
            angle=theta_bq - theta_bp,
            arc_center=B,
            color=ANGLE_BETA,
            stroke_width=3.2,
        )
        half_sum_angle = Arc(
            radius=0.30,
            start_angle=0,
            angle=theta_c,
            arc_center=A,
            color=ANGLE_HALF_SUM,
            stroke_width=3.2,
        )
        half_difference_angle = Arc(
            radius=0.40,
            start_angle=theta_bq,
            angle=PI - theta_bq,
            arc_center=B,
            color=ANGLE_HALF_DIFFERENCE,
            stroke_width=3.2,
        )
        angle_arcs = VGroup(
            central_angle,
            alpha_angle,
            beta_angle,
            half_sum_angle,
            half_difference_angle,
        )

        central_label = MathTex(
            r"\alpha+\beta", font_size=24, color=ANGLE_SUM
        ).move_to(point_from_angle(P, 0.56, (theta_c + theta_b) / 2))
        alpha_label = MathTex(
            r"\alpha", font_size=24, color=ANGLE_ALPHA
        ).move_to(
            point_from_angle(Q, 0.49, (theta_qb + theta_c) / 2)
            + np.array([0, 0.12, 0])
        )
        beta_label = MathTex(
            r"\beta", font_size=24, color=ANGLE_BETA
        ).move_to(B + np.array([-0.33, 0.28, 0]))
        half_sum_label = MathTex(
            r"\frac{\alpha+\beta}{2}",
            font_size=22,
            color=ANGLE_HALF_SUM,
        ).move_to(
            point_from_angle(A, 0.58, theta_c / 2)
            + np.array([0, 0.22, 0])
        )
        half_difference_label = MathTex(
            r"\frac{\alpha-\beta}{2}",
            font_size=22,
            color=ANGLE_HALF_DIFFERENCE,
        ).move_to(
            point_from_angle(B, 0.95, (theta_bq + PI) / 2)
            + np.array([0, 0.23, 0])
        )
        angle_labels = VGroup(
            central_label,
            alpha_label,
            beta_label,
            half_sum_label,
            half_difference_label,
        )
        for label in angle_labels:
            label.set_stroke(WHITE, width=3, background=True)

        outer_length_labels = VGroup(
            side_label(r"a", P, C, offset=0.18, side=1, t=0.52),
            side_label(r"b", Q, P, offset=0.18, side=1, t=0.48),
            side_label(
                r"a-b", A, Q, offset=0.43, side=1, t=0.48, font_size=23
            ),
        )
        inner_length_labels = VGroup(
            side_label(r"a", P, B, offset=0.35, side=1, t=0.52),
        )
        projection_labels = VGroup(
            MathTex(r"x", font_size=24, color=BLACK).move_to(
                (E + Q) / 2 + np.array([0.13, 0, 0])
            ),
            MathTex(r"y", font_size=24, color=BLACK).move_to(
                (A + E) / 2 + np.array([0, -0.16, 0])
            ),
            MathTex(r"z", font_size=24, color=BLACK).move_to(
                (E + B) / 2 + np.array([0, -0.16, 0])
            ),
        )

        derivation = MathTex(
            r"\begin{aligned}"
            r"\frac{\tan((\alpha-\beta)/2)}"
            r"{\tan((\alpha+\beta)/2)}"
            r"&=\frac{x/z}{x/y}\\[0.15em]"
            r"&=\frac{y}{z}\\[0.15em]"
            r"&=\frac{a-b}{a+b}."
            r"\end{aligned}",
            font_size=24,
            color=BLACK,
        ).move_to([0, -2.35, 0])
        if derivation.width > 3.9:
            derivation.scale_to_fit_width(3.9)

        self.play(
            Create(circle_arcs),
            Create(outer_lines[0]),
            run_time=1.5,
        )
        self.wait(0.5)
        self.play(
            Create(outer_lines[1:]),
            run_time=1.5,
        )
        self.wait(0.5)
        self.play(
            Create(inner_lines),
        )
        self.wait(0.5)
        self.play(
            Write(inner_length_labels),
            Write(outer_length_labels),
            run_time=1.3,
        )
        self.wait(0.5)
        self.play(
            Create(projections),
            FadeIn(right_marks),
            Write(projection_labels),
            run_time=1.2,
        )
        self.wait(0.5)
        self.play(
            Create(angle_arcs),
            Write(angle_labels),
            run_time=1.3,
        )
        self.play(Write(derivation), run_time=1.4)

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        ref = VGroup(
            Tex(r"Mathematics Magazine,", font_size=30, color=BLACK),
            Tex(r"vol. 74, no. 2 (Apr. 2001),", font_size=30, color=BLACK),
            Tex(r"p. 161", font_size=30, color=BLACK),
        ).arrange(DOWN, aligned_edge=np.array([-1, 0, 0]), buff=0.1)
        ref.move_to([0, 2, 0])

        self.play(Write(ref))

        text = Text(
            "chill.maths",
            font="CMU Typewriter Text",
            weight=LIGHT,
            color=BLACK,
        )
        sine_wave = FunctionGraph(
            lambda value: 0.1 * np.sin(2 * np.pi * value),
            x_range=[-3, 3],
            color=BLACK,
        )
        sine_wave.next_to(text, DOWN, buff=0.2)

        self.play(
            FadeIn(text, scale=0.5),
            Create(sine_wave),
            run_time=2,
        )
        self.wait(1)
