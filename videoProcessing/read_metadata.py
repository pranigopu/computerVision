# READ METADATA
# Get video metadata

import cv2 # OpenCV for Python

# EXTRA: For passing argument to this script in command line:
import sys
'''
For notes on my use of `sys` here, see...
"Use of `sys` in my video processing programs"
... in "https://github.com/pranigopu/computerVision/blob/main/videoProcessing/workingNotes.md"
'''

#================================================
fileName = sys.argv[1] + 'mp4'
capture = cv2.VideoCapture(fileName)
print(fileName, cv2.CAP_PROP_FRAME_COUNT)