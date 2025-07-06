"""
Visual proof of a relation between the inradius of a right triangle and the
side of the triangle.
Proofs without Words II. Roger B. Nelsen. p. 13.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, TransformFromCopy, FadeTransform
from manim import VGroup, FadeIn, FadeOut , FunctionGraph, Rotate
from manim import Line, Circle, Polygon, RoundedRectangle, Square, Angle
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


class Triangle(MovingCameraScene):
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
            Tex(r"La rayon du cercle", font_size=48, color=BLACK),
            Tex(r"inscrit dans un", font_size=48, color=BLACK),
            Tex(r"triangle rectangle", font_size=48, color=BLACK),
            Tex(r"Partie I", font_size=24, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Liu Hui", font_size=28, color=BLACK)
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

        # Triangle
        A = [-1, -0.75 + 1.5, 0]
        B = [1, -0.75 + 1.5, 0]
        C = [1, 0.75 + 1.5, 0]
        line_AB = Line(
            A, B, color=BLACK, stroke_width=2
        )
        line_BC = Line(
            B, C, color=BLACK, stroke_width=2
        )
        line_AC = Line(
            A, C, color=BLACK, stroke_width=2
        )
        triangle_b = Polygon(
            A, B, C,
            stroke_width=2,
            color=BLACK, fill_color=BLUE, fill_opacity=1
        )
        txt_a = Tex(r"$a$", font_size=28, color=BLACK).\
            next_to(triangle_b, DOWN, buff=0.1)
        txt_b = Tex(r"$b$", font_size=28, color=BLACK).\
            next_to(triangle_b, RIGHT, buff=0.1)
        txt_c = Tex(r"$c$", font_size=28, color=BLACK).\
            next_to(triangle_b.get_center(), UP + LEFT, buff=0.1)

        self.play(
            Create(triangle_b),
            Write(txt_a),
            Write(txt_b),
            Write(txt_c)
        )

        # Inside circle
        a = 2
        b = 1.5
        c = np.sqrt(a**2 + b**2)
        xr = (b * -1 + c * 1 + a * 1) / (a + b + c) 
        yr = (b * -0.75 + c * -0.75 + a * 0.75) / (a + b + c) + 1.5
        R = [xr, yr, 0]
        r = (a * b) / (a + b + c)
        circle = Circle(
            radius=r, color=BLACK, fill_color=VIOLET, fill_opacity=1, stroke_width=2
        ).move_to(R)
        self.play(
            Create(circle),
        )

        # Inside triangle
        D = [xr, A[1], 0]
        E = [B[0], yr, 0]
        F = line_AC.point_from_proportion((a - r) / c)

        line_AR = Line(
            A, R, color=BLACK, stroke_width=2
        )
        line_CR = Line(
            C, R, color=BLACK, stroke_width=2
        )
        line_RD = Line(
            R, D, color=BLACK, stroke_width=2
        )
        line_RE = Line(
            R, E, color=BLACK, stroke_width=2
        )
        line_RF = Line(
            R, F, color=BLACK, stroke_width=2
        )
        txt_r = Tex(r"$r$", font_size=18, color=BLACK).\
            next_to(line_RE, DOWN, buff=0.1)


        self.play(
            Create(line_AR),
            Create(line_CR),
            Create(line_RD),
            Create(line_RE),
            Create(line_RF),
            Write(txt_r)
        )

        # Lots of triangles and one square
        triangle_AFR = Polygon(
            A, F, R,
            stroke_width=2,
            color=BLACK, fill_color=YELLOW, fill_opacity=0.75
        )
        triangle_ADR = Polygon(
            A, D, R,
            stroke_width=2,
            color=BLACK, fill_color=YELLOW, fill_opacity=0.75
        )
        triangle_CFR = Polygon(
            C, F, R,
            stroke_width=2,
            color=BLACK, fill_color=ORANGE, fill_opacity=0.75
        )
        triangle_CER = Polygon(
            C, E, R,
            stroke_width=2,
            color=BLACK, fill_color=ORANGE, fill_opacity=0.75
        )
        square_BERD = Polygon(
            B, E, R, D,
            stroke_width=2,
            color=BLACK, fill_color=GREEN, fill_opacity=0.75
        )

        self.play(
            Create(triangle_AFR),
            Create(triangle_ADR),
            Create(triangle_CFR),
            Create(triangle_CER),
            Create(square_BERD)
        )

        # Rotate triangles
        triangle_group = VGroup(
            triangle_AFR.copy(), triangle_ADR.copy(),
            triangle_CFR.copy(), triangle_CER.copy(),
            square_BERD.copy()
        )
        self.play(
            triangle_group.animate.rotate(PI, about_point=txt_c.get_center())
        )

        # Move the triangles and square

        # For a
        square_BERD_c = square_BERD.copy().move_to([-1, -0.75, 0])
        triangle_ADR_c = triangle_ADR.copy().next_to(
            square_BERD_c, RIGHT, buff=0
        )
        triangle_group_ADR_c = triangle_group[1].copy().next_to(
            square_BERD_c, RIGHT, buff=0
        )
        self.play(
            TransformFromCopy(square_BERD, square_BERD_c),
            TransformFromCopy(triangle_ADR, triangle_ADR_c),
            TransformFromCopy(triangle_group[1], triangle_group_ADR_c),
        )

        group_a = VGroup(
            square_BERD_c, triangle_ADR_c, triangle_group_ADR_c
        )

        txt_r1 = Tex(r"$r$", font_size=28, color=BLACK).\
            next_to(group_a, LEFT, buff=0.1)
        txt_a2 = Tex(r"$a$", font_size=28, color=BLACK).\
            next_to(group_a, DOWN, buff=0.1)
        self.play(
            Write(txt_r1),
            Write(txt_a2)
        )

        # For b
        square_BERD_c_b = triangle_group[4].copy().next_to(
            group_a, DOWN, buff=0.5, aligned_edge=LEFT
        )
        triangle_CER_c_b = triangle_CER.copy().rotate(PI / 2).next_to(
            square_BERD_c_b, RIGHT, buff=0
        )
        triangle_group_CER_c_b = triangle_group[3].copy().rotate(PI / 2).next_to(
            square_BERD_c_b, RIGHT, buff=0
        )
        self.play(
            TransformFromCopy(triangle_group[4], square_BERD_c_b),
            TransformFromCopy(triangle_CER, triangle_CER_c_b),
            TransformFromCopy(triangle_group[3], triangle_group_CER_c_b),
        )

        group_b = VGroup(
            square_BERD_c_b, triangle_CER_c_b, triangle_group_CER_c_b
        )
        
        txt_r2 = Tex(r"$r$", font_size=28, color=BLACK).\
            next_to(group_b, LEFT, buff=0.1)
        txt_b2 = Tex(r"$b$", font_size=28, color=BLACK).\
            next_to(group_b, DOWN, buff=0.1)
        self.play(
            Write(txt_r2),
            Write(txt_b2)
        )

        # For c
        triangle_AFR_c = triangle_AFR.copy().\
            rotate(-np.arccos(a / c)).\
            next_to(group_b, DOWN, buff=0.5, aligned_edge=LEFT)
        triangle_group_AFR_c = triangle_group[0].copy().\
            rotate(-np.arccos(a / c)).\
            next_to(group_b, DOWN, buff=0.5, aligned_edge=LEFT)
        triangle_CFR_c = triangle_CFR.copy().\
            rotate(PI / 2 + np.arccos(b / c)).\
            next_to(triangle_AFR_c, RIGHT, buff=0)
        triangle_group_CFR_c = triangle_group[2].copy().\
            rotate(PI / 2 + np.arccos(b / c)).\
            next_to(triangle_AFR_c, RIGHT, buff=0)
        self.play(
            TransformFromCopy(triangle_AFR, triangle_AFR_c),
            TransformFromCopy(triangle_group[0], triangle_group_AFR_c),
            TransformFromCopy(triangle_CFR, triangle_CFR_c),
            TransformFromCopy(triangle_group[2], triangle_group_CFR_c),
        )

        group_c = VGroup(
            triangle_AFR_c, triangle_group_AFR_c,
            triangle_CFR_c, triangle_group_CFR_c
        )

        txt_r3 = Tex(r"$r$", font_size=28, color=BLACK).\
            next_to(group_c, LEFT, buff=0.1)
        txt_c2 = Tex(r"$c$", font_size=28, color=BLACK).\
            next_to(group_c, DOWN, buff=0.1)
        self.play(
            Write(txt_r3),
            Write(txt_c2)
        )

        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, 0, 0])
        txt = Tex(
            r"$a$", r"$b$", r"$~=~$", r"$r$", r"$a$",
            r"$~+~$", r"$r$", r"$b$", r"$~+~$", r"$r$", r"$c$",
            font_size=28, color=BLACK
         ).move_to([0, 0, 0])

        rect.z_index = 0
        txt.z_index = 1
        self.play(
            Create(rect),
            run_time=0.5
        )
        self.play(
            TransformFromCopy(txt_a[0], txt[0]),
            TransformFromCopy(txt_b[0], txt[1]),
            Write(txt[2]),
            TransformFromCopy(txt_r1[0], txt[3]),
            TransformFromCopy(txt_a2[0], txt[4]),
            Write(txt[5]),
            TransformFromCopy(txt_r2[0], txt[6]),
            TransformFromCopy(txt_b2[0], txt[7]),
            Write(txt[8]),
            TransformFromCopy(txt_r3[0], txt[9]),
            TransformFromCopy(txt_c2[0], txt[10]),
        )

        txt_2 = Tex(
            r"$ab = r(a + b +c)$",
            font_size=28, color=BLACK
         ).move_to([0, 0, 0])
        self.play(
            FadeTransform(txt, txt_2),
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine, vol. 71,", font_size=30, color=BLACK),
            Tex(r"no. 3 (June 1998)", font_size=30, color=BLACK),
            Tex(r"p. 196", font_size=30, color=BLACK),
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