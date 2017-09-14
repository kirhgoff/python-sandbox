import pyautogui

x, y = pyautogui.locateCenterOnScreen('life.png')
pyautogui.click(x, y)

movements = ['W', 'D', 'S', 'A']
shoots = ['left', 'right', 'up', 'down']

for x in range(0, 3):
    for _ in range(15):
        pyautogui.press(movements[x])
        pyautogui.press(shoots[x])
