"""
Visual proof of the triangle of medians has three-fourth the area of the original
triangle.
Proofs without Words II. Roger B. Nelsen. p. 16.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, TransformFromCopy
from manim import VGroup, FadeIn, FadeOut , FunctionGraph
from manim import DashedVMobject, Line, Point, Polygon, RoundedRectangle
from manim import Text, Tex

from manim import config
from manim import ORIGIN, LEFT, RIGHT, DOWN, LIGHT, UP, PI

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


class Triangle(MovingCameraScene):
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
            Tex(r"L'aire du triangle", font_size=48, color=BLACK),
            Tex(r"des médianes est égale", font_size=48, color=BLACK),
            Tex(r"aux trois-quarts", font_size=48, color=BLACK),
            Tex(r"du triangle original", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Norbert Hungerbühler", font_size=28, color=BLACK)
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

        # Triangle
        pA = Point([-2, -1, 0], color=BLACK)
        pB = Point([2, -1, 0], color=BLACK)
        pC = Point([-1, 2, 0], color=BLACK)
        AB = Line(pA, pB, color=BLACK, stroke_width=2)
        BC = Line(pB, pC, color=BLACK, stroke_width=2)
        CA = Line(pC, pA, color=BLACK, stroke_width=2)
        AMb = Line(pA, BC.get_center_of_mass(), color=BLUE)
        BMc = Line(pB, CA.get_center_of_mass(), color=VIOLET)
        CMa = Line(pC, AB.get_center_of_mass(), color=RED)
        A = Tex(r"$A$", font_size=36, color=BLACK).next_to(pA, DOWN, buff=0.1)
        B = Tex(r"$B$", font_size=36, color=BLACK).next_to(pB, DOWN, buff=0.1)
        C = Tex(r"$C$", font_size=36, color=BLACK).next_to(pC, UP, buff=0.1)
        Ma = Tex(r"$M_a$", font_size=36, color=BLUE).\
            next_to(BC.get_center_of_mass(), RIGHT, buff=0.1)
        Mb = Tex(r"$M_b$", font_size=36, color=VIOLET).\
            next_to(CA.get_center_of_mass(), LEFT, buff=0.1)
        Mc = Tex(r"$M_c$", font_size=36, color=RED).\
            next_to(AB.get_center_of_mass(), DOWN, buff=0.1)
        triangle = VGroup(AB, BC, CA)

        self.play(
            Create(triangle),
        )
        self.play(           
            Create(AMb),
            Create(BMc),
            Create(CMa),
            Create(Ma),
            Create(Mb),
            Create(Mc),
            Create(A),
            Create(B),
            Create(C),
        )

        # Small triangles
        triangle_MaMbMc = Polygon(
            AB.get_center_of_mass(),
            BC.get_center_of_mass(),
            CA.get_center_of_mass(),
            stroke_width=0
        )
        triangle_MaMbMc.set_fill(GREEN, 0.5)
        triangle_MaMbMc_c = DashedVMobject(
            triangle_MaMbMc.copy(),
            num_dashes=15, dashed_ratio=0.3,
        ).set_color(BLACK).set_stroke(width=2)
        self.play(
            Create(triangle_MaMbMc),
            Create(triangle_MaMbMc_c),
            run_time=0.5
        )

        triangle_MaMbMc_cc = triangle_MaMbMc.copy()
        triangle_MbMaC = Polygon(
            BC.get_center_of_mass(),
            CA.get_center_of_mass(),
            pC.get_center_of_mass(),
            stroke_width=0
        )
        triangle_MbMaC.set_fill(ORANGE, 0.5)
        self.play(
            Transform(triangle_MaMbMc_cc, triangle_MbMaC),
            run_time=0.5
        )

        triangle_MaMbMc_ccc = triangle_MaMbMc_cc.copy()
        triangle_McMbA = Polygon(
            AB.get_center_of_mass(),
            pA.get_center_of_mass(),
            CA.get_center_of_mass(),
            stroke_width=0
        )
        triangle_McMbA.set_fill(ORANGE, 0.5)
        self.play(
            Transform(triangle_MaMbMc_ccc, triangle_McMbA),
            run_time=0.5
        )

        triangle_MaMbMc_cccc = triangle_MaMbMc_ccc.copy()
        triangle_McMaB = Polygon(
            pB.get_center_of_mass(),
            AB.get_center_of_mass(),
            BC.get_center_of_mass(),
            stroke_width=0
        )
        triangle_McMaB.set_fill(ORANGE, 0.5)
        self.play(
            Transform(triangle_MaMbMc_cccc, triangle_McMaB),
            run_time=0.5
        )

        # Parallelogram
        triangle_and_medians = VGroup(
            triangle,  # triangle
            triangle_MaMbMc, triangle_MaMbMc_c, triangle_MaMbMc_cc, triangle_MaMbMc_ccc, triangle_MaMbMc_cccc,  # small triangles
            AMb, BMc, CMa,  # medians
            A, B, C, Ma, Mb, Mc  # points
        )
        self.play(
            triangle_and_medians.animate.move_to([0, 2, 0]),
        )

        pA_copy = Point([-2, 0.5, 0], color=BLACK)
        pB_copy = Point([2, 0.5, 0], color=BLACK)
        pC_copy = Point([1, -2.5, 0], color=BLACK)
        CA_copy = Line(pC_copy, pA_copy, color=BLACK, stroke_width=2)
        BC_copy = Line(pB_copy, pC_copy, color=BLACK, stroke_width=2)
        triangle_down = VGroup(AB, BC_copy, CA_copy)
        self.play(
            Transform(triangle.copy(), triangle_down),
            run_time=0.5
        )

        # More small triangle
        triangle_MaMbMc_ccccc = triangle_MaMbMc_cccc.copy()
        triangle_BMcMb = Polygon(
            pB.get_center_of_mass() + 1.5 * UP,
            AB.get_center_of_mass(),
            BC_copy.get_center_of_mass(),
            stroke_width=0
        )
        triangle_BMcMb.set_fill(GREEN, 0.5)
        self.play(
            Transform(triangle_MaMbMc_ccccc, triangle_BMcMb),
            run_time=0.5
        )

        triangle_MaMbMc_cccccc = triangle_MaMbMc_ccccc.copy()
        triangle_McMaMc = Polygon(
            AB.get_center_of_mass(),
            CA_copy.get_center_of_mass(),
            BC_copy.get_center_of_mass(),
            stroke_width=0
        )
        triangle_McMaMc.set_fill(ORANGE, 0.5)
        self.play(
            Transform(triangle_MaMbMc_cccccc, triangle_McMaMc),
            run_time=0.5
        )

        triangle_MaMbMc_ccccccc = triangle_MaMbMc_cccccc.copy()
        triangle_AMbMc = Polygon(
            AB.get_center_of_mass(),
            CA_copy.get_center_of_mass(),
            pA.get_center_of_mass() + 1.5 * UP,
            stroke_width=0
        )
        triangle_AMbMc.set_fill(GREEN, 0.5)
        self.play(
            Transform(triangle_MaMbMc_ccccccc, triangle_AMbMc),
            run_time=0.5
        )

        triangle_MaMbMc_cccccccc = triangle_MaMbMc_ccccccc.copy()
        triangle_CMaMb = Polygon(
            CA_copy.get_center_of_mass(),
            pC_copy.get_center_of_mass(),
            BC_copy.get_center_of_mass(),
            stroke_width=0
        )
        triangle_CMaMb.set_fill(GREEN, 0.5)
        self.play(
            Transform(triangle_MaMbMc_cccccccc, triangle_CMaMb),
            run_time=0.5
        )

        # Move medians
        self.play(
            AMb.animate.shift(1.5 * RIGHT + 1.5 * DOWN),
            Ma.animate.next_to(triangle_and_medians[10], UP),
            CMa.animate.shift(0.5 * LEFT + 1.5 * DOWN),
            Mc.animate.next_to(triangle_down[2].get_center_of_mass(), LEFT)
        )

        # Small triangles for the triangle of medians
        HK = Line(AB.get_center_of_mass(), BC.get_center_of_mass())
        AH = Line(pA.get_center_of_mass() + 1.5 * UP, AB.get_center_of_mass())
        McMa = Line(CA_copy.get_center_of_mass(), pB_copy.get_center_of_mass())

        triangle_MbHK = Polygon(
            CA.get_center_of_mass(),
            HK.get_center_of_mass(),
            AB.get_center_of_mass(),
            stroke_width=0
        )
        triangle_MbHK.set_fill(RED, 0.5)
        txt_1 = Tex(r"$1$", font_size=28, color=BLACK).\
            next_to(triangle_MbHK.get_center_of_mass(), buff=0)
        self.play(
            Create(triangle_MbHK),
            Write(txt_1),
            run_time=0.5
        )

        triangle_HKB = Polygon(
            pB.get_center_of_mass() + 1.5 * UP,
            HK.get_center_of_mass(),
            AB.get_center_of_mass(),
            stroke_width=0
        )
        triangle_HKB.set_fill(RED, 0.5)
        txt_2 = Tex(r"$2$", font_size=28, color=BLACK).\
            next_to(triangle_HKB.get_center_of_mass(), buff=0)
        self.play(
            Transform(triangle_MbHK, triangle_HKB),
            Write(txt_2),
            run_time=0.5
        )

        triangle_MbIH = Polygon(
            AH.get_center_of_mass(),
            CA.get_center_of_mass(),
            AB.get_center_of_mass(),
            stroke_width=0
        )
        triangle_MbIH.set_fill(RED, 0.5)
        txt_3 = Tex(r"$3$", font_size=28, color=BLACK).\
            next_to(triangle_MbIH.get_center_of_mass(), buff=0)
        self.play(
            Transform(triangle_MbHK, triangle_MbIH),
            Write(txt_3),
            run_time=0.5
        )

        triangle_IMcH = Polygon(
            AH.get_center_of_mass(),
            CA_copy.get_center_of_mass(),
            AB.get_center_of_mass(),
            stroke_width=0
        )
        triangle_IMcH.set_fill(RED, 0.5)
        txt_4 = Tex(r"$4$", font_size=28, color=BLACK).\
            next_to(triangle_IMcH.get_center_of_mass(), buff=0)
        self.play(
            Transform(triangle_MbHK, triangle_IMcH),
            Write(txt_4),
            run_time=0.5
        )

        triangle_McJH = Polygon(
            CA_copy.get_center_of_mass(),
            McMa.get_center_of_mass(),
            AB.get_center_of_mass(),
            stroke_width=0
        )
        triangle_McJH.set_fill(RED, 0.5)
        txt_5 = Tex(r"$5$", font_size=28, color=BLACK).\
            next_to(triangle_McJH.get_center_of_mass(), buff=0)
        self.play(
            Transform(triangle_MbHK, triangle_McJH),
            Write(txt_5),
            run_time=0.5
        )

        triangle_MaJH = Polygon(
            pB_copy.get_center_of_mass(),
            McMa.get_center_of_mass(),
            AB.get_center_of_mass(),
            stroke_width=0
        )
        triangle_MaJH.set_fill(RED, 0.5)
        txt_6 = Tex(r"$6$", font_size=28, color=BLACK).\
            next_to(triangle_MaJH.get_center_of_mass(), buff=0)
        self.play(
            Transform(triangle_MbHK, triangle_MaJH),
            Write(txt_6),
            run_time=0.5
        )

        self.play(FadeOut(triangle_MbHK), run_time=0.5)

        # Small triangles for the big triangle
        triangle_AMbI = Polygon(
            pA_copy.get_center_of_mass(),
            CA.get_center_of_mass(),
            AH.get_center_of_mass(),
            stroke_width=0
        )
        triangle_AMbI.set_fill(BLUE, 0.5)
        txt_1 = Tex(r"$1$", font_size=28, color=RED).\
            next_to(triangle_AMbI.get_center_of_mass(), buff=0)
        self.play(
            Create(triangle_AMbI),
            Write(txt_1),
            run_time=0.5
        )

        triangle_MbIH = Polygon(
            AH.get_center_of_mass(),
            CA.get_center_of_mass(),
            AB.get_center_of_mass(),
            stroke_width=0
        )
        triangle_MbIH.set_fill(BLUE, 0.5)
        txt_2 = Tex(r"$2$", font_size=28, color=RED).\
            next_to(triangle_MbIH.get_center_of_mass() + 0.2 * LEFT + 0.2 * UP, buff=0)
        self.play(
            Transform(triangle_AMbI, triangle_MbIH),
            Write(txt_2),
            run_time=0.5
        )

        triangle_MbHK = Polygon(
            CA.get_center_of_mass(),
            HK.get_center_of_mass(),
            AB.get_center_of_mass(),
            stroke_width=0
        )
        triangle_MbHK.set_fill(BLUE, 0.5)
        txt_3 = Tex(r"$3$", font_size=28, color=RED).\
            next_to(
                triangle_MbHK.get_center_of_mass() + 0.2 * RIGHT + 0.2 * DOWN, buff=0
            )
        self.play(
            Transform(triangle_AMbI, triangle_MbHK),
            Write(txt_3),
            run_time=0.5
        )

        triangle_HKB = Polygon(
            pB_copy.get_center_of_mass(),
            HK.get_center_of_mass(),
            AB.get_center_of_mass(),
            stroke_width=0
        )
        triangle_HKB.set_fill(BLUE, 0.5)
        txt_4 = Tex(r"$4$", font_size=28, color=RED).\
            next_to(triangle_HKB.get_center_of_mass() + 0.2 * LEFT + 0.2 * UP, buff=0)
        self.play(
            Transform(triangle_AMbI, triangle_HKB),
            Write(txt_4),
            run_time=0.5
        )

        triangle_MaKB = Polygon(
            pB_copy.get_center_of_mass(),
            BC.get_center_of_mass(),
            HK.get_center_of_mass(),
            stroke_width=0
        )
        triangle_MaKB.set_fill(BLUE, 0.5)
        txt_5 = Tex(r"$5$", font_size=28, color=RED).\
            next_to(triangle_MaKB.get_center_of_mass(), buff=0)
        self.play(
            Transform(triangle_AMbI, triangle_MaKB),
            Write(txt_5),
            run_time=0.5
        )

        triangle_MaKMb = Polygon(
            CA.get_center_of_mass(),
            BC.get_center_of_mass(),
            HK.get_center_of_mass(),
            stroke_width=0
        )
        triangle_MaKMb.set_fill(BLUE, 0.5)
        txt_6_2 = Tex(r"$6$", font_size=28, color=RED).\
            next_to(triangle_MaKMb.get_center_of_mass(), buff=0)
        self.play(
            Transform(triangle_AMbI, triangle_MaKMb),
            Write(txt_6_2),
            run_time=0.5
        )

        MbMa = Line(CA.get_center_of_mass(), BC.get_center_of_mass())
        triangle_CMbL = Polygon(
            CA.get_center_of_mass(),
            MbMa.get_center_of_mass(),
            pC.get_center_of_mass() + 1.5 * UP,
            stroke_width=0
        )
        triangle_CMbL.set_fill(BLUE, 0.5)
        txt_7 = Tex(r"$7$", font_size=28, color=RED).\
            next_to(triangle_CMbL.get_center_of_mass(), buff=0)
        self.play(
            Transform(triangle_AMbI, triangle_CMbL),
            Write(txt_7),
            run_time=0.5
        )

        triangle_CMaL = Polygon(
            MbMa.get_center_of_mass(),
            BC.get_center_of_mass(),
            pC.get_center_of_mass() + 1.5 * UP,
            stroke_width=0
        )
        triangle_CMaL.set_fill(BLUE, 0.5)
        txt_8 = Tex(r"$8$", font_size=28, color=RED).\
            next_to(triangle_CMaL.get_center_of_mass(), buff=0)
        self.play(
            Transform(triangle_AMbI, triangle_CMaL),
            Write(txt_8),
            run_time=0.5
        )

        self.play(FadeOut(triangle_AMbI), run_time=0.5)

        # Write results
        rect = RoundedRectangle(
            height=1, width=4,
            stroke_width=2,
            color=BLACK,
            fill_color=WHITE, fill_opacity=1
        ).move_to([0, -2.5, 0])
        txt = Tex(
            r"Aire $M_aM_bM_c = \frac{6}{8}$ Aire $ABC$",
            font_size=28, color=BLACK
        ).move_to([0, -2.5, 0])

        self.play(
            Create(rect),
            Write(txt)
        )
        self.wait(0.5)

        txt_2 = Tex(
            r"Aire $M_aM_bM_c = \frac{3}{4}$ Aire $ABC$",
            font_size=28, color=BLACK
        ).move_to([0, -2.5, 0])
        
        self.play(
            Transform(txt, txt_2),
        )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine, vol. 72,", font_size=30, color=BLACK),
            Tex(r"no. 2 (April 1999), p. 142", font_size=30, color=BLACK),
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