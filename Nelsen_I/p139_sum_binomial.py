"""
Visual proof of binomial sum.
Proofs without Words I. Roger B. Nelsen. p. 139.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write
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

        # Construct the triangle from its selected bottom row to its apex.
        self.play(FadeIn(symbolic_rows[last_row]), run_time=0.5)
        for row in range(last_row - 1, 3, -1):
            self.play(
                Create(row_arrows[row + 1]),
                FadeIn(symbolic_rows[row]),
                run_time=0.5
            )

        self.play(
            Create(row_arrows[4]),
            Create(continuation),
            FadeIn(numerical_rows[3], shift=0.04 * DOWN),
            run_time=0.5
        )
        for row in range(2, -1, -1):
            self.play(
                FadeIn(numerical_rows[row], shift=0.04 * DOWN),
                run_time=0.5
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

        self.play(Write(derivation), run_time=1.5)


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
