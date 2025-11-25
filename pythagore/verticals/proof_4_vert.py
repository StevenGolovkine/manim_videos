"""
Visual proof of the Pythagorean theorem.
Proofs without Words III. Roger B. Nelsen. p. 4.
"""
import numpy as np

from manim import MovingCameraScene, Mobject
from manim import Square, Polygon, Line, RoundedRectangle
from manim import Create, Rotate, Transform, Uncreate, Write
from manim import TransformFromCopy, DashedVMobject
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

        txt_dem = Tex(r"Démonstration IV", font_size=48, color=BLACK)\
            .next_to(txt_title, DOWN, buff=0.7)
        txt_desc = [
            Tex(r"Roger B. Nelsen", font_size=28, color=BLACK),
        ]
        txt_desc = VGroup(*txt_desc).arrange(DOWN).next_to(txt_dem, DOWN, buff=0.5)

        self.add(
            txt_title, txt_dem, txt_desc
        )
        self.wait(1)
        self.play(Uncreate(txt_title), Uncreate(txt_dem), Uncreate(txt_desc))
        self.wait(1)

        # Create a sqaure triangle with squares on each side
        triangle = Polygon(
            [-0.5, 1, 0],
            [-0.5, 2, 0],
            [0.5, 1, 0],
            color=BLACK,
            fill_opacity=1,
            fill_color=WHITE,
            stroke_width=2
        )
        square_a = Square(
            side_length=1,
            color=BLACK,
            fill_opacity=1,
            fill_color=BLUE,
            stroke_width=2
        ).next_to(triangle, DOWN, buff=0)
        txt_a = Tex(r"$a^2$", font_size=24, color=BLACK).move_to(square_a.get_center())
        square_b = Square(
            side_length=1,
            color=BLACK,
            fill_opacity=1,
            fill_color=RED,
            stroke_width=2,
        ).next_to(triangle, LEFT, buff=0)
        txt_b = Tex(r"$b^2$", font_size=24, color=BLACK).move_to(square_b.get_center())
        square_c = Square(
            side_length=np.sqrt(2),
            color=BLACK,
            fill_opacity=1,
            fill_color=GREEN,
            stroke_width=2,
        ).rotate(-PI / 4).next_to(triangle.get_center(), UP + RIGHT, buff=-0.5)
        txt_c = Tex(r"$c^2$", font_size=24, color=BLACK).move_to(square_c.get_center())
        self.play(
            Create(triangle),
            Create(square_a),
            Create(square_b),
            Create(square_c),
            Write(txt_a),
            Write(txt_b),  
            Write(txt_c),
            run_time=2
        )

        # Create big square around
        big_square = Polygon(
            [-1.5, 0, 0],
            [-1.5, 3, 0],
            [1.5, 3, 0],
            [1.5, 0, 0],
            color=BLACK,
            fill_opacity=0,
            stroke_width=2,
        )
        line_a = Line(
            [-0.5, 0, 0],
            [-0.5, 3, 0],
            color=BLACK, stroke_width=2
        )
        line_b = Line(
            [1.5, 1, 0],
            [-1.5, 1, 0],
            color=BLACK, stroke_width=2
        )
        self.play(
            Create(big_square),
            Create(line_a),
            Create(line_b),
            run_time=2
        )

        # Cut the big square into four triangles and the two squares
        line_dashed = DashedVMobject(Line(
            [-1.5, 3, 0],
            [1.5, 0, 0],
            color=BLACK, stroke_width=2,
        ))
        self.play(Create(line_dashed), run_time=1)

        
        # Get lower part of the square
        square_a_lower = square_a.copy().\
            set_fill(WHITE).\
            next_to(square_a, LEFT, buff=0)
        triangle_lower = triangle.copy().\
            next_to(square_b, UP, buff=0)
        triangle_lower_2 = triangle.copy().\
            next_to(square_a, RIGHT, buff=0)
        lower_part = VGroup(
            square_a.copy(),
            square_b.copy(),
            triangle.copy(),
            square_a_lower,
            triangle_lower,
            triangle_lower_2
        )
        self.play(
            lower_part.animate.move_to([0, -2, 0])
        )

        # Get upper part of the square
        triangle_upper = triangle.copy().\
            rotate(-PI / 2).\
            next_to(square_c.get_center(), LEFT + UP, buff=0)
        triangle_upper_2 = triangle.copy().\
            rotate(PI).\
            next_to(square_c.get_center(), RIGHT + UP, buff=0)
        triangle_upper_3 = triangle.copy().\
            rotate(PI / 2).\
            next_to(square_c.get_center(), RIGHT + DOWN, buff=0)
        triangle_upper_4 = triangle.copy().\
            rotate(PI).\
            next_to(triangle_upper, LEFT, buff=0)
        triangle_upper_5 = triangle.copy().\
            rotate(PI).\
            next_to(triangle_upper_3, DOWN, buff=0)
        upper_part = VGroup(
            square_c.copy(),
            triangle_upper,
            triangle_upper_2,
            triangle_upper_3,
            triangle_upper_4,
            triangle_upper_5
        ).set_opacity(0.5)
        self.play(
            upper_part.animate.rotate(-PI).move_to([0, -2, 0]),
        )
        
        # Finish
        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, 0, 0])
        txt = Tex(
            r"$c^2$", r"$~=~$", r"$a^2 + b^2$",
            font_size=52, color=BLACK
        ).move_to([0, 0, 0])

        self.play(
            Create(rect),
            Write(txt),
        )

        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Proofs without words:", font_size=30, color=BLACK),
            Tex(r"Further Exercises", font_size=30, color=BLACK),
            Tex(r"in visual thinking", font_size=30, color=BLACK),
            Tex(r"Roger B. Nelsen (2015), p. 4", font_size=30, color=BLACK)
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
