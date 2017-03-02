import pyautogui
import time
from PIL import Image
import pytesseract

pyautogui.hotkey('alt', 'tab')
x,y = pyautogui.locateCenterOnScreen('line.png')
pyautogui.click(x=x, y=y, clicks=1, interval=0, button='left')
time.sleep(7)
pyautogui.press('right')
time.sleep(2)
pyautogui.press('right')
time.sleep(1)
x,y = pyautogui.locateCenterOnScreen('friend.png')
pyautogui.click(x=x, y=y, clicks=1, interval=0, button='left')
time.sleep(1)
x,y = pyautogui.locateCenterOnScreen('phone.png')
pyautogui.click(x=x, y=y, clicks=1, interval=0, button='left')
time.sleep(1)
x1,y1 = pyautogui.locateCenterOnScreen('number.png')
pyautogui.click(x=x1, y=y1, clicks=1, interval=0, button='left')
time.sleep(1)
hp = ['81283146336','8999483149','8987469599','85795090951']#,,'8999483149','8987469599',] #'85222194301','85721747187','85771467766','87787019344',
for a in range(0,len(hp)):
    try:
        try:
            xd, yd = pyautogui.locateCenterOnScreen('exit.png')
            pyautogui.click(x=xd, y=yd, clicks=1, interval=0, button='left')
        except:pass
        isi = hp[a]
        nama = isi + '_nama.png'
        pp = isi + '_pp.png'
        pyautogui.typewrite(isi, interval=0.1)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(3)
        try:
            pyautogui.click(x=x1, y=int(y1 + 180), clicks=1, interval=0, button='left')
        except:
            try:
                xe, ye = pyautogui.locateCenterOnScreen('error.png')
                if xe != 0:
                    time.sleep(10800)
                    pyautogui.click(x=xe, y=ye, clicks=1, interval=0, button='left')
                    time.sleep(1)
                    pyautogui.click(x=xe, y=ye, clicks=1, interval=0, button='left')
                else:
                    break
            except:
                xd, yd = pyautogui.locateCenterOnScreen('exit.png')
                pyautogui.click(x=xd, y=yd, clicks=1, interval=0, button='left')
        time.sleep(1)
        pyautogui.screenshot(nama)
        img = Image.open(nama)
        img2 = img.crop((570, 374, 788, 410))
        img2.save(nama)
        varnum = pytesseract.image_to_string(Image.open(nama))
        varnum = str(varnum)
        print varnum
        time.sleep(5)
        if varnum != "user not found." or varnum != "User not found.":
            pass
        else:
            try:
                pyautogui.click(x=x1, y=int(y1 + 180), clicks=1, interval=0, button='left')
                time.sleep(8)
            except:pass
            pyautogui.screenshot(pp)
            img = Image.open(pp)
            img2 = img.crop((470, 150, 912, 566))
            img2.save(pp)
            time.sleep(1)
            for keluar in range(0,15):
                try:
                    xc,yc = pyautogui.locateCenterOnScreen('back.png')
                    break
                except:pass
            pyautogui.click(x=xc, y=yc, clicks=1, interval=0, button='left')
            time.sleep(1)
            try:
                xo, yo = pyautogui.locateCenterOnScreen('parameter.png')
            except:
                pyautogui.click(x=xc, y=yc, clicks=1, interval=0, button='left')
                time.sleep(1)
            xd,yd = pyautogui.locateCenterOnScreen('exit.png')
            pyautogui.click(x=xd, y=yd, clicks=1, interval=0, button='left')
    except:pass


