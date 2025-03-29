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

# Make it square
SCALE_FACTOR = 1
config.pixel_height = 1080
config.pixel_width = 1080
# Change coord system dimensions
config.frame_height = 7
config.frame_width = 7


class Logo(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Créer le texte "ChillMath"
        text = Text(
            "chill.maths", font="CMU Typewriter Text", weight=LIGHT, color=BLACK
        ).move_to(ORIGIN)
        # Ajouter un élément mathématique, par exemple une sinusoïde
        sine_wave = FunctionGraph(
            lambda x: 0.1 * np.sin(2 * np.pi * x),
            x_range=[-5, 5],
            color=BLACK
        )
        sine_wave.next_to(text, DOWN, buff=0.2)
        
        # Animer l'apparition de la sinusoïde
        self.add(
            text, sine_wave
        )
