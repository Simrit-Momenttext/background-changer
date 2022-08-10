import cv2
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

def editImg(imagePath):

  img = cv2.imread(imagePath, 1)
  # converting to LAB color space
  lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
  l_channel, a, b = cv2.split(lab)

  # Applying CLAHE to L-channel
  # feel free to try different values for the limit and grid size:
  clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
  cl = clahe.apply(l_channel)

  # merge the CLAHE enhanced L-channel with the a and b channel
  limg = cv2.merge((cl,a,b))

  # Converting image from LAB Color model to BGR color spcae
  enhanced_img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

  # Stacking the original image with the enhanced image
  result = np.hstack((img, enhanced_img))

  original = result.copy()
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convert image to HSV color space
  hsv = np.array(hsv, dtype = np.float64)
  hsv[:,:,1] = hsv[:,:,1]*2 # scale pixel values up for channel 1
  hsv[:,:,1][hsv[:,:,1]>255]  = 255
  hsv[:,:,2] = hsv[:,:,2]*1.5 # scale pixel values up for channel 2
  hsv[:,:,2][hsv[:,:,2]>255]  = 255
  hsv = np.array(hsv, dtype = np.uint8)
  imgnew = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # converting back to BGR used by OpenCV




  cv2.imwrite(f'results\subject-edited.png', imgnew)