# PULL IMAGES FROM VIDEO
# Version 2: Display a series of images from frames across the video

import cv2 # OpenCV for Python
import matplotlib.pyplot as plt # For image display functionality

# EXTRA: For passing argument to this script in command line:
import sys
'''
For notes on my use of `sys` here, see...
"Use of `sys` in my video processing programs"
... in "https://github.com/pranigopu/computerVision/blob/main/videoProcessing/workingNotes.md"
'''

# The square root and ceiling functions:
from math import sqrt, ceil

#================================================
fileName = '../videos/' + sys.argv[1] + '.mp4'
numFramesToShow = int(sys.argv[2])
capture = cv2.VideoCapture(fileName) # Opening and capturing the frames of the vide file
numFrames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

#------------------------------------
# Defining the subplots in which to place the images

#________________________
# Deciding the dimensions of the grid of subplots

# STRATEGY: First try a square grid, then keep reducing the number of columns until a good-enough fit is achieved
numCols = numRows = ceil(sqrt(numFramesToShow)) # Number of rows and columns in the grid of subplots
while abs(numRows * numCols - numFramesToShow) > 1: # Hence, there can be at most one leftover subplot, no more
    numCols -= 1
    numRows = ceil(numFramesToShow / numCols)

#________________________
fig, axs = plt.subplots(numRows, numCols, figsize=(10, 10), constrained_layout=True)
axs = axs.flatten() # Flattening the array of subplots to easily iterate over them

#------------------------------------
# Display frames evenly spread across the video:
imageIndex = 0 # To keep track of the indices of subplots in which images must be displayed
jumpSize = ceil(numFrames / numFramesToShow) # The number of frames between two frames to be displayed
for frame in range(numFrames):
    moreFramesToRead, image = capture.read()
    if frame % jumpSize == 0:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        axs[imageIndex].imshow(image)
        axs[imageIndex].axis('off')
        imageIndex += 1

# Hide axes for leftover subplots (if any) so they do not show:
while imageIndex < numRows * numCols:
    axs[imageIndex].axis('off')
    imageIndex += 1

plt.show()

#================================================
capture.release() # Releasing the `cv2.VideoCapture` object from memory

#================================================
# FINAL COMMENTS
'''
Consider why the ceiling function was used. If it were not, there
is a risk of getting too few subplots, leading to runtime errors.
'''