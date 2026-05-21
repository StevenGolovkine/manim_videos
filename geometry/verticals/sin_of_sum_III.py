"""
Visual proof of the sine of the sum formula
Proofs without Words III. Roger B. Nelsen. p. 55.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, FadeTransform, TransformFromCopy
from manim import VGroup, FadeIn, FadeOut , FunctionGraph, Rotate
from manim import Line, Point, Polygon, RoundedRectangle, Square, Angle, Arc, Arrow
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
            Tex(r"Long Wang", font_size=28, color=BLACK)
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

        # Figure
        formula = Tex(
            r"$\sin(u+v)=\sin u\cos v+\sin v\cos u$",
            font_size=25, color=BLACK
        ).move_to([0, 2.45, 0])
        formula.scale_to_fit_width(config.frame_width - 0.35)
        self.play(Write(formula))

        u = 29 * DEGREES
        v = 28 * DEGREES
        height = 1
        base_y = -0.8

        H = np.array([0, base_y, 0])
        P = H + np.array([0, height, 0])
        A = H + np.array([-height / np.tan(v), 0, 0])
        B = H + np.array([height / np.tan(u), 0, 0])

        def angle_of(start, end):
            diff = end - start
            return np.arctan2(diff[1], diff[0])

        def point_on_perpendicular_projection(point, start, theta):
            direction = np.array([np.cos(theta), np.sin(theta), 0])
            return start + np.dot(point - start, direction) * direction

        def right_angle_mark(corner, p1, p2, size=0.14):
            side_1 = p1 - corner
            side_2 = p2 - corner
            side_1 = side_1 / np.linalg.norm(side_1)
            side_2 = side_2 / np.linalg.norm(side_2)
            square_corner = corner + size * side_1 + size * side_2
            return VGroup(
                Line(corner + size * side_1, square_corner, color=BLACK, stroke_width=2),
                Line(corner + size * side_2, square_corner, color=BLACK, stroke_width=2),
            )

        def side_label(tex, start, end, offset=0.12, side=1, font_size=24, t=0.5):
            direction = end - start
            direction = direction / np.linalg.norm(direction)
            normal = side * np.array([-direction[1], direction[0], 0])
            label = Tex(tex, font_size=font_size, color=BLACK)
            label.rotate(angle_of(start, end))
            label.move_to(start + t * (end - start) + offset * normal)
            return label

        theta_left_top = angle_of(P, A)
        if theta_left_top < 0:
            theta_left_top += 2 * PI
        theta_left_top -= u + v
        C = point_on_perpendicular_projection(A, P, theta_left_top)

        theta_right_top = angle_of(P, B) + u + v
        D = point_on_perpendicular_projection(B, P, theta_right_top)

        base_left = Line(A, H, color=BLACK, stroke_width=2)
        base_right = Line(H, B, color=BLACK, stroke_width=2)
        left_hypotenuse = Line(A, P, color=BLACK, stroke_width=2)
        right_hypotenuse = Line(P, B, color=BLACK, stroke_width=2)
        altitude = Line(P, H, color=BLACK, stroke_width=2)
        left_outer = Line(A, C, color=BLACK, stroke_width=2)
        left_top = Line(C, P, color=BLACK, stroke_width=2)
        right_top = Line(P, D, color=BLACK, stroke_width=2)
        right_outer = Line(D, B, color=BLACK, stroke_width=2)

        lines = VGroup(
            base_left, base_right,
            left_hypotenuse, right_hypotenuse,
        )

        labels = VGroup(
            Tex(r"$v$", font_size=25, color=BLACK).move_to(A + [0.55, 0.12, 0]),
            Tex(r"$u$", font_size=25, color=BLACK).move_to(B + [-0.45, 0.12, 0]),
        )

        angle_v = Arc(
            radius=0.32, start_angle=0, angle=v,
            arc_center=A, color=BLACK, stroke_width=2
        )
        angle_u = Arc(
            radius=0.32, start_angle=PI - u, angle=u,
            arc_center=B, color=BLACK, stroke_width=2
        )

        angle_marks = VGroup(
            angle_v,
            angle_u,
        )

        self.play(
            Create(lines),
            Create(angle_marks),
            Write(labels),
        )

        self.play(
            Create(altitude),
            Create(right_angle_mark(H, P, B)),
        )

        theta_PC = angle_of(P, C)
        theta_PA = angle_of(P, A)
        if theta_PA < theta_PC:
            theta_PA += 2 * PI
        angle_sum = Arc(
            radius=0.36, start_angle=theta_PC, angle=theta_PA - theta_PC,
            arc_center=P, color=BLACK, stroke_width=2
        )

        angle_sum_label = Tex(r"$u+v$", font_size=18, color=BLACK).\
            move_to(P + [-0.7, 0.18, 0])

        self.play(
            Create(left_outer),
            Create(left_top),
            Create(angle_sum),
            Create(right_angle_mark(C, A, P)),
            Write(angle_sum_label),
        )

        self.play(
            Create(right_top),
            Create(right_outer),
            Create(right_angle_mark(D, P, B)),
        )

        self.play(
            Write(
                side_label(
                    r"$\sin u$", A, P, offset=0.1, side=1,
                    font_size=18, t=0.43
                )
            ),
            Write(
                side_label(
                    r"$\sin(u+v)\cdot\sin u$",
                    A, C, offset=0.1, side=1, font_size=18, t=0.42
                )
            )
        )

        self.play(
            Write(
                side_label(
                    r"$\sin v$", P, B, offset=0.1, side=1,
                    font_size=18, t=0.57
                )
            ),
            Write(
                side_label(
                    r"$\sin(u+v)\cdot\sin v$",
                    D, B, offset=0.1, side=1, font_size=18, t=0.42
                )
            )
        )

        self.play(
            Write(
                Tex(r"$\sin u\cdot\sin v$", font_size=18, color=BLACK)
                    .rotate(PI / 2)
                    .move_to(altitude.get_center() + 0.2 * LEFT + 0.03 * DOWN)
            ),
            Write(
                Tex(r"$\sin u\cdot\cos v$", font_size=18, color=BLACK)
                    .next_to(base_left, DOWN, buff=0.08)
            ),
            Write(
                Tex(r"$\sin v\cdot\cos u$", font_size=18, color=BLACK)
                    .next_to(base_right, DOWN, buff=0.08)
            )
        )


        arrow_y = base_y - 0.67
        left_arrow = Arrow(
            [H[0] - 0.62, arrow_y, 0], [A[0], arrow_y, 0],
            buff=0, color=BLACK, stroke_width=2,
            max_tip_length_to_length_ratio=0.12
        )
        right_arrow = Arrow(
            [H[0] + 0.62, arrow_y, 0], [B[0], arrow_y, 0],
            buff=0, color=BLACK, stroke_width=2,
            max_tip_length_to_length_ratio=0.12
        )
        arrow_label = Tex(
            r"$\sin(u+v)$", font_size=27, color=BLACK
        ).move_to([H[0], arrow_y + 0.02, 0])
        dimension = VGroup(left_arrow, right_arrow, arrow_label)

        self.play(
            Create(dimension),
            run_time=2
        )


        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"College Mathematics Journal,", font_size=30, color=BLACK),
            Tex(r"vol. 33, no. 5 (Dec. 2002),", font_size=30, color=BLACK),
            Tex(r"p. 398", font_size=30, color=BLACK),
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
