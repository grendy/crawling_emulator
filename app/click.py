import pyautogui
import time

time.sleep(75)
pyautogui.press('f11')
time.sleep(2)
pyautogui.click(x=599, y=307, clicks=1, interval=0, button='left')
time.sleep(15)
pyautogui.press(['right', 'right'])
time.sleep(1)
pyautogui.click(x=528, y=287, clicks=1, interval=0, button='left')
time.sleep(1)
pyautogui.click(x=868, y=134, clicks=1, interval=0, button='left')
time.sleep(1)
pyautogui.click(x=595, y=137, clicks=1, interval=0, button='left')
time.sleep(1)
pyautogui.click(x=540, y=222, clicks=1, interval=0, button='left')
time.sleep(1)
hp = ['85771467766','85795090951','8999483149']
for a in range(0,3):
    isi = hp[a]
    pyautogui.typewrite(isi)
    pyautogui.press('enter')
    time.sleep(3)

    pyautogui.click(x=681, y=340, clicks=1, interval=0, button='left')
    time.sleep(2)
    pyautogui.click(x=681, y=340, clicks=1, interval=0, button='left')
    time.sleep(7)
    pyautogui.screenshot(isi + '.png')
    time.sleep(1)
    pyautogui.click(x=549, y=739, clicks=1, interval=0, button='left')
    time.sleep(1)
    pyautogui.click(x=549, y=739, clicks=1, interval=0, button='left')
    time.sleep(1)
    pyautogui.click(x=833, y=251, clicks=1, interval=0, button='left')