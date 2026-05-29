"""
Visual proof of the Pythagorean theorem.
Proofs without Words I. Roger B. Nelsen. p. 5.
"""
import numpy as np

from manim import MovingCameraScene, Mobject
from manim import Square, Polygon, Line, RoundedRectangle
from manim import Create, Rotate, Transform, Uncreate, Write
from manim import TransformFromCopy
from manim import FadeTransform, FadeIn, FadeOut
from manim import VGroup, FunctionGraph
from manim import Text, Tex

from manim import config

from manim import LEFT, RIGHT, UP, DOWN, PI, DEGREES, LIGHT

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

        txt_copy = Text(
            r"@chill.maths", font_size=12,
            font="CMU Typewriter Text", weight=LIGHT, color=BLACK
        ).to_edge(RIGHT + DOWN, buff=0.1)
        self.add(txt_copy)

        # Introduction text
        txt_title = [
            Tex(r"Théorème de", font_size=48, color=BLACK),
            Tex(r"Pythagore", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt_dem = Tex(r"Démonstration III", font_size=48, color=BLACK)\
            .next_to(txt_title, DOWN, buff=0.7)
        txt_desc = [
            Tex(r"basée sur une preuve d'Euclide", font_size=28, color=BLACK),
            Tex(r"(vers 300 av. J.C.)", font_size=28, color=BLACK)
        ]
        txt_desc = VGroup(*txt_desc).arrange(DOWN).next_to(txt_dem, DOWN, buff=0.5)

        self.add(
            txt_title, txt_dem, txt_desc
        )
        self.wait(1)
        self.play(Uncreate(txt_title), Uncreate(txt_dem), Uncreate(txt_desc))
        self.wait(1)


        # First triangle and text
        triangle_b = Polygon(
            [-1, -0.75, 0], [1, -0.75, 0], [1, 0.75, 0],
            stroke_width=2,
            color=BLACK, fill_color=BLUE, fill_opacity=1
        )
        txt_a = Tex(r"$a$", font_size=36, color=BLACK)\
            .next_to(triangle_b, DOWN)
        txt_b = Tex(r"$b$", font_size=36, color=BLACK)\
            .next_to(triangle_b, RIGHT)
        txt_c = Tex(r"$c$", font_size=36, color=BLACK)\
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

        self.play(
            triangle_b.animate.scale(0.8)
        )

        # Expand the squares
        coords_vertices_b = get_vertices(triangle_b)

        sq_a2 = Square(side_length=1.5 * 0.8, stroke_color=BLACK, stroke_width=2)\
            .rotate(PI / 2 - np.arcsin(0.6))\
            .move_to(coords_vertices_b[1], DOWN + RIGHT)
        txt_a2  = Tex(r"$a^2$", font_size=52, color=BLACK)\
            .move_to(sq_a2.get_center_of_mass())
        txt_a2.z_index = 1
        self.play(
            FadeTransform(coords_vertices_b[1].set_color(WHITE), sq_a2, stretch=True),
            Write(txt_a2),
            run_time=1.5
        )


        sq_b2 = Square(side_length=2 * 0.8, stroke_color=BLACK, stroke_width=2)\
            .rotate(np.arcsin(0.8))\
            .move_to(coords_vertices_b[0], DOWN + LEFT)
        txt_b2  = Tex(r"$b^2$", font_size=52, color=BLACK)\
            .move_to(sq_b2.get_center_of_mass())
        txt_b2.z_index = 1
        self.play(
            FadeTransform(coords_vertices_b[0].set_color(WHITE), sq_b2, stretch=True),
            Write(txt_b2),
            run_time=1.5
        )

        sq_c2 = Square(side_length=2.5 * 0.8, stroke_color=BLACK, stroke_width=2)\
            .move_to(coords_vertices_b[2], UP)
        txt_c2  = Tex(r"$c^2$", font_size=52, color=BLACK)\
            .move_to(sq_c2.get_center_of_mass())
        self.play(
            FadeTransform(coords_vertices_b[2].set_color(WHITE), sq_c2, stretch=True),
            Write(txt_c2),
            run_time=1.5
        )

        # Expand lines
        coords_vertices_a2 = get_vertices(sq_a2)
        line_a = coords_vertices_a2[0].copy()
        self.play(
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
        point = [-2, -2 * a1 + b, 0]
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
            point, new_point, vertices[2], vertices[3], stroke_width=2,
            color=BLACK, fill_color=RED, fill_opacity=0.75
        )
        self.play(
            Transform(sq_a2_copy, para_a2)
        )

        # Parallelogram square a2 on top
        point = [vertices[3][0], vertices[3][0] * a1 + b, 0]
        new_point = [vertices[2][0], vertices[2][0] * a1 + b, 0]
        para_a22 = Polygon(
            point, new_point, vertices[2], vertices[3], stroke_width=2,
            color=BLACK, fill_color=RED, fill_opacity=0.75
        )
        self.play(
            Transform(sq_a2_copy, para_a22)
        )

        # Get parallelogram from square b2
        a1 = line_b.get_slope()
        vertices = sq_b2.get_vertices()
        b = vertices[0][1] - a1 * vertices[0][0]
        point = [2, 2 * a1 + b, 0]
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
            point, vertices[1], vertices[2], new_point, stroke_width=2,
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
            stroke_width=2, 
            color=BLACK, fill_color=RED, fill_opacity=0.75
        )
        self.play(
            Transform(sq_b2_copy, para_b22)
        )

        group = VGroup(
            triangle_b, sq_a2, sq_b2, sq_c2, line_a, line_b,
            sq_a2_copy, sq_b2_copy,
            para_a22.set_opacity(0), para_b22.set_opacity(0),
            txt_c2.scale(0.8)
        )
        self.play(
            group.animate.scale(1.25)
        )

        group.remove(para_a22, para_b22)

        new_poly_up = Polygon(
            para_a22.get_vertices()[0],
            para_a22.get_vertices()[1],
            triangle_b.get_vertices()[2],
            triangle_b.get_vertices()[1],
            triangle_b.get_vertices()[0],
            para_b22.get_vertices()[3],
            stroke_width=2,
            color=BLACK, fill_color=RED, fill_opacity=0.75
        )

        new_poly_down = Polygon(
            triangle_b.get_vertices()[1],
            triangle_b.get_vertices()[2],
            sq_c2.get_vertices()[2],
            [triangle_b.get_vertices()[1][0], triangle_b.get_vertices()[1][1] - 2.5, 0],
            sq_c2.get_vertices()[3],
            sq_c2.get_vertices()[0],
            stroke_width=2,
            color=BLACK, fill_color=RED, fill_opacity=0.75
        )
        txt_ab  = Tex(r"$a^2 + b^2$", font_size=52, color=BLACK)\
            .move_to(new_poly_up.get_center_of_mass())
        txt_ab2  = Tex(r"$a^2 + b^2$", font_size=52, color=BLACK)\
            .move_to(new_poly_down.get_center_of_mass())
        txt_ab.z_index = 1
        self.play(
            FadeOut(sq_a2_copy),
            FadeOut(sq_b2_copy),
            FadeOut(txt_a2),
            FadeOut(txt_b2),
            FadeIn(new_poly_up),
            FadeIn(txt_ab),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            Transform(new_poly_up, new_poly_down),
            Transform(txt_ab, txt_ab2)
        )

        self.wait(1)

        triangle_b_copy = triangle_b.copy().set_color(RED).set_opacity(0.75)
        vertices = triangle_b_copy.get_vertices()
        new_triangle = Polygon(
            [vertices[0][0], vertices[0][1] - 2.5, 0],
            [vertices[1][0], vertices[1][1] - 2.5, 0],
            [vertices[2][0], vertices[2][1] - 2.5, 0],
            stroke_width=2,
            color=BLACK, fill_color=RED, fill_opacity=0.75
        )
        new_poly_down2 = Polygon(
            triangle_b.get_vertices()[2],
            sq_c2.get_vertices()[2],
            [triangle_b.get_vertices()[1][0], triangle_b.get_vertices()[1][1] - 2.5, 0],
            sq_c2.get_vertices()[3],
            sq_c2.get_vertices()[0],
            stroke_width=2,
            color=BLACK, fill_color=RED, fill_opacity=0.75
        )
        self.remove(new_poly_up)
        self.add(new_poly_down2)
        self.play(
            Transform(triangle_b_copy, new_triangle)
        )

        sq_c2_copy = sq_c2.copy()
        self.play(
            FadeOut(VGroup(new_poly_down2, triangle_b_copy)),
            FadeIn(sq_c2_copy.set_color(RED).set_opacity(0.75))
        )
        self.wait(0.5)

        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, 2, 0])
        txt = Tex(
            r"$c^2$", r"$~=~$", r"$a^2 + b^2$",
            font_size=52, color=BLACK
        ).move_to([0, 2, 0])

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

        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Proofs without words:", font_size=30, color=BLACK),
            Tex(r"Exercises in visual thinking", font_size=30, color=BLACK),
            Tex(r"Roger B. Nelsen (1993), p. 5", font_size=30, color=BLACK)
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
