from PIL import Image
from glob import glob
from os.path import join
import os

listImage =  os.path.dirname(os.path.realpath(__file__))

pathInput =  listImage + "\input"
pathOutput = listImage + "\output"

images = glob(pathInput + '\*.png') + glob(pathInput + '\*.jpg')
#print(images)

def HorizontalFlip_image():
    for image in images:
        originalImage = Image.open(image)

        outputImage = originalImage.transpose(Image.FLIP_LEFT_RIGHT)
        outputImage.save(
            pathOutput + "/"+ os.path.basename(image),
            quality=100,
            subsampling=0
            )
        print(pathOutput + '/' + os.path.basename(image))

if __name__ == '__main__':
    HorizontalFlip_image()

