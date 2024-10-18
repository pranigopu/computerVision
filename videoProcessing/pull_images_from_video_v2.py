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

# Additional feature:
import math

#================================================
fileName = sys.argv[1] + '.mp4'
numFramesToShow = int(sys.argv[2])
capture = cv2.VideoCapture(fileName)
numFrames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

#------------------------------------
size = int(math.sqrt(numFramesToShow))
fig, axs = plt.subplots(size, size, figsize=(10, 10), tight_layout=True)
axs = axs.flatten()

#------------------------------------
imageIndex = 0
jumpSize = math.ceil(numFrames/numFramesToShow)
for frame in range(numFrames):
    moreFramesToRead, image = capture.read()
    if frame % jumpSize == 0:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        axs[imageIndex].imshow(image)
        axs[imageIndex].axis('off')
        imageIndex += 1

plt.show()

#================================================
capture.release() # Releasing the `cv2.VideoCapture` object from memory