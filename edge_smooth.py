import numpy as np
import cv2
from PIL import Image
import os

def contour_smooth(imgPath, savePath, mask, x, y, w, h):

  img = cv2.imread(imgPath)
  img2 = img
  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  img_trans = np.zeros_like(img_gray)
  trans_img = cv2.merge((img_trans, img_trans, img_trans))

  cv2.imwrite('trans.png', trans_img)

  image = Image.open('trans.png')

  image = image.convert("RGBA")

  data = image.getdata()

  newData = []

  for item in data:
    newData.append((255, 255, 255, 0))

  image.putdata(newData)
  image.save('trans.png', "PNG")

  transparent = cv2.imread('trans.png')

  mask = mask[x:w, y:h]

  mask_show = mask * 255

  mask_show = np.uint8(mask_show)

  contours, _ = cv2.findContours(mask_show,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

  cv2.drawContours(img2, contours, -1, (255,255,255),5)

  output = np.where(img2==np.array([255, 255, 255]), transparent, img)

  cv2.imwrite(savePath, output)

  os.remove('trans.png')