"""
Visual proof of the arithmetic mean - geometric mean inequality IV
Proofs without Words II. Roger B. Nelsen. p. 74.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, TransformFromCopy
from manim import VGroup, FadeIn, FadeOut, FunctionGraph, Rectangle, RoundedRectangle
from manim import DashedLine, Polygon
from manim import Text, Tex

from manim import config
from manim import LEFT, RIGHT, DOWN, LIGHT, UP

# COLORS
BLUE = "#B0E1FA"
VIOLET = "#E8C9FA"
RED = "#F79BC5"
PINK = "#FFC5CB"
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
            Tex(r"arithmetico-", font_size=48, color=BLACK),
            Tex(r"géométrique", font_size=48, color=BLACK),
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


        # Proof figure
        a = 2.2
        b = 1.35
        side = a + b
        bottom_left = np.array([-side / 2, -1.25, 0])
        bottom_right = bottom_left + np.array([side, 0, 0])
        top_right = bottom_left + np.array([side, side, 0])
        top_left = bottom_left + np.array([0, side, 0])

        left_split = bottom_left + np.array([0, b, 0])
        bottom_split = bottom_left + np.array([a, 0, 0])
        right_split = bottom_right + np.array([0, a, 0])
        top_split = top_left + np.array([b, 0, 0])

        outer_square = Polygon(
            bottom_left, bottom_right, top_right, top_left,
            color=BLACK, stroke_width=2.6, fill_opacity=0
        )

        tilted_square = Polygon(
            left_split, bottom_split, right_split, top_split,
            color=BLACK, fill_color="#9D9D9D", fill_opacity=0.58,
            stroke_width=2.2
        )

        def rotate_clockwise(vector):
            return np.array([vector[1], -vector[0], 0])

        def right_angle_vertex(start, end):
            side_vector = end - start
            leg_direction = (
                b * side_vector - a * rotate_clockwise(side_vector)
            ) / (a**2 + b**2)
            return start + b * leg_direction

        inner_left = right_angle_vertex(left_split, bottom_split)
        inner_bottom = right_angle_vertex(bottom_split, right_split)
        inner_right = right_angle_vertex(right_split, top_split)
        inner_top = right_angle_vertex(top_split, left_split)

        inner_square = Polygon(
            inner_left, inner_bottom, inner_right, inner_top,
            color=WHITE, fill_color=WHITE, fill_opacity=1,
            stroke_width=0
        )

        dashed_segments = VGroup(
            DashedLine(top_split, inner_top, color=BLACK, stroke_width=1.6, dash_length=0.07),
            DashedLine(right_split, inner_right, color=BLACK, stroke_width=1.6, dash_length=0.07),
            DashedLine(bottom_split, inner_bottom, color=BLACK, stroke_width=1.6, dash_length=0.07),
            DashedLine(left_split, inner_left, color=BLACK, stroke_width=1.6, dash_length=0.07),
        ).set_opacity(0.65)

        external_labels = VGroup(
            Tex(r"$a$", font_size=28, color=BLACK).move_to((top_left + left_split) / 2 + 0.18 * LEFT),
            Tex(r"$b$", font_size=28, color=BLACK).move_to((bottom_left + left_split) / 2 + 0.18 * LEFT),
            Tex(r"$a$", font_size=28, color=BLACK).move_to((bottom_left + bottom_split) / 2 + 0.18 * DOWN),
            Tex(r"$b$", font_size=28, color=BLACK).move_to((bottom_right + bottom_split) / 2 + 0.18 * DOWN),
        )

        def readable_segment_angle(start, end):
            angle = np.arctan2((end - start)[1], (end - start)[0])
            if angle > np.pi / 2 or angle < -np.pi / 2:
                angle += np.pi
            return angle

        right_b_label = Tex(r"$b$", font_size=22, color=BLACK)
        right_b_label.move_to(
            0.48 * right_split + 0.52 * inner_right + 0.08 * UP
        )

        lower_b_label = Tex(r"$b$", font_size=22, color=BLACK)
        lower_b_label.move_to(
            0.48 * bottom_split + 0.52 * inner_bottom + 0.08 * LEFT
        )

        inner_label = Tex(r"$a-b$", font_size=23, color=BLACK)
        bottom_inner_side = inner_right - inner_bottom
        bottom_inner_side /= np.linalg.norm(bottom_inner_side)
        label_offset = np.array([-bottom_inner_side[1], bottom_inner_side[0], 0])
        inner_label.rotate(readable_segment_angle(inner_bottom, inner_right))
        inner_label.move_to((inner_bottom + inner_right) / 2 + 0.1 * label_offset)

        formula = VGroup(
            Tex(r"$(a+b)^2 \geq 4ab$", font_size=28, color=BLACK),
            Tex(r"$\Longrightarrow$", font_size=28, color=BLACK),
            Tex(r"$\frac{a+b}{2} \geq \sqrt{ab}$", font_size=28, color=BLACK),
        ).arrange(DOWN, buff=0.08).move_to([0, -2.5, 0])

        self.play(
            Create(outer_square),
        )
        self.wait(0.8)
        self.play(
            FadeIn(tilted_square),
            Write(external_labels),
        )
        self.wait(0.8)
        self.play(
            Create(dashed_segments),
        )
        self.play(
            Create(inner_square),
        )
        self.play(
            Write(right_b_label),
            Write(lower_b_label),
            Write(inner_label),
        )

        self.play(
            Write(formula)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematis and Computer", font_size=26, color=BLACK),
            Tex(r"Education, vol. 31, no. 3,", font_size=26, color=BLACK),
            Tex(r"(May 1997), p. 186.", font_size=26, color=BLACK)
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
