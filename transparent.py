from PIL import Image
import os
import cv2
import numpy as np

def contour_smooth(imgPath, savePath):

  img = cv2.imread(imgPath)

  blurred_img = cv2.GaussianBlur(img, (21, 21), 0)
  mask = np.zeros(img.shape, np.uint8)

  gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
  ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
  contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  cv2.drawContours(mask, contours, -1, (255,255,255),5)
  output = np.where(mask==np.array([255, 255, 255]), blurred_img, img)

  print('Edge Smoothening Done')

  os.remove(imgPath)
  
  cv2.imwrite(savePath, output)


'''Transparent BG Image'''
def convertImageBG(imagePath, savePath):

  img = Image.open(imagePath)

  img = img.convert("RGBA")
  
  data = img.getdata()
#   print(list(data))

  newData = []
  
  for item in data:
      if (item[0] <= 80 and item[1] >= 180 and item[2] <= 100 and item[3] >= 250):
          newData.append((255, 255, 255, 0))
      else:
          newData.append(item)
  
  img.putdata(newData)
  img.save(savePath, "PNG")

  contour_smooth(savePath, f'remove_bg\smooth-edge.png')

  img = Image.open(f'remove_bg\smooth-edge.png')

  img = img.convert("RGBA")
  
  data = img.getdata()
#   print(list(data))

  newData = []
  
  for item in data:
      if (item[0] >= 250 and item[1] >= 250 and item[2] >= 250 and item[3] >= 250):
          newData.append((255, 255, 255, 0))
      else:
          newData.append(item)
  
  img.putdata(newData)
  img.save(savePath, "PNG")
  print("Transparent Segment Background Done")

  os.remove(f'remove_bg\smooth-edge.png')