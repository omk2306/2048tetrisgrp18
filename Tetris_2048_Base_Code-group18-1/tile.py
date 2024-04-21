import lib.stddraw as stddraw
from lib.color import Color
import random

class Tile:
    boundary_thickness = 0.001
    font_family, font_size = "Arial Black", 14

    def __init__(self):
        self.number = random.choice([2, 4])
        self.background_color = self.get_background_color()  # Set the background color based on the number
        self.foreground_color = Color(0, 100, 200)
        self.box_color = Color(0, 100, 200)

    def get_background_color(self):
        colors = {
            2: Color(255, 255, 255),        # White
            4: Color(255, 165, 0),          # Bright orange
            8: Color(255, 140, 0),          # Orange
            16: Color(255, 69, 0),          # Dark orange
            32: Color(255, 99, 71),         # Red-orange
            64: Color(255, 0, 0),           # Red
            128: Color(165, 42, 42)         # Brown
        }
        return colors.get(self.number, Color(151, 178, 199))  # Default color for other numbers

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