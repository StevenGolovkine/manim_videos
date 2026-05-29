"""
Visual proof of the integral of cos^2(x).
Proofs without Words III. Roger B. Nelsen. p. 88.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import Arc, Arrow, Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Angle
from manim import Text, Tex, RoundedRectangle, Rectangle, Line, RightAngle, Polygon
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
            Tex(r"L'intégrale de", font_size=48, color=BLACK),
            Tex(r"$\cos^2 \theta$", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Nick Lord", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        formula = Tex(
            r"$\int \cos^2 \theta d\theta = \frac{\theta}{2} + \frac{1}{4} \sin 2\theta$",
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

        # Proof figure
        unit = 1
        origin = np.array([-1.15, -0.55, 0])
        alpha_value = PI / 3

        def p(x, y):
            return origin + unit * np.array([x, y, 0])

        O = p(0, 0)
        C = p(1, 0)
        B = p(2, 0)
        A = p(
            2 * np.cos(alpha_value) ** 2,
            2 * np.cos(alpha_value) * np.sin(alpha_value)
        )

        grid = VGroup()
        for radius in np.linspace(0.4, 2.4, 6):
            grid.add(
                Arc(
                    radius=radius * unit,
                    start_angle=0,
                    angle=PI / 2,
                    arc_center=O,
                    color="#AEB2B5",
                    stroke_width=1,
                    stroke_opacity=0.8
                )
            )
        for theta in np.linspace(PI / 12, 5 * PI / 12, 5):
            grid.add(
                Line(
                    O,
                    p(2.35 * np.cos(theta), 2.35 * np.sin(theta)),
                    color="#AEB2B5",
                    stroke_width=1,
                    stroke_opacity=0.8
                )
            )

        arc_points = [
            p(1 + np.cos(theta), np.sin(theta))
            for theta in np.linspace(PI, 0, 80)
        ]
        shaded_region = Polygon(
            *arc_points,
            fill_color="#D8D8D8",
            fill_opacity=0.55,
            stroke_width=0
        )

        x_axis = Arrow(
            p(-0.15, 0),
            p(2.58, 0),
            buff=0,
            color=BLACK,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.06
        )
        y_axis = Line(
            p(0, -0.12),
            p(0, 2.52),
            color="#AEB2B5",
            stroke_width=1.4
        )

        polar_curve = Arc(
            radius=unit,
            start_angle=PI,
            angle=-PI,
            arc_center=C,
            color="#222222",
            stroke_width=3.2
        )
        radius_OA = Line(O, A, color="#222222", stroke_width=2.2)
        radius_CA = Line(C, A, color="#222222", stroke_width=2.2)

        alpha_arc = Arc(
            radius=0.34 * unit,
            start_angle=0,
            angle=alpha_value,
            arc_center=O,
            color="#222222",
            stroke_width=1.4
        )
        double_alpha_arc = Arc(
            radius=0.25 * unit,
            start_angle=0,
            angle=2 * alpha_value,
            arc_center=C,
            color="#222222",
            stroke_width=1.4
        )

        label_O = Tex(r"$O$", font_size=20, color=BLACK).\
            next_to(O, DOWN + LEFT, buff=0.02)
        label_A = Tex(r"$A$", font_size=20, color=BLACK).\
            next_to(A, UP + LEFT, buff=0.01)
        label_C = Tex(r"$C(1,0)$", font_size=20, color=BLACK).\
            next_to(C, DOWN, buff=0.05)
        label_B = Tex(r"$B(2,0)$", font_size=20, color=BLACK).\
            next_to(B, DOWN, buff=0.05)
        label_curve = Tex(r"$r = 2\cos\theta$", font_size=18, color=BLACK).\
            move_to(p(1.6, 1.12))
        label_alpha = Tex(r"$\alpha$", font_size=18, color=BLACK).\
            move_to(
                O + 0.48 * np.array([
                    np.cos(alpha_value / 2),
                    np.sin(alpha_value / 2),
                    0
                ])
            )
        label_double_alpha = Tex(r"$2\alpha$", font_size=18, color=BLACK).\
            move_to(
            C + 0.42 * np.array([
                np.cos(alpha_value),
                np.sin(alpha_value),
                0
            ])
        )

        grid.set_z_index(0)
        shaded_region.set_z_index(1)
        for mob in [
            y_axis,
            x_axis,
            polar_curve,
            radius_OA,
            radius_CA,
            alpha_arc,
            double_alpha_arc,
            label_O,
            label_A,
            label_C,
            label_B,
            label_curve,
            label_alpha,
            label_double_alpha
        ]:
            mob.set_z_index(2)

        diagram = VGroup(
            grid,
            shaded_region,
            y_axis,
            x_axis,
            polar_curve,
            radius_OA,
            radius_CA,
            alpha_arc,
            double_alpha_arc,
            label_O,
            label_A,
            label_C,
            label_B,
            label_curve,
            label_alpha,
            label_double_alpha
        )

        equations = VGroup(
            Tex(
                r"$\int_0^\alpha \cos^2\theta\,d\theta"
                r"=\frac{1}{2}\int_0^\alpha \frac{1}{2}r^2\,d\theta$",
                font_size=27,
                color=BLACK
            ),
            Tex(
                r"$=\frac{1}{2}\left("
                r"\operatorname{Area}\triangle OAC"
                r"+\operatorname{AreaSector}ACB\right)$",
                font_size=27,
                color=BLACK
            ),
            Tex(
                r"$=\frac{1}{2}\left("
                r"\frac{1}{2}\cdot 1\cdot \sin 2\alpha"
                r"+\frac{1}{2}\cdot 1^2\cdot 2\alpha\right)$",
                font_size=27,
                color=BLACK
            ),
            Tex(
                r"$=\frac{1}{2}\alpha + \frac{1}{4}\sin 2\alpha$",
                font_size=27,
                color=BLACK
            )
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)

        diagram.scale_to_fit_width(config.frame_width - 0.4)
        equations.scale_to_fit_width(config.frame_width - 0.45)

        diagram.move_to([0, 1.5, 0])
        equations.next_to(diagram, DOWN, buff=0.3)

        self.play(
            Create(grid),
            Create(y_axis),
            Create(x_axis),
            run_time=1
        )

        self.play(
            FadeIn(shaded_region),
            Create(polar_curve),
            Write(label_O),
            Write(label_B),
            Write(label_curve),
        )

        self.play(
            Write(equations[0])
        )

        self.play(
            Create(radius_OA),
            Write(label_A),
            Write(label_alpha),
            Create(alpha_arc),
            run_time=2
        )

        self.play(
            Create(radius_CA),
            Create(double_alpha_arc),
            Write(label_C),
            Write(label_double_alpha),
            run_time=2
        )

        self.play(
            Write(equations[1:]),
            run_time=2
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematical Gazette, vol. 80,", font_size=26, color=BLACK),
            Tex(r"no. 489 (Nov. 1996), p.583.", font_size=26, color=BLACK)
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
