"""
Visual proof of an arithmetic-geometric-harmonic mean inequality.
Proofs without Words III. Roger B. Nelsen. p. 103.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Arc, Line, Brace
from manim import VGroup, FadeIn, FadeOut, FunctionGraph, RightAngle
from manim import Text, Tex

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
            Tex(r"L'inégalité des", font_size=48, color=BLACK),
            Tex(r"moyennes", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Pappus d'Alexandrie", font_size=28, color=BLACK)
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

        # Text
        txt = [
            Tex(r"$a, b > 0 \Rightarrow \frac{a + b}{2} \geq \sqrt{ab} \geq \frac{2ab}{a + b}$", font_size=30, color=BLACK),
        ]
        txt = VGroup(*txt).arrange(DOWN, aligned_edge=LEFT).move_to([0, 2.5, 0])

        self.play(
            Write(txt),
        )

        # Half-circle 
        half_circle = Arc(
            radius=2,
            start_angle=0,
            angle=PI,
            color=BLACK
        )
        
        A = half_circle.get_start()
        B = half_circle.get_end()
        
        # Create a line connecting the extremities
        AB = Line(A, B, color=BLACK)
        O = AB.get_center()
        txt_A = Tex(r"$A$", font_size=24, color=BLACK).\
            next_to(A, DOWN, buff=0.1)
        txt_B = Tex(r"$B$", font_size=24, color=BLACK).\
            next_to(B, DOWN, buff=0.1)
        txt_O = Tex(r"$O$", font_size=24, color=BLACK).\
            next_to(O, DOWN, buff=0.1)

        self.play(
            Create(half_circle),
            Create(AB),
            Write(txt_A),
            Write(txt_B),
            Write(txt_O)
        )

        # Get a point on the half-circle
        P = half_circle.point_from_proportion(0.35)
        txt_P = Tex(r"$P$", font_size=24, color=BLACK).\
            next_to(P, UP + RIGHT, buff=0.1)
        OP = Line(O, P, color=BLACK)
        self.play(
            Create(OP),
            Write(txt_P)
        )

        # Perpendicular from P to AB
        P_proj = np.array([P[0], O[1], 0])
        txt_P_proj = Tex(r"$G$", font_size=24, color=BLACK).\
            next_to(P_proj, DOWN, buff=0.1)
        PP_proj = Line(P, P_proj, color=BLACK)
        r_angle = RightAngle(
            AB, PP_proj, length=0.2, quadrant=(-1, -1), color=BLACK, stroke_width=1
        )
        self.play(
            Create(PP_proj),
            Write(txt_P_proj),
            Create(r_angle)
        )

        # Perpendicular from P_proj to OP
        abx = P[0] - O[0]
        aby = P[1] - O[1]
        acx = P_proj[0] - O[0]
        acy = P_proj[1]- O[1]

        coeff = (abx*acx + aby*acy) / (abx*abx+aby*aby)
        dx = O[0] + abx * coeff
        dy = O[1] + aby * coeff
        H = np.array([dx, dy, 0])
        txt_H = Tex(r"$H$", font_size=24, color=BLACK).\
            next_to(H, LEFT + UP, buff=0.1)
        GH = Line(P_proj, H, color=BLACK)
        r_angle2 = RightAngle(
            OP, GH, length=0.2, quadrant=(1, -1), color=BLACK, stroke_width=1
        )

        self.play(
            Create(GH),
            Write(txt_H),
            Create(r_angle2)
        )


        # Brace from B to P_proj and from P_proj to A
        BP_proj = Line(B, P_proj, color=BLACK)
        AP_proj = Line(A, P_proj, color=BLACK)
        BP_proj_brace = Brace(BP_proj, DOWN, color=BLACK, buff=0.5)
        AP_proj_brace = Brace(AP_proj, DOWN, color=BLACK, buff=0.5)
        txt_BP_proj = Tex(r"$b$", font_size=24, color=BLACK).\
            next_to(BP_proj_brace, DOWN, buff=0.1)
        txt_AP_proj = Tex(r"$a$", font_size=24, color=BLACK).\
            next_to(AP_proj_brace, DOWN, buff=0.1)
        self.play(
            Create(BP_proj_brace),
            Create(AP_proj_brace),
            Write(txt_BP_proj),
            Write(txt_AP_proj)
        )

        # Write formulas
        txt_formulas = [
            Tex(r"$OP = \frac{a + b}{2}$", font_size=24, color=BLACK),
            Tex(r"$PG = \sqrt{ab}$", font_size=24, color=BLACK),
            Tex(r"$GH = \frac{2ab}{a + b}$", font_size=24, color=BLACK),
        ]
        txt_formulas = VGroup(*txt_formulas).arrange(RIGHT).\
            move_to([0, -2, 0])
        self.play(
            Write(txt_formulas)
        )

        txt_inequality = Tex((r"$OP \geq PG \geq GH$"), font_size=30, color=BLACK).\
            next_to(txt_formulas, DOWN, buff=0.2)
        self.play(
            Write(txt_inequality)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"American Mathematical Monthly,", font_size=26, color=BLACK),
            Tex(r"vol. 88, no. 3 (March 1981),", font_size=26, color=BLACK),
            Tex(r"p. 192.", font_size=26, color=BLACK),
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