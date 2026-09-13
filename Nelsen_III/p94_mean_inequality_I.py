"""
Visual proof of the arithmetic mean - geometric mean inequality VIII.
Proofs without Words III. Roger B. Nelsen. p. 94.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, TransformFromCopy
from manim import VGroup, FadeIn, FadeOut, FunctionGraph, Polygon
from manim import Text, Tex, MathTex, Line, Arc, Circle, Angle, DoubleArrow, Dot

from manim import config
from manim import LEFT, RIGHT, DOWN, LIGHT, UP, PI, DEGREES

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
            Tex(r"Une inégalité", font_size=48, color=BLACK),
            Tex(r"de moyennes", font_size=48, color=BLACK),
            Tex(r"par trigonométrie", font_size=48, color=BLACK),
            Tex(r"Partie I", font_size=24, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Roger B. Nelsen", font_size=28, color=BLACK)
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

        statement = MathTex(
            r"x\in\left(0,\frac{\pi}{2}\right)",
            r"\Longrightarrow",
            r"\tan x", r"+", r"\cot x", r"\geq 2",
            font_size=29,
            color=BLACK,
        ).move_to([0, 3.35, 0])
        statement[2].set_color("#3F91BB")
        statement[4].set_color("#BC7042")
        statement.scale_to_fit_width(4.05)

        x_value = 34 * DEGREES
        tangent = np.tan(x_value)
        cotangent = 1 / tangent
        scale = 0.91
        baseline_y = -0.35

        A = np.array([-1.97, baseline_y, 0])
        D = A + scale * np.array([2 * cotangent, 0, 0])
        B = D + scale * np.array([2 * tangent, 0, 0])
        P = D + scale * np.array([0, 2, 0])
        O = (A + B) / 2
        radius = np.linalg.norm(B - A) / 2

        left_region = Polygon(
            A, P, D,
            fill_color=ORANGE,
            fill_opacity=0.24,
            stroke_width=0,
        )
        right_region = Polygon(
            D, P, B,
            fill_color=BLUE,
            fill_opacity=0.24,
            stroke_width=0,
        )
        semicircle = Arc(
            radius=radius,
            start_angle=0,
            angle=PI,
            arc_center=O,
            color=BLACK,
            stroke_width=2.0,
        )
        diameter = Line(A, B, color=BLACK, stroke_width=2.0)
        AP = Line(A, P, color=BLACK, stroke_width=1.8)
        PB = Line(P, B, color=BLACK, stroke_width=1.8)
        PD = Line(P, D, color="#B44978", stroke_width=2.2)
        OP = Line(O, P, color="#438B5C", stroke_width=2.2)

        def right_angle_marker(vertex, ray_1, ray_2, size=0.13):
            unit_1 = (ray_1 - vertex) / np.linalg.norm(ray_1 - vertex)
            unit_2 = (ray_2 - vertex) / np.linalg.norm(ray_2 - vertex)
            corner_1 = vertex + size * unit_1
            corner_2 = corner_1 + size * unit_2
            corner_3 = vertex + size * unit_2
            return VGroup(
                Line(corner_1, corner_2, color=BLACK, stroke_width=1.4),
                Line(corner_2, corner_3, color=BLACK, stroke_width=1.4),
            )

        right_P = right_angle_marker(P, A, B, size=0.14)
        right_D = right_angle_marker(D, P, B, size=0.13)

        angle_A = Angle(
            Line(A, B),
            Line(A, P),
            radius=0.28,
            color=BLACK,
            stroke_width=1.5,
        )
        angle_P = Angle(
            Line(P, D),
            Line(P, B),
            radius=0.29,
            color=BLACK,
            stroke_width=1.5,
        )
        label_x_A = MathTex(r"x", font_size=23, color=BLACK).move_to(
            A + 0.43 * np.array([
                np.cos(x_value / 2), np.sin(x_value / 2), 0
            ])
        )
        label_x_P = MathTex(r"x", font_size=23, color=BLACK).move_to(
            P + 0.43 * np.array([
                np.cos(-PI / 2 + x_value / 2),
                np.sin(-PI / 2 + x_value / 2),
                0,
            ])
        )

        center_point = Circle(
            radius=0.045,
            fill_color=WHITE,
            fill_opacity=1,
            stroke_color=BLACK,
            stroke_width=1.5,
        ).move_to(O)
        point_A = Dot(A, radius=0.035, color=BLACK)
        point_B = Dot(B, radius=0.035, color=BLACK)
        point_P = Dot(P, radius=0.035, color=BLACK)
        point_D = Dot(D, radius=0.035, color=BLACK)
        label_A = MathTex(r"A", font_size=18, color=BLACK).next_to(
            point_A, DOWN, buff=0.07
        ).shift(0.06 * LEFT)
        label_B = MathTex(r"B", font_size=18, color=BLACK).next_to(
            point_B, DOWN, buff=0.07
        ).shift(0.06 * RIGHT)
        label_O = MathTex(r"O", font_size=18, color=BLACK).next_to(
            center_point, DOWN, buff=0.07
        )
        label_P = MathTex(r"P", font_size=18, color=BLACK).next_to(
            point_P, UP, buff=0.07
        ).shift(0.06 * LEFT)
        label_D = MathTex(r"D", font_size=18, color=BLACK).next_to(
            point_D, DOWN, buff=0.07
        )

        altitude_label = MathTex(
            r"2", font_size=25, color="#B44978"
        ).next_to(PD, LEFT, buff=0.12)
        radius_label = MathTex(
            r"\tan x", r"+", r"\cot x",
            font_size=22,
            color=BLACK,
        )
        radius_label[0].set_color("#3F91BB")
        radius_label[2].set_color("#BC7042")
        radius_angle = np.arctan2(*(P - O)[1::-1])
        radius_normal = np.array([
            -np.sin(radius_angle), np.cos(radius_angle), 0
        ])
        radius_label.rotate(radius_angle).move_to(
            OP.get_center() + 0.22 * radius_normal
        )

        arrow_y = baseline_y - 0.38
        left_arrow = DoubleArrow(
            [A[0], arrow_y, 0],
            [D[0], arrow_y, 0],
            buff=0,
            tip_length=0.10,
            stroke_width=1.5,
            color=BLACK,
        )
        right_arrow = DoubleArrow(
            [D[0], arrow_y, 0],
            [B[0], arrow_y, 0],
            buff=0,
            tip_length=0.10,
            stroke_width=1.5,
            color=BLACK,
        )
        left_measure = MathTex(
            r"2\cot x", font_size=22, color="#BC7042"
        ).move_to(left_arrow.get_center())
        right_measure = MathTex(
            r"2\tan x", font_size=22, color="#3F91BB"
        ).move_to(right_arrow.get_center())
        for measure in (left_measure, right_measure):
            measure.set_stroke(WHITE, width=5, background=True)

        construction = VGroup(
            left_region,
            right_region,
            semicircle,
            diameter,
            AP,
            PB,
            PD,
            OP,
            right_P,
            right_D,
            angle_A,
            angle_P,
            label_x_A,
            label_x_P,
            center_point,
            point_A,
            point_B,
            point_P,
            point_D,
            label_A,
            label_B,
            label_O,
            label_P,
            label_D,
            altitude_label,
            radius_label,
            left_arrow,
            right_arrow,
            left_measure,
            right_measure,
        )

        altitude_formula = MathTex(
            r"PD^2", r"=AD\cdot DB",
            r"=(2\cot x)(2\tan x)=4",
            font_size=22,
            color=BLACK,
        ).move_to([0, -1.5, 0])
        altitude_formula[0].set_color("#B44978")
        radius_formula = MathTex(
            r"OP", r"=\frac{AB}{2}",
            r"=\tan x+\cot x",
            font_size=22,
            color=BLACK,
        ).move_to([0, -2.08, 0])
        radius_formula[0].set_color("#438B5C")
        conclusion = MathTex(
            r"OP\geq PD=2",
            r"\Longrightarrow",
            r"\tan x+\cot x\geq2",
            font_size=24,
            color=BLACK,
        ).arrange(DOWN, buff=0.16).move_to([0, -2.88, 0])
        conclusion[0][0:2].set_color("#438B5C")
        conclusion[0][3:5].set_color("#B44978")
        conclusion[2].set_color("#3F6F82")

        self.play(Write(statement), run_time=1)
        self.wait(0.5)
        self.play(
            Create(semicircle),
            Create(diameter),
            FadeIn(point_A),
            FadeIn(point_B),
            Write(label_A),
            Write(label_B),
            run_time=1.0,
        )
        self.wait(0.5)
        self.play(
            Create(AP),
            Create(PB),
            FadeIn(right_P),
            FadeIn(point_P),
            Write(label_P),
            run_time=1,
        )
        self.play(
            FadeIn(left_region),
            FadeIn(right_region),
            Create(PD),
            FadeIn(point_D),
            Write(label_D),
        )
        self.wait(0.5)
        self.play(
            FadeIn(right_D),
            Create(angle_A),
            Create(angle_P),
            Write(label_x_A),
            Write(label_x_P),
            run_time=1,
        )
        self.play(
            Create(left_arrow),
            Create(right_arrow),
            Write(left_measure),
            Write(right_measure),
            run_time=1,
        )
        self.wait(0.5)
        self.play(
            Create(OP),
            FadeIn(center_point),
            Write(label_O),
            Write(altitude_label),
            Write(radius_label),
            run_time=0.9,
        )
        self.play(Write(altitude_formula), run_time=0.8)
        self.play(Write(radius_formula), run_time=0.8)
        self.play(Write(conclusion), run_time=1.0)

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"College Mathematics Journal,", font_size=26, color=BLACK),
            Tex(r"vol. 46, no. 1 (Jan. 2015), p.42", font_size=26, color=BLACK)
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
