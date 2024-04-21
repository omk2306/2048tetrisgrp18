import lib.stddraw as stddraw
from lib.color import Color
import random

class Tile:
    boundary_thickness = 0.008
    font_family, font_size = "Arial Black", 14

    def __init__(self):
        self.number = random.choice([2, 4])
        self.set_colors()

    def set_colors(self):
        if self.number == 2:
            self.background_color = Color(0, 255, 0)
            self.foreground_color = Color(0, 0, 0)
            self.box_color = Color(0, 150, 0)
        elif self.number == 4:
            self.background_color = Color(255, 255, 0)
            self.foreground_color = Color(0, 0, 0)
            self.box_color = Color(200, 200, 0)
        elif self.number == 8:
            self.background_color = Color(255, 0, 0)
            self.foreground_color = Color(255, 255, 255)
            self.box_color = Color(150, 0, 0)
        elif self.number == 16:
            self.background_color = Color(0, 0, 255)
            self.foreground_color = Color(255, 255, 255)
            self.box_color = Color(0, 0, 150)
        elif self.number == 32:
            self.background_color = Color(128, 0, 128)
            self.foreground_color = Color(255, 255, 255)
            self.box_color = Color(75, 0, 75)  # Darker
        elif self.number == 64:
            self.background_color = Color(255, 165, 0)
            self.foreground_color = Color(255, 255, 255)
            self.box_color = Color(200, 120, 0)
        elif self.number == 128:
            self.background_color = Color(255, 192, 203)
            self.foreground_color = Color(255, 255, 255)
            self.box_color = Color(200, 100, 120)
        elif self.number == 256:
            self.background_color = Color(128, 0, 0)
            self.foreground_color = Color(255, 255, 255)
            self.box_color = Color(75, 0, 0)
        elif self.number == 512:
            self.background_color = Color(255, 215, 0)
            self.foreground_color = Color(255, 255, 255)
            self.box_color = Color(200, 160, 0)
        elif self.number == 1024:
            self.background_color = Color(0, 128, 128)
            self.foreground_color = Color(255, 255, 255)
            self.box_color = Color(0, 100, 100)
        elif self.number == 2048:
            self.background_color = Color(128, 128, 0)
            self.foreground_color = Color(255, 255, 255)
            self.box_color = Color(100, 100, 0)
        


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