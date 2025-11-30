"""
Visual proof of Triangular Numbers Modulo 3.
Proofs without Words II. Roger B. Nelsen. p. 96.
"""
import numpy as np

from manim import MovingCameraScene, Scene, ManimColor
from manim import Create, Uncreate, Write
from manim import Brace, VGroup, FadeIn, FadeOut, FunctionGraph, Rotate
from manim import Text, Tex, Rectangle, RoundedRectangle, Transform
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
            Tex(r"triangulaires", font_size=48, color=BLACK),
            Tex(r"modulo 3", font_size=48, color=BLACK),
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



        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Proofs without words II,", font_size=30, color=BLACK),
            Tex(r"Roger B. Nelsen (2000)", font_size=30, color=BLACK),
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