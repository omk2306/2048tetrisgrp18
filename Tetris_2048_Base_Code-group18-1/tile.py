import lib.stddraw as stddraw
from lib.color import Color
import random

class Tile:
    boundary_thickness = 0.001
    font_family, font_size = "Arial Black", 14

    def __init__(self):
        self.number = random.choice([2, 4])
        self.set_colors()

    def set_colors(self):
        if self.number == 2:
            self.background_color = Color(0, 255, 0)  # Green for 2
            self.foreground_color = Color(0, 0, 0)    # Black for number
            self.box_color = Color(0, 255, 0)         # Green for boundary
        elif self.number == 4:
            self.background_color = Color(255, 255, 0)  # Yellow for 4
            self.foreground_color = Color(0, 0, 0)      # Black for number
            self.box_color = Color(255, 255, 0)         # Yellow for boundary
        elif self.number == 8:
            self.background_color = Color(255, 0, 0)  # Red for 8
            self.foreground_color = Color(255, 255, 255)  # White for number
            self.box_color = Color(255, 0, 0)          # Red for boundary
        elif self.number == 16:
            self.background_color = Color(0, 0, 255)  # Blue for 16
            self.foreground_color = Color(255, 255, 255)  # White for number
            self.box_color = Color(0, 0, 255)          # Blue for boundary
        elif self.number == 32:
            self.background_color = Color(128, 0, 128)  # Purple for 32
            self.foreground_color = Color(255, 255, 255)  # White for number
            self.box_color = Color(128, 0, 128)          # Purple for boundary
        elif self.number == 64:
            self.background_color = Color(255, 165, 0)  # Orange for 64
            self.foreground_color = Color(255, 255, 255)  # White for number
            self.box_color = Color(255, 165, 0)          # Orange for boundary
        elif self.number == 128:
            self.background_color = Color(255, 192, 203)  # Pink for 128
            self.foreground_color = Color(255, 255, 255)  # White for number
            self.box_color = Color(255, 192, 203)          # Pink for boundary
        elif self.number == 256:
            self.background_color = Color(128, 0, 0)  # Maroon for 256
            self.foreground_color = Color(255, 255, 255)  # White for number
            self.box_color = Color(128, 0, 0)          # Maroon for boundary
        elif self.number == 512:
            self.background_color = Color(255, 215, 0)  # Gold for 512
            self.foreground_color = Color(255, 255, 255)  # White for number
            self.box_color = Color(255, 215, 0)          # Gold for boundary
        elif self.number == 1024:
            self.background_color = Color(0, 128, 128)  # Teal for 1024
            self.foreground_color = Color(255, 255, 255)  # White for number
            self.box_color = Color(0, 128, 128)          # Teal for boundary
        elif self.number == 2048:
            self.background_color = Color(128, 128, 0)  # Olive for 2048
            self.foreground_color = Color(255, 255, 255)  # White for number
            self.box_color = Color(128, 128, 0)          # Olive for boundary
        else:
            self.background_color = Color(151, 178, 199)  # Default background color
            self.foreground_color = Color(0, 100, 200)     # Default foreground color
            self.box_color = Color(0, 100, 200)           # Default box color

    def draw(self, position, length=1):
        stddraw.setPenColor(self.background_color)
        stddraw.filledSquare(position.x, position.y, length / 2)
        stddraw.setPenColor(self.box_color)
        stddraw.setPenRadius(Tile.boundary_thickness)
        stddraw.square(position.x, position.y, length / 2)
        stddraw.setPenRadius()
        stddraw.setPenColor(self.foreground_color)
        stddraw.setFontFamily(Tile.font_family)
        stddraw.setFontSize(Tile.font_size)
        stddraw.text(position.x, position.y, str(self.number))