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

        # More text
        txt_3 = Tex(
            r"$N = 2^n \times (2k + 1), n \geq 0, k \geq 1$",
            font_size=22, color=BLACK
        )
        txt_4 = Tex(
            r"$m = \min\{2^{n + 1}, 2k + 1 \}$",
            font_size=22, color=BLACK
        )
        txt_5 = Tex(
            r"$M = \max\{2^{n + 1}, 2k + 1 \}$",
            font_size=22, color=BLACK
        )
        txt_6 = Tex(
            r"$2 N = m \times M$",
            font_size=22, color=BLACK
        )
        txt2 = VGroup(txt_3, txt_4, txt_5, txt_6).\
            arrange(DOWN, center=True, buff=0.1).\
            move_to([0, 2, 0])
        self.play(
            Write(txt2)
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
                if j <= i + 2:
                    # Filled circle (dark)
                    circle = Circle(
                        radius=circle_radius,
                        fill_opacity=1, fill_color=WHITE,
                        stroke_width=1, stroke_color=BLACK
                    )
                else:
                    # Empty circle (light)
                    circle = Circle(
                        radius=circle_radius,
                        fill_opacity=1, fill_color=WHITE,
                        stroke_width=1, stroke_color=BLACK
                    )
                
                circle.move_to([x, y, 0])
                circles.add(circle)
        circles.move_to([0, -1.5, 0])
        self.play(
            Create(circles),
            run_time=2
        )

        # Left vertical dimension m
        left_top = circles[0].get_center() + LEFT * 0.3 + UP * 0.2
        left_bottom = circles[27].get_center() + LEFT * 0.3 + DOWN * 0.2
        left_arrow = DoubleArrow(
            left_top, left_bottom, buff=0.1, stroke_width=1,
            max_tip_length_to_length_ratio=0.1, color=BLACK
        )
        left_label = Tex(r"$m$", color=BLACK, font_size=18).\
            next_to(left_arrow, LEFT, buff=0.05)
        
        # Bottom horizontal dimension M
        bottom_left = circles[27].get_center() + DOWN * 0.3 + LEFT * 0.3
        bottom_right = circles[35].get_center() + DOWN * 0.3 + RIGHT * 0.3
        bottom_arrow = DoubleArrow(
            bottom_left, bottom_right, buff=0.1, stroke_width=1,
            max_tip_length_to_length_ratio=0.05, color=BLACK
        )
        bottom_label = Tex(r"$M$", color=BLACK, font_size=18).\
            next_to(bottom_arrow, DOWN, buff=0.1)
        

        self.play(
            Create(left_arrow),
            Write(left_label),
            Create(bottom_arrow),
            Write(bottom_label)
        )
        
        # Create the diagonal line
        # Line goes from top-left of empty region to bottom-right of filled region
        line_start = [-0.8, 0.8 - 1.5, 0]  # Approximate position
        line_end = [0.8, -0.8 - 1.5, 0]    # Approximate position
        diagonal_line = Line(line_start, line_end, stroke_width=2, color=BLACK)
        
        self.play(Create(diagonal_line))

        # Color the circles
        cicles_color = VGroup()
        for i in range(rows):
            for j in range(cols):
                # Position of each circle
                x = j * spacing - (cols - 1) * spacing / 2
                y = -(i * spacing - (rows - 1) * spacing / 2)
                
                # Determine if circle should be filled based on diagonal
                # Approximate diagonal boundary: if j > i + 3.5, then empty
                if j <= i + 2:
                    # Filled circle (dark)
                    circle = Circle(
                        radius=circle_radius,
                        fill_opacity=1, fill_color=RED,
                        stroke_width=1, stroke_color=BLACK
                    )
                else:
                    # Empty circle (light)
                    circle = Circle(
                        radius=circle_radius,
                        fill_opacity=1, fill_color=BLUE,
                        stroke_width=1, stroke_color=BLACK
                    )
                
                circle.move_to([x, y, 0])
                cicles_color.add(circle)
        cicles_color.move_to([0, -1.5, 0])
        self.play(
            Create(cicles_color),
            run_time=2
        )


        # Create dimension arrows and labels        
        # Top horizontal dimension (M-m+1)/2
        top_left = cicles_color[0].get_center() + UP * 0.3 + LEFT * 0.2
        top_right = cicles_color[3].get_center() + UP * 0.3 + LEFT * 0.2
        top_arrow = DoubleArrow(
            top_left, top_right, buff=0, stroke_width=1,
            max_tip_length_to_length_ratio=0.1, color=BLACK
        )
        top_label = Tex(r"$\frac{M-m+1}{2}$", color=BLACK, font_size=18).\
            next_to(top_arrow, UP, buff=0.1)
        
        # Right horizontal dimension (M+m-1)/2
        right_start = cicles_color[4].get_center() + UP * 0.3 + LEFT * 0.5
        right_end = cicles_color[8].get_center() + UP * 0.3 + RIGHT * 0.15
        right_arrow = DoubleArrow(
            right_start, right_end, buff=0, stroke_width=1,
            max_tip_length_to_length_ratio=0.05, color=BLACK
        )
        right_label = Tex(r"$\frac{M+m-1}{2}$", color=BLACK, font_size=18).\
            next_to(right_arrow, UP, buff=0.1)
        
        self.play(
            Create(top_arrow),
            Write(top_label),
            Create(right_arrow),
            Write(right_label)
        )

        # Final formula
        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, 0.5, 0])
        txt_formula3 = Tex(r"$N = \left(\frac{M - m + 1}{2}\right) + \left(\frac{M - m + 1}{2} + 1\right) + \cdots + \left(\frac{M + m - 1}{2}\right)$",
            font_size=16, color=BLACK).move_to([0, 0.5, 0])

        self.play(
            Create(rect),
            Write(txt_formula3)
        )
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