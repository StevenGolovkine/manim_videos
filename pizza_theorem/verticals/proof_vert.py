"""
Visual proof of the sums of odd integers.
Proofs without Words II. Roger B. Nelsen. p. 27.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Dot, ArcBetweenPoints, Line, ArcPolygonFromArcs, RoundedRectangle
from manim import Create, Uncreate, Write
from manim import VGroup, Transform
from manim import Tex, TexFontTemplates

from manim import config

from manim import LEFT, RIGHT, DOWN, PI

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


class Pizza(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame.save_state()

        Tex.set_default(tex_template=TexFontTemplates.droid_sans)
        txt_copy = Tex(
            r"@Maths\&Chill", font_size=12, color=BLACK
        ).to_edge(RIGHT + DOWN, buff=0.1)
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

        # Create importante points on the circle
        theta_1 = PI / 9
        theta_2 = PI / 3
        
        b = np.sin(theta_1) - np.cos(theta_2)
        xf = (- 2 * b + 2 * np.sqrt(2 - b**2)) / 2
        yf = (2 * b + 2 * np.sqrt(2 - b**2)) / 2
        xg = (- 2 * b - 2 * np.sqrt(2 - b**2)) / 2
        yg = (2 * b - 2 * np.sqrt(2 - b**2)) / 2

        b = np.sin(theta_1) + np.cos(theta_2)
        xi = (2 * b + 2 * np.sqrt(2 - b**2)) / 2
        yi = (2 * b - 2 * np.sqrt(2 - b**2)) / 2
        xh = (2 * b - 2 * np.sqrt(2 - b**2)) / 2
        yh = (2 * b + 2 * np.sqrt(2 - b**2)) / 2

        shift = -1
        points = {
            'O': [0, 0 + shift, 0],
            'A': [2 * np.cos(theta_1), 2 * np.sin(theta_1) + shift, 0],
            'B': [2 * np.cos(theta_2), 2 * np.sin(theta_2) + shift, 0], 
            'D': [2 * np.cos(PI - theta_1), 2 * np.sin(theta_1) + shift, 0],
            'E': [2 * np.cos(theta_2), 2 * np.sin(-theta_2) + shift, 0],
            'C': [2 * np.cos(theta_2), 2 * np.sin(theta_1) + shift, 0],
            'C2': [2 * np.cos(theta_2), -2 * np.sin(theta_1) + shift, 0],
            'C3': [-2 * np.cos(theta_2), 2 * np.sin(theta_1) + shift, 0],
            'C4': [2 * np.cos(theta_2) - 4 * np.sin(theta_1), 2 * np.sin(theta_1) + shift, 0],
            'C5': [4 * np.sin(theta_1) - 2 * np.cos(theta_2), 2 * np.sin(theta_1) + shift, 0],
            'F': [xf, yf + shift, 0],
            'F2': [xf, -yf + shift, 0],
            'F3': [-xf, yf + shift, 0],
            'G': [xg, yg + shift, 0],
            'I': [xi, yi + shift, 0],
            'I2': [-xi, yi + shift, 0],
            'H': [xh, yh + shift, 0],
            'H2': [xh, -yh + shift, 0],
            'J': [-2 * np.sin(theta_1), 4 * np.sin(theta_1) - 2 * np.cos(theta_2) + shift, 0],
            'J2': [-2 * np.sin(theta_1), 2 * np.cos(theta_2) + shift, 0],
            'K': [2 * np.sin(theta_1), 2 * np.cos(theta_2) + shift, 0],
            'L': [-2 * np.sin(theta_1), -2 * np.cos(theta_2) + shift, 0],
            'L2': [2 * np.sin(theta_1), -2 * np.cos(theta_2) + shift, 0]
        }

        lines = [
            Line(start=points['B'], end=points['E'], color=BLACK, stroke_width=1),
            Line(start=points['A'], end=points['D'], color=BLACK, stroke_width=1),
            Line(start=points['F'], end=points['G'], color=BLACK, stroke_width=1),
            Line(start=points['H'], end=points['I'], color=BLACK, stroke_width=1)
        ]
        self.play([Create(line) for line in lines])

        arc_param = {
            'stroke_width': 0,
            'radius': 2
        }
        line_param = {
            'stroke_width': 0,
            'radius': 10000
        }

        arc_AF = ArcBetweenPoints(points['A'], points['F'], **arc_param)
        line_FC = ArcBetweenPoints(points['F'], points['C'], **line_param)
        line_CA = ArcBetweenPoints(points['C'], points['A'], **line_param)

        arc_FB = ArcBetweenPoints(points['F'], points['B'], **arc_param)
        line_BC = ArcBetweenPoints(points['B'], points['C'], **line_param)
        line_CF = ArcBetweenPoints(points['C'], points['F'], **line_param)

        arc_BH = ArcBetweenPoints(points['B'], points['H'], **arc_param)
        line_HC = ArcBetweenPoints(points['H'], points['C'], **line_param)
        line_CB = ArcBetweenPoints(points['C'], points['B'], **line_param)

        arc_HD = ArcBetweenPoints(points['H'], points['D'], **arc_param)
        line_DC = ArcBetweenPoints(points['D'], points['C'], **line_param)
        line_CH = ArcBetweenPoints(points['C'], points['H'], **line_param)

        arc_DG = ArcBetweenPoints(points['D'], points['G'], **arc_param)
        line_GC = ArcBetweenPoints(points['G'], points['C'], **line_param)
        line_CD = ArcBetweenPoints(points['C'], points['D'], **line_param)

        arc_GE = ArcBetweenPoints(points['G'], points['E'], **arc_param)
        line_EC = ArcBetweenPoints(points['E'], points['C'], **line_param)
        line_CG = ArcBetweenPoints(points['C'], points['G'], **line_param)

        arc_EI = ArcBetweenPoints(points['E'], points['I'], **arc_param)
        line_IC = ArcBetweenPoints(points['I'], points['C'], **line_param)
        line_CE = ArcBetweenPoints(points['C'], points['E'], **line_param)

        arc_IA = ArcBetweenPoints(points['I'], points['A'], **arc_param)
        line_AC = ArcBetweenPoints(points['A'], points['C'], **line_param)
        line_CI = ArcBetweenPoints(points['C'], points['I'], **line_param)


        poly_param = {
            'stroke_color': BLACK,
            'fill_opacity': 0.5,
            'stroke_width': 1
        }
        poly_AFC = ArcPolygonFromArcs(
            line_CA, arc_AF, line_FC, color=RED, **poly_param
        )
        poly_FBC = ArcPolygonFromArcs(
            line_CF, arc_FB, line_BC, color=BLUE, **poly_param
        )
        poly_BHC = ArcPolygonFromArcs(
            line_CB, arc_BH, line_HC, color=RED, **poly_param
        )
        poly_HDC = ArcPolygonFromArcs(
            line_CH, arc_HD, line_DC, color=BLUE, **poly_param
        )
        poly_DGC = ArcPolygonFromArcs(
            line_CD, arc_DG, line_GC, color=RED, **poly_param
        )
        poly_GEC = ArcPolygonFromArcs(
            line_CG, arc_GE, line_EC, color=BLUE, **poly_param
        )
        poly_EIC = ArcPolygonFromArcs(
            line_CE, arc_EI, line_IC, color=RED, **poly_param
        )
        poly_IAC = ArcPolygonFromArcs(
            line_CI, arc_IA, line_AC, color=BLUE, **poly_param
        )

        self.play(Create(poly_AFC), run_time=0.5)
        self.play(Create(poly_FBC), run_time=0.5)
        self.play(Create(poly_BHC), run_time=0.5)
        self.play(Create(poly_HDC), run_time=0.5)
        self.play(Create(poly_DGC), run_time=0.5)
        self.play(Create(poly_GEC), run_time=0.5)
        self.play(Create(poly_EIC), run_time=0.5)
        self.play(Create(poly_IAC), run_time=0.5)

        # Proof -> convert blue areas into red areas.
        arc_DI2 = ArcBetweenPoints(points['D'], points['I2'], **arc_param)
        line_I2C3 = ArcBetweenPoints(points['I2'], points['C3'], **line_param)
        line_C3D = ArcBetweenPoints(points['C3'], points['D'], **line_param)
        poly_DIC2 = ArcPolygonFromArcs(
            line_C3D, arc_DI2, line_I2C3, color=BLUE, **poly_param
        )
        self.play(
            Transform(poly_IAC.copy(), poly_DIC2)
        )

        arc_EF2 = ArcBetweenPoints(points['E'], points['F2'], **arc_param)
        line_F2C2 = ArcBetweenPoints(points['F2'], points['C2'], **line_param)
        line_C2E = ArcBetweenPoints(points['C2'], points['E'], **line_param)
        poly_F3DC3 = ArcPolygonFromArcs(
            line_C2E, arc_EF2, line_F2C2, color=BLUE, **poly_param
        )
        self.play(
            Transform(poly_FBC.copy(), poly_F3DC3)
        )

        arc_H2E = ArcBetweenPoints(points['H2'], points['E'], **arc_param)
        line_EC2= ArcBetweenPoints(points['E'], points['C2'], **line_param)
        line_C2H2 = ArcBetweenPoints(points['C2'], points['H2'], **line_param)
        poly_H2EC2 = ArcPolygonFromArcs(
            line_C2H2, arc_H2E, line_EC2, color=BLUE, **poly_param
        )
        poly_BHC_c = ArcPolygonFromArcs(
            line_CB, arc_BH, line_HC, color=BLUE, **poly_param
        )
        line_C2H2_c = line_C2H2.copy().set_stroke(width=1).set_color(BLACK)
        self.play(Create(line_C2H2_c), run_time=0.5)
        self.play(Transform(poly_H2EC2, poly_BHC_c))

        arc_F3D = ArcBetweenPoints(points['F3'], points['D'], **arc_param)
        line_DC3 = ArcBetweenPoints(points['D'], points['C3'], **line_param)
        line_C3F3 = ArcBetweenPoints(points['C3'], points['F3'], **line_param)
        poly_F3DC3 = ArcPolygonFromArcs(
            line_C3F3, arc_F3D, line_DC3, color=BLUE, **poly_param
        )
        poly_AFC_c = ArcPolygonFromArcs(
            line_CA, arc_AF, line_FC, color=BLUE, **poly_param
        )
        line_C3F3_c = line_C3F3.copy().set_stroke(width=1).set_color(BLACK)
        self.play(Create(line_C3F3_c), run_time=0.5)
        self.play(
            Transform(poly_F3DC3, poly_AFC_c)
        )

        arc_GH2 = ArcBetweenPoints(points['G'], points['H2'], **arc_param)
        line_H2L2 = ArcBetweenPoints(points['H2'], points['L2'], **line_param)
        line_L2L = ArcBetweenPoints(points['L2'], points['L'], **line_param)
        line_LG = ArcBetweenPoints(points['L'], points['G'], **line_param)
        poly_GH2L2L = ArcPolygonFromArcs(
            line_L2L, line_LG, arc_GH2, line_H2L2, color=BLUE, **poly_param
        )

        arc_F2I = ArcBetweenPoints(points['F2'], points['I'], **arc_param)
        line_IC = ArcBetweenPoints(points['I'], points['C'], **line_param)
        line_CC2 = ArcBetweenPoints(points['C'], points['C2'], **line_param)
        line_C2F2 = ArcBetweenPoints(points['C2'], points['F2'], **line_param)
        poly_F2ICC2F2 = ArcPolygonFromArcs(
            line_CC2, line_C2F2, arc_F2I, line_IC, color=BLUE, **poly_param
        )
        line_L2L_c = line_L2L.copy().set_stroke(width=1).set_color(BLACK)
        self.play(Create(line_L2L_c), run_time=0.5)
        self.play(
            Transform(poly_GH2L2L, poly_F2ICC2F2)
        )
        
        line_CL = ArcBetweenPoints(points['C'], points['L'], **line_param)
        line_LJ = ArcBetweenPoints(points['L'], points['J'], **line_param)
        line_JC4 = ArcBetweenPoints(points['J'], points['C4'], **line_param)
        line_C4C = ArcBetweenPoints(points['C4'], points['C'], **line_param)
        poly_HF3C3C5K = ArcPolygonFromArcs(
            line_CL, line_LJ, line_JC4, line_C4C, color=BLUE, **poly_param
        )
        
        line_CL = ArcBetweenPoints(points['C'], points['L'], **line_param)
        line_LL2 = ArcBetweenPoints(points['L'], points['L2'], **line_param)
        line_L2C2 = ArcBetweenPoints(points['L2'], points['C2'], **line_param)
        line_C2C = ArcBetweenPoints(points['C2'], points['C'], **line_param)
        poly_CLL2C2 = ArcPolygonFromArcs(
            line_CL, line_LL2, line_L2C2, line_C2C, color=BLUE, **poly_param
        )

        self.play(
            Transform(poly_CLL2C2, poly_HF3C3C5K)
        )

        line_KC = ArcBetweenPoints(points['K'], points['C'], **line_param)
        line_CC5 = ArcBetweenPoints(points['C'], points['C5'], **line_param)
        line_C5K = ArcBetweenPoints(points['C5'], points['K'], **line_param)
        poly_KCC5 = ArcPolygonFromArcs(
            line_KC, line_CC5, line_C5K, color=BLUE, **poly_param
        )

        line_JC3 = ArcBetweenPoints(points['J'], points['C3'], **line_param)
        line_C3C4 = ArcBetweenPoints(points['C3'], points['C4'], **line_param)
        line_C4J = ArcBetweenPoints(points['C4'], points['J'], **line_param)
        poly_JC3C4 = ArcPolygonFromArcs(
            line_JC3, line_C3C4, line_C4J, color=BLUE, **poly_param
        )
        line_C5K_c = line_C5K.copy().set_stroke(width=1).set_color(BLACK)
        self.play(Create(line_C5K_c), run_time=0.5)
        self.play(
            Transform(poly_KCC5, poly_JC3C4)
        )

        arc_HF3 = ArcBetweenPoints(points['H'], points['F3'], **arc_param)
        line_F3C3 = ArcBetweenPoints(points['F3'], points['C3'], **line_param)
        line_C3C5 = ArcBetweenPoints(points['C3'], points['C5'], **line_param)
        line_C5K = ArcBetweenPoints(points['C5'], points['K'], **line_param)
        line_KH = ArcBetweenPoints(points['K'], points['H'], **line_param)
        poly_HF3C3C5K = ArcPolygonFromArcs(
            line_C3C5, line_C5K, line_KH, arc_HF3, line_F3C3, color=BLUE, **poly_param
        )
        
        arc_I2G = ArcBetweenPoints(points['I2'], points['G'], **arc_param)
        line_GL = ArcBetweenPoints(points['G'], points['L'], **line_param)
        line_LJ = ArcBetweenPoints(points['L'], points['J'], **line_param)
        line_JC3 = ArcBetweenPoints(points['J'], points['C3'], **line_param)
        line_C3I2 = ArcBetweenPoints(points['C3'], points['I2'], **line_param)
        poly_I2GLJC3 = ArcPolygonFromArcs(
            line_LJ, line_JC3, line_C3I2, arc_I2G, line_GL, color=BLUE, **poly_param
        )

        self.play(
            Transform(poly_HF3C3C5K, poly_I2GLJC3)
        )

        rect = RoundedRectangle(
            height=1, width=4,
            color=BLACK,
            stroke_width=2,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, 0.75, 0])
        txt = Tex(
            r"Aire ", r"$\blacksquare$", r" $=$ ",
            r"Aire ", r"$\blacksquare$",
            font_size=40, color=BLACK,
        ).move_to([0, 0.75, 0])
        txt[1].set_color(RED).set_opacity(0.5)
        txt[4].set_color(BLUE).set_opacity(0.5)

        rect.z_index = 0
        txt.z_index = 1
        self.play(
            Create(rect),
            Write(txt),
            run_time=0.5
        )

        self.wait(3)
        # # Different point on the circle
        # point_A = Dot(points['A'], color=BLUE)
        # point_B = Dot(points['B'], color=RED)
        # point_D = Dot(points['D'], color=VIOLET)
        # point_E = Dot(points['E'], color=YELLOW)
        # self.add(point_A, point_E, point_B, point_D)

        # point_C = Dot(points["C"], color=BLACK)
        # point_C2 = Dot(points["C2"], color=BLACK)
        # point_C3 = Dot(points["C3"], color=BLACK)
        # point_C4 = Dot(points["C4"], color=BLACK)
        # point_C5 = Dot(points["C5"], color=BLACK)
        # self.add(point_C, point_C2, point_C3, point_C4, point_C5)

        # point_F = Dot(points["F"], color=RED)
        # point_F2 = Dot(points["F2"], color=BLUE)
        # point_F3 = Dot(points["F3"], color=BLUE)
        # self.add(point_F, point_F2, point_F3)

        # point_G = Dot(points["G"], color=RED)
        # self.add(point_G)

        # point_I = Dot(points["I"], color=ORANGE)
        # point_I2 = Dot(points["I2"], color=ORANGE)
        # self.add(point_I, point_I2)
        
        # point_H = Dot(points["H"], color=RED)
        # point_H2 = Dot(points["H2"], color=RED)
        # self.add(point_H, point_H2)
        
        # point_J = Dot(points["J"], color=BLUE)
        # point_J2 = Dot(points["J2"], color=BLUE)
        # self.add(point_J, point_J2)
        
        # point_K = Dot(points["K"], color=BLUE)
        # self.add(point_K)

        # point_L = Dot(points["L"], color=BLUE)
        # point_L2 = Dot(points["L2"], color=BLUE)
        # self.add(point_L, point_L2)

        # point_O = Dot(points["O"], color=BLUE)
        # self.add(point_O)

        # lines = [
        #     Line(start=point_B, end=point_E, color=RED),
        #     Line(start=point_A, end=point_D, color=YELLOW),
        #     Line(start=point_F, end=point_G, color=BLUE),
        #     Line(start=point_H, end=point_I, color=VIOLET),
        #     Line(start=point_C2, end=point_F2, color=RED),
        #     Line(start=point_C2, end=point_H2, color=RED),
        #     Line(start=point_C3, end=point_F3, color=RED),
        #     Line(start=point_C3, end=point_I2, color=RED),
        #     Line(start=point_C3, end=point_J, color=BLACK),
        #     Line(start=point_C4, end=point_J, color=BLACK),
        #     Line(start=point_C5, end=point_K, color=BLACK),
        #     Line(start=point_J, end=point_L, color=BLACK),
        #     Line(start=point_L, end=point_L2, color=RED)
        # ]

        # self.play([Create(line) for line in lines])
