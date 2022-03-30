from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(714,600)[0] == 0:
        click(714,600)
    if pyautogui.pixel(780,600)[0] == 0:
        click(780,600)
    if pyautogui.pixel(879,600)[0] == 0:
        click(879,600)
    if pyautogui.pixel(974,600)[0] == 0:
        click(974,600)
    
    
        
