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


class Chords(MovingCameraScene):
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
            Tex(r"Une corde", font_size=48, color=BLACK),
            Tex(r"constante", font_size=48, color=BLACK),
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Ross Honsberger", font_size=28, color=BLACK)
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

        # Circles
        big_circle = Circle(
            radius=1.5, color=BLACK, fill_color=WHITE, fill_opacity=0, stroke_width=2
        ).move_to([0, -0.5, 0])
        small_circle = Circle(
            radius=1.4, color=BLACK, fill_color=WHITE, fill_opacity=0, stroke_width=2
        ).move_to([0, 1, 0])

        self.play(
            Create(big_circle),
            Create(small_circle)
        )


        A = Dot([-1.24, 0.35, 0], color=BLACK, radius=0.05, stroke_width=2)
        B = Dot([1.24, 0.35, 0], color=BLACK, radius=0.05, stroke_width=2)
        txt_A = Tex(r"$A$", font_size=28, color=BLACK).next_to(
            A, LEFT, buff=0.2
        )
        txt_B = Tex(r"$B$", font_size=28, color=BLACK).next_to(
            B, RIGHT, buff=0.2
        )
        self.play(
            Create(A),
            Create(B),
            Write(txt_A),
            Write(txt_B)
        )

        # Points
        point_tracker = ValueTracker(0.1)
        P = Dot(
            small_circle.point_from_proportion(point_tracker.get_value()), color=BLACK,
            radius=0.05, stroke_width=2
        )
        txt_P = Tex(r"$P$", font_size=28, color=BLACK).next_to(P, UP + RIGHT, buff=0.1)
        self.play(
            Create(P),
            Write(txt_P)
        )
 
        # Lines
        line_AP = get_line(A, P)
        line_BP = get_line(B, P)
        self.play(
            Create(line_AP),
            Create(line_BP)
        )

        # Points that intersect lines and circles
        C = get_intersection(line_AP, big_circle, A)
        D = get_intersection(line_BP, big_circle, B)
        txt_C = Tex(r"$C$", font_size=20, color=BLACK).next_to(C, UP + LEFT, buff=0.1)
        txt_D = Tex(r"$D$", font_size=20, color=BLACK).next_to(D, UP + RIGHT, buff=0.1)
        self.play(
            Create(C),
            Create(D),
            Write(txt_C),
            Write(txt_D)
        )

        # Chord
        chord_CD = Line(C.get_center(), D.get_center(), color=RED, stroke_width=2)
        self.play(
            Create(chord_CD)
        )

        # Update
        P.add_updater(
            lambda x: x.become(P.copy().move_to(
                small_circle.point_from_proportion(point_tracker.get_value())
            ))
        )
        txt_P.add_updater(
            lambda x: x.become(txt_P.copy().next_to(
                P, UP + LEFT, buff=0.1
            ))
        )

        line_AP.add_updater(
            lambda x: x.become(get_line(A, P))
        )
        line_BP.add_updater(
            lambda x: x.become(get_line(B, P))
        )
        C.add_updater(
            lambda x: x.become(get_intersection(line_AP, big_circle, A))
        )
        txt_C.add_updater(
            lambda x: x.become(txt_C.copy().next_to(
                C, UP + LEFT, buff=0.1
            ))
        )
        D.add_updater(
            lambda x: x.become(get_intersection(line_BP, big_circle, B))
        )
        txt_D.add_updater(
            lambda x: x.become(txt_D.copy().next_to(
                D, UP + RIGHT, buff=0.1
            ))
        )
        chord_CD.add_updater(
            lambda x: x.become(
                Line(C.get_center(), D.get_center(), color=RED, stroke_width=2)
            )
        )

        self.play(
            point_tracker.animate.set_value(0.4),
            run_time=2
        )
        self.wait(1)
        self.play(
            point_tracker.animate.set_value(0.05),
            run_time=2
        )

        # C = get_intersection(line_AP, big_circle, A)
        # D = get_intersection(line_BP, big_circle, B)
        # self.play(Create(C), Create(D))
        

        # Finish
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

        # Logo
        ref = [
            Tex(r"Mathematical Morsels,", font_size=30, color=BLACK),
            Tex(r"The Mathematical Association", font_size=30, color=BLACK),
            Tex(r"of America, Washington,", font_size=30, color=BLACK),
            Tex(r"1978, pp. 126-127.", font_size=30, color=BLACK)
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