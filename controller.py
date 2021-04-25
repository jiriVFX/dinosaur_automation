import pyautogui
import PIL


class Controller:
    def open_game(self):
        """Opens the Chrome browser and starts the dinosaur game."""
        # Get the screen size
        screen_width = pyautogui.size()[0]
        screen_height = pyautogui.size()[1]

        # Move mouse to a specific position of chrome icon
        pyautogui.moveTo(710, 1060, duration=2, tween=pyautogui.easeInOutQuad)
        # Click to open Chrome
        pyautogui.click()
        pyautogui.click()

        # Move mouse to a Chrome address bar
        pyautogui.moveTo(510, 50, duration=2, tween=pyautogui.easeInOutQuad)

        # Make address bar active
        pyautogui.click()
        # Type a web address
        pyautogui.write("google.com", interval=0.15)
        pyautogui.press("enter")

    def jump(self):
        pyautogui.press("up")
