#nino.py

from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con
import pydirectinput
startou = 0

time.sleep(1)

def click( x, y):


    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(1)

while keyboard.is_pressed('q') == False:
    start = pyautogui.locateCenterOnScreen('skip.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.8)
    if start is not None:
        pyautogui.moveTo(start)
        pydirectinput.click()
        mouseDown()
        time.sleep(0.5)
        mouseUp()
        time.sleep(1)
        startou = startou + 1
        print(f'cliquei 1x')
    quest = pyautogui.locateCenterOnScreen('quest.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.8)
    if quest is not None:
        pyautogui.moveTo(quest)
        pydirectinput.click()
        mouseDown()
        time.sleep(0.5)
        mouseUp()
        time.sleep(1)
        print(f'cliquei 2x')
    aceitar = pyautogui.locateCenterOnScreen('aceitar.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.8)
    if aceitar is not None:
        pyautogui.moveTo(aceitar)
        pydirectinput.click()
        mouseDown()
        time.sleep(0.1)
        mouseUp()
        time.sleep(1)
        print(f'cliquei 3x')
    quest2 = pyautogui.locateCenterOnScreen('quest2.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.8)
    if quest2 is not None:
        pyautogui.moveTo(quest2)
        pydirectinput.click()
        mouseDown()
        time.sleep(0.1)
        mouseUp()
        time.sleep(1)
        print(f'cliquei 3x')
    questcomplete = pyautogui.locateCenterOnScreen('questcomplete.png', region=(0, 0, 1920, 1080), grayscale=True, confidence=0.8)
    if questcomplete is not None:
        pyautogui.moveTo(questcomplete)
        pydirectinput.click()
        mouseDown()
        time.sleep(0.1)
        mouseUp()
        time.sleep(1)
        print(f'cliquei questcomplete')
    main = pyautogui.locateCenterOnScreen('main.png', region=(0, 0, 1920, 1080), grayscale=True,
                                                   confidence=0.8)
    if main is not None:
        pyautogui.moveTo(main)
        pydirectinput.click()
        mouseDown()
        time.sleep(0.1)
        mouseUp()
        time.sleep(1)
        print(f'cliquei main')