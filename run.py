import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
from bboxFinder import bboxFinder
from editSubject import editImg
from transparent import convertImageBG
from subjectExtractor import subjectExtractor
from bgChanger import background_changer
from cropImage import cropImage
from main import pointillismEffect

imagePath = input('Enter the subject image path: ')
bgPath = input('Enter the background image path: ')

pos_w = int(input('Enter x position: '))
pos_h = int(input('Enter y position: '))

scale = float(input('Enter the scale factor (0.5 means half, 4 means four times): '))

def create_dir(path):
  if not os.path.exists(path):
    os.makedirs(path)

create_dir('results')

editImg(imagePath)
mask = subjectExtractor(f'results\subject-edited.png')
x,y,w,h = bboxFinder(imagePath)
cropImage(f'results\subject-segment.png', x, y, w, h)
pointillismEffect(f'results\subject-seg-crop.png', f'results\subject-painted.png')
convertImageBG(f'results\subject-painted.png', f'results\subject-transparent.png', mask, x, y, w, h)
background_changer(f'results\subject-transparent.png', bgPath, pos_w, pos_h, scale)