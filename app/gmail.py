from PIL import Image
img = Image.open('8999483149.png')
img2 = img.crop((470, 150, 912, 566))
img2.save('coy.png')

img = Image.open('85771467766_nama.png')
img2 = img.crop((570, 374, 780, 410))
img2.save('coy.png')