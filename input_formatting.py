import numpy as np
import cv2
from PIL import Image
import openslide
#import torchvision

PATCH_SIZE = 304
def input_formatting(slide):

    img = openslide.OpenSlide(slide)
    size=img.dimensions
    w = size[0]
    h = size[1]
    patches = []
    print('original size: ' + str(size[0]) + ',' + str(size[1]))

    # make grid patches as np.array
    x=0
    y=0
    while x<w:
        while y<h:
            patch = img.read_region((x,y), 0, (PATCH_SIZE,PATCH_SIZE))     #y , x
            patch = np.array(patch)
            patch = cv2.cvtColor(patch, cv2.COLOR_RGBA2RGB)#y, x , 3
            patch = np.transpose(patch)
            patches.append(patch)
            y+=PATCH_SIZE
        x+=PATCH_SIZE

    #patches = np.transpose(patches)
    return patches


#patches = input_formatting('/mnt/tmpfs/interns/slides/b_1.tif')
#print(np.array(patches).shape)


