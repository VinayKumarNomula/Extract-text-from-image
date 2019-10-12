# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 10:49:43 2019

@author: vinay
"""




import pytesseract
from PIL import Image


img = Image.open('vinay.jpg')
text=pytesseract.image_to_string(img)
print (text)

