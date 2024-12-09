"""
Animation logo
"""
import numpy as np

from manim import Scene
from manim import Create
from manim import Text, FadeIn
from manim import FunctionGraph

from manim import config, ORIGIN
from manim import DOWN, LIGHT

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


class Logo(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Créer le texte "ChillMath"
        text = Text(
            "chillmath", font="CMU Typewriter Text", weight=LIGHT, color=BLACK
        ).move_to(ORIGIN)
        # Ajouter un élément mathématique, par exemple une sinusoïde
        sine_wave = FunctionGraph(
            lambda x: 0.1 * np.sin(2 * np.pi * x),
            x_range=[-3, 3],
            color=BLACK
        )
        sine_wave.next_to(text, DOWN, buff=0.2)
        
        # Animer l'apparition de la sinusoïde
        self.play(
            FadeIn(text, scale=0.5),
            Create(sine_wave),
            run_time=2
        )

        self.wait(1)
