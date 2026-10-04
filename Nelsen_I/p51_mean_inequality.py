"""
Visual proof of the arithmetic mean - geometric mean inequality III.
Proofs without Words I. Roger B. Nelsen. p. 51.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, TransformFromCopy
from manim import TransformMatchingTex
from manim import VGroup, FadeIn, FadeOut, FunctionGraph, Polygon
from manim import (
    Text, Tex, MathTex, Line, Arc, Circle, Angle, DoubleArrow, Dot,
    DashedLine,
)

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
            Tex(r"L'inégalité", font_size=48, color=BLACK),
            Tex(r"arithmético", font_size=48, color=BLACK),
            Tex(r"géométrique", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Roland H. Eddy", font_size=28, color=BLACK)
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

        statement = VGroup(
            MathTex(
                r"\frac{a+b}{2}\geq\sqrt{ab}",
                font_size=31,
                color=BLACK,
            )
        ).arrange(RIGHT, buff=0.13).move_to([0, 3.35, 0])

        # The displayed diameters are representatives of a > b > 0.
        # All positions are derived from them, so tangency is exact.
        a_length = 2.78
        b_length = 1.18
        big_radius = a_length / 2
        small_radius = b_length / 2
        baseline_y = -1.30

        big_center = np.array([-0.72, baseline_y + big_radius, 0])
        horizontal_separation = np.sqrt(a_length * b_length)
        small_center = np.array([
            big_center[0] + horizontal_separation,
            baseline_y + small_radius,
            0,
        ])

        big_bottom = np.array([big_center[0], baseline_y, 0])
        big_top = np.array([big_center[0], baseline_y + a_length, 0])
        small_bottom = np.array([small_center[0], baseline_y, 0])
        small_top = np.array([small_center[0], baseline_y + b_length, 0])

        big_circle = Circle(
            radius=big_radius,
            color=BLACK,
            stroke_width=2.5,
            fill_color=ORANGE,
            fill_opacity=0.16,
        ).move_to(big_center)
        small_circle = Circle(
            radius=small_radius,
            color=BLACK,
            stroke_width=2.5,
            fill_color=BLUE,
            fill_opacity=0.20,
        ).move_to(small_center)
        baseline = Line(big_bottom, small_bottom, color=BLACK, stroke_width=2.2)

        big_diameter = Line(big_bottom, big_top, color=BLACK, stroke_width=1.7)
        small_diameter = Line(
            small_bottom, small_top, color=BLACK, stroke_width=1.7
        )
        big_diameter_arrow = DoubleArrow(
            big_bottom + 0.10 * LEFT,
            big_top + 0.10 * LEFT,
            buff=0,
            tip_length=0.08,
            stroke_width=1.6,
            color=BLACK,
        )
        small_diameter_arrow = DoubleArrow(
            small_bottom + 0.10 * RIGHT,
            small_top + 0.10 * RIGHT,
            buff=0,
            tip_length=0.08,
            stroke_width=1.6,
            color=BLACK,
        )
        big_label = MathTex("a", font_size=25, color=BLACK).next_to(
            big_diameter_arrow, LEFT, buff=0.04
        )
        small_label = MathTex("b", font_size=25, color=BLACK).next_to(
            small_diameter_arrow, RIGHT, buff=0.03
        )

        center_vector = small_center - big_center
        center_distance = np.linalg.norm(center_vector)
        center_direction = center_vector / center_distance
        center_normal = np.array([
            -center_direction[1], center_direction[0], 0
        ])
        tangent_point = big_center + big_radius * center_direction

        center_segment = Line(
            big_center, small_center, color=BLACK, stroke_width=2.1
        )
        center_dimension = DoubleArrow(
            big_center + 0.16 * center_normal,
            small_center + 0.16 * center_normal,
            buff=0,
            tip_length=0.08,
            stroke_width=1.5,
            color=BLACK,
        )
        sum_label = MathTex(
            r"\frac{a+b}{2}", font_size=18, color=BLACK
        ).move_to(
            center_dimension.get_center() + 0.12 * center_normal
        )

        projection = np.array([big_center[0], small_center[1], 0])
        horizontal_projection = DashedLine(
            projection,
            small_center,
            dash_length=0.10,
            dashed_ratio=0.58,
            color=BLACK,
            stroke_width=1.8,
        )
        difference_x = big_center[0] + 0.19
        difference_dimension = DoubleArrow(
            [difference_x, small_center[1], 0],
            [difference_x, big_center[1], 0],
            buff=0,
            tip_length=0.07,
            stroke_width=1.5,
            color=BLACK,
        )
        difference_label = MathTex(
            r"\frac{a-b}{2}", font_size=18, color=BLACK
        ).next_to(difference_dimension, LEFT, buff=0.3)

        product_dimension = DoubleArrow(
            [big_bottom[0], baseline_y - 0.24, 0],
            [small_bottom[0], baseline_y - 0.24, 0],
            buff=0,
            tip_length=0.09,
            stroke_width=1.6,
            color=BLACK,
        )
        product_label = MathTex(
            r"\sqrt{ab}", font_size=18, color=BLACK
        ).move_to(product_dimension.get_center() + 0.12 * DOWN)

        center_points = VGroup(
            Dot(big_center, radius=0.025, color=BLACK),
            Dot(small_center, radius=0.025, color=BLACK),
            Dot(tangent_point, radius=0.027, color=BLACK),
        )

        self.play(Write(statement))
        self.play(
            Create(big_circle),
            Create(small_circle),
            run_time=1.5,
        )
        self.play(
            Create(big_diameter),
            Create(small_diameter),
        )
        self.play(
            Write(big_label),
            Write(small_label),
        )
        self.play(
            Create(center_segment),
            FadeIn(center_points),
            Write(sum_label),
        )
        self.play(
            Create(horizontal_projection),
            Write(difference_label),
        )
        self.play(
            Create(baseline),
            Write(product_label)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"College Mathematics Journal,", font_size=26, color=BLACK),
            Tex(r"vol. 16, no. 3 (June 1987), p.208", font_size=26, color=BLACK)
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
