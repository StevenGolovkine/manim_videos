"""
Visual proof of A Putnam Area Problem.
Proofs without Words II. Roger B. Nelsen. p. 30.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, TransformFromCopy
from manim import Polygon, VGroup, FadeIn, FadeOut, FunctionGraph
from manim import Text, Tex, Line, Angle, Arc, DashedLine, MathTex
from manim import LaggedStart

from manim import config
from manim import LEFT, RIGHT, DOWN, LIGHT, UP, ORIGIN, PI

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


class Area(MovingCameraScene):
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
            Tex(r"Un problème", font_size=48, color=BLACK),
            Tex(r"d'aire", font_size=48, color=BLACK),
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

        # Énoncé du problème
        statement = VGroup(
            Tex(
                r"Soit $s$ un arc quelconque du cercle unité,",
                font_size=18,
                color=BLACK,
            ),
            Tex(
                r"Soit $A$ l'aire sous $s$ et $B$ l'aire à gauche de $s$.",
                font_size=18,
                color=BLACK,
            ),
            Tex(
                r"$A+B$ dépend seulement de la longueur de $s$.",
                font_size=18,
                color=BLACK,
            ),
        ).arrange(DOWN, buff=0.16).move_to([0, 3, 0])

        self.play(
            LaggedStart(*[FadeIn(line, shift=0.08 * UP) for line in statement],
                         lag_ratio=0.12),
            run_time=1.4,
        )
        self.wait(1.5)


        upper_angle = 68 * PI / 180
        lower_angle = 32 * PI / 180

        def point_on_circle(origin, radius, angle):
            return origin + radius * np.array([
                np.cos(angle), np.sin(angle), 0
            ])

        def geometry(origin, radius):
            origin = np.array(origin, dtype=float)
            p = point_on_circle(origin, radius, upper_angle)
            q = point_on_circle(origin, radius, lower_angle)
            corner = np.array([p[0], q[1], 0])
            arc_points = [
                point_on_circle(origin, radius, angle)
                for angle in np.linspace(lower_angle, upper_angle, 24)
            ]
            return origin, p, q, corner, arc_points

        def filled_polygon(points, color, opacity=0.62):
            return Polygon(
                *points,
                stroke_width=0,
                fill_color=color,
                fill_opacity=opacity,
            )

        def quarter_frame(origin, radius, guides=True):
            origin, p, q, _, _ = geometry(origin, radius)
            outline = VGroup(
                Line(origin, origin + radius * RIGHT, color=BLACK,
                     stroke_width=2.2),
                Line(origin, origin + radius * UP, color=BLACK,
                     stroke_width=2.2),
                Arc(
                    radius=radius,
                    start_angle=0,
                    angle=PI / 2,
                    arc_center=origin,
                    color=BLACK,
                    stroke_width=2.2,
                ),
            )
            if not guides:
                return outline
            guide_lines = VGroup(
                DashedLine(
                    [p[0], origin[1], 0], p,
                    dash_length=0.055, color=BLACK, stroke_width=1.2,
                ),
                DashedLine(
                    [q[0], origin[1], 0], q,
                    dash_length=0.055, color=BLACK, stroke_width=1.2,
                ),
                DashedLine(
                    [origin[0], p[1], 0], p,
                    dash_length=0.055, color=BLACK, stroke_width=1.2,
                ),
                DashedLine(
                    [origin[0], q[1], 0], q,
                    dash_length=0.055, color=BLACK, stroke_width=1.2,
                ),
            )
            return VGroup(outline, guide_lines)

        def area_parts(origin, radius):
            origin, p, q, corner, arc_points = geometry(origin, radius)
            a_rectangle = filled_polygon(
                [
                    [p[0], origin[1], 0],
                    [q[0], origin[1], 0],
                    q,
                    corner,
                ],
                BLUE,
            )
            b_rectangle = filled_polygon(
                [
                    [origin[0], q[1], 0],
                    corner,
                    p,
                    [origin[0], p[1], 0],
                ],
                ORANGE,
            )
            overlap = filled_polygon(
                [corner, q, *arc_points[1:], p],
                VIOLET,
                opacity=0.72,
            )
            return a_rectangle, b_rectangle, overlap

        # Les deux aires initiales et leur intersection C.
        main_origin = np.array([-1.13, 1, 0])
        main_radius = 1.35
        main_o, main_p, main_q, main_corner, _ = geometry(
            main_origin, main_radius
        )
        main_a, main_b, main_c = area_parts(main_origin, main_radius)
        main_frame = quarter_frame(main_origin, main_radius)
        selected_arc = Arc(
            radius=main_radius,
            start_angle=lower_angle,
            angle=upper_angle - lower_angle,
            arc_center=main_origin,
            color=RED,
            stroke_width=4,
        )
        arc_label = MathTex(r"s", font_size=23, color=RED).next_to(
            point_on_circle(
                main_origin, main_radius, (upper_angle + lower_angle) / 2
            ),
            RIGHT,
            buff=0.08,
        )
        main_labels = VGroup(
            MathTex(r"A_0", font_size=21, color="#3F91BB").move_to(
                [(main_p[0] + main_q[0]) / 2,
                 (main_origin[1] + main_q[1]) / 2, 0]
            ),
            MathTex(r"B_0", font_size=21, color="#BC7042").move_to(
                [(main_origin[0] + main_p[0]) / 2,
                 (main_q[1] + main_p[1]) / 2, 0]
            ),
            MathTex(r"C", font_size=21, color="#8D63A7").move_to(
                0.34 * main_p + 0.34 * main_q + 0.32 * main_corner
                + 0.07 * UP
            ),
        )
        area_key = VGroup(
            MathTex(r"A", r"=", r"A_0", r"+", r"C",
                    font_size=22, color=BLACK),
            MathTex(r"B", r"=", r"B_0", r"+", r"C",
                    font_size=22, color=BLACK),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16).move_to([1.08, 1.75, 0])
        area_key[0][2].set_color("#3F91BB")
        area_key[0][4].set_color("#8D63A7")
        area_key[1][2].set_color("#BC7042")
        area_key[1][4].set_color("#8D63A7")

        self.play(
            Create(main_frame),
            Create(selected_arc),
            Write(arc_label),
            run_time=1.2,
        )
        self.wait(0.5)
        self.play(
            FadeIn(main_a),
            FadeIn(main_b),
            FadeIn(main_c),
        )
        self.play(
            Write(main_labels),
            Write(area_key),
            run_time=1,
        )
        self.wait(1)

        overlap_note = Tex(
            r"Les deux aires se recouvrent sur $C$.",
            font_size=18,
            color=BLACK,
        ).move_to([0, 0.8, 0])
        decomposition_1 = MathTex(
            r"A+B=A_0+B_0+2C",
            font_size=24,
            color=BLACK,
        ).move_to([0, 0.5, 0])
        decomposition_1[0][4:6].set_color("#3F91BB")
        decomposition_1[0][7:9].set_color("#BC7042")
        decomposition_1[0][-1].set_color("#8D63A7")
        self.play(Write(overlap_note), Write(decomposition_1), run_time=0.8)

        # A_0/2 et B_0/2 sont des triangles; avec C ils forment un secteur.
        mini_radius = 0.66
        mini_origins = [
            np.array([-1.74, -1.4, 0]),
            np.array([-0.58, -1.4, 0]),
            np.array([0.58, -1.4, 0]),
        ]
        mini_frames = VGroup(*[
            quarter_frame(origin, mini_radius)
            for origin in mini_origins
        ])

        o_1, p_1, _, r_1, _ = geometry(mini_origins[0], mini_radius)
        b_triangle = filled_polygon([o_1, p_1, r_1], ORANGE, opacity=0.7)
        o_2, _, q_2, r_2, _ = geometry(mini_origins[1], mini_radius)
        a_triangle = filled_polygon([o_2, r_2, q_2], BLUE, opacity=0.7)
        _, p_3, q_3, r_3, arc_3 = geometry(mini_origins[2], mini_radius)
        c_copy = filled_polygon(
            [r_3, q_3, *arc_3[1:], p_3], VIOLET, opacity=0.72
        )
        radial_lines = VGroup(
            Line(o_1, p_1, color=BLACK, stroke_width=1.4),
            Line(o_1, r_1, color=BLACK, stroke_width=1.4),
            Line(o_2, r_2, color=BLACK, stroke_width=1.4),
            Line(o_2, q_2, color=BLACK, stroke_width=1.4),
        )
        plus_signs = VGroup(
            MathTex(r"+", font_size=24, color=BLACK).move_to([-0.87, -1, 0]),
            MathTex(r"+", font_size=24, color=BLACK).move_to([0.29, -1, 0]),
        )
        mini_labels = VGroup(
            MathTex(r"\frac{B_0}{2}", font_size=20, color="#BC7042"),
            MathTex(r"\frac{A_0}{2}", font_size=20, color="#3F91BB"),
            MathTex(r"C", font_size=20, color="#8D63A7"),
        )
        for label, origin in zip(mini_labels, mini_origins):
            label.move_to(origin + np.array([mini_radius / 2, -0.22, 0]))

        decomposition_2 = MathTex(
            r"=", r"2\left(", r"\frac{B_0}{2}", r"+",
            r"\frac{A_0}{2}", r"+", r"C", r"\right)",
            font_size=23,
            color=BLACK,
        ).next_to(decomposition_1, DOWN, buff=0.2)
        decomposition_2[2].set_color("#BC7042")
        decomposition_2[4].set_color("#3F91BB")
        decomposition_2[6].set_color("#8D63A7")
        self.play(
            Write(decomposition_2),
        )
        self.play(
            Create(mini_frames),
        )
        self.play(
            TransformFromCopy(main_b, b_triangle),
            Write(mini_labels[0]),
        )
        self.play(
            TransformFromCopy(main_a, a_triangle),
            Write(mini_labels[1]),
        )
        self.play(
            TransformFromCopy(main_c, c_copy),
            Write(mini_labels[2])
        )
        self.play(
            Write(plus_signs),
        )

        # Réunion des trois pièces dans le secteur d'angle theta.
        final_origin = np.array([-0.5, -3.25, 0])
        final_radius = 0.88
        final_o, final_p, final_q, final_r, final_arc = geometry(
            final_origin, final_radius
        )
        final_b = filled_polygon(
            [final_o, final_p, final_r], ORANGE, opacity=0.7
        )
        final_a = filled_polygon(
            [final_o, final_r, final_q], BLUE, opacity=0.7
        )
        final_c = filled_polygon(
            [final_r, final_q, *final_arc[1:], final_p],
            VIOLET,
            opacity=0.72,
        )
        final_frame = quarter_frame(final_origin, final_radius, guides=False)
        final_radii = VGroup(
            Line(final_o, final_p, color=BLACK, stroke_width=1.7),
            Line(final_o, final_q, color=BLACK, stroke_width=1.7),
        )
        theta_angle = Angle(
            Line(final_o, final_q),
            Line(final_o, final_p),
            radius=0.2,
            color=BLACK,
            stroke_width=1.6,
        )
        theta_label = MathTex(r"\theta", font_size=19, color=BLACK).move_to(
            final_origin + 0.29 * np.array([
                np.cos((upper_angle + lower_angle) / 2),
                np.sin((upper_angle + lower_angle) / 2),
                0,
            ])
        )
        sector_note = Tex(
            r"Les trois morceaux forment un secteur.",
            font_size=18,
            color=BLACK,
        ).move_to([0, -2, 0])

        self.play(Write(sector_note), Create(final_frame), run_time=0.7)
        self.play(
            TransformFromCopy(b_triangle, final_b),
            TransformFromCopy(a_triangle, final_a),
            TransformFromCopy(c_copy, final_c),
            Create(final_radii),
            Create(theta_angle),
            Write(theta_label),
            run_time=1.2,
        )


        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"American Mathematical", font_size=30, color=BLACK),
            Tex(r"Monthly, vol. 106, no. 9", font_size=30, color=BLACK),
            Tex(r"(Nov. 1999), pp. 844-846.", font_size=30, color=BLACK),
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
