import cv2
import numpy as np

# image numpy.arrays are [Row, Column, Channel] 

def avg_overlaps(pred_arr):

    shape = pred_arr.shape
    arr = np.zeros((shape[0] + 1, shape[1] + 1))

    # Bounds are inclusive
    u_bound_row = shape[0] - 1
    u_bound_col = shape[1] - 1
    l_bound = 0

    for ind, x in np.ndenumerate(arr):
        # candidates refer to indices from pred_arr that may have overlapping 
        # sections, to consider them for prediction value averaging.
        candidates = (ind,
                     (ind[0], ind[1] - 1), 
                     (ind[0] - 1, ind[1]), 
                     (ind[0] - 1, ind[1] - 1))
        valid = []

        for cand in candidates:
            if (l_bound <= cand[0] <= u_bound_row) and (l_bound <= cand[1] <= u_bound_col):
                valid.append(pred_arr[cand])

        arr[ind] = sum(valid) / len(valid)

    return np.array(arr)


def heatmap(pred_arr, patch_size, overlaps = True, binary = True, threshold = 0.5):
    # This function does everything from start to finish.

    # Patch size is recommended to be even.

    # If binary = T, heatmap has binary color scheme. Otherwise, will be
    # colored along a continuous spectrum.

    # In case of overlap = T, stride is assumed to be (patch_size / 2).
    if overlaps:
        arr = avg_overlaps(pred_arr)
        p_size = round(patch_size / 2)

    else:
        arr = pred_arr
        p_size = patch_size

    arr = create_mapping(arr, p_size, binary, threshold)

    return arr

def create_mapping(pred_arr, patch_size, binary = True, threshold = 0.5):
# pred_arr is a 2D numpy array containing prediction values, ordered so that preserves the
# relative spatial information of patches.
# patch_size is a single int indicating patch dimensions.
# (assumes length = width)

    rows, cols = pred_arr.shape

    # Creates empty template that will be colored depending on prediction
    # value. This array is assumed to be equal to the initial slide
    # image in shape.
    mapping = np.zeros((rows * patch_size, cols * patch_size), dtype = np.uint8)

    # One loop iteration fills pixels corresponding to one patch
    for index, x in np.ndenumerate(pred_arr):
        row_l = patch_size * index[0]
        row_r = patch_size * (index[0] + 1)
        col_t = patch_size * index[1]
        col_b = patch_size * (index[1] + 1)
        
        if binary:
            # If binary = T, assign white or black using threshold. [0 or 255] 
            if x >= threshold:
                mapping[row_l:row_r, col_t:col_b] = 255
            else:
                mapping[row_l:row_r, col_t:col_b] = 0
                
        else:
            # Converts prediction value [0 ~ 1] to grayscale [0 ~ 255]
            mapping[row_l:row_r, col_t:col_b] = round(x * 255)

    return mapping


# Main for unit testing-----------------------------

if __name__ == '__main__':
    
    PATCH_SIZE = 100
    OVERLAPS = True
    BINARY = False
    THRESHOLD = 0.5
    TEST_ARR = np.array([[0. , 0. , 0.3, 0.2],
                         [0.6, 0. , 0.1, 0. ],
                         [1. , 0.4, 0. , 0. ]])


    heatmap = heatmap(TEST_ARR, PATCH_SIZE, OVERLAPS, BINARY, THRESHOLD)

    cv2.imwrite('heatmap.jpg', heatmap)
