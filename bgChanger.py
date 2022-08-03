import os
import cv2
import cvzone
from inputValidity import validInput

def background_changer(subjectPath, name, pos_w, pos_h, scale):

    bgList = os.listdir('images/background/')

    ''' The background '''
    for bgs in bgList:
        bg_image = cv2.imread(f'images/background/{bgs}', cv2.IMREAD_COLOR)
        bg_h, bg_w, _ = bg_image.shape
        bg_name = bgs.split(".")[0]
        subject_image = cv2.imread(subjectPath, cv2.IMREAD_UNCHANGED)
        sub_h, sub_w, _ = subject_image.shape

        os.remove(subjectPath)
        
        valid = validInput(pos_w, pos_h, scale, bg_w, bg_h, sub_w, sub_h)

        if not valid:
            print('Invalid Input! Default parameters applied.')
            ratio = round(bg_h / sub_h)
            if ratio > 4 or ratio < 2:
                scaling = round((bg_h/2)/sub_h, 1)
                subject_image = cv2.resize(subject_image, None, fx= scaling, fy= scaling, interpolation= cv2.INTER_LINEAR)
                sub_h, sub_w, _ = subject_image.shape
            # finalSubject = segment_style(subject_image, bg_image)
            # res = cv2.seamlessClone(subject_image, bg_image, mask, [bg_w - sub_w, bg_h - sub_h], cv2.NORMAL_CLONE)
            res = cvzone.overlayPNG(bg_image, subject_image, [bg_w - sub_w, bg_h - sub_h])
            # bg_image_copy = bg_image
            # bg_image_copy = cv2.cvtColor(bg_image_copy, cv2.COLOR_BGR2BGRA)
            # bg_part = bg_image_copy[pos_h: sub_h, pos_w:sub_w]
            # print('Subject: ', subject_image.shape)
            # print('BG Part: ', bg_part.shape)
            # res = cv2.addWeighted(subject_image, 0.9, bg_part, 0.1, 0.2)
            # bg_image_copy[pos_h: sub_h, pos_w:sub_w] = res
            cv2.imwrite(f'remove_bg/{name}-{bg_name}.png', res)
            print('Background change done')

        else:
            print('Preparing image with the input parameters.')
            sub_hnew = int(sub_h * scale)
            sub_wnew = int(sub_w * scale)
            new_dim = (sub_wnew, sub_hnew)
            # scaling = round(sub_hnew/sub_h, 1)
            subject_image = cv2.resize(subject_image, new_dim, interpolation= cv2.INTER_LINEAR)
            # finalSubject = segment_style(subject_image, bg_image)
            # res = cv2.seamlessClone(subject_image, bg_image, mask, [pos_w, pos_h], cv2.NORMAL_CLONE)

            res = cvzone.overlayPNG(bg_image, subject_image, [pos_w, pos_h])
            cv2.imwrite(f'remove_bg/{name}-{bg_name}.png', res)
            print('Background change done')