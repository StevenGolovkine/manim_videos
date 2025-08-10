"""
Visual proof of nonnegative integer solutions and triangular numbers
Proofs without Words III. Roger B. Nelsen. p. 166.
"""
import numpy as np

from manim import MovingCameraScene, Scene, ManimColor
from manim import Create, Uncreate, Write, Transform, TransformFromCopy
from manim import VGroup, FadeIn, FadeOut , FunctionGraph, Rotate
from manim import Line, Point, Polygon, RoundedRectangle, Circle, Angle
from manim import line_intersection, DashedLine, RightAngle
from manim import Text, Tex, Intersection, LaggedStart

from manim import config
from manim import ORIGIN, LEFT, RIGHT, DOWN, LIGHT, UP, PI, DEGREES

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

class DynamicTriangleCircles(Scene):
    def __init__(self, num_circles=10, **kwargs):
        self.num_circles = num_circles
        super().__init__(**kwargs)
    
    def get_triangular_positions(self, n, radius=0.3, spacing_factor=2.2):
        """
        Calculate positions for n circles arranged in triangular formation.
        Uses the triangular number pattern: 1, 3, 6, 10, 15, 21, ...
        """
        positions = []
        
        # Find how many complete rows we can make
        rows = 0
        total_in_complete_rows = 0
        while total_in_complete_rows + (rows + 1) <= n:
            rows += 1
            total_in_complete_rows += rows
        
        # Remaining circles for the incomplete row
        remaining = n - total_in_complete_rows
        
        # Calculate spacing
        circle_spacing = radius * spacing_factor
        
        # Start from the top and work down
        current_circle = 0
        
        for row in range(rows):
            circles_in_row = row + 1
            
            # Calculate y position (top to bottom)
            y_pos = (rows - 1 - row) * circle_spacing * np.sqrt(3) / 2
            
            # Calculate x positions for this row (centered)
            for col in range(circles_in_row):
                x_pos = (col - (circles_in_row - 1) / 2) * circle_spacing
                positions.append([x_pos, y_pos, 0])
                current_circle += 1
        
        # Add remaining circles in incomplete row
        if remaining > 0:
            y_pos = -circle_spacing * np.sqrt(3) / 2  # Below the last complete row
            for col in range(remaining):
                x_pos = (col - (remaining - 1) / 2) * circle_spacing
                positions.append([x_pos, y_pos, 0])
        
        return positions
    
    def construct(self):
        # Title showing number of circles
        title = Text(f"Triangular Arrangement: {self.num_circles} Circles", 
                    font_size=24).to_edge(UP)
        self.play(Write(title))
        
        # Get positions
        positions = self.get_triangular_positions(self.num_circles)
        
        # Create circles with gradient colors
        circles = VGroup()
        colors = self.generate_color_gradient(self.num_circles)
        
        for i, (pos, color) in enumerate(zip(positions, colors)):
            circle = Circle(radius=0.3, color=color, fill_opacity=0.7, stroke_width=2)
            circle.move_to(pos)
            
            # Add number label
            label = Text(str(i+1), font_size=16, color=WHITE)
            label.move_to(circle.get_center())
            
            circle_with_label = VGroup(circle, label)
            circles.add(circle_with_label)
        
        # Animate creation with wave effect
        self.play(LaggedStart(
            *[Create(circle) for circle in circles],
            lag_ratio=0.1
        ))
        
        self.wait(2)
        
        # Show triangle outline
        if len(positions) >= 3:
            triangle_outline = self.create_triangle_outline(positions)
            self.play(Create(triangle_outline))
            self.wait(1)
    
    def generate_color_gradient(self, n):
        """Generate a smooth color gradient for n circles"""
        colors = []
        for i in range(n):
            # Create a rainbow gradient
            hue = (i / n) * 360 if n > 1 else 0
            color = ManimColor.from_hsv([hue/360, 0.8, 0.9])
            colors.append(color)
        return colors
    
    def create_triangle_outline(self, positions):
        """Create an outline connecting the perimeter circles"""
        if len(positions) < 3:
            return VGroup()
        
        # Find perimeter points for triangle outline
        # Top point
        top_point = max(positions, key=lambda p: p[1])
        # Bottom left and right points
        bottom_points = [
            p for p in positions if abs(p[1] - min(pos[1] for pos in positions)) < 0.1
        ]
        left_point = min(bottom_points, key=lambda p: p[0])
        right_point = max(bottom_points, key=lambda p: p[0])
        
        triangle = Polygon(
            top_point, left_point, right_point, 
            color=YELLOW, stroke_width=3, fill_opacity=0
        )
        return triangle


class Proof(MovingCameraScene):
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
            Tex(r"Les solutions de", font_size=48, color=BLACK),
            Tex(r"$x + y + z = n$", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"M. Haines \& M. Jones", font_size=28, color=BLACK)
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

        # Write theorem
        theorem_1 = Tex(
            r"Soit $i, j$ et $k$ des entiers compris entre $0$ et $n$.",
            font_size=20, color=BLACK
        )
        theorem_1.to_edge(UP)
        theorem_2 = Tex(
            r"Le nombre de solutions non négatives et",
            font_size=20, color=BLACK
        )
        theorem_2.next_to(theorem_1, DOWN, aligned_edge=LEFT, buff=0.1)
        theorem_3 = Tex(
            r"entières de $x + y + z = n$ avec $x \leq i$,",
            font_size=20, color=BLACK
        )
        theorem_3.next_to(theorem_2, DOWN, aligned_edge=LEFT, buff=0.1)
        theorem_4 = Tex(
            r"$y \leq j$, $z \leq k$, est donné par",
            font_size=20, color=BLACK
        )
        theorem_4.next_to(theorem_3, DOWN, aligned_edge=LEFT, buff=0.1)
        theorem_5 = Tex(
            r"$T_{i + j + k - n + 1} - T_{i + j - n} - T_{i + k - n}$",
            r"$- T_{j + k - n}$,",
            font_size=20, color=BLACK
        )
        theorem_5.next_to(theorem_4, DOWN, aligned_edge=LEFT, buff=0.1)
        theorem_6 = Tex(
            r"où $T_n$ est le $n^{\text{e}}$ nombre triangulaire.",
            font_size=20, color=BLACK
        )
        theorem_6.next_to(theorem_5, DOWN, aligned_edge=LEFT, buff=0.1)
        self.play(
            Write(theorem_1),
            Write(theorem_2),
            Write(theorem_3),
            Write(theorem_4),
            Write(theorem_5),
            Write(theorem_6)
        )

        # Example
        txt_example = Tex(
            r"Exemple : $n = 23$, $i = 15$, $j = 11$, $k = 17$",
            font_size=20, color=BLACK
        ).next_to(theorem_6, DOWN, aligned_edge=LEFT, buff=0.1)
        self.play(
            Write(txt_example)
        )
        

        # Results for (n, i, j, k) = (23, 15, 11, 17)
        txt_sol = Tex(
            r"Ensemble des solutions de l'équation :",
            font_size=15, color=BLACK
        ).next_to(txt_example, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(
            Write(txt_sol),
        )

        n = 23 + 1
        n_circle = int(n * (n + 1) / 2)
        
        # Create triangle
        scene = DynamicTriangleCircles(n_circle)
        positions = scene.get_triangular_positions(
            n_circle, radius=0.05, spacing_factor=4
        )

        circles = VGroup()
        for j, pos in enumerate(positions):
            circle = Circle(
                radius=0.05,
                color=WHITE, fill_opacity=0.6,
                stroke_color=BLACK, stroke_width=1
            )
            circle.move_to([p * 0.7 for p in pos])  # Scale down
            circles.add(circle)
        
        circles.move_to([0, -0.75, 0])
        self.play(
            Create(circles),
        )

        txt_00n = Tex(r"$(0, 0, n)$", font_size=12, color=BLACK).\
            next_to(circles[0], UP, buff=0.1)
        txt_n00 = Tex(r"$(n, 0, 0)$", font_size=12, color=BLACK).\
            next_to(circles[-n], DOWN, buff=0.1)
        txt_0n0 = Tex(r"$(0, n, 0)$", font_size=12, color=BLACK).\
            next_to(circles[-1], DOWN, buff=0.1)
        self.play(
            Write(txt_00n),
            Write(txt_n00),
            Write(txt_0n0),
        )

        # Second triangle
        txt_sol_2 = Tex(
            r"Ensemble des solutions avec $x \leq i, y \leq j, z \leq k$ :",
            font_size=15, color=BLACK
        ).next_to(txt_example, DOWN, aligned_edge=LEFT, buff=0.4)

        n_2 = 21
        n_circle_2 = int(n_2 * (n_2 + 1) / 2)
        scene_2 = DynamicTriangleCircles(n_circle_2)
        positions_2 = scene_2.get_triangular_positions(
            n_circle_2, radius=0.05, spacing_factor=4
        )
        
        circles_2 = VGroup()
        for j, pos in enumerate(positions_2):
            circle = Circle(
                radius=0.05,
                color=WHITE, fill_opacity=0.6,
                stroke_color=BLACK, stroke_width=1
            )
            circle.move_to([p * 0.7 for p in pos])  # Scale down
            circles_2.add(circle)
        
        circles_2.rotate(PI).move_to(circles.get_center() - [0.29, 0.55, 0])
        self.play(
            Uncreate(txt_sol),
            Write(txt_sol_2),
            Create(circles_2),
        )

        txt_ik = Tex(r"$(i, n - i - k, k)$", font_size=12, color=BLACK).\
            next_to(circles_2[-1], UP, buff=0.1)
        txt_jk = Tex(r"$(n - j - k, j, k)$", font_size=12, color=BLACK).\
            next_to(circles_2[-n_2], UP, buff=0.1)
        txt_ij = Tex(r"$(i, j, n - i - j)$", font_size=12, color=BLACK).\
            next_to(circles_2[0], DOWN, buff=0.1)
        self.play(
            Write(txt_ik),
            Write(txt_jk),
            Write(txt_ij),
        )

        # Get the different circle
        A_x = circles_2[-1].get_center()
        B_x = circles_2[-9].get_center()
        C_x = circles_2[90].get_center()
        D_x = circles_2[-10].get_center()
        E_x = circles_2[77].get_center()

        A_y = circles_2[0].get_center()
        B_y = circles_2[3].get_center()
        C_y = circles_2[5].get_center()
        D_y = circles_2[6].get_center()
        E_y = circles_2[9].get_center()

        A_z = circles_2[-21].get_center()
        B_z = circles_2[-17].get_center()
        C_z = circles_2[-95].get_center()
        D_z = circles_2[-16].get_center()
        E_z = circles_2[-111].get_center()

        # Triangle T_{i + j - n}
        triangle_ijn = Polygon(
            A_y, B_y, C_y,
            color=BLUE, stroke_width=2, fill_opacity=0.9
        )
        txt_ijn = Tex(r"$T_{i + j - n}$", font_size=18, color=BLACK).\
            next_to(triangle_ijn.get_center(), RIGHT, buff=0.3)
        self.play(
            Create(triangle_ijn),
            Write(txt_ijn),
        )

        # Triangle T_{i + k - n}
        triangle_ikn = Polygon(
            A_x, B_x, C_x,
            color=RED, stroke_width=2, fill_opacity=0.9
        )
        txt_ikn = Tex(r"$T_{i + k - n}$", font_size=18, color=BLACK).\
            next_to(triangle_ikn.get_center(), LEFT, buff=0.3)
        self.play(
            Create(triangle_ikn),
            Write(txt_ikn)
        )

        # Triangle T_{j + k - n}
        triangle_jkn = Polygon(
            A_z, B_z, C_z,
            color=GREEN, stroke_width=2, fill_opacity=0.9
        )
        txt_jkn = Tex(r"$T_{j + k - n}$", font_size=18, color=BLACK).\
            next_to(triangle_jkn.get_center(), RIGHT, buff=0.3)
        self.play(
            Create(triangle_jkn),
            Write(txt_jkn)
        )

        # Polygon T_{i + j + k - n + 1}
        polygon = Polygon(
            D_x, E_x, E_y, D_y, E_z, D_z,
            color=YELLOW, stroke_width=2, fill_opacity=0.9
        )
        txt_polygon_1 = Tex(r"$T_{i + j + k - n + 1}$", font_size=18, color=BLACK)
        txt_polygon_2 = Tex(r"$- T_{i + j - n}$", font_size=18, color=BLACK)
        txt_polygon_3 = Tex(r"$- T_{i + k - n}$", font_size=18, color=BLACK)
        txt_polygon_4 = Tex(r"$- T_{j + k - n}$", font_size=18, color=BLACK)
        txt_polygon = VGroup(
            txt_polygon_1, txt_polygon_2, txt_polygon_3, txt_polygon_4
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to(polygon.get_center())
        self.play(
            Create(polygon),
            Write(txt_polygon),
        )

        # Lines
        # A_x = circles_2[0].get_center()
        # B_x = circles_2[-1].get_center()
        # AB_x = Line(A_x, B_x, color=BLACK, stroke_width=2)
        # txt_x = Tex(r"$x = i$", font_size=16, color=BLACK).\
        #     next_to(circles_2[-1], UP, buff=0.1)
        # self.play(
        #     Create(AB_x),
        #     Write(txt_x)
        # )

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematics Magazine,", font_size=30, color=BLACK),
            Tex(r"vol. 75, no. 5 (Dec. 2002),", font_size=30, color=BLACK),
            Tex(r"p. 388", font_size=30, color=BLACK),
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