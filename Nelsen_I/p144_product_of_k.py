"""
Visual proof of the product of k^k times k! = (n!)^(n + 1)
Proofs without Words I. Roger B. Nelsen. p. 144.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Square, Brace
from manim import Axes, VGroup, FadeIn, FadeOut, FunctionGraph, Line, Polygon
from manim import Text, Tex, Transform
from manim import NumberPlane, always_redraw

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
            Tex(
                r"${\displaystyle \prod_{k = 1}^n k^k k! = n!^{n + 1}}$",
                font_size=48, color=BLACK
            ),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])


        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Edward T. H. Wang", font_size=28, color=BLACK)
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

        # Create the table
        squares = VGroup()
        squares.add(Square(side_length=0.3, color=BLACK, stroke_width=1))
        for idx in range(9):
            new_square = Square(side_length=0.3, color=BLACK, stroke_width=1).\
                next_to(squares[idx], direction=RIGHT, buff=0.05)
            squares.add(new_square)
        for idx in range(80):
            new_square = Square(side_length=0.3, color=BLACK, stroke_width=1).\
                next_to(squares[idx], direction=DOWN, buff=0.05)
            squares.add(new_square)
        squares.move_to([0, 1, 0])
        self.play(
            Create(squares)
        )

        brace = Brace(squares, direction=[0, -1, 0], sharpness=1, color=BLACK)
        txt_2n = Tex(r"$n + 1$", font_size=30, color=BLACK).next_to(brace, 0.5 * DOWN)

        self.play(
            Create(brace),
            Write(txt_2n)
        )

        txt_1 = [
            Tex(r"$1$", font_size=30, color=BLACK).\
                move_to(squares[0].get_center())
        ]
        for i in range(1, 10):
            if i in [1, 2, 3, 8, 9]:
                txt_1.append(Tex(r"$1$", font_size=30, color=BLACK).\
                    move_to(squares[i].get_center()))
            else:
                txt_1.append(Tex(r"$\cdot$", font_size=30, color=BLACK).\
                    move_to(squares[i].get_center()))
        
        txt_1 = VGroup(*txt_1)
        self.play(Write(txt_1))

        txt_2 = [
            Tex(r"$2$", font_size=30, color=BLACK).\
                move_to(squares[10].get_center())
        ]
        for i in range(11, 20):
            if i in [11, 12, 13, 18, 19]:
                txt_2.append(Tex(r"$2$", font_size=30, color=BLACK).\
                    move_to(squares[i].get_center()))
            else:
                txt_2.append(Tex(r"$\cdot$", font_size=30, color=BLACK).\
                    move_to(squares[i].get_center()))
        
        txt_2 = VGroup(*txt_2)
        self.play(Write(txt_2))


        txt_3 = [
            Tex(r"$3$", font_size=30, color=BLACK).\
                move_to(squares[20].get_center())
        ]
        for i in range(21, 30):
            if i in [21, 22, 23, 28, 29]:
                txt_3.append(Tex(r"$3$", font_size=30, color=BLACK).\
                    move_to(squares[i].get_center()))
            else:
                txt_3.append(Tex(r"$\cdot$", font_size=30, color=BLACK).\
                    move_to(squares[i].get_center()))
        
        txt_3 = VGroup(*txt_3)
        self.play(Write(txt_3))


        txt_n2 = [
            Tex(r"$n-2$", font_size=12, color=BLACK).\
                move_to(squares[60].get_center())
        ]
        for i in range(61, 70):
            if i in [61, 62, 63, 68, 69]:
                txt_n2.append(Tex(r"$n-2$", font_size=12, color=BLACK).\
                    move_to(squares[i].get_center()))
            else:
                txt_n2.append(Tex(r"$\cdot$", font_size=30, color=BLACK).\
                    move_to(squares[i].get_center()))
        
        txt_n2 = VGroup(*txt_n2)
        self.play(Write(txt_n2))

        txt_n1 = [
            Tex(r"$n-1$", font_size=12, color=BLACK).\
                move_to(squares[70].get_center())
        ]
        for i in range(71, 80):
            if i in [71, 72, 73, 78, 79]:
                txt_n1.append(Tex(r"$n-1$", font_size=12, color=BLACK).\
                    move_to(squares[i].get_center()))
            else:
                txt_n1.append(Tex(r"$\cdot$", font_size=30, color=BLACK).\
                    move_to(squares[i].get_center()))
        
        txt_n1 = VGroup(*txt_n1)
        self.play(Write(txt_n1))

        txt_n = [
            Tex(r"$n$", font_size=30, color=BLACK).\
                move_to(squares[80].get_center())
        ]
        for i in range(81, 90):
            if i in [81, 82, 83, 88, 89]:
                txt_n.append(Tex(r"$n$", font_size=30, color=BLACK).\
                    move_to(squares[i].get_center()))
            else:
                txt_n.append(Tex(r"$\cdot$", font_size=30, color=BLACK).\
                    move_to(squares[i].get_center()))
        
        txt_n = VGroup(*txt_n)
        self.play(Write(txt_n))

        txt_nfac_list = []
        for i in range(0, 10):
            txt_nfac_ = Tex(r"$n!$", font_size=30, color=BLACK)
            txt_arrow = Tex(r"$\downarrow$", font_size=30, color=BLACK).\
                next_to(txt_nfac_, DOWN, buff=0.1)
            txt_nfac = VGroup(txt_nfac_, txt_arrow).next_to(squares[i], UP, buff=0.25)
            txt_nfac_list.append(txt_nfac)
        txt_nfac_group = VGroup(*txt_nfac_list)
        self.play(Write(txt_nfac_group))

        # Color the blocks
        self.play(
            squares[0].animate.set_fill(BLUE, opacity=0.5),
            squares[1].animate.set_fill(BLUE, opacity=0.5),
        )
        self.play(
            squares[2].animate.set_fill(RED, opacity=0.5),
            squares[10].animate.set_fill(RED, opacity=0.5),
            squares[11].animate.set_fill(RED, opacity=0.5),
            squares[12].animate.set_fill(RED, opacity=0.5),
        )
        self.play(
            squares[3].animate.set_fill(BLUE, opacity=0.5),
            squares[13].animate.set_fill(BLUE, opacity=0.5),
            squares[20].animate.set_fill(BLUE, opacity=0.5),
            squares[21].animate.set_fill(BLUE, opacity=0.5),
            squares[22].animate.set_fill(BLUE, opacity=0.5),
            squares[23].animate.set_fill(BLUE, opacity=0.5),
        )
        self.play(
            squares[4].animate.set_fill(RED, opacity=0.5),
            squares[14].animate.set_fill(RED, opacity=0.5),
            squares[24].animate.set_fill(RED, opacity=0.5),
            squares[30].animate.set_fill(RED, opacity=0.5),
            squares[31].animate.set_fill(RED, opacity=0.5),
            squares[32].animate.set_fill(RED, opacity=0.5),
            squares[33].animate.set_fill(RED, opacity=0.5),
            squares[34].animate.set_fill(RED, opacity=0.5),
        )
        self.play(
            squares[5].animate.set_fill(BLUE, opacity=0.5),
            squares[15].animate.set_fill(BLUE, opacity=0.5),
            squares[25].animate.set_fill(BLUE, opacity=0.5),
            squares[35].animate.set_fill(BLUE, opacity=0.5),
            squares[40].animate.set_fill(BLUE, opacity=0.5),
            squares[41].animate.set_fill(BLUE, opacity=0.5),
            squares[42].animate.set_fill(BLUE, opacity=0.5),
            squares[43].animate.set_fill(BLUE, opacity=0.5),
            squares[44].animate.set_fill(BLUE, opacity=0.5),
            squares[45].animate.set_fill(BLUE, opacity=0.5),
        )
        self.play(
            squares[6].animate.set_fill(RED, opacity=0.5),
            squares[16].animate.set_fill(RED, opacity=0.5),
            squares[26].animate.set_fill(RED, opacity=0.5),
            squares[36].animate.set_fill(RED, opacity=0.5),
            squares[46].animate.set_fill(RED, opacity=0.5),
            squares[50].animate.set_fill(RED, opacity=0.5),
            squares[51].animate.set_fill(RED, opacity=0.5),
            squares[52].animate.set_fill(RED, opacity=0.5),
            squares[53].animate.set_fill(RED, opacity=0.5),
            squares[54].animate.set_fill(RED, opacity=0.5),
            squares[55].animate.set_fill(RED, opacity=0.5),
            squares[56].animate.set_fill(RED, opacity=0.5),
        )
        self.play(
            squares[7].animate.set_fill(BLUE, opacity=0.5),
            squares[17].animate.set_fill(BLUE, opacity=0.5),
            squares[27].animate.set_fill(BLUE, opacity=0.5),
            squares[37].animate.set_fill(BLUE, opacity=0.5),
            squares[47].animate.set_fill(BLUE, opacity=0.5),
            squares[57].animate.set_fill(BLUE, opacity=0.5),
            squares[60].animate.set_fill(BLUE, opacity=0.5),
            squares[61].animate.set_fill(BLUE, opacity=0.5),
            squares[62].animate.set_fill(BLUE, opacity=0.5),
            squares[63].animate.set_fill(BLUE, opacity=0.5),
            squares[64].animate.set_fill(BLUE, opacity=0.5),
            squares[65].animate.set_fill(BLUE, opacity=0.5),
            squares[66].animate.set_fill(BLUE, opacity=0.5),
            squares[67].animate.set_fill(BLUE, opacity=0.5),
        )
        self.play(
            squares[8].animate.set_fill(RED, opacity=0.5),
            squares[18].animate.set_fill(RED, opacity=0.5),
            squares[28].animate.set_fill(RED, opacity=0.5),
            squares[38].animate.set_fill(RED, opacity=0.5),
            squares[48].animate.set_fill(RED, opacity=0.5),
            squares[58].animate.set_fill(RED, opacity=0.5),
            squares[68].animate.set_fill(RED, opacity=0.5),
            squares[70].animate.set_fill(RED, opacity=0.5),
            squares[71].animate.set_fill(RED, opacity=0.5),
            squares[72].animate.set_fill(RED, opacity=0.5),
            squares[73].animate.set_fill(RED, opacity=0.5),
            squares[74].animate.set_fill(RED, opacity=0.5),
            squares[75].animate.set_fill(RED, opacity=0.5),
            squares[76].animate.set_fill(RED, opacity=0.5),
            squares[77].animate.set_fill(RED, opacity=0.5),
            squares[78].animate.set_fill(RED, opacity=0.5),
        )
        self.play(
            squares[9].animate.set_fill(BLUE, opacity=0.5),
            squares[19].animate.set_fill(BLUE, opacity=0.5),
            squares[29].animate.set_fill(BLUE, opacity=0.5),
            squares[39].animate.set_fill(BLUE, opacity=0.5),
            squares[49].animate.set_fill(BLUE, opacity=0.5),
            squares[59].animate.set_fill(BLUE, opacity=0.5),
            squares[69].animate.set_fill(BLUE, opacity=0.5),
            squares[79].animate.set_fill(BLUE, opacity=0.5),
            squares[80].animate.set_fill(BLUE, opacity=0.5),
            squares[81].animate.set_fill(BLUE, opacity=0.5),
            squares[82].animate.set_fill(BLUE, opacity=0.5),
            squares[83].animate.set_fill(BLUE, opacity=0.5),
            squares[84].animate.set_fill(BLUE, opacity=0.5),
            squares[85].animate.set_fill(BLUE, opacity=0.5),
            squares[86].animate.set_fill(BLUE, opacity=0.5),
            squares[87].animate.set_fill(BLUE, opacity=0.5),
            squares[88].animate.set_fill(BLUE, opacity=0.5),
            squares[89].animate.set_fill(BLUE, opacity=0.5),
        )

        # Final writing
        txt = Tex(
            r"${\displaystyle \prod_{k = 1}^n k^k k! = n!^{n + 1}}$",
            font_size=40, color=BLACK
        ).move_to([0, -2.5, 0])
        self.play(Write(txt))


        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Collega Mathematics Journal,", font_size=26, color=BLACK),
            Tex(r"vol. 20, no. 2 (March 1989), p.152", font_size=26, color=BLACK),
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