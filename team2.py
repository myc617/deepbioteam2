import openslide
import numpy as np
from PIL import Image
from xml.etree.ElementTree import parse
import cv2 


xml_filename =[]
tif_filename =[]
for i in range(1,10):
    xml_filename.append('b_'+str(i)+'.xml')
    tif_filename.append('b_'+str(i)+'.tif')

tif_path='/mnt/tmpfs/interns/slides/'
xml_path='/mnt/tmpfs/interns/annotations/'
patch_size = (304,340)
threshold_parameter = 0.3 #threshold parameter in (0,1)

# terminology : slide_patch , mask_patch 
# mask is the grayscale image we get and process 



def wholeslide_to_filled_mask(xml_root):
    #### Complete Here 
    return mask_filled #cv2 file 


def filled_mask_to_list_of_mask_patches(filled_mask):
    #### Complete Here 
    return list_of_patches_of_filled_mask 


def calculate_portion_of_cancer_in_patch(patch_of_filled_mask)
    ### Complete Here 
    return portion_of_cancer_in_patch # value in [0,1]

def check_tumor_in_patch(mask_patch,threshold):
    if calculate_portion_of_cancer_in_patch(patch)>=threshold:
        return 1
    else:
        return 0

def wholeslide_to_list_of_patches(slide_image):
    ### Complete Here 
    return list_of_patches_of_whole_slide_image

def mask_patch_corresponds_to_slide_patch(slide_patch,list_of_mask_patches):
    ### Complete Here 
    return mask_patch

def attach_label_to_patch(slide_patch,list_of_mask_patches):
    return [ slide_patch,check_tumor_in_patch(mask_patch_corresponds_to_slide_patch(slide_patch,list_of_mask_patches) ,threshold) ]

def attach_labels_to_patches_in_list(list_of_slide_patches,list_of_mask_patches):
    list_of_labeled_patches=[]
    for patch in list_of_slide_patches:
        list_of_labeled_patches.append( attach_label_to_patch(patch,list_of_mask_patches) )
    return list_of_labeled_patches

def WholeSlide_to_List_of_Patches(slide_image,xmlroot):
    GrayScaleImage_with_Filled_Mask = wholeslide_to_filled_mask(xml_root)
    List_of_Patches_of_Filled_Mask = filled_mask_to_list_of_mask_patches(GrayScaleImage_with_Filled_Mask)    
    List_of_Patches_of_Whole_Slide_Image = wholeslide_to_list_of_patches(slide_image)
    List_of_Labeled_Patches=attach_labels_to_patches_in_list(List_of_Patches_of_Whole_Slide_Image,List_of_Patches_of_Filled_Mask)

    return List_of_Labeled_Patches 








    
    


