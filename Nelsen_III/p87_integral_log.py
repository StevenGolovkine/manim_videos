"""
Visual proof of Integrating the Natural Logarithm.
Proofs without Words III. Roger B. Nelsen. p. 87.
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


class Log(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame.save_state()

        txt_copy = Text(
            r"@chill.maths", font_size=12,
            font="CMU Typewriter Text", weight=LIGHT, color=BLACK
        ).to_edge(RIGHT + DOWN, buff=0.18)
        self.add(txt_copy)

        # Introduction text
        txt_title = [
            Tex(r"Intégrer", font_size=48, color=BLACK),
            Tex(r"le logarithme", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Roger B. Nelsen", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        self.add(
            txt_title,
            txt,
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt),
        )

        a = 2.7
        b = 5.0
        ln_a = np.log(a)
        ln_b = np.log(b)

        axes = Axes(
            x_range=[-0.2, 5.8, 1],
            y_range=[-0.15, 1.9, 0.5],
            x_length=3.75,
            y_length=3.8,
            axis_config={
                "color": BLACK,
                "stroke_width": 1.7,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.14,
                "tip_height": 0.18
            }
        ).move_to([0.15, 0.58, 0])

        log_curve = axes.plot(
            np.log,
            x_range=[0.78, 5.55],
            color="#252324",
            stroke_width=2.6,
            use_smoothing=True
        )

        log_color = "#3278A8"
        inverse_color = "#B84F7A"
        rectangle_color = "#4D8A59"

        shaded_area = axes.get_area(
            log_curve,
            x_range=[a, b],
            color=BLUE,
            opacity=0.72
        )
        inverse_area = Polygon(
            axes.c2p(0, ln_a),
            axes.c2p(a, ln_a),
            *[
                axes.c2p(x, np.log(x))
                for x in np.linspace(a, b, 80)
            ],
            axes.c2p(0, ln_b),
            fill_color=RED,
            fill_opacity=0.55,
            stroke_width=0
        )
        rectangle_difference = Polygon(
            axes.c2p(0, ln_a),
            axes.c2p(a, ln_a),
            axes.c2p(a, 0),
            axes.c2p(b, 0),
            axes.c2p(b, ln_b),
            axes.c2p(0, ln_b),
            fill_opacity=0,
            stroke_color=rectangle_color,
            stroke_width=2.4
        )

        horizontal_a = Line(
            axes.c2p(0, ln_a),
            axes.c2p(a, ln_a),
            color=BLACK,
            stroke_width=1.1
        )
        horizontal_b = Line(
            axes.c2p(0, ln_b),
            axes.c2p(b, ln_b),
            color=BLACK,
            stroke_width=1.1
        )
        vertical_a = Line(
            axes.c2p(a, 0),
            axes.c2p(a, ln_a),
            color=BLACK,
            stroke_width=1.1
        )
        vertical_b = Line(
            axes.c2p(b, 0),
            axes.c2p(b, ln_b),
            color=BLACK,
            stroke_width=1.1
        )
        guides = VGroup(horizontal_a, horizontal_b, vertical_a, vertical_b)

        x_label = Tex(r"$x$", font_size=24, color=BLACK)
        x_label.next_to(axes.x_axis.get_end(), RIGHT, buff=0.08)
        y_label = Tex(r"$y$", font_size=24, color=BLACK)
        y_label.next_to(axes.y_axis.get_end(), UP, buff=0.08)

        a_label = Tex(r"$a$", font_size=22, color=BLACK)
        a_label.next_to(axes.c2p(a, 0), DOWN, buff=0.06)
        b_label = Tex(r"$b$", font_size=22, color=BLACK)
        b_label.next_to(axes.c2p(b, 0), DOWN, buff=0.06)
        ln_a_label = Tex(r"$\ln a$", font_size=21, color=BLACK)
        ln_a_label.next_to(axes.c2p(0, ln_a), LEFT, buff=0.08)
        ln_b_label = Tex(r"$\ln b$", font_size=21, color=BLACK)
        ln_b_label.next_to(axes.c2p(0, ln_b), LEFT, buff=0.08)
        curve_label = Tex(r"$y=\ln x$", font_size=21, color=BLACK)
        curve_label.move_to(axes.c2p(5.05, np.log(5.05) + 0.16))

        axis_labels = VGroup(x_label, y_label)
        boundary_labels = VGroup(
            a_label,
            b_label,
            ln_a_label,
            ln_b_label
        )

        area_labels = VGroup(
            Tex(
                r"$\displaystyle\int_a^b\ln x\,dx$",
                font_size=12,
                color=log_color
            ).move_to(axes.c2p(3.85, 0.52)),
            Tex(
                r"$\displaystyle\int_{\ln a}^{\ln b}e^y\,dy$",
                font_size=11,
                color=inverse_color
            ).move_to(axes.c2p(1.55, 1.35)),
            Tex(
                r"$b\ln b-a\ln a$",
                font_size=12,
                color=rectangle_color
            ).move_to(axes.c2p(2.35, ln_b + 0.14))
        )

        inverse_caption = Tex(
            r"Pour une fonction croissante $f$ et son inverse $f^{-1}$:",
            font_size=16,
            color=BLACK
        )

        inverse_identity = VGroup(
            Tex(
                r"$\displaystyle\int_a^b f(x)\,dx$",
                font_size=17,
                color=log_color
            ),
            Tex(r"$+$", font_size=17, color=BLACK),
            Tex(
                r"$\displaystyle\int_{f(a)}^{f(b)}f^{-1}(y)\,dy$",
                font_size=17,
                color=inverse_color
            ),
            Tex(r"$=$", font_size=17, color=BLACK),
            Tex(
                r"$bf(b)-af(a)$",
                font_size=17,
                color=rectangle_color
            )
        ).arrange(RIGHT, buff=0.04)
        if inverse_identity.width > 3.85:
            inverse_identity.scale_to_fit_width(3.85)

        specialization = VGroup(
            Tex(r"$f(x)=\ln x$", font_size=17, color=log_color),
            Tex(r"$,$", font_size=17, color=BLACK),
            Tex(r"$f^{-1}(y)=e^y$", font_size=17, color=inverse_color)
        ).arrange(RIGHT, buff=0.12)
        inverse_explanation = VGroup(
            inverse_caption,
            inverse_identity,
            specialization
        ).arrange(DOWN, buff=0.08)

        first_equal = Tex(r"$=$", font_size=19, color=BLACK)
        first_line = VGroup(
            Tex(
                r"$\displaystyle\int_a^b\ln x\,dx$",
                font_size=19,
                color=log_color
            ),
            first_equal,
            Tex(r"$b\ln b-a\ln a$", font_size=19, color=rectangle_color),
            Tex(r"$-$", font_size=19, color=BLACK),
            Tex(
                r"$\displaystyle\int_{\ln a}^{\ln b}e^y\,dy$",
                font_size=19,
                color=inverse_color
            )
        ).arrange(RIGHT, buff=0.04)
        if first_line.width > 3.75:
            first_line.scale_to_fit_width(3.75)

        second_equal = Tex(r"$=$", font_size=19, color=BLACK)
        second_line = VGroup(
            second_equal,
            Tex(
                r"$\left.x\ln x\right|_a^b$",
                font_size=19,
                color=rectangle_color
            ),
            Tex(r"$-$", font_size=19, color=BLACK),
            Tex(r"$(b-a)$", font_size=19, color=inverse_color)
        ).arrange(RIGHT, buff=0.04)

        third_equal = Tex(r"$=$", font_size=19, color=BLACK)
        third_line = VGroup(
            third_equal,
            Tex(
                r"$\left.(x\ln x-x)\right|_a^b$",
                font_size=19,
                color=log_color
            )
        ).arrange(RIGHT, buff=0.04)

        log_derivation = VGroup(
            first_line,
            second_line,
            third_line
        ).arrange(DOWN, buff=0.12)
        for line, equal_sign in (
            (first_line, first_equal),
            (second_line, second_equal),
            (third_line, third_equal)
        ):
            line.shift(-equal_sign.get_center()[0] * RIGHT)

        derivation = VGroup(
            inverse_explanation,
            log_derivation
        ).arrange(DOWN, buff=0.22)
        derivation.move_to([0, -2.95, 0])

        proof_content = VGroup(
            axes,
            log_curve,
            shaded_area,
            inverse_area,
            rectangle_difference,
            guides,
            axis_labels,
            boundary_labels,
            curve_label,
            area_labels,
            derivation
        )
        proof_content.shift(0.75 * UP)

        shaded_area.set_z_index(0)
        inverse_area.set_z_index(0)
        axes.set_z_index(1)
        guides.set_z_index(2)
        rectangle_difference.set_z_index(2.5)
        log_curve.set_z_index(3)
        axis_labels.set_z_index(4)
        boundary_labels.set_z_index(4)
        curve_label.set_z_index(4)
        area_labels.set_z_index(4)

        self.play(Create(axes), Write(axis_labels), run_time=1.2)
        self.play(Create(log_curve), Write(curve_label), run_time=1.2)
        self.play(Create(guides), Write(boundary_labels), run_time=1)
        self.play(
            FadeIn(shaded_area),
            FadeIn(inverse_area),
            Create(rectangle_difference),
            Write(area_labels),
            run_time=1.2
        )
        self.play(Write(derivation), run_time=1.5)

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"College Mathematics Journal,", font_size=26, color=BLACK),
            Tex(r"vol. 32, no. 5 (Nov. 2001), p. 368.", font_size=26, color=BLACK)
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
