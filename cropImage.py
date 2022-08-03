import cv2
import os
from PIL import Image

def cropImage(imagePath, name, x, y, w, h):
  img = cv2.imread(imagePath, cv2.IMREAD_COLOR)

  cv2.imwrite(f'remove_bg\{name}-seg-crop.png', img[x:w, y:h])
  os.remove(imagePath)
  print('Segment Crop Done')
     
  image = Image.open(f'remove_bg\{name}-seg-crop.png')
  
  data = image.getdata()
#   print(list(data))

  newData = []
  
  for item in data:
      if (item[0] <= 10 and item[1] <= 10 and item[2] <= 10):
          newData.append((0, 255, 0))
      else:
          newData.append(item)
  
  image.putdata(newData)
  image.save(f'remove_bg\{name}-seg-crop.png', "PNG")
  print("Transparent Segment Background Done")
