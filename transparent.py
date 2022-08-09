from PIL import Image
import os
import cv2
import numpy as np
from edge_smooth import contour_smooth

'''Transparent BG Image'''
def convertImageBG(imagePath, savePath, mask, x, y, w, h):

  contour_smooth(imagePath, f'remove_bg\smooth-edge.png', mask, x, y, w, h)

  img = Image.open(f'remove_bg\smooth-edge.png')

  img = img.convert("RGBA")
  
  data = img.getdata()
#   print(list(data))

  newData = []
  
  for item in data:
      if (item[0] <= 80 and item[1] >= 180 and item[2] <= 100 and item[3] >= 250):
          newData.append((255, 255, 255, 0))
      elif (item[0] == 255 and item[1] == 255 and item[2] == 255 and item[3] >= 250):
          newData.append((255, 255, 255, 0))
      else:
          newData.append(item)
  
  img.putdata(newData)
  img.save(savePath, "PNG")
  print("Transparent Segment Background Done")

  os.remove(f'remove_bg\smooth-edge.png')
  os.remove(imagePath)