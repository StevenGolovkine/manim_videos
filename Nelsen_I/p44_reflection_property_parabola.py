"""
Visual proof of the reflection property of the parabola.
Proofs without Words I. Roger B. Nelsen. p. 44.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, Group
from manim import (
    Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Dot, Line, Polygon,
    Text, Tex, MathTex, DashedVMobject, DashedLine, RoundedRectangle,
    Arrow, Circle, Arc, ParametricFunction,
)

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


class Parabola(MovingCameraScene):
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
            Tex(r"La propriété", font_size=48, color=BLACK),
            Tex(r"de réflexion", font_size=48, color=BLACK),
            Tex(r"de la parabole", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Ayoub B. Ayoub", font_size=28, color=BLACK)
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

        origin = np.array([-0.60, -0.20, 0])
        p = 0.42
        y_q = 1.55
        x_q = y_q**2 / (4 * p)

        def point(x, y):
            return origin + np.array([x, y, 0])

        vertex = point(0, 0)
        focus = point(p, 0)
        q_point = point(x_q, y_q)
        d_point = point(-p, y_q)

        x_axis = Arrow(
            point(-0.78, 0),
            point(2.62, 0),
            buff=0,
            tip_length=0.15,
            stroke_width=2.2,
            color=BLACK,
        )
        y_axis = Arrow(
            point(0, -2.38),
            point(0, 2.48),
            buff=0,
            tip_length=0.15,
            stroke_width=2.2,
            color=BLACK,
        )
        x_label = MathTex("x", font_size=25, color=BLACK).next_to(
            x_axis.get_end(), RIGHT, buff=0.08
        )
        y_label = MathTex("y", font_size=25, color=BLACK).next_to(
            y_axis.get_end(), UP, buff=0.06
        )
        origin_label = MathTex("0", font_size=21, color=BLACK).next_to(
            vertex, LEFT + DOWN, buff=0.05
        )

        directrix = Line(
            point(-p, -0.82),
            point(-p, 2.15),
            color=BLACK,
            stroke_width=2.1,
        )
        directrix_label = MathTex(
            r"x=-p", font_size=19, color=BLACK
        ).move_to(point(-p, -1))

        parabola = ParametricFunction(
            lambda t: point(t**2 / (4 * p), t),
            t_range=[-2.02, 1.88],
            color=BLACK,
            stroke_width=2.5,
        )
        parabola_label = MathTex(
            r"y^2=4px", font_size=21, color=BLACK
        ).rotate(-0.38).move_to(point(1.78, -2))

        qd_segment = DashedLine(
            d_point,
            q_point + [1, 0, 0],
            dash_length=0.09,
            dashed_ratio=0.58,
            color=BLACK,
            stroke_width=1.8,
        )
        qf_segment = Line(
            focus, q_point, color=BLACK, stroke_width=2.2
        )
        df_segment = DashedLine(
            d_point,
            focus,
            dash_length=0.09,
            dashed_ratio=0.58,
            color=BLACK,
            stroke_width=1.8,
        )

        m_1 = 2 * p / y_q
        m_2 = -y_q / (2 * p)
        tangent_y = lambda x: y_q + m_1 * (x - x_q)
        tangent = Line(
            point(-0.20, tangent_y(-0.20)),
            point(2.30, tangent_y(2.30)),
            color=BLACK,
            stroke_width=2.5,
        )
        horizontal_ray = Line(
            q_point, point(2.25, y_q), color=BLACK, stroke_width=1.8
        )

        tangent_angle = np.arctan(m_1)
        df_angle = np.arctan(m_2)
        tangent_label = MathTex(
            r"m_1=y'= 2p / y", font_size=18, color=BLACK
        ).rotate(tangent_angle).move_to(point(1.82, tangent_y(1.82) + 0.23))
        normal_label = MathTex(
            r"m_2=-y / 2p", font_size=16, color=BLACK
        ).rotate(df_angle).move_to(
            d_point + 0.55 * (focus - d_point) + 0.3 * LEFT
        )

        d_label = MathTex(
            r"D(-p,y)", font_size=15, color=BLACK
        ).move_to(d_point + 0.35 * LEFT + 0.14 * UP)
        q_label = MathTex(
            r"Q(x,y)", font_size=19, color=BLACK
        ).next_to(q_point, DOWN + RIGHT, buff=0.06)
        f_label = MathTex(
            r"F(p,0)", font_size=19, color=BLACK
        ).next_to(focus, DOWN, buff=0.06)

        key_points = VGroup(
            Dot(d_point, radius=0.025, color=BLACK),
            Dot(q_point, radius=0.025, color=BLACK),
            Dot(focus, radius=0.025, color=BLACK),
        )

        # Matching hollow marks encode QD = QF.
        equality_marks = VGroup(
            Circle(
                radius=0.045,
                color=BLACK,
                stroke_width=1.6,
                fill_color=WHITE,
                fill_opacity=1,
            ).move_to(d_point + 0.53 * (q_point - d_point)),
            Circle(
                radius=0.045,
                color=BLACK,
                stroke_width=1.6,
                fill_color=WHITE,
                fill_opacity=1,
            ).move_to(qf_segment.point_from_proportion(0.52)),
        )

        # The tangent and DF meet at E=(0,y/2) and are perpendicular.
        e_point = point(0, y_q / 2)
        tangent_direction = np.array([1, m_1, 0])
        tangent_direction /= np.linalg.norm(tangent_direction)
        df_direction = np.array([1, m_2, 0])
        df_direction /= np.linalg.norm(df_direction)
        marker_size = 0.13
        right_angle = Polygon(
            e_point,
            e_point + marker_size * tangent_direction,
            e_point + marker_size * (tangent_direction + df_direction),
            e_point + marker_size * df_direction,
            color=BLACK,
            stroke_width=1.5,
            fill_opacity=0,
        )

        angle_2 = Arc(
            radius=0.45,
            start_angle=PI,
            angle=tangent_angle,
            arc_center=q_point,
            color=BLACK,
            stroke_width=1.7,
        )
        angle_1 = Arc(
            radius=0.34,
            start_angle=PI + tangent_angle,
            angle=tangent_angle,
            arc_center=q_point,
            color=BLACK,
            stroke_width=1.7,
        )
        angle_3 = Arc(
            radius=0.45,
            start_angle=0,
            angle=tangent_angle,
            arc_center=q_point,
            color=BLACK,
            stroke_width=1.7,
        )

        def polar_label(number, radius, angle):
            location = q_point + radius * np.array([
                np.cos(angle), np.sin(angle), 0
            ])
            return MathTex(number, font_size=19, color=BLACK).move_to(location)

        angle_labels = VGroup(
            polar_label("1", 0.46, PI + 1.5 * tangent_angle),
            polar_label("2", 0.58, PI + 0.5 * tangent_angle),
            polar_label("3", 0.58, 0.5 * tangent_angle),
        )

        diagram = VGroup(
            x_axis, y_axis, x_label, y_label, origin_label,
            directrix, directrix_label, parabola, parabola_label,
            qd_segment, qf_segment, df_segment, tangent, horizontal_ray,
            tangent_label, normal_label, d_label, q_label, f_label,
            key_points, equality_marks, right_angle,
            angle_1, angle_2, angle_3, angle_labels,
        )
        diagram.scale(1.07, about_point=origin).shift(0.62 * UP + 0.5 * LEFT)

        conclusion = VGroup(
            MathTex(
                r"QF=QD\quad\&\quad m_1m_2=-1",
                font_size=25,
                color=BLACK,
            ),
            MathTex(
                r"\Longrightarrow\quad \angle 1=\angle 2=\angle 3",
                font_size=25,
                color=BLACK,
            ),
        ).arrange(DOWN, buff=0.13).move_to([0, -2.86, 0])

        self.play(
            Create(x_axis),
            Create(y_axis),
            Write(x_label),
            Write(y_label),
            Write(origin_label),
        )
        self.wait(0.5)
        self.play(
            Create(parabola),
            Write(parabola_label),
            run_time=1.5,
        )
        self.wait(0.5)
        self.play(
            Write(q_label),
            Create(key_points[1]),
        )
        self.wait(0.5)
        self.play(
            Create(qd_segment),
            Create(directrix),
            Write(directrix_label),
        )
        self.play(
            Write(d_label),
            Create(key_points[0])
        )
        self.wait(0.5)
        self.play(
            Create(qf_segment),
            Write(f_label),
            Create(key_points[2])
        )
        self.play(
            FadeIn(equality_marks),
        )
        self.wait(0.5)
        self.play(
            Create(tangent),
        )
        self.wait(0.5)
        self.play(
            Write(tangent_label),
        )
        self.wait(0.5)
        self.play(
            Create(df_segment),
            Create(right_angle),
        )
        self.wait(0.5)
        self.play(
            Write(normal_label),
        )
        self.play(
            Create(angle_1),
            Create(angle_2),
            Create(angle_3),
            Write(angle_labels),
        )
        self.wait(0.5)
        self.play(Write(conclusion))


        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine, vol. 64,", font_size=26, color=BLACK),
            Tex(r"no. 3 (June 1991), p.175.", font_size=26, color=BLACK),
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
