"""
Visual proof of the sums of odd integers.
Proofs without Words II. Roger B. Nelsen. p. 80.
"""
from manim import MovingCameraScene
from manim import Dot, Line, RoundedRectangle
from manim import Create, Uncreate, Write
from manim import VGroup, Transform
from manim import Tex, TexFontTemplates

from manim import config

from manim import LEFT, RIGHT, DOWN

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


class Young(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame.save_state()

        txt_copy = Tex(
            r"@Maths\&Chill", font_size=12,
            color=BLACK, tex_template=TexFontTemplates.droid_sans
        ).to_edge(RIGHT + DOWN, buff=0.1)
        self.add(txt_copy)

        # Introduction text
        txt_title = [
            Tex(r"Une inégalité d'aire", font_size=48, color=BLACK),
            Tex(r"Théorème de Young", font_size=48, color=BLACK)
        ]
        txt_title = VGroup(*txt_title).arrange(DOWN).move_to([0, 2, 0])

        txt = [
            Tex(r"Démonstration", font_size=36, color=BLACK),
            Tex(r"Young (1912)", font_size=28, color=BLACK)
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

