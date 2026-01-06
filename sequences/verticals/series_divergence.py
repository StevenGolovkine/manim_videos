"""
Visual proof of the divergence of a series.
Proofs without Words II. Roger B. Nelsen. p. 114.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
from manim import Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Line, Polygon
from manim import Text, Tex, Transform, RightAngle, Angle, Circle, Dot
from manim import NumberPlane, Intersection


from manim import config
from manim import LEFT, RIGHT, DOWN, LIGHT, UP, BLUE, GREEN

# COLORS
# BLUE = "#B0E1FA"
VIOLET = "#E8C9FA"
RED = "#F79BC5"
# GREEN = "#DBF9E7"
YELLOW = "#EFE9B7"
ORANGE = "#F6CCB0"
BLACK = "#000000"
GREY = "#D0D0D0"
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


class Series(MovingCameraScene):
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
            Tex(r"La divergence", font_size=48, color=BLACK),
            Tex(r"d'une série", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Sidney H. Kung", font_size=28, color=BLACK)
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

        # Write results
        result = Tex(
            r"$n > 1 \Rightarrow \displaystyle\sum_{k=1}^{n} \frac{1}{\sqrt{n}} > \sqrt{n}$",
            font_size=30, color=BLACK
        ).move_to([0, 3, 0])
        
        self.play(Write(result))

        # Create a right triangle
        A = np.array([-2.5, 0, 0])
        B = np.array([1, 0, 0])
        C = np.array([1, 3, 0])
        txt = Tex(r"Pour $k > 1$", font_size=24, color=BLACK).\
            move_to([-1.5, 2, 0])
        triangle = Polygon(
            A,
            B,
            C,
            color=BLACK,
            fill_color=WHITE,
            fill_opacity=1,
            stroke_width=2
        )
        txt_1 = Tex(r"$1$", font_size=24, color=BLACK).\
            next_to(triangle, RIGHT, buff=0.2)
        txt_2 = Tex(r"$\sqrt{k}$", font_size=24, color=BLACK).\
            next_to(triangle.get_center(), LEFT + UP, buff=0.2)
        txt_3 = Tex(r"$\sqrt{k - 1}$", font_size=24, color=BLACK).\
            next_to(triangle, DOWN, buff=0.2)
        angle = RightAngle(
            Line(A, B),
            Line(B, C),
            length=0.2,
            quadrant=(-1, 1),
            color=BLACK,
            stroke_width=2
        )
        triangle_g = VGroup(triangle, angle, txt_1, txt_2, txt_3)

        self.play(
            Create(triangle_g),
            Write(txt),
        )

        # Projection of B on AC
        D = [1, 0, 0]
        E = [1 - 3 / np.sqrt(9 + 1), 3 / np.sqrt(9 + 1), 0]
        projection = Line(D, E, color=RED, stroke_width=2)
        self.play(Create(projection))

        # Circle with diameter AB
        circle = Circle(
            radius=3.5,
            color=BLACK, stroke_width=2
        ).move_to(A)
        self.play(
            Create(circle)
        )

        # Intersection of circle and AC
        intersection = Intersection(circle, Line(A, C), color=GREEN, stroke_width=2)
        self.play(Create(intersection))

        # Final txt
        final_txt = Tex(
            r"$\frac{1}{\sqrt{k}} > \sqrt{k} - \sqrt{k - 1}$",
            font_size=30, color=BLACK
        ).move_to([0, -3, 0])

        self.play(
            Write(final_txt)
        )
        self.wait(1)

        final_txt2 = [
            Tex(
                r"$\frac{1}{\sqrt{2}} + \frac{1}{\sqrt{3}} + \cdots + \frac{1}{\sqrt{n}} > $",
                font_size=20, color=BLACK
            ),
            Tex(
                r"$(\sqrt{2} - 1) + (\sqrt{3} - \sqrt{2}) + \cdots + (\sqrt{n} - \sqrt{n - 1})$",
                font_size=20, color=BLACK
            ),
        ]
        final_txt2 = VGroup(*final_txt2).arrange(DOWN).move_to([0, -3, 0])
        self.play(
            Transform(final_txt, final_txt2)
        )
        self.wait(1)

        final_txt3 = Tex(
            r"$1 + \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{3}} + \cdots + \frac{1}{\sqrt{n}} > \sqrt{n}$",
            font_size=30, color=BLACK
        ).move_to([0, -3, 0])
        self.play(
            Transform(final_txt, final_txt3)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"College Mathematics Journal, vol. 26,", font_size=26, color=BLACK),
            Tex(r"no. 4 (Sept. 1995), p. 301.", font_size=26, color=BLACK),
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