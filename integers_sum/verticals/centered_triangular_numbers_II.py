"""
Visual proof of Centered Triangular Numbers 2.
Proofs without Words III. Roger B. Nelsen. p. 149.
"""
import numpy as np

from manim import MovingCameraScene, Scene, ManimColor
from manim import Create, Uncreate, Write
from manim import Brace, VGroup, FadeIn, FadeOut, FunctionGraph, Rotate, Line
from manim import Text, Tex, Rectangle, RoundedRectangle, Transform, Dot
from manim import Circle, Polygon, LaggedStart

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



class Tri(MovingCameraScene):
    
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
            Tex(r"Les nombres", font_size=48, color=BLACK),
            Tex(r"triangulaires centrés", font_size=48, color=BLACK),
            Tex(r"Partie II", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])


        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Roger B. Nelsen", font_size=28, color=BLACK),
        ]
        txt = VGroup(*txt).arrange(DOWN)

        self.add(
            txt_title,
            txt,
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt),
            run_time=0.5
        )
        self.wait(0.5)

        # Definition of centered triangular numbers
        definition = [
            Tex(r"Un nombre triangulaire centré $c_n$", font_size=24, color=BLACK),
            Tex(r"compte le nombre de points dans un", font_size=24, color=BLACK),
            Tex(r"tableau ayant un point central et", font_size=24, color=BLACK),
            Tex(r"entouré de points arrangé en $n$", font_size=24, color=BLACK),
            Tex(r"bordures triangulaires.", font_size=24, color=BLACK)
        ]
        definition = VGroup(*definition).\
            arrange(DOWN, aligned_edge=LEFT, buff=0.1).\
            to_edge(UP)
        self.play(
            Write(definition)
        )

        # Show c0 to c4

        # c0
        txt_c0 = Tex(r"$c_0 = 1$", font_size=36, color=BLACK).move_to([0, 1, 0])
        c0 = Dot(point=[0, 0, 0], radius=0.1, color=BLACK).move_to([0, -1, 0])
        self.play(
            Write(txt_c0),
            Create(c0)
        )
        self.wait(0.5)

        # c1
        txt_c1 = Tex(r"$c_1 = 4$", font_size=36, color=BLACK).move_to([0, 1, 0])
        c1 = VGroup(
            Dot([0, 0, 0], radius=0.1, color=BLUE).next_to(c0, UP, buff=.15),
            Dot([0, 0, 0], radius=0.1, color=BLUE).next_to(
                c0, LEFT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=BLUE).next_to(
                c0, RIGHT + 0.5 * DOWN, buff=0.1
            ),
        )
        line_c1 = [
            Line(c1[0].get_center(), c1[1].get_center(), color=BLUE),
            Line(c1[1].get_center(), c1[2].get_center(), color=BLUE),
            Line(c1[0].get_center(), c1[2].get_center(), color=BLUE),
        ]
        self.play(
            Transform(txt_c0, txt_c1),
            Create(c1),
            *[Create(line_c1[i]) for i in range(3)]
        )
        self.wait(0.5)

        # c2
        txt_c2 = Tex(r"$c_2 = 10$", font_size=36, color=BLACK).move_to([0, 1, 0])
        c2 = VGroup(
            Dot([0, 0, 0], radius=0.1, color=VIOLET).next_to(c1[0], UP, buff=.15),
            Dot([0, 0, 0], radius=0.1, color=VIOLET).next_to(
                c1[0], LEFT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=VIOLET).next_to(
                c1[0], RIGHT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=VIOLET).next_to(
                c1[1], LEFT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=VIOLET).next_to(
                c1[2], RIGHT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=VIOLET).next_to(
                c1[1], RIGHT + 0.5 * DOWN, buff=0.1
            ),
        )
        line_c2 = [
            Line(c2[0].get_center(), c2[1].get_center(), color=VIOLET),
            Line(c2[0].get_center(), c2[2].get_center(), color=VIOLET),
            Line(c2[1].get_center(), c2[3].get_center(), color=VIOLET),
            Line(c2[2].get_center(), c2[4].get_center(), color=VIOLET),
            Line(c2[3].get_center(), c2[5].get_center(), color=VIOLET),
            Line(c2[4].get_center(), c2[5].get_center(), color=VIOLET),
        ]
        self.play(
            Transform(txt_c0, txt_c2),
            Create(c2),
            *[Create(line_c2[i]) for i in range(6)]
        )
        self.wait(0.5)

        # c3
        txt_c3 = Tex(r"$c_3 = 19$", font_size=36, color=BLACK).move_to([0, 1, 0])
        c3 = VGroup(
            Dot([0, 0, 0], radius=0.1, color=RED).next_to(c2[0], UP, buff=.15),
            Dot([0, 0, 0], radius=0.1, color=RED).next_to(
                c2[0], LEFT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=RED).next_to(
                c2[0], RIGHT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=RED).next_to(
                c2[1], LEFT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=RED).next_to(
                c2[2], RIGHT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=RED).next_to(
                c2[5], RIGHT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=RED).next_to(
                c2[3], LEFT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=RED).next_to(
                c2[4], RIGHT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=RED).next_to(
                c2[3], RIGHT + 0.5 * DOWN, buff=0.1
            ),
        )
        line_c3 = [
            Line(c3[0].get_center(), c3[1].get_center(), color=RED),
            Line(c3[0].get_center(), c3[2].get_center(), color=RED),
            Line(c3[1].get_center(), c3[3].get_center(), color=RED),
            Line(c3[2].get_center(), c3[4].get_center(), color=RED),
            Line(c3[7].get_center(), c3[5].get_center(), color=RED),
            Line(c3[8].get_center(), c3[5].get_center(), color=RED),
            Line(c3[3].get_center(), c3[6].get_center(), color=RED),
            Line(c3[4].get_center(), c3[7].get_center(), color=RED),
            Line(c3[6].get_center(), c3[8].get_center(), color=RED),
        ]
        self.play(
            Transform(txt_c0, txt_c3),
            Create(c3),
            *[Create(line_c3[i]) for i in range(9)]
        )
        self.wait(0.5)

        # c4
        txt_c4 = Tex(r"$c_4 = 31$", font_size=36, color=BLACK).move_to([0, 1, 0])
        c4 = VGroup(
            Dot([0, 0, 0], radius=0.1, color=BLACK).next_to(c3[0], UP, buff=.15),
            Dot([0, 0, 0], radius=0.1, color=BLACK).next_to(
                c3[0], LEFT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=BLACK).next_to(
                c3[0], RIGHT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=BLACK).next_to(
                c3[1], LEFT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=BLACK).next_to(
                c3[2], RIGHT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=BLACK).next_to(
                c3[5], RIGHT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=BLACK).next_to(
                c3[3], LEFT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=BLACK).next_to(
                c3[4], RIGHT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=BLACK).next_to(
                c3[6], RIGHT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=BLACK).next_to(
                c3[6], LEFT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=BLACK).next_to(
                c3[7], RIGHT + 0.5 * DOWN, buff=0.1
            ),
            Dot([0, 0, 0], radius=0.1, color=BLACK).next_to(
                c3[8], RIGHT + 0.5 * DOWN, buff=0.1
            ),
        )
        line_c4 = [
            Line(c4[0].get_center(), c4[1].get_center(), color=BLACK),
            Line(c4[0].get_center(), c4[2].get_center(), color=BLACK),
            Line(c4[1].get_center(), c4[3].get_center(), color=BLACK),
            Line(c4[2].get_center(), c4[4].get_center(), color=BLACK),
            Line(c4[9].get_center(), c4[5].get_center(), color=BLUE),
            Line(c4[8].get_center(), c4[5].get_center(), color=BLACK),
            Line(c4[3].get_center(), c4[6].get_center(), color=BLACK),
            Line(c4[4].get_center(), c4[7].get_center(), color=BLACK),
            Line(c4[6].get_center(), c4[9].get_center(), color=BLACK),
            Line(c4[9].get_center(), c4[10].get_center(), color=BLACK),
            Line(c4[7].get_center(), c4[10].get_center(), color=BLACK),
        ]   
        self.play(
            Transform(txt_c0, txt_c4),
            Create(c4),
            *[Create(line_c4[i]) for i in range(11)]
        )
        self.wait(0.5)


        # Write results
        results = [
            Tex(
                r"$\forall n \geq 2, c_n = t_{n -1} + t_n + t_{n+1}$",
                font_size=30, color=BLACK
            ),
            Tex(r"avec $t_n = 1 + \dots + n$", font_size=30, color=BLACK),
        ]
        results = VGroup(*results).\
            arrange(DOWN, aligned_edge=LEFT, buff=0.1).\
            move_to([0, 1, 0])
        self.play(
            Write(results),
            Uncreate(txt_c0),
        )

        # Proof
        triangle_1 = Polygon(
            c4[1].get_center(),
            c4[6].get_center(),
            c2[1].get_center(),
            color=ORANGE,
            fill_opacity=0.75
        )
        txt_t1 = Tex(r"$t_{n - 1}$", font_size=36, color=BLACK).\
            move_to(triangle_1.get_center_of_mass())
        triangle_2 = Polygon(
            c0.get_center(),
            c4[9].get_center(),
            c4[10].get_center(),
            color=ORANGE,
            fill_opacity=0.75
        )
        txt_t2 = Tex(r"$t_{n + 1}$", font_size=36, color=BLACK).\
            move_to(triangle_2.get_center_of_mass())
        triangle_3 = Polygon(
            c4[0].get_center(),
            c4[7].get_center(),
            c1[0].get_center(),
            color=ORANGE,
            fill_opacity=0.75
        )
        txt_t3 = Tex(r"$t_n$", font_size=36, color=BLACK).\
            move_to(triangle_3.get_center_of_mass())
        self.play(
            Create(triangle_1),
            Write(txt_t1),
            Create(triangle_2),
            Write(txt_t2),
            Create(triangle_3),
            Write(txt_t3)
        )


        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Proofs without words III,", font_size=30, color=BLACK),
            Tex(r"Roger B. Nelsen (2015)", font_size=30, color=BLACK),
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