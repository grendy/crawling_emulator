# crawling_emulator
Crawling from emulator and use pytesseract to image processing
#Pyautogui for automation
Install pyautogui
```bash
pip install pyautogui
```
For automated click, must crop image and save it in same directory with source code
```bash
x,y = pyautogui.locateCenterOnScreen('friend.png')
pyautogui.click(x=x, y=y, clicks=1, interval=0, button='left')
time.sleep(1)
```
#Pytesseract library for image processing and convert image to string
Install pytesseract
```bash
pip install pytesseract
```
Crop the image that you want to convert to a string
```bash
pyautogui.screenshot(nama)
img = Image.open(nama)
img2 = img.crop((570, 374, 788, 410))
img2.save(nama)
varnum = pytesseract.image_to_string(Image.open(nama))
varnum = str(varnum)
print varnum
```
#Tools
Using genymotion emulator
