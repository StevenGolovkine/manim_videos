"""
Visual proof of the Geometric Series VI
Proofs without Words III. Roger B. Nelsen. p. 154.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, TransformFromCopy
from manim import VGroup, FadeIn, FadeOut, FunctionGraph, RoundedRectangle
from manim import RegularPolygon, Line
from manim import Text, Tex

from manim import config
from manim import LEFT, RIGHT, DOWN, LIGHT, UP

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
            Tex(r"Séries géométriques", font_size=48, color=BLACK),
            Tex(r"$\frac{1}{9} + \frac{1}{9^2} + \frac{1}{9^3} + \cdots = \frac{1}{8}$", font_size=24, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"James Tanton", font_size=28, color=BLACK)
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

        # Create octogones
        base_radius = 2
        octo = RegularPolygon(
            n=8,
            radius=base_radius,
            stroke_width=2,
            stroke_color=BLACK,
        )
        line = Line(
            octo.get_vertices()[2],
            octo.get_vertices()[3],
            stroke_color = BLUE
        )
        txt_1 = Tex(
            r"$1$", font_size=32, color=BLACK
        ).next_to(line.get_center(), UP + LEFT, buff=0.2)
        self.play(
            Create(octo),
            run_time=0.5
        )
        self.play(
            Create(line),
            Write(txt_1)
        )

        group = VGroup(octo, line, txt_1)

        octo_2 = RegularPolygon(
            n=8,
            radius=base_radius / 3,
            stroke_width=2,
            stroke_color=BLACK,
        )
        line_2 = Line(
            octo_2.get_vertices()[2],
            octo_2.get_vertices()[3],
            stroke_color = BLUE
        )
        txt_2 = Tex(
            r"$1 / 3$", font_size=24, color=BLACK
        ).next_to(line_2.get_center(), UP, buff=0.05)
        self.play(
            Create(octo_2),
        )
        self.play(
            Create(line_2),
            Write(txt_2)
        )

        # Lines
        lines = [
            Line(
                octo.get_vertices()[i],
                octo_2.get_vertices()[i],
                stroke_color=BLACK,
                stroke_width=1
            ) for i in range(8)
        ]
        self.play(
            *[Create(line) for line in lines]
        )

        # Text area
        txt_area = [
            Tex(r"$1/ 9$", font_size=16, color=BLACK).\
                move_to(lines[0].get_center() + [0, 0.5, 0]),
            Tex(r"$1/ 9$", font_size=16, color=BLACK).\
                move_to(lines[1].get_center() + [-0.4, 0.25, 0]),
            Tex(r"$1/ 9$", font_size=16, color=BLACK).\
                move_to(lines[2].get_center() + [-0.5, 0, 0]),
            Tex(r"$1/ 9$", font_size=16, color=BLACK).\
                move_to(lines[3].get_center() + [-0.25, -0.5, 0]),
            Tex(r"$1/ 9$", font_size=16, color=BLACK).\
                move_to(lines[4].get_center() + [0, -0.5, 0]),
            Tex(r"$1/ 9$", font_size=16, color=BLACK).\
                move_to(lines[5].get_center() + [0.34, -0.25, 0]),
            Tex(r"$1/ 9$", font_size=16, color=BLACK).\
                move_to(lines[6].get_center() + [0.5, 0, 0]),
            Tex(r"$1/ 9$", font_size=16, color=BLACK).\
                move_to(lines[7].get_center() + [0.25, 0.4, 0]),    
            Tex(r"$1/ 9$", font_size=16, color=BLACK).\
                move_to(octo_2.get_center_of_mass())
        ]
        self.play(
            *[Write(txt) for txt in txt_area]
        )

        self.wait(1)

        group_2 = VGroup(octo_2, line_2, txt_2, txt_area[2], lines[2:4])
        vgroup = VGroup(group, group_2)


        # Zoom in
        
        self.play(
            *[FadeOut(txt) for txt in txt_area[:2]],
            *[FadeOut(txt) for txt in txt_area[3:]],
            *[FadeOut(line)for line in lines[:2]],
            *[FadeOut(line)for line in lines[4:]],
            vgroup.animate.scale(3)
        )

        octo_3 = RegularPolygon(
            n=8,
            radius=base_radius / 9,
            stroke_width=2,
            stroke_color=BLACK,
        )
        line_3 = Line(
            octo_3.get_vertices()[2],
            octo_3.get_vertices()[3],
            stroke_color = BLUE
        )
        txt_3 = Tex(
            r"$1 / 9$", font_size=24, color=BLACK
        ).next_to(line_3.get_center(), UP, buff=0.05)
        self.play(
            Create(octo_3),
        )
        self.play(
            Create(line_3),
            Write(txt_3)
        )

        # Lines
        lines_2 = [
            Line(
                octo_2.get_vertices()[i],
                octo_3.get_vertices()[i],
                stroke_color=BLACK,
                stroke_width=1
            ) for i in range(8)
        ]
        self.play(
            *[Create(line) for line in lines_2]
        )

        # Text area
        txt_area_2 = [
            Tex(r"$1/ 9^2$", font_size=16, color=BLACK).\
                move_to(lines_2[0].get_center() + [0, 0.5, 0]),
            Tex(r"$1/ 9^2$", font_size=16, color=BLACK).\
                move_to(lines_2[1].get_center() + [-0.4, 0.25, 0]),
            Tex(r"$1/ 9^2$", font_size=16, color=BLACK).\
                move_to(lines_2[2].get_center() + [-0.5, 0, 0]),
            Tex(r"$1/ 9^2$", font_size=16, color=BLACK).\
                move_to(lines_2[3].get_center() + [-0.25, -0.5, 0]),
            Tex(r"$1/ 9^2$", font_size=16, color=BLACK).\
                move_to(lines_2[4].get_center() + [0, -0.5, 0]),
            Tex(r"$1/ 9^2$", font_size=16, color=BLACK).\
                move_to(lines_2[5].get_center() + [0.34, -0.25, 0]),
            Tex(r"$1/ 9^2$", font_size=16, color=BLACK).\
                move_to(lines_2[6].get_center() + [0.5, 0, 0]),
            Tex(r"$1/ 9^2$", font_size=16, color=BLACK).\
                move_to(lines_2[7].get_center() + [0.25, 0.4, 0]),    
            Tex(r"$1/ 9^2$", font_size=16, color=BLACK).\
                move_to(octo_2.get_center_of_mass() + [0, 0.1, 0])
        ]
        self.play(
            *[Write(txt) for txt in txt_area_2]
        )

        self.wait(1)

        group_3 = VGroup(octo_3, line_3, txt_3, txt_area_2[2], lines_2[2:4])
        vgroup_2 = VGroup(group, group_2, group_3)

        self.play(
            *[FadeOut(txt) for txt in txt_area_2[:2]],
            *[FadeOut(txt) for txt in txt_area_2[3:]],
            *[FadeOut(line)for line in lines_2[:2]],
            *[FadeOut(line)for line in lines_2[4:]],
            vgroup_2.animate.scale(1/3)
        )


        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"College Mathematics Journal, vol. 39,", font_size=26, color=BLACK),
            Tex(r"no. 2(March 2008), p.106.", font_size=26, color=BLACK)
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