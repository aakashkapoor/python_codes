# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 18:23:34 2018

@author: Delol
"""

from PIL import Image

img = Image.open("sample.jpg").convert("L")
area = (0,0,160,204)
new_img = img.crop(area)
new_img = img.rotate(270)
new_img.thumbnail((75, 75))    


new_img.show()
