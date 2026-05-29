"""
Visual proof of the sine of the sum formula
Proofs without Words I. Roger B. Nelsen. p. 29.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, TransformFromCopy
from manim import VGroup, FadeIn, FadeOut , FunctionGraph, Rotate
from manim import Line, Point, Polygon, RoundedRectangle, Circle, Angle
from manim import line_intersection, DashedLine, RightAngle
from manim import Text, Tex, Intersection

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


def get_vertices(obj: Polygon) -> list[Line]:
    vertices = obj.get_vertices()
    coords_vertices = []
    for i in range(len(vertices)):
        if i < len(vertices)-1:
            p1, p2 = [vertices[i], vertices[i + 1]]
        else:
            p1, p2 = [vertices[-1], vertices[0]]
        guide_line = Line(p1, p2)
        coords_vertices.append(guide_line)
    return coords_vertices


class Sum(MovingCameraScene):
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
            Tex(r"Le sinus de", font_size=48, color=BLACK),
            Tex(r"la somme de", font_size=48, color=BLACK),
            Tex(r"deux angles", font_size=48, color=BLACK),
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

        # Circle
        circle = Circle(radius=1.5, color=BLACK, stroke_width=2)
        circle.move_to([0, 2, 0])
        self.play(Create(circle))

        # Triangle on the circle
        A = circle.point_at_angle(7 * PI / 6)
        B = circle.point_at_angle(- PI / 6)  
        C = circle.point_at_angle(5 * PI / 8)

        triangle = Polygon(A, B, C, stroke_width=2)
        self.play(Create(triangle))

        # Angle and distance
        AB = Line(A, B)
        BC = Line(B, C)
        CA = Line(C, A)

        alpha = Angle(
            AB, CA, quadrant=(1, -1),
            radius=0.3, color=BLACK, stroke_width=2
        )
        txt_alpha = Tex(r"$\alpha$", font_size=15, color=BLACK).\
            move_to(alpha.get_center() + [0.15, 0.1, 0])
        txt_a = Tex(r"$a$", font_size=20, color=BLACK).\
            move_to(BC.get_center() + [0.1, 0.1, 0])
        self.play(
            Create(alpha), Write(txt_alpha), Write(txt_a)
        )

        beta = Angle(
            AB, BC, quadrant=(-1, 1), other_angle=True,
            radius=0.3, color=BLACK, stroke_width=2
        )
        txt_beta = Tex(r"$\beta$", font_size=15, color=BLACK).\
            move_to(beta.get_center() - [0.15, 0, 0])
        txt_b = Tex(r"$b$", font_size=20, color=BLACK).\
            move_to(CA.get_center() - [0.15, -0.1, 0])
        self.play(
            Create(beta), Write(txt_beta), Write(txt_b)
        )

        gamma = Angle(
            CA, BC, quadrant=(1, -1),
            radius=0.3, color=BLACK, stroke_width=2
        )
        txt_gamma = Tex(r"$\gamma$", font_size=15, color=BLACK).\
            move_to(gamma.get_center() + [0, -0.15, 0])
        txt_c = Tex(r"$c$", font_size=20, color=BLACK).\
            move_to(AB.get_center() - [0.1, 0.1, 0])
        self.play(
            Create(gamma), Write(txt_gamma), Write(txt_c)
        )

        # Vertical line 
        H = Point([C[0], A[1], 0])
        CH = DashedLine(C, H, color=BLACK, stroke_width=2)
        r_angle = RightAngle(
            CH, AB, quadrant=(-1, 1), length=0.1, color=BLACK, stroke_width=2
        )
        self.play(
            Create(CH),
            Create(r_angle)
        )

        # c = a cos(beta) + b cos(alpha)
        AH = Line(A, H, color=RED, stroke_width=4)
        HB = Line(H, B, color=RED, stroke_width=4)

        txt_c_eq = Tex(
            r"$c$", r"$~=~$", r"$a \cos(\beta)$", r"$~+~$", r"$b \cos(\alpha)$",
            font_size=20, color=BLACK
        ).move_to([0, 0, 0])
        self.play(  
            TransformFromCopy(txt_c, txt_c_eq[0]),
            Write(txt_c_eq[1]),
        )

        self.play(
            Create(AH),
            Write(txt_c_eq[2]),
        )
        self.play(
            Uncreate(AH),
            run_time=0.5
        )

        self.play(
            Write(txt_c_eq[3]),
            Create(HB),
            Write(txt_c_eq[4]),
        )
        self.play(
            Uncreate(HB),
            run_time=0.5
        )

        # Inside triangle for gamma
        R = circle.get_center()
        I = Point([R[0], A[1], 0])
        AR = Line(A, R, color=RED, stroke_width=2)
        RI = Line(R, I, color=RED, stroke_width=2)
        AI = Line(A, I, color=RED, stroke_width=2)
        self.play(
            Uncreate(CH),
            Uncreate(r_angle),
            Create(AR),
            Create(RI),
            Create(AI)
        )

        txt_c2 = Tex(
            r"$c / 2$",
            font_size=15, color=BLACK
        ).next_to(AI, DOWN, buff=0.1)
        txt_r = Tex(
            r"$r$",
            font_size=15, color=BLACK
        ).move_to(AR.get_center() - [0.1, -0.1, 0])
        gamma2 = Angle(
            AR, RI, quadrant=(-1, 1),
            radius=0.2, color=BLACK, stroke_width=2
        )
        txt_gamma2 = Tex(r"$\gamma$", font_size=15, color=BLACK).\
            move_to(gamma2.get_center() + [-0.05, -0.15, 0])
        self.play(
            Write(txt_c2),
            Write(txt_r),
            Create(gamma2),
            Write(txt_gamma2)
        )

        txt_singamma = Tex(
            r"$r = \frac{1}{2} \Rightarrow \sin \gamma = \frac{c / 2}{1 / 2} = c$", font_size=20, color=BLACK
        ).next_to(txt_c_eq, DOWN, buff=0.1)
        self.play(
            Write(txt_singamma)
        )

        self.play(
            Uncreate(AR),
            Uncreate(RI),
            Uncreate(AI),
            Uncreate(gamma2),
            Uncreate(txt_r),
            Uncreate(txt_gamma2),
            Uncreate(txt_c2)
        )

        # Inside triangle for alpha
        J = BC.get_projection(R)
        BR = Line(B, R, color=RED, stroke_width=2)
        RJ = Line(R, J, color=RED, stroke_width=2)
        BJ = Line(B, J, color=RED, stroke_width=2)
        self.play(
            Create(BR),
            Create(RJ),
            Create(BJ)
        )

        txt_a2 = Tex(
            r"$a / 2$",
            font_size=15, color=BLACK
        ).move_to(BJ.get_center() + [0.1, 0.1, 0])
        txt_r2 = Tex(
            r"$r$",
            font_size=15, color=BLACK
        ).move_to(BR.get_center() - [0.1, 0.1, 0])
        alpha2 = Angle(
            BR, RJ, quadrant=(-1, 1),
            radius=0.1, color=BLACK, stroke_width=2
        )
        txt_alpha2 = Tex(r"$\alpha$", font_size=15, color=BLACK).\
            move_to(alpha2.get_center() + [0.1, 0, 0])
        self.play(
            Write(txt_a2),
            Write(txt_r2),
            Create(alpha2),
            Write(txt_alpha2)
        )

        txt_sinalpha = Tex(
            r"$r = \frac{1}{2} \Rightarrow \sin \alpha = \frac{a / 2}{1 / 2} = a$", font_size=20, color=BLACK
        ).next_to(txt_singamma, DOWN, buff=0.1)
        self.play(
            Write(txt_sinalpha)
        )

        self.play(
            Uncreate(BR),
            Uncreate(RJ),
            Uncreate(BJ),
            Uncreate(alpha2),
            Uncreate(txt_r2),
            Uncreate(txt_alpha2),
            Uncreate(txt_a2)
        )

        # Inside triangle for beta
        K = CA.get_projection(R)
        CR = Line(C, R, color=RED, stroke_width=2)
        RK = Line(R, K, color=RED, stroke_width=2)
        CK = Line(C, K, color=RED, stroke_width=2)
        self.play(
            Create(CR),
            Create(RK),
            Create(CK)
        )

        txt_b2 = Tex(
            r"$b / 2$",
            font_size=15, color=BLACK
        ).move_to(CK.get_center() - [0.2, 0.2, 0])
        txt_r3 = Tex(
            r"$r$",
            font_size=15, color=BLACK
        ).move_to(CR.get_center() + [0.1, 0, 0])
        beta2 = Angle(
            CR, RK, quadrant=(-1, 1),
            radius=0.2, color=BLACK, stroke_width=2
        )
        txt_beta2 = Tex(r"$\beta$", font_size=15, color=BLACK).\
            move_to(beta2.get_center() + [-0.1, 0.1, 0])
        self.play(
            Write(txt_b2),
            Write(txt_r3),
            Create(beta2),
            Write(txt_beta2)
        )

        txt_sinbeta = Tex(
            r"$r = \frac{1}{2} \Rightarrow \sin \beta = \frac{b / 2}{1 / 2} = b$", font_size=20, color=BLACK
        ).next_to(txt_sinalpha, DOWN, buff=0.1)
        self.play(
            Write(txt_sinbeta)
        )
        self.play(
            Uncreate(CR),
            Uncreate(RK),
            Uncreate(CK),
            Uncreate(beta2),
            Uncreate(txt_r3),
            Uncreate(txt_beta2),
            Uncreate(txt_b2)
        )

        # Write formula
        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, -2, 0])
        txt_formula = Tex(
            r"$\sin(\alpha + \beta) = $", r"$~\sin( \pi - (\alpha + \beta) )$",
            font_size=20, color=BLACK
        ).move_to([0, -2, 0])
        self.play(
            Create(rect),
            Write(txt_formula)
        )

        txt_formula2 = Tex(
            r"$\sin(\gamma)$",
            font_size=20, color=BLACK
        ).move_to(txt_formula[1].get_center())
        self.play(
            Transform(txt_formula[1], txt_formula2)
        )

        txt_formula3 = Tex(
            r"$\sin(\alpha+\beta) = \sin(\alpha)\cos(\beta) + \cos(\alpha)\sin(\beta)$",
            font_size=20, color=BLACK
        ).move_to([0, -2, 0])
        self.play(
            Transform(txt_formula, txt_formula3)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine,", font_size=30, color=BLACK),
            Tex(r"vol. 64, no. 2 (April 1991),", font_size=30, color=BLACK),
            Tex(r"p. 97", font_size=30, color=BLACK),
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