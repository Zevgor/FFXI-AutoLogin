# Get requirements:
# pip install keyboard pywinauto
from dotenv import load_dotenv
import os

# You can wrap this script up as a Windows shortcut:
# Have python.exe in your PATH
# - Make a new shortcut, target: python.exe C:\FFXI\autologin\autologin.py
# - Shortcut Properties > Advanced > Run as administrator

load_dotenv()

# Change these:
your_password = os.getenv('SQX_PASSWORD')
windower_launch_param = r'C:\Program Files (x86)\PlayOnline\SquareEnix\Windower\Windower.exe --p Default Profile'
windower_dir = r'C:\Program Files (x86)\PlayOnline\SquareEnix\Windower'

# ==================================================================
import time
from pywinauto.application import Application
import keyboard

print('> Opening Windower + POL')
app = Application().start(windower_launch_param, work_dir=windower_dir)
time.sleep(15)

print('> Selecting Account')
keyboard.press_and_release('enter')
time.sleep(1)

print('> Selecting Account')
keyboard.press_and_release('enter')
time.sleep(1)

print('> Confirming Account')
keyboard.press_and_release('enter')
time.sleep(1)

print('> Selecting Password Box')
keyboard.press_and_release('enter')
time.sleep(1)

print('> Selecting Password Text Entry Box')
keyboard.press_and_release('up')
keyboard.press_and_release('right')
keyboard.press_and_release('right')
keyboard.press_and_release('enter')
time.sleep(1)

print('> Entering password')
keyboard.write(your_password)
keyboard.press_and_release('enter')
time.sleep(3)

print('> Logging into POL, waiting...')
keyboard.press_and_release('down')
keyboard.press_and_release('enter')
time.sleep(30)

print('> Opening FFXI game menu, waiting...')
keyboard.press_and_release('enter')
time.sleep(15)

print('> Logging into FFXI, waiting...')
keyboard.press_and_release('enter')
time.sleep(1)
keyboard.press_and_release('enter')
time.sleep(1)
keyboard.press_and_release('enter')
time.sleep(15)

print('> Logging into FFXI main screen, waiting...')
keyboard.press_and_release('enter')
time.sleep(10)

print('> Logging into FFXI character')
keyboard.press_and_release('enter')
time.sleep(3)
keyboard.press_and_release('enter')
time.sleep(1)
keyboard.press_and_release('enter')
time.sleep(1)
keyboard.press_and_release('enter')
time.sleep(1)
