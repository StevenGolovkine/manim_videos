"""
Visual proof of A Golden Section Problem from the Monthly
Proofs without Words II. Roger B. Nelsen. p. 18.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, Group
from manim import Polygon, VGroup, FadeIn, FadeOut, FunctionGraph
from manim import Text, Tex, Triangle, RoundedRectangle, Circle, Line, Dot, Angle

from manim import config
from manim import LEFT, RIGHT, DOWN, LIGHT, UP, SMALL_BUFF, PI

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


class Golden(MovingCameraScene):
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
            Tex(r"Une construction", font_size=40, color=BLACK),
            Tex(r"du nombre d'or $\varphi$", font_size=40, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Jan van de Craats", font_size=28, color=BLACK)
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

        # Create the triangle
        triangle = Triangle(color=BLACK, stroke_width=2).scale(2)
        points = triangle.get_vertices()

        p_D = Tex(r"$D$", font_size=28, color=BLACK).\
            next_to(points[0], 0.5 * UP)
        D = Dot(points[0], color=BLACK)
        p_E = Tex(r"$E$", font_size=28, color=BLACK).\
            next_to(points[1], 0.5 * (DOWN + LEFT))
        E = Dot(points[1], color=BLACK)
        p_F = Tex(r"$F$", font_size=28, color=BLACK).\
            next_to(points[2], 0.5 * (DOWN + RIGHT))
        F = Dot(points[2], color=BLACK)

        txt = Tex(r"$DEF$ est équilatéral", font_size=32, color=BLACK).\
            next_to(triangle, 2 * UP)

        self.play(
            Write(txt),
            Create(triangle),
            Write(p_D),
            Write(p_E),
            Write(p_F)
        )

        # Create the middle points
        DE = Line(points[0], points[1])
        DF = Line(points[0], points[2])
        p_A = Tex(r"$A$", font_size=28, color=BLACK).\
            next_to(DE.get_center(), 0.5 * (UP + LEFT))
        A = Dot(DE.get_center(), color=BLACK)
        p_B = Tex(r"$B$", font_size=28, color=BLACK).\
            next_to(DF.get_center(), 0.5 * (UP + RIGHT))
        B = Dot(DF.get_center(), color=BLACK)

        AD = Line(A, D)
        AE = Line(A, E)
        DB = Line(D, B)
        BF = Line(B, F)
        AB = Line(A, B)

        xs = [
            Tex(r"$x$", font_size=20, color=BLACK).\
                next_to(AD.get_center(), 0.2 * (UP + LEFT)),
            Tex(r"$x$", font_size=20, color=BLACK).\
                next_to(AE.get_center(), 0.2 * (UP + LEFT)),
            Tex(r"$x$", font_size=20, color=BLACK).\
                next_to(DB.get_center(), 0.2 * (UP + RIGHT)),
            Tex(r"$x$", font_size=20, color=BLACK).\
                next_to(BF.get_center(), 0.2 * (UP + RIGHT)),
            Tex(r"$x$", font_size=20, color=BLACK).\
                next_to(AB.get_center(), 0.2 * UP)
        ]

        self.play(
            Write(p_A),
            Create(A),
            Write(p_B),
            Create(B),
            *[Write(x) for x in xs]
        )

        # Create the circle
        origin = triangle.get_center_of_mass()
        circle = Circle(radius=2, color=BLACK, stroke_width=2).move_to(origin)
        self.play(
            Create(circle)
        )

        # Intersect AB and the circle
        p_G = Tex(r"$G$", font_size=28, color=BLACK).\
            next_to([-1.9373, 0.25, 0], 0.1 * (LEFT + UP))
        p_C = Tex(r"$C$", font_size=28, color=BLACK).\
            next_to([1.9373, 0.25, 0], 0.1 * (RIGHT + UP))
        G = Dot([-1.9373, 0.25, 0], color=BLACK)
        C = Dot([1.9373, 0.25, 0], color=BLACK)
        GC = Line(G.get_center(), C.get_center(), color=BLACK, stroke_width=2)

        GA = Line(G, A)
        BC = Line(B, C)
        ys = [
            Tex(r"$y$", font_size=20, color=BLACK).\
                next_to(GA.get_center(), 0.2 * UP),
            Tex(r"$y$", font_size=20, color=BLACK).\
                next_to(BC.get_center(), 0.2 * UP),
        ]

        self.play(
            Create(GC),
            Write(p_G),
            Write(p_C),
            *[Write(y) for y in ys]
        )

        # Create GBD and BCF
        GB = Line(G, B, color=BLACK, stroke_width=2)
        BD = Line(B, D, color=BLACK, stroke_width=2)
        DG = Line(D, G, color=BLACK, stroke_width=2)
        GBD = Polygon(
            G.get_center(),
            B.get_center(),
            D.get_center(),
            stroke_width=2,
            color=BLACK
        ).set_fill(RED, 0.5)
        self.play(
            Create(GBD)
        )

        BCF = Polygon(
            C.get_center(),
            B.get_center(),
            F.get_center(),
            stroke_width=2,
            color=BLACK
        ).set_fill(BLUE, 0.5)
        self.play(
            Create(BCF)
        )

        # Angles
        BC = Line(B, C, color=BLACK, stroke_width=2)
        CF = Line(C, F, color=BLACK, stroke_width=2)
        BF = Line(B, F, color=BLACK, stroke_width=2)
        angle_GDB = Angle(
            BD, DG, color=BLACK, radius=0.25, stroke_width=2,
            quadrant=(-1, 1), other_angle=True
        )
        angle_BCF = Angle(
            CF, BC, color=BLACK, radius=0.25, stroke_width=2,
            quadrant=(1, -1), other_angle=True
        )

        self.play(
            Create(angle_BCF),
            Create(angle_GDB)
        )

        angle_DGB = Angle(
            GB, DG, color=BLACK, radius=0.3, stroke_width=2,
            quadrant=(1, -1),
            dot=True, dot_color=BLACK
        )
        angle_CFB = Angle(
            CF, BF, color=BLACK, radius=0.25, stroke_width=2,
            quadrant=(-1, -1),
            dot=True, dot_color=True
        )

        self.play(
            Create(angle_DGB),
            Create(angle_CFB)
        )

        all = Group(*[mob for mob in self.mobjects[1:]])
        self.play(
            FadeOut(txt),
            all.animate.shift([0, -1, 0])
        )

        # Write results
        rect = RoundedRectangle(
            height=2, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=0
        ).move_to([0, 2.5, 0])

        txt = Tex(
            r"sont semblables.",
            font_size=28, color=BLACK
        ).move_to([0, 2, 0])
        et = Tex(
            r"et",
            font_size=28, color=BLACK
        ).move_to([0.25, 2.75, 0])

        GBD_c = GBD.copy()
        BCF_c = BCF.copy()

        self.play(
            Create(rect),
            GBD_c.animate.scale(0.5).move_to([-0.75, 2.75, 0]),
            Write(et),
            BCF_c.animate.scale(0.5).move_to([1, 2.75, 0]),
            Write(txt)
        )

        self.wait(0.5)

        equation = Tex(
            r"$\frac{GD}{CF} = \frac{GB}{BF} = \frac{DB}{BC}$",
            color=BLACK, font_size=34
        ).move_to([0, 2.5, 0])
        self.play(
            FadeOut(GBD_c), FadeOut(BCF_c), FadeOut(et), FadeOut(txt),
            Write(equation)
        )
        self.wait(0.5)

        equation2 = Tex(
            r"$\frac{x + y}{x} = \frac{x}{y}$",
            color=BLACK, font_size=34
        ).move_to([0, 2.5, 0])
        self.play(
            Transform(equation, equation2)
        )
        self.wait(0.5)

        equation3 = Tex(
            r"$1 + \frac{y}{x} = \frac{x}{y}$",
            color=BLACK, font_size=34
        ).move_to([0, 2.5, 0])
        self.play(
            Transform(equation, equation3)
        )
        self.wait(0.5)

        equation4 = Tex(
            r"$\frac{x}{y} + 1 = \left(\frac{x}{y}\right)^2$",
            color=BLACK, font_size=34
        ).move_to([0, 2.5, 0])
        self.play(
            Transform(equation, equation4)
        )
        self.wait(0.5)

        equation5 = Tex(
            r"Nombre d'or $\phi = \frac{x}{y}$",
            color=BLACK, font_size=34
        ).move_to([0, 2.5, 0])
        self.play(
            Transform(equation, equation5)
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Proofs without words II:", font_size=30, color=BLACK),
            Tex(r"More exercises in", font_size=30, color=BLACK),
            Tex(r"visual thinking", font_size=30, color=BLACK),
            Tex(r"Roger B. Nelsen (2000), p. 18", font_size=30, color=BLACK)
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