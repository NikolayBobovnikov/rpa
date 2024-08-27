import subprocess
import pyautogui
import random
import time
import ctypes

# Wait for Notepad++ to open
pyautogui.sleep(100)


def get_caret_position():
    
    class CaretInfo(ctypes.Structure):
        _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

    info = CaretInfo()
    ctypes.windll.user32.GetCaretPos(ctypes.byref(info))
    return info.x, info.y


while True:
    pyautogui.sleep(random.randint(100, 2000) / 1000)
    pyautogui.press('enter')
    pyautogui.sleep(random.randint(100, 2000) / 1000)
    pyautogui.press('esc')
