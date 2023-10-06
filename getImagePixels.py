from PIL import Image

img = Image.open('TestingPictures/Eric_WhiteBG.jpg')
thresh = 105
fn = lambda x: 255 if x > thresh else 0
r = img.convert('L').point(fn, mode='1')
r.save('TestingPictures/new_BW.png')
"""
new_BW = Image.open("TestingPictures/new_BW.png")


img = Image.open("TestingPictures/new_BW.png")

img.resize((50, 75))

img.save("TestingPictures/reSized.png")
"""