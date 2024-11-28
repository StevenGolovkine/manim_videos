"""
Visual proof of the sums of odd integers.
Proofs without Words II. Roger B. Nelsen. p. 27.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Dot, BraceBetweenPoints, RoundedRectangle, Line
from manim import Create, Uncreate, Write
from manim import VGroup, TransformFromCopy
from manim import Tex

from manim import config

from manim import LEFT, RIGHT, DOWN, PI

# COLORS
BLUE = "#648FFF"
VIOLET = "#785EF0"
RED = "#DC267F"
ORANGE = "#FE6100"
YELLOW = "#FFB000"
BLACK = "#000000"
WHITE = "#FFFFFF"

# Make it vertical
SCALE_FACTOR = 1
# Flip width => height, height => width
tmp_pixel_height = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = tmp_pixel_height
# Change coord system dimensions
config.frame_height = config.frame_height / SCALE_FACTOR
config.frame_width = config.frame_height * 9 / 16


class Pizza(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame.save_state()

        txt_copy = Tex(r"@Math\&Moi", font_size=12, color=BLACK)\
            .to_edge(RIGHT + DOWN, buff=0.1)
        self.add(txt_copy)

        # Introduction text
        txt_title = [
            Tex(r"Comment couper", font_size=48, color=BLACK),
            Tex(r"une pizza en huit", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Carter and Wagon (1994)", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        self.play(
            Write(txt_title),
            Write(txt)
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt)
        )
        self.wait(1)

        # Pizza
        circle = Dot(
            [0, 0, 0], radius=2,
            color=WHITE, stroke_color=BLACK, stroke_width=2
        )
        self.play(
            Create(circle)
        )

        # Different point on the circle
        theta_v = PI / 2.5
        theta_h = PI / 8
        point_A = Dot([2 * np.cos(theta_v), 2 * np.sin(theta_v), 0], color=BLACK)
        point_B = Dot([2 * np.cos(theta_h), 2 * np.sin(theta_h), 0], color=BLACK)
        point_C = Dot([2 * np.cos(theta_v), 2 * np.sin(-theta_v), 0], color=RED)
        point_D = Dot([2 * np.cos(PI - theta_h), 2 * np.sin(theta_h), 0], color=BLACK)
        
        self.add(point_A, point_B, point_C, point_D)

        point_center = Dot([2 * np.cos(theta_v), 2 * np.sin(theta_h), 0], color=BLACK)

        self.add(point_center)

        line_v = Line(start=point_A, end=point_C, color=RED)
        line_h = Line(start=point_B, end=point_D, color=RED)


        b = np.sin(theta_h) - np.cos(theta_v)
        x = (- 2 * b + 2 * np.sqrt(2 - b**2)) / 2
        y = (2 * b + 2 * np.sqrt(2 - b**2)) / 2
        point_E = Dot([x, y, 0], color=RED)

        x = (- 2 * b - 2 * np.sqrt(2 - b**2)) / 2
        y = (2 * b - 2 * np.sqrt(2 - b**2)) / 2
        point_F = Dot([x, y, 0], color=RED)
        self.add(point_E, point_F)

        line_bt = Line(start=point_E, end=point_F, color=RED)


        b = np.sin(theta_h) + np.cos(theta_v)
        x = (2 * b + 2 * np.sqrt(2 - b**2)) / 2
        y = (2 * b - 2 * np.sqrt(2 - b**2)) / 2
        point_G = Dot([x, y, 0], color=RED)

        x = (2 * b - 2 * np.sqrt(2 - b**2)) / 2
        y = (2 * b + 2 * np.sqrt(2 - b**2)) / 2
        point_H = Dot([x, y, 0], color=RED)
        self.add(point_G, point_H)
        
        line_tb = Line(start=point_G, end=point_H, color=RED)

        mid = Dot([0, 0, 0], color=BLUE)
        self.add(mid)

        self.play(
            Create(line_v),
            Create(line_h),
            Create(line_bt),
            Create(line_tb)
        )
        self.wait(1)