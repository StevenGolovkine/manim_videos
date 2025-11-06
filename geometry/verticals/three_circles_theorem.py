"""
Visual proof of A Constant Chord
Proofs without Words II. Roger B. Nelsen. p. 29.
"""
import numpy as np

from manim import MovingCameraScene
from manim import Create, Uncreate, Write, Transform, Group, ValueTracker
from manim import Polygon, VGroup, FadeIn, FadeOut, FunctionGraph
from manim import Text, Tex, RoundedRectangle, Circle, Line, Dot, Angle

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


def get_line(p1, p2):
    """
    Returns a line between two points.

    Args:
        p1: The first point as a Dot.
        p2: The second point as a Dot.
    """
    if not isinstance(p1, Dot) or not isinstance(p2, Dot):
        raise TypeError("Both p1 and p2 must be instances of Dot.")
    coords_p1 = p1.get_center()
    coords_p2 = p2.get_center()

    m = (coords_p2[1] - coords_p1[1]) / (coords_p2[0] - coords_p1[0])
    p = coords_p1[1] - m * coords_p1[0]

    new_p1 = np.array([-5, -5 * m + p, 0])
    new_p2 = np.array([5, 5 * m + p, 0])
    return Line(new_p1, new_p2, color=BLUE, stroke_width=2)

def get_intersection(line, circle, point):
    """
    Returns the intersection point of a line and a circle.

    Args:
        line: The line as a Line object.
        circle: The circle as a Circle object.
        point: On of the point where the line intersects the circle.

    """
    if not isinstance(line, Line) or not isinstance(circle, Circle):
        raise TypeError(
            "line must be an instance of Line and circle must be an",
            "instance of Circle."
        )
    
    # Get the equation of the line
    m = (line.get_end()[1] - line.get_start()[1]) / (line.get_end()[0] - line.get_start()[0])
    b = line.get_start()[1] - m * line.get_start()[0]

    # Get the equation of the circle
    r = circle.radius
    center = circle.get_center()
    h = center[0]
    k = center[1]

    # Solve for intersection points
    A = 1 + m**2
    B = 2 * (m * b - m * k - h)
    C = h**2 + (b - k)**2 - r**2

    discriminant = B**2 - 4 * A * C
    if discriminant < 0:
        return point

    x1 = (-B + np.sqrt(discriminant)) / (2 * A)
    y1 = m * x1 + b
    x2 = (-B - np.sqrt(discriminant)) / (2 * A)
    y2 = m * x2 + b
    if (
        np.abs(point.get_center()[0] - x1) < 0.1 and 
        np.abs(point.get_center()[1] - y1) < 0.1
    ):
        return Dot([x2, y2, 0], color=BLACK, radius=0.05)
    else:
        return Dot([x1, y1, 0], color=BLACK, radius=0.05)


class Circles(MovingCameraScene):
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
            Tex(r"Un théorème", font_size=48, color=BLACK),
            Tex(r"des trois cercles", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"R. S. Hu", font_size=28, color=BLACK)
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
        theorem = [
            Tex(r"Soit trois cercles, tracer les tangentes", font_size=20, color=BLACK),
            Tex(r"communes à chaque paire de cercles.", font_size=20, color=BLACK),
            Tex(r"Connecter leur points d'intersection", font_size=20, color=BLACK),
            Tex(r"avec le centre des autres cercles.", font_size=20, color=BLACK),
            Tex(r"Les trois segments obtenus sont concourrents.", font_size=20, color=BLACK),
        ]
        theorem = VGroup(*theorem)\
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)\
            .to_edge(0.75 * UP + 0.5 * LEFT)
        self.play(Write(theorem, run_time=4))

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"College Mathematics Journal,", font_size=30, color=BLACK),
            Tex(r"vol. 25, no.3,", font_size=30, color=BLACK),
            Tex(r"(May 1994), p.211.", font_size=30, color=BLACK),
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