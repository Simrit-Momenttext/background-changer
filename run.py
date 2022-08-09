from bboxFinder import bboxFinder
from editSubject import editImg
from transparent import convertImageBG
from subjectExtractor import subjectExtractor
from bgChanger import background_changer
from cropImage import cropImage
from main import pointillismEffect
import os

pos_w = int(input('Enter x position: '))
pos_h = int(input('Enter y position: '))

scale = float(input('Enter the scale factor (0.5 means half, 4 means four times): '))

def create_dir(path):
  if not os.path.exists(path):
    os.makedirs(path)

""" Load the dataset """
imageList = os.listdir('images/subject/')
bgList = os.listdir('images/background/')

currPath = os.getcwd()
imagePath = os.path.join(currPath, f'images\subject\{imageList[0]}')
bgPath = os.path.join(currPath, f'images/background/{bgList[0]}')

""" Extracting name """
name = imageList[0].split("/")[-1].split(".")[0]

create_dir('remove_bg')

editImg(imagePath, name)
mask = subjectExtractor(f'remove_bg\{name}-edited.png', name)
x,y,w,h = bboxFinder(imagePath)
cropImage(f'remove_bg\{name}-segment.png', name, x, y, w, h)
pointillismEffect(f'remove_bg\{name}-seg-crop.png', f'remove_bg\{name}-painted.png')
convertImageBG(f'remove_bg\{name}-painted.png', f'remove_bg\{name}-transparent.png', mask, x, y, w, h)
background_changer(f'remove_bg\{name}-transparent.png', name, pos_w, pos_h, scale)