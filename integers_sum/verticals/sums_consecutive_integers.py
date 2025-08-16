"""
Visual proof of Sums of Consecutive Positive Integers.
Proofs without Words II. Roger B. Nelsen. p. 84.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, DoubleArrow
from manim import Brace, VGroup, FadeIn, FadeOut, FunctionGraph, Circle, Line
from manim import Text, Tex, Rectangle, RoundedRectangle, Transform

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


class Sums(MovingCameraScene):
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
            Tex(r"Sur la somme des", font_size=48, color=BLACK),
            Tex(r"des entiers positifs", font_size=48, color=BLACK),
            Tex(r"consécutifs", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"C. L. Frenzen", font_size=28, color=BLACK),
        ]
        txt = VGroup(*txt).arrange(DOWN)

        results = [
            Tex(r"$N = \left(\frac{M - m + 1}{2}\right) + \left(\frac{M - m + 1}{2} + 1\right) + \cdots + \left(\frac{M + m - 1}{2}\right)$",
            font_size=18, color=BLACK),
        ]
        results = VGroup(*results).arrange(DOWN).move_to([0, -1, 0])


        self.add(
            txt_title,
            txt,
            results
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt),
            Uncreate(results),
            run_time=0.5
        )
        self.wait(0.5)

        # Text 
        txt_1 = Tex(
            r"Tout entier positif $N$ peut s'écrire comme",
            font_size=18, color=BLACK
        )
        txt_2 = Tex(
            r"la somme de $2$ entiers consécutifs (ou plus).",
            font_size=18, color=BLACK
        )
        txt = VGroup(txt_1, txt_2).\
            arrange(DOWN, center=True, buff=0.1).\
            move_to([0, 3.5, 0])
        self.play(
            Write(txt)
        )

                # Parameters
        rows = 4
        cols = 9
        circle_radius = 0.15
        spacing = 0.4
        
        # Create circles grid
        circles = VGroup()
        
        # Define the diagonal line boundary (approximately)
        # The line seems to go from around (3.5, 1.5) to (6.5, -1.5) in grid coordinates
        
        for i in range(rows):
            for j in range(cols):
                # Position of each circle
                x = j * spacing - (cols - 1) * spacing / 2
                y = -(i * spacing - (rows - 1) * spacing / 2)
                
                # Determine if circle should be filled based on diagonal
                # Approximate diagonal boundary: if j > i + 3.5, then empty
                if j <= i + 3:
                    # Filled circle (dark)
                    circle = Circle(radius=circle_radius, fill_opacity=1, fill_color=BLACK, stroke_width=1)
                else:
                    # Empty circle (light)
                    circle = Circle(radius=circle_radius, fill_opacity=0, stroke_color=YELLOW, stroke_width=1)
                
                circle.move_to([x, y, 0])
                circles.add(circle)
        
        # Create the diagonal line
        # Line goes from top-left of empty region to bottom-right of filled region
        line_start = [-0.6, 0.8, 0]  # Approximate position
        line_end = [1.0, -0.8, 0]    # Approximate position
        diagonal_line = Line(line_start, line_end, stroke_width=2, color=BLACK)
        
        # Create dimension arrows and labels
        
        # Top horizontal dimension (M-m+1)/2
        top_left = circles[0].get_center() + UP * 0.4
        top_right = circles[3].get_center() + UP * 0.4
        top_arrow = DoubleArrow(top_left, top_right, buff=0.1, stroke_width=2, max_tip_length_to_length_ratio=0.1)
        top_label = Tex(r"$\frac{M-m+1}{2}$").next_to(top_arrow, UP, buff=0.1).scale(0.8)
        
        # Right horizontal dimension (M+m-1)/2
        right_start = circles[4].get_center() + UP * 0.4
        right_end = circles[8].get_center() + UP * 0.4
        right_arrow = DoubleArrow(right_start, right_end, buff=0.1, stroke_width=2, max_tip_length_to_length_ratio=0.1)
        right_label = Tex(r"$\frac{M+m-1}{2}$").next_to(right_arrow, UP, buff=0.1).scale(0.8)
        
        # Left vertical dimension m
        left_top = circles[0].get_center() + LEFT * 0.4
        left_bottom = circles[27].get_center() + LEFT * 0.4  # Last row, first column
        left_arrow = DoubleArrow(left_top, left_bottom, buff=0.1, stroke_width=2, max_tip_length_to_length_ratio=0.1)
        left_label = Tex(r"$m$").next_to(left_arrow, LEFT, buff=0.1).scale(0.8)
        
        # Bottom horizontal dimension M
        bottom_left = circles[27].get_center() + DOWN * 0.4
        bottom_right = circles[35].get_center() + DOWN * 0.4  # Last row, last column
        bottom_arrow = DoubleArrow(bottom_left, bottom_right, buff=0.1, stroke_width=2, max_tip_length_to_length_ratio=0.1)
        bottom_label = Tex(r"$M$").next_to(bottom_arrow, DOWN, buff=0.1).scale(0.8)
        
        # Add all elements to the scene
        self.add(circles)
        self.add(diagonal_line)
        self.add(top_arrow, top_label)
        self.add(right_arrow, right_label)
        self.add(left_arrow, left_label)
        self.add(bottom_arrow, bottom_label)
        
        # Center everything
        everything = VGroup(circles, diagonal_line, top_arrow, top_label, 
                           right_arrow, right_label, left_arrow, left_label,
                           bottom_arrow, bottom_label)

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine,", font_size=30, color=BLACK),
            Tex(r"vol. 70, no. 4,", font_size=30, color=BLACK),
            Tex(r"(Oct. 1997), p. 294.", font_size=30, color=BLACK)
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