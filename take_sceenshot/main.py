print("---------SCREENSHOT TAKER---------")

import pyautogui
import time
import os

class ScreenshotTaker:
    pass 

save_folder = input("Enter the folder path where screenshots will be saved: ")
if not os.path.exists(save_folder):
    os.makedirs(save_folder)
    
time_interval = input("Enter the interval (in seconds) between screenshots: ")
interval = float(time_interval)
