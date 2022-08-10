import cv2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
from PIL import Image

def cropImage(imagePath, x, y, w, h):
  img = cv2.imread(imagePath, cv2.IMREAD_COLOR)

  cv2.imwrite(f'results\subject-seg-crop.png', img[x:w, y:h])
  os.remove(imagePath)
  print('Segment Crop Done')
     
  image = Image.open(f'results\subject-seg-crop.png')
  
  data = image.getdata()
#   print(list(data))

  newData = []
  
  for item in data:
      if (item[0] <= 16 and item[1] <= 16 and item[2] <= 16):
          newData.append((0, 255, 0))
      else:
          newData.append(item)
  
  image.putdata(newData)
  image.save(f'results\subject-seg-crop.png', "PNG")
  print("Green screen Background Done")
