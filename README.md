# Photo Background Changer

Using a MaskRCNN model and a DeepLabV3 model for instance segmentation, we can change the background of a person's image to any background with an oil painting poster look.

## MaskRCNN

-   Trained Model with Weights: [mask_rcnn_coco.h5](https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5)

## DeepLabV3+

-   Trained Model with Weights: [model.h5](https://drive.google.com/file/d/17QKxSIBFhyJoDps93-sCVHnVV6UWS1sG/view?usp=sharing)

## How to use

-   Go to the directory where you want this to be installed.
-   Open the terminal and type `git clone https://github.com/Simrit-Momenttext/background-changer.git`
-   Now the project will be cloned. Type `cd background-changer` to enter the project directory.

-   For the models to work we need to have the models first. The links to the 'mask_rcnn_coco.h5' and 'model.h5' files are given above.
-   Download the models and keep them in the project root directory.
-   Once the above steps are complete, go back to the terminal and ensure it is in the project directory.
-   It is recommended to create a virtual environment for this project using `python -m venv venv`.
-   To activate the virtual environment on CMD type `venv/Scripts/activate.bat`.
-   To activate the virtual environment on Powershell type `venv/Scripts/Activate.ps1`.
-   To install the packages required, type `pip install -r requirements.txt`.
-   Run the code by typing `python run.py`
-   Input the path of the subject and background images, the position coordinates and and the scaling factor of the image and wait for the result.
-   A folder called results is created and inside you will see all the changed backgrounds on the subject image as different images.

## Results

Subject

![Subject](https://github.com/Simrit-Momenttext/Photo-BG-Changer/blob/master/images/subject/girl7.jpg?raw=true "Subject")

Background

![Background](https://github.com/Simrit-Momenttext/Photo-BG-Changer/blob/master/images/background/Animal_Tracks-cover.png?raw=true "Background")

Result

![Result](https://github.com/Simrit-Momenttext/Photo-BG-Changer/blob/master/remove_bg/girl7-Animal_Tracks-cover.png?raw=true "Result")

## References

-   [MaskRCNN](https://github.com/matterport/Mask_RCNN)
-   [Human Image Segmentation](https://github.com/nikhilroxtomar/Remove-Photo-Background-using-TensorFlow)
-   [Pointillism Effect](https://github.com/matteo-ronchetti/Pointillism)
