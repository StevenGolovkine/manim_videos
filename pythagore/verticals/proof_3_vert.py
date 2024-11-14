"""
Visual proof of the Pythagorean theorem.
Proofs without Words I. Roger B. Nelsen. p. 4.
"""
import numpy as np

from manim import MovingCameraScene, Mobject
from manim import Point, Square, Polygon, Line, RoundedRectangle
from manim import Create, Rotate, Transform, Uncreate, Write
from manim import TransformFromCopy
from manim import FadeTransform
from manim import VGroup
from manim import Tex

from manim import config

from manim import LEFT, RIGHT, UP, DOWN, PI, DEGREES

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


class RotateAndColor(Rotate, Transform):
    def __init__(
        self,
        mobject: Mobject,            
        angle: float,
        new_color,
        **kwargs,
    ) -> None:
        self.new_color = new_color
        super().__init__(mobject, angle=angle, **kwargs)

    def create_target(self) -> Mobject:
        target = self.mobject.copy()
        target.set_fill(self.new_color)
        target.rotate(
            self.angle,
            axis=self.axis,
            about_point=self.about_point,
            about_edge=self.about_edge,
        )
        return target


class Pythagorean(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame.save_state()

        # Camera set
        points = [
            Point(location=[0, 0, 0]),
            Point(location=[0, 1, 0]),
            Point(location=[6, 1, 0])
        ]

                # Introduction text
        txt_title = [
            Tex(r"Théorème de", font_size=48, color=BLACK),
            Tex(r"Pythagore", font_size=72, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt_dem = Tex(r"Démonstration III", font_size=48, color=BLACK)\
            .next_to(txt_title, DOWN, buff=0.7)
        txt_desc = [
            Tex(r"basée sur une preuve d'Euclide", font_size=28, color=BLACK),
            Tex(r"(vers 300 av. J.C.)", font_size=28, color=BLACK)
        ]
        txt_desc = VGroup(*txt_desc).arrange(DOWN).next_to(txt_dem, DOWN, buff=0.5)

        self.play(
            Write(txt_title), Write(txt_dem), Write(txt_desc),
            run_time=3
        )
        self.wait(3)
        self.play(Uncreate(txt_title), Uncreate(txt_dem), Uncreate(txt_desc))
        self.wait(1)


        # First triangle and text
        self.play(
            self.camera.frame.animate.move_to(points[0]).set(height=10),
            run_time=0.1
        )
        triangle_b = Polygon(
            [-2, -1.5, 0], [2, -1.5, 0], [2, 1.5, 0],
            color=BLACK, fill_color=BLUE, fill_opacity=1
        )
        txt_a = Tex(r"$a$", font_size=48, color=BLACK)\
            .next_to(triangle_b, DOWN)
        txt_b = Tex(r"$b$", font_size=48, color=BLACK)\
            .next_to(triangle_b, RIGHT)
        txt_c = Tex(r"$c$", font_size=48, color=BLACK)\
            .next_to(triangle_b.get_center(), UP + LEFT)

        self.play(
            Create(triangle_b),
            Write(txt_a),
            Write(txt_b),
            Write(txt_c)
        )

        self.wait(1)

        # Remove txt and rotate the triangle
        self.play(
            Uncreate(txt_a),
            Uncreate(txt_b),
            Uncreate(txt_c),
            Rotate(triangle_b, 143 * DEGREES, about_point=[0, 0, 0]),
        )

        # Expand the squares
        self.play(
            self.camera.frame.animate.move_to(points[0]).set(height=18)
        )

        coords_vertices_b = get_vertices(triangle_b)

        sq_a2 = Square(side_length=3, stroke_color=BLACK)\
            .rotate(PI / 2 - np.arcsin(0.6))\
            .move_to(coords_vertices_b[1], DOWN + RIGHT)
        txt_a2  = Tex(r"$a^2$", font_size=72, color=BLACK)\
            .move_to(sq_a2.get_center_of_mass())
        txt_a2.z_index = 1
        self.play(
            FadeTransform(coords_vertices_b[1], sq_a2, stretch=True),
            Write(txt_a2),
            run_time=1.5
        )


        sq_b2 = Square(side_length=4, stroke_color=BLACK)\
            .rotate(np.arcsin(0.8))\
            .move_to(coords_vertices_b[0], DOWN + LEFT)
        txt_b2  = Tex(r"$b^2$", font_size=72, color=BLACK)\
            .move_to(sq_b2.get_center_of_mass())
        txt_b2.z_index = 1
        self.play(
            FadeTransform(coords_vertices_b[0], sq_b2, stretch=True),
            Write(txt_b2),
            run_time=1.5
        )

        sq_c2 = Square(side_length=5, stroke_color=BLACK)\
            .move_to(coords_vertices_b[2], UP)
        txt_c2  = Tex(r"$c^2$", font_size=72, color=BLACK)\
            .move_to(sq_c2.get_center_of_mass())
        self.play(
            FadeTransform(coords_vertices_b[2], sq_c2, stretch=True),
            Write(txt_c2),
            run_time=1.5
        )

        # Expand lines
        coords_vertices_a2 = get_vertices(sq_a2)
        line_a = coords_vertices_a2[0].copy()
        self.play(
            self.camera.frame.animate.move_to(points[1]).set(height=20),
            Create(line_a.set(color=RED).set_length(15))
        )

        coords_vertices_b2 = get_vertices(sq_b2)
        line_b = coords_vertices_b2[3].copy()
        self.play(
            Create(line_b.set(color=RED).set_length(15))
        )

        # Get parallelogram from square a2
        a1 = line_a.get_slope()
        vertices = sq_a2.get_vertices()
        b = vertices[0][1] - a1 * vertices[0][0]
        point = [-4, -4 * a1 + b, 0]
        a2 = (point[1] - vertices[3][1]) / (point[0] - vertices[3][0])
        xx = (a1 * point[0] - a2 * vertices[2][0] - point[1] + vertices[2][1]) / (a1 - a2)
        yy = vertices[2][1] + a2 * (xx - vertices[2][0])
        new_point = [xx, yy, 0]
        sq_a2_copy = sq_a2.copy()

        txt_a2.add_updater(
            lambda mob: mob.move_to(sq_a2_copy.get_center_of_mass())
        )
        self.add(txt_a2)

        para_a2 = Polygon(
            point, new_point, vertices[2], vertices[3],
            color=BLACK, fill_color=RED, fill_opacity=0.75
        )
        self.play(
            Transform(sq_a2_copy, para_a2)
        )

        # Parallelogram sqaure a2 on top
        point = [vertices[3][0], vertices[3][0] * a1 + b, 0]
        new_point = [vertices[2][0], vertices[2][0] * a1 + b, 0]
        para_a22 = Polygon(
            point, new_point, vertices[2], vertices[3],
            color=BLACK, fill_color=RED, fill_opacity=0.75
        )
        self.play(
            Transform(sq_a2_copy, para_a22)
        )

        # Get parallelogram from square b2
        a1 = line_b.get_slope()
        vertices = sq_b2.get_vertices()
        b = vertices[0][1] - a1 * vertices[0][0]
        point = [4, 4 * a1 + b, 0]
        a2 = (point[1] - vertices[1][1]) / (point[0] - vertices[1][0])
        xx = (a1 * point[0] - a2 * vertices[2][0] - point[1] + vertices[2][1]) / (a1 - a2)
        yy = vertices[2][1] + a2 * (xx - vertices[2][0])
        new_point = [xx, yy, 0]
        sq_b2_copy = sq_b2.copy()

        txt_b2.add_updater(
            lambda mob: mob.move_to(sq_b2_copy.get_center_of_mass())
        )
        self.add(txt_b2)

        para_b2 = Polygon(
            point, vertices[1], vertices[2], new_point,
            color=BLACK, fill_color=RED, fill_opacity=0.75
        )
        self.play(
           Transform(sq_b2_copy, para_b2)
        )

        # Parallelogram square a2 on top
        point = [vertices[1][0], vertices[1][0] * a1 + b, 0]
        new_point = [vertices[2][0], vertices[2][0] * a1 + b, 0]
        para_b22 = Polygon(
            point, vertices[1], vertices[2], new_point,
            color=BLACK, fill_color=RED, fill_opacity=0.75
        )
        self.play(
            Transform(sq_b2_copy, para_b22)
        )

        self.play(
            self.camera.frame.animate.move_to(points[0]).set(height=16)
        )

        new_poly_up = Polygon(
            para_a22.get_vertices()[0],
            para_a22.get_vertices()[1],
            triangle_b.get_vertices()[2],
            triangle_b.get_vertices()[1],
            triangle_b.get_vertices()[0],
            para_b22.get_vertices()[3],
            color=BLACK, fill_color=RED, fill_opacity=0.75
        )

        new_poly_down = Polygon(
            triangle_b.get_vertices()[1],
            triangle_b.get_vertices()[2],
            sq_c2.get_vertices()[2],
            [triangle_b.get_vertices()[1][0], triangle_b.get_vertices()[1][1] - 5, 0],
            sq_c2.get_vertices()[3],
            sq_c2.get_vertices()[0],
            color=BLACK, fill_color=RED, fill_opacity=0.75
        )
        txt_ab  = Tex(r"$a^2 + b^2$", font_size=72, color=BLACK)\
            .move_to(new_poly_down.get_center_of_mass())
        txt_ab.z_index = 1
        self.remove(sq_a2_copy, txt_a2, sq_b2_copy, txt_b2)
        self.play(
            Transform(new_poly_up, new_poly_down),
            Write(txt_ab)
        )

        self.wait(1)

        triangle_b_copy = triangle_b.copy().set_color(RED).set_opacity(0.75)
        vertices = triangle_b_copy.get_vertices()
        new_triangle = Polygon(
            [vertices[0][0], vertices[0][1] - 5, 0],
            [vertices[1][0], vertices[1][1] - 5, 0],
            [vertices[2][0], vertices[2][1] - 5, 0],
            color=BLACK, fill_color=RED, fill_opacity=0.75
        )
        new_poly_down2 = Polygon(
            triangle_b.get_vertices()[2],
            sq_c2.get_vertices()[2],
            [triangle_b.get_vertices()[1][0], triangle_b.get_vertices()[1][1] - 5, 0],
            sq_c2.get_vertices()[3],
            sq_c2.get_vertices()[0],
            color=BLACK, fill_color=RED, fill_opacity=0.75
        )
        self.remove(new_poly_up)
        self.add(new_poly_down2)
        self.play(
            Transform(triangle_b_copy, new_triangle)
        )

        sq_c2_copy = sq_c2.copy()
        self.play(
            sq_c2_copy.animate.set_color(RED).set_opacity(0.75)
        )
        self.remove(new_poly_down2, triangle_b_copy)

        rect = RoundedRectangle(
            height=2.0, width=6.0,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, 5, 0])
        txt = Tex(
            r"$c^2$", r"$~=~$", r"$a^2 + b^2$",
            font_size=96, color=BLACK
        ).move_to([0, 5, 0])

        rect.z_index = 0
        txt.z_index = 1
        self.play(
            Create(rect),
            run_time=0.5
        )
        self.play(
            TransformFromCopy(txt_c2[0], txt[0]),
            Write(txt[1]),
            TransformFromCopy(txt_ab[0], txt[2])
        )

        self.wait(1)
