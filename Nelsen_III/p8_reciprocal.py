"""
Visual proof of the reciprocal of Pythagorean Theorem.
Proofs without Words III. Roger B. Nelsen. p. 8.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Rotate, RightAngle, Transform
from manim import VGroup, FadeIn, FadeOut , FunctionGraph
from manim import DashedVMobject, Line, Dot, Polygon, RoundedRectangle
from manim import Text, Tex

from manim import line_intersection

from manim import config
from manim import ORIGIN, LEFT, RIGHT, DOWN, LIGHT, UP, PI, DEGREES

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


class Pythagore(MovingCameraScene):
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
            Tex(r"Une réciproque du", font_size=48, color=BLACK),
            Tex(r"théorème de", font_size=48, color=BLACK),
            Tex(r"Pythagore", font_size=48, color=BLACK),
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

        # First triangle and text
        A = [-1.75, 0, 0]
        B = [1.75, 0, 0]
        C = [-0.75, np.sqrt(2.5), 0]
        H = [-0.75, 0, 0]

        line_AB = Line(A, B, color=BLACK)
        line_AC = Line(A, C, color=BLACK)
        line_BC = Line(B, C, color=BLACK)
        line_CH = DashedVMobject(Line(C, H, color=BLACK), num_dashes=20, color=BLACK)

        triangle_b = Polygon(
            A, B, C,
            stroke_width=2,
            color=BLACK, fill_color=BLUE, fill_opacity=1
        )
        txt_a = Tex(r"$a$", font_size=36, color=BLACK)\
            .next_to(line_AC.get_center(), UP + LEFT, buff=0.1)
        txt_b = Tex(r"$b$", font_size=36, color=BLACK)\
            .next_to(line_BC.get_center(), UP + RIGHT, buff=0.1)
        txt_c = Tex(r"$c$", font_size=36, color=BLACK)\
            .next_to(triangle_b, DOWN, buff=0.1)
        angle_ACB = RightAngle(
            line_AC, line_BC,
            color=BLACK, quadrant=(-1,-1), length=0.2, stroke_width=1
        )

        self.play(
            Create(triangle_b),
            Write(txt_a),
            Write(txt_b),
            Write(txt_c),
            Create(angle_ACB)
        )

        txt_h = Tex(r"$h$", font_size=36, color=BLACK)\
            .next_to(line_CH, LEFT, buff=0.1)
        angle_CHB = RightAngle(
            Line(C, H, color=BLACK), line_AB,
            color=BLACK, length=0.2, stroke_width=1, quadrant=(-1, 1)
        )
        self.play(
            Create(line_CH),
            Write(txt_h),
            Create(angle_CHB)
        )

        # Write formula
        formula = Tex(
            r"$\frac{1}{2} ab = \frac{1}{2} ch$",
            font_size=30, color=BLACK
        ).move_to([0, 2.5, 0])

        self.play(Write(formula))

        formula2 = Tex(
            r"$h = \frac{ab}{c}$",
            font_size=30, color=BLACK
        ).move_to([0, 2.5, 0])

        self.play(Transform(formula, formula2))

        # Multiply by 1 / ab
        txt_aab = Tex(r"$a \times \frac{1}{ab}$", font_size=30, color=BLACK)\
            .next_to(line_AC.get_center(), UP + LEFT, buff=0.1)
        txt_bab = Tex(r"$b \times \frac{1}{ab}$", font_size=30, color=BLACK)\
            .next_to(line_BC.get_center(), UP + RIGHT, buff=0.1)
        txt_cab = Tex(r"$c \times \frac{1}{ab}$", font_size=30, color=BLACK)\
            .next_to(triangle_b, DOWN, buff=0.1)
        
        self.play(
            Transform(txt_a, txt_aab),
            Transform(txt_b, txt_bab),
            Transform(txt_c, txt_cab),
        )

        # Transform 
        txt_1b = Tex(r"$\frac{1}{b}$", font_size=30, color=BLACK)\
            .next_to(line_AC.get_center(), UP + LEFT, buff=0.1)
        txt_1a = Tex(r"$\frac{1}{a}$", font_size=30, color=BLACK)\
            .next_to(line_BC.get_center(), UP + RIGHT, buff=0.1)
        txt_1h = Tex(r"$\frac{1}{h}$", font_size=30, color=BLACK)\
            .next_to(triangle_b, DOWN, buff=0.1)
        
        self.play(
            Transform(txt_a, txt_1b),
            Transform(txt_b, txt_1a),
            Transform(txt_c, txt_1h),
        )

        # Write resutls
        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, -1.5, 0])
        txt = Tex(
            r"$\frac{1}{a^2} + \frac{1}{b^2} = \frac{1}{h^2}$",
            font_size=52, color=BLACK
        ).move_to([0, -1.5, 0])

        rect.z_index = 0
        txt.z_index = 1
        self.play(
            Create(rect),
            Write(txt)
        )

        

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine, vol. 82,", font_size=30, color=BLACK),
            Tex(r"no. 5 (Dec. 2009), p.370.", font_size=30, color=BLACK),
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