#!/usr/bin/env python3 
# pip3 install pyautogui

import time
import pyautogui

class Mouse:
  def move(self):
    pyautogui.moveTo(100, 100, duration =1)
    pyautogui.moveTo(200, 200, duration =1)
    pyautogui.moveTo(300, 300, duration =1)
    pyautogui.moveTo(400, 400, duration =1)
    time.sleep(2)

mouse = Mouse()
while True:
  mouse.move()
