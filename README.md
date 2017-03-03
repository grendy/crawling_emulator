# Crawling_emulator
Crawling from emulator and use pytesseract to image processing
#Pyautogui for automation
Install pyautogui
```bash
pip install pyautogui
```
Open Genymotion Emulator using os library
```bash
os.system("/opt/genymobile/genymotion/player --args --vm-name 7ac12b95-d01f-4e20-aa10-3766bd1d9e22")
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
```
Convert image to string
```bash
varnum = pytesseract.image_to_string(Image.open(nama))
varnum = str(varnum)
print varnum
```
#Tools
Using genymotion emulator

##Running engine
Open Genymotion
```bash
python2.7 lineapp.py
```
Automation and convert image to string
```bash
python2.7 click.py
```
