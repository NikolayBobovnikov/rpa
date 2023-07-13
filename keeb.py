import subprocess
import pyautogui
import random
import time
import ctypes

# Launch Notepad++
vs_exe_path = r"C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe"
notepad_path = r'C:\Program Files\Notepad++\notepad++.exe'
project_path = r"C:\home\projects\SPORT v2\SPORTv2\SPORTv2.sln"
command = f'"{vs_exe_path}" "{project_path}"'
subprocess.Popen(command, shell=True)

# Wait for Notepad++ to open
pyautogui.sleep(40)


def get_caret_position():
    class CaretInfo(ctypes.Structure):
        _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

    info = CaretInfo()
    ctypes.windll.user32.GetCaretPos(ctypes.byref(info))
    return info.x, info.y


# Read text from file
file_path = "data/test.txt"  # Replace with the path to your text file
with open(file_path, 'r') as file:
    while True:
        counter = 0
        # Read each line in the file
        for line in file:
            counter = counter + 1
            interval = random.randint(10, 200) / 1000
            print(line.strip())  # strip() removes the newline character
            pyautogui.typewrite(line, interval=interval)
            pyautogui.press('enter')
            pyautogui.sleep(random.randint(100, 2000) / 1000)
            if counter == 10:
                caret_x, caret_y = get_caret_position()
                pyautogui.moveTo(caret_x, caret_y)
                pyautogui.sleep(random.randint(5, 100))
                pyautogui.scroll(3)  # Scroll three units up
                pyautogui.sleep(random.randint(5, 10))
                pyautogui.scroll(-3)  # Scroll three units down
                pyautogui.sleep(random.randint(5, 10))
                counter = 0

# Wait for a moment
pyautogui.sleep(1)

# Save the file
pyautogui.hotkey('ctrl', 's')

# Wait for the Save dialog to open
pyautogui.sleep(1)

# Press Enter to save the file
pyautogui.press('enter')
