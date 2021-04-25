# dinosaur_automation
Bot that plays the chrome dino game.

https://youtu.be/LtdlVmYI54c

Simple bot built using PIL and PyAutoGUI libraries.

Make sure your internet connection is off before running the code.

The bot turns on the Chrome browser, types an address and starts playing the dino game.
The area of the screen with the dino game is being constantly captured and converted to pure black and white only colours (0 or 255) for easier night/day mode detection using the PIL library.
The bot is tuned to work on 1920x1080 display and may need code changes to work on different display resolutions.

I am getting mixed results with this bot, even after fine-tuning the detection pixels' coordinates.
The bot often does not recognize the night mode is on, especialy when not given enough time - meaning when onstacle is too close to the dino at the moment the day / night mode changes.
The results are often different with the same code, I suspect that is partially caused by variable frequence of capturing the screen with PIL library.
