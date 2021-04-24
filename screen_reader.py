from PIL import ImageGrab
from datetime import datetime
from constants import *


class ScreenReader:
    def __init__(self):
        self.screen_grab = None
        self.pixels = ()
        self.obstacle_colour = BLACK

    def capture_screen(self):
        # convert screenshot to monochrome
        self.screen_grab = ImageGrab.grab(bbox=(630, 80, 1280, 280))
        # Convert all pixels to 255 or 0
        # Threshold must be 171 as obstacles in night mode are 172 in greyscale or (172, 172, 172) in RGB
        black_n_white = lambda x: 255 if x > THRESHOLD else 0
        self.screen_grab = self.screen_grab.convert("L").point(black_n_white, mode="1")

        # load image pixels for access per pixel
        self.pixels = self.screen_grab.load()

        # self.pixels[POS_MODE[0], POS_MODE[1]] = 0
        # for position in POS:
        #     self.pixels[position[0], position[1]] = 0
        #
        # file_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # datetime.now()
        # self.screen_grab.save(f"screengrab{file_name}.png")

    def detect_obstacle(self):
        """Detects Day / Night modes and obstacles.
        When obstacle is detected returns True, otherwise returns False.
        :rtype: bool"""
        # Dinosaur and obstacles colour during the day mode - (83, 83, 83)
        # Dinosaur and obstacles colour during the night mode - (172, 172, 172)

        # If any of the pixels in day mode gets dark -> jump
        # If all pixels are dark, night mode is on
        # If all pixels are light, day mode is on

        # Check mode detection pixel
        if self.pixels[POS_MODE[0], POS_MODE[1]] == self.obstacle_colour:
            # Day / Night mode has been changed
            if self.obstacle_colour == WHITE:
                self.obstacle_colour = BLACK
                #self.obstacle_colour = GREY
                print("Day mode is on.")
            else:
                self.obstacle_colour = WHITE
                print("Night mode is on.")

        for position in POS:
            # print(self.pixels[position[0], position[1]])
            if self.pixels[position[0], position[1]] == self.obstacle_colour:
                print(f"Pixel = {self.obstacle_colour}")
                # if obstacle was detected, return True
                return True
        # Otherwise return False
        return False

        # self.screen_grab.save("screengrab.png")
        # self.screen_grab.show()
