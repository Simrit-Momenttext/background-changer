import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import tensorflow as tf
from tensorflow.keras.utils import CustomObjectScope
from metrics import dice_loss, dice_coef, iou
import cv2
import numpy as np

""" Global parameters """
H = 512
W = 512

""" Loading model: DeepLabV3+ """
def subjectExtractor(imagePath, name):
  with CustomObjectScope({'iou': iou, 'dice_coef': dice_coef, 'dice_loss': dice_loss}):
    model = tf.keras.models.load_model("deeplab-model.h5")

  image = cv2.imread(imagePath, cv2.IMREAD_COLOR)
  h, w, _ = image.shape
  x = cv2.resize(image, (W, H))
  x = x/255.0
  x = x.astype(np.float32)
  x = np.expand_dims(x, axis=0)

  # """ Prediction """
  y = model.predict(x)[0]
  y = cv2.resize(y, (w, h))
  y = np.expand_dims(y, axis=-1)
  y = y > 0.5

  photo_mask = y
  masked_photo = image * photo_mask
  cv2.imwrite(f'remove_bg\{name}-segment.png', masked_photo)
  os.remove(imagePath)
  print('Segment Extraction Done')
  return photo_mask