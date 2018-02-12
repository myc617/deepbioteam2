import numpy as np
import openslide
import pickle

f = open(path+'slide'+str(i)+'scores_ver3','rb')


outputs=[]
for inputs in test_result:
    point, output = class_score(test_net,inputs)
    outputs.append((point,output))#######use from here

path = './testslide0206/t_'
for img in range(1,8):
    image = openslide.OpenSlide(path + str(img) + '.tif')
    image_width, image_height = image.dimensions
    row_patch_num = int(image_width*2/patch_width)
    col_patch_num = int(image_height*2/patch_height)
    shape_transform(outputs,patch_width,row_patch_num, col_patch_num)



def shape_transform(outputs,patch_size,row_patch_num, col_patch_num):
    a = np.zeros([row_patch_num,col_patch_num])
    print(a)
    for point, output in outputs:
        row = int(point[0] / patch_size)
        col = int(point[1] / patch_size)
        print(row,col)
        a[row, col] = output
    return a

