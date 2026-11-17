import sys

import logging
from testing_config import epd7in5b_V2
import time
import traceback
from PIL import Image

# Setup the logger to show log messages from DEBUG level and higher
logging.basicConfig(level=logging.DEBUG)

logging.info("Starting the setup.")

my_display = epd7in5b_V2.EPD()

# Setup the communication and clear the display.
logging.info("Initializing (init and clear).")
my_display.init()
my_display.Clear()

himage_black = Image.open('black_picture.jpg').convert('1')
himage_red = Image.open('red_picture.jpg').convert('1')

# Check if the dimensions are right.
if himage_black.size != (800, 480) or himage_red.size != (800, 480):
    logging.warning("The image dimensions are not right. Resizing ...")
    himage_black = himage_black.resize((800, 480))
    himage_red = himage_red.resize((800, 480))

logging.info("Sending the image to the display...")
my_display.display(my_display.getbuffer(himage_black), my_display.getbuffer(himage_red))

logging.info("Display update done. Putting display to sleep...")
time.sleep(2)
my_display.sleep()