"""
Visual proof of the sums of odd integers.
Proofs without Words II. Roger B. Nelsen. p. 27.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Dot, ArcBetweenPoints, RoundedRectangle, Line, ArcPolygonFromArcs
from manim import Create, Uncreate, Write
from manim import VGroup, TransformFromCopy
from manim import Tex

from manim import config

from manim import LEFT, RIGHT, DOWN, PI

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


class Pizza(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame.save_state()

        txt_copy = Tex(r"@Math\&Moi", font_size=12, color=BLACK)\
            .to_edge(RIGHT + DOWN, buff=0.1)
        self.add(txt_copy)

        # Introduction text
        txt_title = [
            Tex(r"Comment couper", font_size=48, color=BLACK),
            Tex(r"une pizza en huit ?", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Carter and Wagon (1994)", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        self.play(
            Write(txt_title),
            Write(txt)
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt)
        )
        self.wait(1)

        # Theorem
        txt_theorem = [
            Tex(r"Si une pizza est coupée en huit", font_size=28, color=BLACK),
            Tex(r"en faisant des coupes à $45^{\circ}$", font_size=28, color=BLACK),
            Tex(r"à partir d'un point quelconque", font_size=28, color=BLACK),
            Tex(r"de la pizza, alors les sommes", font_size=28, color=BLACK),
            Tex(r"des aires des parts alternées", font_size=28, color=BLACK),
            Tex(r"sont égales.", font_size=28, color=BLACK)
        ]
        txt_theorem = VGroup(*txt_theorem)\
            .arrange(DOWN, aligned_edge=LEFT, center=False, buff=0.1)\
                .move_to([0, 2.5, 0])

        self.play(Write(txt_theorem))


        # Pizza
        circle = Dot(
            [0, -1, 0], radius=2,
            color=WHITE, stroke_color=BLACK, stroke_width=2
        )
        self.play(
            Create(circle)
        )

        # Different point on the circle
        theta_1 = PI / 9
        theta_2 = PI / 3
        point_A = Dot([2 * np.cos(theta_1), 2 * np.sin(theta_1), 0], color=BLUE)
        point_B = Dot([2 * np.cos(theta_2), 2 * np.sin(theta_2), 0], color=RED)
        point_D = Dot([2 * np.cos(PI - theta_1), 2 * np.sin(theta_1), 0], color=VIOLET)
        point_E = Dot([2 * np.cos(theta_2), 2 * np.sin(-theta_2), 0], color=YELLOW)
        self.add(point_A, point_E, point_B, point_D)

        point_C = Dot([2 * np.cos(theta_2), 2 * np.sin(theta_1), 0], color=BLACK)
        point_C2 = Dot([2 * np.cos(theta_2), -2 * np.sin(theta_1), 0], color=BLACK)
        point_C3 = Dot([-2 * np.cos(theta_2), 2 * np.sin(theta_1), 0], color=BLACK)
        point_C4 = Dot([2 * np.cos(theta_2) - 4 * np.sin(theta_1), 2 * np.sin(theta_1), 0], color=BLACK)
        point_C5 = Dot([4 * np.sin(theta_1) - 2 * np.cos(theta_2), 2 * np.sin(theta_1), 0], color=BLACK)
        self.add(point_C, point_C2, point_C3, point_C4, point_C5)

        b = np.sin(theta_1) - np.cos(theta_2)
        x = (- 2 * b + 2 * np.sqrt(2 - b**2)) / 2
        y = (2 * b + 2 * np.sqrt(2 - b**2)) / 2
        point_F = Dot([x, y, 0], color=RED)
        point_F2 = Dot([x, -y, 0], color=BLUE)
        point_F3 = Dot([-x, y, 0], color=BLUE)
        self.add(point_F, point_F2, point_F3)

        x = (- 2 * b - 2 * np.sqrt(2 - b**2)) / 2
        y = (2 * b - 2 * np.sqrt(2 - b**2)) / 2
        point_G = Dot([x, y, 0], color=RED)
        self.add(point_G)


        b = np.sin(theta_1) + np.cos(theta_2)
        x = (2 * b + 2 * np.sqrt(2 - b**2)) / 2
        y = (2 * b - 2 * np.sqrt(2 - b**2)) / 2
        point_I = Dot([x, y, 0], color=ORANGE)
        point_I2 = Dot([-x, y, 0], color=ORANGE)
        self.add(point_I, point_I2)

        x = (2 * b - 2 * np.sqrt(2 - b**2)) / 2
        y = (2 * b + 2 * np.sqrt(2 - b**2)) / 2
        point_H = Dot([x, y, 0], color=RED)
        point_H2 = Dot([x, -y, 0], color=RED)
        self.add(point_H, point_H2)
        
        point_J = Dot([-2 * np.sin(theta_1), 4 * np.sin(theta_1) - 2 * np.cos(theta_2), 0], color=BLUE)
        point_J2 = Dot([-2 * np.sin(theta_1), 2 * np.cos(theta_2), 0], color=BLUE)
        self.add(point_J, point_J2)
        
        point_K = Dot([2 * np.sin(theta_1), 2 * np.cos(theta_2), 0], color=BLUE)
        self.add(point_K)

        point_L = Dot([-2 * np.sin(theta_1), -2 * np.cos(theta_2), 0], color=BLUE)
        point_L2 = Dot([2 * np.sin(theta_1), -2 * np.cos(theta_2), 0], color=BLUE)
        self.add(point_L, point_L2)


        point_O = Dot([0, 0, 0], color=BLUE)
        self.add(point_O)        

        lines = [
            Line(start=point_B, end=point_E, color=RED),
            Line(start=point_A, end=point_D, color=YELLOW),
            Line(start=point_F, end=point_G, color=BLUE),
            Line(start=point_H, end=point_I, color=VIOLET),
            Line(start=point_C2, end=point_F2, color=RED),
            Line(start=point_C2, end=point_H2, color=RED),
            Line(start=point_C3, end=point_F3, color=RED),
            Line(start=point_C3, end=point_I2, color=RED),
            Line(start=point_C3, end=point_J, color=BLACK),
            Line(start=point_C4, end=point_J, color=BLACK),
            Line(start=point_C5, end=point_K, color=BLACK),
            Line(start=point_J, end=point_L, color=BLACK),
            Line(start=point_L, end=point_L2, color=RED)
        ]

        self.play([Create(line) for line in lines])

        arc_AF = ArcBetweenPoints(
            point_A.get_center_of_mass(),
            point_F.get_center_of_mass(),
            stroke_width=0,
            radius=2
        )
        line_FC = ArcBetweenPoints(
            point_F.get_center_of_mass(),
            point_C.get_center_of_mass(),
            stroke_width=0,
            radius=100
        )
        line_CA = ArcBetweenPoints(
            point_C.get_center_of_mass(),
            point_A.get_center_of_mass(),
            stroke_width=0,
            radius=100
        )

        arc_FB = ArcBetweenPoints(
            point_F.get_center_of_mass(),
            point_B.get_center_of_mass(),
            stroke_width=0,
            radius=2
        )
        line_BC = ArcBetweenPoints(
            point_B.get_center_of_mass(),
            point_C.get_center_of_mass(),
            stroke_width=0,
            radius=100
        )
        line_CF = ArcBetweenPoints(
            point_C.get_center_of_mass(),
            point_F.get_center_of_mass(),
            stroke_width=0,
            radius=100
        )

        arc_BH = ArcBetweenPoints(
            point_B.get_center_of_mass(),
            point_H.get_center_of_mass(),
            stroke_width=0,
            radius=2
        )
        line_HC = ArcBetweenPoints(
            point_H.get_center_of_mass(),
            point_C.get_center_of_mass(),
            stroke_color=BLACK,
            stroke_width=0,
            radius=100
        )
        line_CB = ArcBetweenPoints(
            point_C.get_center_of_mass(),
            point_B.get_center_of_mass(),
            stroke_color=BLACK,
            stroke_width=0,
            radius=100
        )

        arc_HD = ArcBetweenPoints(
            point_H.get_center_of_mass(),
            point_D.get_center_of_mass(),
            stroke_width=0,
            radius=2
        )
        line_DC = ArcBetweenPoints(
            point_D.get_center_of_mass(),
            point_C.get_center_of_mass(),
            stroke_color=BLACK,
            stroke_width=0,
            radius=100
        )
        line_CH = ArcBetweenPoints(
            point_C.get_center_of_mass(),
            point_H.get_center_of_mass(),
            stroke_color=BLACK,
            stroke_width=0,
            radius=100
        )

        arc_DG = ArcBetweenPoints(
            point_D.get_center_of_mass(),
            point_G.get_center_of_mass(),
            stroke_width=0,
            radius=2
        )
        line_GC = ArcBetweenPoints(
            point_G.get_center_of_mass(),
            point_C.get_center_of_mass(),
            stroke_color=BLACK,
            stroke_width=0,
            radius=100
        )
        line_CD = ArcBetweenPoints(
            point_C.get_center_of_mass(),
            point_D.get_center_of_mass(),
            stroke_color=BLACK,
            stroke_width=0,
            radius=100
        )

        arc_GE = ArcBetweenPoints(
            point_G.get_center_of_mass(),
            point_E.get_center_of_mass(),
            stroke_width=0,
            radius=2
        )
        line_EC = ArcBetweenPoints(
            point_E.get_center_of_mass(),
            point_C.get_center_of_mass(),
            stroke_color=BLACK,
            stroke_width=0,
            radius=100
        )
        line_CG = ArcBetweenPoints(
            point_C.get_center_of_mass(),
            point_G.get_center_of_mass(),
            stroke_color=BLACK,
            stroke_width=0,
            radius=100
        )

        arc_EI = ArcBetweenPoints(
            point_E.get_center_of_mass(),
            point_I.get_center_of_mass(),
            stroke_width=0,
            radius=2
        )
        line_IC = ArcBetweenPoints(
            point_I.get_center_of_mass(),
            point_C.get_center_of_mass(),
            stroke_color=BLACK,
            stroke_width=0,
            radius=100
        )
        line_CE = ArcBetweenPoints(
            point_C.get_center_of_mass(),
            point_E.get_center_of_mass(),
            stroke_color=BLACK,
            stroke_width=0,
            radius=100
        )

        arc_IA = ArcBetweenPoints(
            point_I.get_center_of_mass(),
            point_A.get_center_of_mass(),
            stroke_width=0,
            radius=2
        )
        line_AC = ArcBetweenPoints(
            point_A.get_center_of_mass(),
            point_C.get_center_of_mass(),
            stroke_color=BLACK,
            stroke_width=0,
            radius=100
        )
        line_CI = ArcBetweenPoints(
            point_C.get_center_of_mass(),
            point_I.get_center_of_mass(),
            stroke_color=BLACK,
            stroke_width=0,
            radius=100
        )


        poly_param = {
            'stroke_color': BLACK,
            'fill_opacity': 0.5,
            'stroke_width': 1
        }
        poly_AFC = ArcPolygonFromArcs(
            arc_AF, line_FC, line_CA, color=RED, **poly_param
        )
        poly_FBC = ArcPolygonFromArcs(
            arc_FB, line_BC, line_CF, color=BLUE, **poly_param
        )
        poly_BHC = ArcPolygonFromArcs(
            arc_BH, line_HC, line_CB, color=RED, **poly_param
        )
        poly_HDC = ArcPolygonFromArcs(
            arc_HD, line_DC, line_CH, color=BLUE, **poly_param
        )
        poly_DGC = ArcPolygonFromArcs(
            arc_DG, line_GC, line_CD, color=RED, **poly_param
        )
        poly_GEC = ArcPolygonFromArcs(
            arc_GE, line_EC, line_CG, color=BLUE, **poly_param
        )
        poly_EIC = ArcPolygonFromArcs(
            arc_EI, line_IC, line_CE, color=RED, **poly_param
        )
        poly_IAC = ArcPolygonFromArcs(
            arc_IA, line_AC, line_CI, color=BLUE, **poly_param
        )

        self.play(
            Create(poly_AFC),
            Create(poly_FBC),
            Create(poly_BHC),
            Create(poly_HDC),
            Create(poly_DGC),
            Create(poly_GEC),
            Create(poly_EIC),
            Create(poly_IAC)
        )

        self.wait(2)

        circle2 = circle.copy()
        self.play(
            Create(circle2)
        )

        lines = [
            Line(start=point_A, end=point_D, color=RED),
            Line(start=point_B, end=point_E, color=RED),
            Line(start=point_F, end=point_G, color=RED),
            Line(start=point_I, end=point_H, color=RED),
            Line(start=point_C2, end=point_F2, color=RED),
            Line(start=point_C2, end=point_H2, color=RED),
            Line(start=point_C3, end=point_F3, color=RED),
            Line(start=point_C3, end=point_I2, color=RED)
        ]
        self.play([Create(line) for line in lines])

        self.wait(1)