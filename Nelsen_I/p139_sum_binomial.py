"""
Visual proof of binomial sum.
Proofs without Words I. Roger B. Nelsen. p. 139.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Indicate, TransformMatchingTex, Uncreate, Write
from manim import Arrow, Axes, Circle, DashedLine, VGroup
from manim import FadeIn, FadeOut, FunctionGraph, Line, Polygon
from manim import Text, Tex, RoundedRectangle
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
            Tex(r"Une somme de", font_size=48, color=BLACK),
            Tex(r"binômes", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Dean S. Clark", font_size=28, color=BLACK)
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

        # The first four rows orient the construction in Pascal's triangle.
        x_step = 0.3
        triangle_y_shift = 1.0
        row_positions = {}
        row_nodes = {}
        numerical_rows = VGroup()
        pascal_values = (
            (1,),
            (1, 1),
            (1, 2, 1),
            (1, 3, 3, 1)
        )

        for row, values in enumerate(pascal_values):
            y = 2.25 - 0.32 * row + triangle_y_shift
            row_positions[row] = []
            row_nodes[row] = []
            displayed_row = VGroup()
            for column, value in enumerate(values):
                point = np.array([
                    (column - row / 2) * x_step,
                    y,
                    0
                ])
                number = Tex(str(value), font_size=17, color=BLACK)
                number.move_to(point)
                row_positions[row].append(point)
                row_nodes[row].append(number)
                displayed_row.add(number)
            numerical_rows.add(displayed_row)

        # Rows 4 through 12 display the repeating three-column pattern.
        # Positive row sums are filled; negative row sums are hollow.
        symbolic_rows = {}
        row_arrows = {}
        circle_radius = 0.052
        first_symbolic_y = 0.96
        symbolic_step = 0.34
        last_row = 12

        for row in range(4, last_row + 1):
            y = (
                first_symbolic_y
                - symbolic_step * (row - 4)
                + triangle_y_shift
            )
            row_positions[row] = []
            row_nodes[row] = []
            displayed_row = VGroup()

            for column in range(row + 1):
                point = np.array([
                    (column - row / 2) * x_step,
                    y,
                    0
                ])
                is_selected = column % 3 == 0
                is_positive_row = row % 2 == 1
                is_filled = (
                    is_selected if row == last_row else is_positive_row
                )
                node = Circle(
                    radius=circle_radius,
                    stroke_width=1.2,
                    stroke_color=BLACK,
                    fill_color=BLACK if is_filled else WHITE,
                    fill_opacity=1
                ).move_to(point)
                node.set_z_index(2)
                row_positions[row].append(point)
                row_nodes[row].append(node)
                displayed_row.add(node)

            if row < last_row:
                sign = "+" if row % 2 == 1 else "-"
                for column in range(row):
                    sign_mob = Tex(sign, font_size=12, color=BLACK)
                    sign_mob.move_to(
                        (row_positions[row][column]
                         + row_positions[row][column + 1]) / 2
                    )
                    sign_mob.set_z_index(2)
                    displayed_row.add(sign_mob)
                if sign == "-":
                    leading_sign = Tex("-", font_size=12, color=BLACK)
                    leading_sign.move_to(
                        row_positions[row][0] + 0.5 * x_step * LEFT
                    )
                    leading_sign.set_z_index(2)
                    displayed_row.add(leading_sign)

            symbolic_rows[row] = displayed_row

        # Dotted sides indicate that the same pattern continues for general n.
        continuation = VGroup(
            DashedLine(
                row_positions[3][0] + 0.08 * DOWN,
                row_positions[4][0] + 0.07 * UP,
                dash_length=0.035,
                dashed_ratio=0.55,
                stroke_width=1,
                color=BLACK
            ),
            DashedLine(
                row_positions[3][-1] + 0.08 * DOWN,
                row_positions[4][-1] + 0.07 * UP,
                dash_length=0.035,
                dashed_ratio=0.55,
                stroke_width=1,
                color=BLACK
            )
        )

        # At row r, the distinguished class is 12-r (mod 3).
        # Its two arrows are precisely the two summands in Pascal's rule.
        for row in range(4, last_row + 1):
            arrows = VGroup()
            selected_residue = (last_row - row) % 3
            for column in range(selected_residue, row + 1, 3):
                for parent_column in (column - 1, column):
                    if not 0 <= parent_column < row:
                        continue
                    arrow = Arrow(
                        row_positions[row][column] + 0.06 * UP,
                        row_positions[row - 1][parent_column] + 0.07 * DOWN,
                        buff=0,
                        stroke_width=0.9,
                        max_tip_length_to_length_ratio=0.24,
                        max_stroke_width_to_length_ratio=3,
                        color=BLACK
                    )
                    arrow.set_z_index(1)
                    arrows.add(arrow)
            row_arrows[row] = arrows

        bottom_label_y = row_positions[last_row][0][1] - 0.3
        bottom_labels = VGroup()
        for column, label in (
            (0, r"$\binom{3n}{0}$"),
            (3, r"$\binom{3n}{3}$"),
            (6, r"$\cdots$"),
            (9, r"$\binom{3n}{3n-3}$"),
            (12, r"$\binom{3n}{3n}$")
        ):
            coefficient = Tex(label, font_size=20, color=BLACK)
            coefficient.move_to([
                row_positions[last_row][column][0],
                bottom_label_y,
                0
            ])
            bottom_labels.add(coefficient)

        residue_colors = ("#C23B3B", BLUE, GREEN)

        def residue_rings(row, residue):
            rings = VGroup()
            for column in range(residue, row + 1, 3):
                ring = Circle(
                    radius=0.078,
                    stroke_width=1.8,
                    color=residue_colors[residue]
                )
                ring.move_to(row_positions[row][column])
                ring.set_z_index(3)
                rings.add(ring)
            return rings

        def proof_formula(tex, width=3.65, y=-2.2):
            formula = Tex(tex, font_size=22, color=BLACK)
            if formula.width > width:
                formula.scale_to_fit_width(width)
            formula.move_to([0, y, 0])
            return formula

        selection_formula = proof_formula(
            r"$S_{3n}(0)=\displaystyle\sum_{j=0}^{n}"
            r"\binom{3n}{3j}$"
        )

        cycle = VGroup(
            Tex(r"$r:$", font_size=15, color=BLACK),
            Tex(r"$0$", font_size=15, color=residue_colors[0]),
            Tex(r"$\longrightarrow$", font_size=15, color=BLACK),
            Tex(r"$1$", font_size=15, color=residue_colors[1]),
            Tex(r"$\longrightarrow$", font_size=15, color=BLACK),
            Tex(r"$2$", font_size=15, color=residue_colors[2]),
            Tex(r"$\longrightarrow 0\longrightarrow\cdots$",
                font_size=15, color=BLACK)
        ).arrange(RIGHT, buff=0.05)
        cycle.move_to([0, -2.9, 0])

        # Begin with the coefficients whose indices are multiples of three.
        self.play(
            FadeIn(symbolic_rows[last_row]),
            FadeIn(bottom_labels, shift=0.03 * UP),
            run_time=1
        )
        self.wait(0.5)
        active_rings = residue_rings(last_row, 0)
        proof_text = selection_formula
        self.play(
            Create(active_rings),
            Write(proof_text),
            run_time=1
        )
        self.wait(0.5)

        # The first V makes the two-parent form of Pascal's rule explicit.
        pascal_rule = proof_formula(
            r"$\displaystyle\binom{m}{k}="
            r"\binom{m-1}{k-1}+\binom{m-1}{k}$"
        )
        self.play(
            Create(row_arrows[last_row]),
            FadeIn(symbolic_rows[last_row - 1]),
            TransformMatchingTex(proof_text, pascal_rule),
            run_time=1
        )
        proof_text = pascal_rule
        self.wait(0.5)

        pascal_example = (
            row_nodes[last_row][3],
            row_nodes[last_row - 1][2],
            row_nodes[last_row - 1][3],
            row_arrows[last_row][1],
            row_arrows[last_row][2]
        )
        self.play(
            *[
                Indicate(mob, color=residue_colors[0], scale_factor=1.35)
                for mob in pascal_example
            ],
            run_time=1
        )

        recurrence = proof_formula(
            r"$\begin{aligned}"
            r"S_m(r)&=S_{m-1}(r-1)+S_{m-1}(r)\\"
            r"&=2^{m-1}-S_{m-1}(r+1)"
            r"\end{aligned}$",
            width=3.7,
            y=-2.25
        )
        next_rings = residue_rings(last_row - 1, 1)
        self.play(
            TransformMatchingTex(proof_text, recurrence),
            FadeOut(active_rings),
            FadeIn(next_rings),
            FadeIn(cycle),
            run_time=1
        )
        proof_text = recurrence
        active_rings = next_rings
        self.wait(1)

        expansion_1 = proof_formula(
            r"$S_{3n}(0)=2^{3n-1}-S_{3n-1}(1)$"
        )
        self.play(
            TransformMatchingTex(proof_text, expansion_1),
            run_time=1
        )
        proof_text = expansion_1
        self.wait(0.5)

        expansion_by_row = {
            10: proof_formula(
                r"$S_{3n}(0)=2^{3n-1}-2^{3n-2}"
                r"+S_{3n-2}(2)$"
            ),
            9: proof_formula(
                r"$S_{3n}(0)=2^{3n-1}-2^{3n-2}+2^{3n-3}"
                r"-S_{3n-3}(0)$"
            ),
            8: proof_formula(
                r"$S_{3n}(0)=2^{3n-1}-2^{3n-2}"
                r"+2^{3n-3}-\cdots$"
            )
        }

        # Continue upward; the rings show the cycle 1, 2, 0, ... .
        for row in range(last_row - 2, 3, -1):
            residue = (last_row - row) % 3
            next_rings = residue_rings(row, residue)
            animations = [
                Create(row_arrows[row + 1]),
                FadeIn(symbolic_rows[row]),
                FadeOut(active_rings),
                FadeIn(next_rings)
            ]
            if row in expansion_by_row:
                next_formula = expansion_by_row[row]
                animations.append(
                    TransformMatchingTex(proof_text, next_formula)
                )
                proof_text = next_formula
            self.play(*animations, run_time=1)
            self.wait(0.5)
            active_rings = next_rings

        top_rings = residue_rings(3, 0)
        self.play(
            Create(row_arrows[4]),
            Create(continuation),
            FadeIn(numerical_rows[3], shift=0.04 * DOWN),
            FadeOut(active_rings),
            FadeIn(top_rings),
            run_time=1
        )
        active_rings = top_rings
        for row in range(2, -1, -1):
            self.play(
                FadeIn(numerical_rows[row], shift=0.04 * DOWN),
                run_time=1
            )

        derivation = Tex(
            r"$\begin{aligned}"
            r"\displaystyle\sum_{j=0}^{n}\binom{3n}{3j}"
            r"&=\displaystyle\sum_{j=1}^{3n-1}"
            r"(-1)^{j-1}2^{3n-j}\\[0.08cm]"
            r"&=-2^{3n}\displaystyle\sum_{j=1}^{3n-1}"
            r"\left(-\frac12\right)^j\\[0.08cm]"
            r"&=\dfrac{8^n+2(-1)^n}{3}"
            r"\end{aligned}$",
            font_size=18,
            color=BLACK
        )
        derivation.scale_to_fit_width(3)
        derivation.to_edge(DOWN, buff=0.32)

        self.play(
            TransformMatchingTex(proof_text, derivation),
            FadeOut(cycle),
            FadeOut(active_rings),
            run_time=1.5
        )


        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine,", font_size=26, color=BLACK),
            Tex(r"vol. 63, no. 1 (Feb. 1990)", font_size=26, color=BLACK),
            Tex(r"p. 29.", font_size=26, color=BLACK)
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
