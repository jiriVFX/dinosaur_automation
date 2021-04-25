from controller import Controller
from screen_reader import ScreenReader
import time

if __name__ == "__main__":
    # Works for 1920x1080 screen size
    # Create Controller object
    controller = Controller()
    # Create ScreenReader object
    screen_reader = ScreenReader()

    # Open the game
    controller.open_game()

    # Start the game loop ----------------------------------------------------------------------------------------------

    time.sleep(0.5)
    controller.jump()

    time.sleep(1)
    screen_reader.capture_screen()

    while True:
        screen_reader.capture_screen()

        if screen_reader.detect_obstacle():
            controller.jump()
            print("JUMP")
