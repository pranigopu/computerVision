# PULL IMAGES FROM VIDEO
# Version 2: Display a series of images from frames across the video

import cv2 # OpenCV for Python
import matplotlib.pyplot as plt # For image display functionality

# EXTRA: For passing arguments to this script in command line:
from sys import argv
'''
For notes on my use of `argv` from `sys`, see...
"Use of `argv` from `sys` in my video processing programs"
... in "https://github.com/pranigopu/computerVision/blob/main/videoProcessing/workingNotes.md"
'''

# The square root and ceiling functions:
from math import sqrt, ceil

#================================================
fileName = '../videos/' + argv[1] + '.mp4'
numFramesToShow = int(argv[2])
capture = cv2.VideoCapture(fileName) # Opening and capturing the frames of the vide file
numFrames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

#================================================
# Defining the subplots in which to place the images

#------------------------------------
# Deciding the dimensions of the grid of subplots:
# STRATEGY: First try a square grid, then keep reducing the number of columns until a good-enough fit is achieved
numCols = numRows = ceil(sqrt(numFramesToShow)) # Number of rows and columns in the grid of subplots
while abs(numRows * numCols - numFramesToShow) > 1: # Hence, there can be at most one leftover subplot, no more
    numCols -= 1
    numRows = ceil(numFramesToShow / numCols)

#------------------------------------
fig, axs = plt.subplots(numRows, numCols, figsize=(10, 10), constrained_layout=True)
axs = axs.flatten() # Flattening the array of subplots to easily iterate over them

#================================================
# Displaying frames evenly spread across the video

#------------------------------------
# Storing images as subplots:
imageIndex = 0 # To keep track of the indices of subplots in which images must be displayed
jumpSize = ceil(numFrames / numFramesToShow) # The number of frames between two frames to be displayed
for frame in range(numFrames):
    moreFramesToRead, image = capture.read()
    if frame % jumpSize == 0:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # NOTE 1: `cv2.COLOR_BGR2RGB` is an integer constant representing the colour conversion option for BGR-to-RBG
        # NOTE 2: Colour order must be converted since OpenCV and Matplotlib use the BGR and RGB colour orders respectively
        axs[imageIndex].imshow(image)
        axs[imageIndex].axis('off')
        imageIndex += 1

#------------------------------------
# Hiding axes for leftover subplots (if any) so they do not show:
while imageIndex < numRows * numCols:
    axs[imageIndex].axis('off')
    imageIndex += 1

plt.show()

#================================================
capture.release() # Releasing the `cv2.VideoCapture` object from memory

#================================================
# FINAL COMMENTS
'''
Consider why the ceiling function was used. If it were not, and if
rounding or integer division was done instead, there would be a
risk of getting too few subplots, leading to runtime errors.
'''