"""
Visual proof of Sums of Squares II
Proofs without Words I. Roger B. Nelsen. p. 78.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Dot, BraceBetweenPoints, RoundedRectangle, Square, Rectangle
from manim import Create, Uncreate, Write
from manim import VGroup, TransformFromCopy, FadeIn, FadeOut, FunctionGraph
from manim import Text, Tex, MathTex

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

class Sums(MovingCameraScene):
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
            Tex(r"Somme des carrés", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"M. Gardner \& D. Kalman", font_size=28, color=BLACK)
        ]
        txt = VGroup(*txt).arrange(DOWN)

        txt_formula = Tex(
            r"$3(1^2 + 2^2 + \cdots + n^2) = (2n+1)(1 + 2 + \cdots + n)$", 
            font_size=18, color=BLACK
        ).next_to(txt, 2 * DOWN)

        self.add(
            txt_title,
            txt,
            txt_formula
        )
        self.wait(1)
        self.play(
            Uncreate(txt_title),
            Uncreate(txt),
            Uncreate(txt_formula),
            run_time=0.5
        )
        self.wait(0.5)

        n = 5
        small_cell_size = 0.18
        grid_cell_size = 0.215
        layer_colors = {
            1: BLUE,
            2: ORANGE,
            3: GREEN,
            4: YELLOW,
            5: VIOLET,
        }

        def colored_cell(side_length, color, stroke_width=1.0):
            return Square(
                side_length=side_length,
                color=BLACK,
                stroke_width=stroke_width,
                fill_color=color,
                fill_opacity=0.82,
            )

        def nested_square(order):
            cells = VGroup()
            layers = {k: VGroup() for k in range(1, order + 1)}

            for row in range(order):
                for column in range(order):
                    # The preceding square sits in the upper-right corner.
                    layer = max(order - column, row + 1)
                    cell = colored_cell(
                        small_cell_size,
                        layer_colors[layer],
                        stroke_width=0.9,
                    ).move_to([
                        (column - (order - 1) / 2) * small_cell_size,
                        ((order - 1) / 2 - row) * small_cell_size,
                        0,
                    ])
                    cells.add(cell)
                    layers[layer].add(cell)

            outline = Square(
                side_length=order * small_cell_size,
                color=BLACK,
                stroke_width=2.0,
            )
            return VGroup(cells, outline), layers

        left_squares = []
        layer_cells = {k: [] for k in range(1, n + 1)}
        for order in range(1, n + 1):
            square, layers = nested_square(order)
            left_squares.append(square)
            for layer, cells in layers.items():
                layer_cells[layer].extend(cells)

        left_column = VGroup(*left_squares).arrange(DOWN, buff=0.24)
        left_column.move_to([-1.63, -0.24, 0])
        source_layers = {
            layer: VGroup(*cells)
            for layer, cells in layer_cells.items()
        }

        rows = n * (n + 1) // 2
        columns = 2 * n + 1
        grid_center = np.array([0.72, -0.27, 0])
        grid_left = grid_center[0] - columns * grid_cell_size / 2
        grid_top = grid_center[1] + rows * grid_cell_size / 2

        def grid_position(row, column):
            return np.array([
                grid_left + (column + 0.5) * grid_cell_size,
                grid_top - (row + 0.5) * grid_cell_size,
                0,
            ])

        base_grid = VGroup()
        for row in range(rows):
            for column in range(columns):
                base_grid.add(
                    Square(
                        side_length=grid_cell_size,
                        color=BLACK,
                        stroke_width=0.65,
                        fill_color=WHITE,
                        fill_opacity=0.12,
                    ).move_to(grid_position(row, column))
                )

        target_blocks = {}
        block_outlines = VGroup()
        side_square_outlines = VGroup()
        row_start = 0
        for layer in range(1, n + 1):
            block_height = n - layer + 1
            block_width = 2 * layer - 1
            column_start = (columns - block_width) // 2
            block_cells = VGroup()

            for local_row in range(block_height):
                for local_column in range(block_width):
                    block_cells.add(
                        colored_cell(
                            grid_cell_size,
                            layer_colors[layer],
                            stroke_width=0.8,
                        ).move_to(grid_position(
                            row_start + local_row,
                            column_start + local_column,
                        ))
                    )

            target_blocks[layer] = block_cells
            block_center = np.mean(
                [mob.get_center() for mob in block_cells], axis=0
            )
            block_outlines.add(
                Rectangle(
                    width=block_width * grid_cell_size,
                    height=block_height * grid_cell_size,
                    color=BLACK,
                    stroke_width=2.1,
                ).move_to(block_center)
            )

            # Each uncolored side of this band is a square of the same height.
            left_square_center = np.mean([
                grid_position(row_start, 0),
                grid_position(
                    row_start + block_height - 1,
                    block_height - 1,
                ),
            ], axis=0)
            right_square_center = np.mean([
                grid_position(row_start, columns - block_height),
                grid_position(
                    row_start + block_height - 1,
                    columns - 1,
                ),
            ], axis=0)
            for square_center in (left_square_center, right_square_center):
                side_square_outlines.add(
                    Square(
                        side_length=block_height * grid_cell_size,
                        color=BLACK,
                        stroke_width=1.45,
                    ).move_to(square_center)
                )

            row_start += block_height

        outer_grid = Rectangle(
            width=columns * grid_cell_size,
            height=rows * grid_cell_size,
            color=BLACK,
            stroke_width=2.5,
        ).move_to(grid_center)
        height_label = MathTex(
            r"1+2+\cdots+n", font_size=22, color=BLACK
        ).rotate(PI / 2).next_to(outer_grid, LEFT, buff=0.10)
        width_label = MathTex(
            r"2n+1", font_size=22, color=BLACK
        ).next_to(outer_grid, DOWN, buff=0.10)

        construction = VGroup(
            left_column,
            base_grid,
            outer_grid,
            side_square_outlines,
            block_outlines,
            height_label,
            width_label,
            *target_blocks.values(),
        )
        construction.shift(0.75 * UP)

        for square in left_squares:
            self.play(FadeIn(square, shift=0.08 * UP), run_time=0.35)

        self.play(
            Create(base_grid),
            Create(outer_grid),
            FadeIn(side_square_outlines),
            Write(height_label),
            Write(width_label),
            run_time=2,
        )

        for layer in range(1, n + 1):
            self.play(
                TransformFromCopy(source_layers[layer], target_blocks[layer]),
                Create(block_outlines[layer - 1]),
                run_time=0.8,
            )

        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Scientic American, vol. 229, ", font_size=30, color=BLACK),
            Tex(r"no. 4 (Oct. 1973), p.115.", font_size=30, color=BLACK),
            Tex(r"College Mathematics Journal,", font_size=30, color=BLACK),
            Tex(r"vol. 22, no. 3 (May 1991),", font_size=30, color=BLACK),
            Tex(r"p.124.", font_size=30, color=BLACK)
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
