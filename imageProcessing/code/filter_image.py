# FILTER IMAGE

import cv2
import matplotlib.pyplot as plt
from glob import glob
import numpy as np
import sys

#================================================
# Obtaining the image

imageFiles = glob('../images/*.jpg')
imageIndex = int(sys.argv[1])
image = plt.imread(imageFiles[imageIndex])

#================================================
# Defining kernels

kernel = {}
kernel['edge_detection'] = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
kernel['sharpen'] = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
kernel['gaussian_blur'] = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
kernel['box_blur'] = np.ones((3, 3)) / 9

# Reference: https://en.wikipedia.org/wiki/Kernel_(image_processing)

#================================================
# Applying the specified kernel

chosenKernel = sys.argv[2]
newImage = cv2.filter2D(image, -1, kernel[chosenKernel])
'''
`cv2.filter2D` convolves an image with a given kernel (typically a
2D matrix) to apply a filter on the images. This function has the
following arguments:

- `src`    : Image array
- `ddepth` : Desired depth of the image (bit depth)
- `kernel` : The specified convolutional kernel

NOTE: `ddepth=-1` => Resulting image's depth same as source image's.

References:
- https://www.geeksforgeeks.org/python-opencv-filter2d-function/
- https://www.askpython.com/python-modules/opencv-filter2d
- https://docs.opencv.org/3.4/d4/d86/group__imgproc__filter.html (documentation)

------------------------------------
MORE ON BIT DEPTH:
In the context of image processing, bit depth is the number of bits
used by each color component to represent a pixel. For example:
8 bits => 256 (i.e. 2^8) shades of a given primary color

References for bit depth:
- https://photofocus.com/photography/bit-depth-what-you-must-know/
- https://photographylife.com/8-bit-vs-16-bit-images
'''

#================================================
# Displaying the image

# Determining the display dimensions:
scale = float(sys.argv[3])
n = float(max(newImage.shape[0], newImage.shape[1]))
height = scale * newImage.shape[0] / n
width = scale * newImage.shape[1] / n

# Displaying the image:
fig, ax = plt.subplots(figsize=(width, height), tight_layout=True)
ax.imshow(newImage)
ax.axis('off')
plt.show()

#================================================
# Saving image (if specified)
if len(sys.argv) > 4 and sys.argv[4] == 'save':
    plt.imsave(imageFiles[imageIndex][:-4] + ' (filter-' + chosenKernel + ').jpg', newImage) # No return value to indicate success or failure
    '''
    ALTERNATE CODE:
    cv2.imwrite(imageFiles[imageIndex][:-4] + ' - ' + chosenKernel + '.jpg', newImage) # Returns `True` if save is successful
    '''