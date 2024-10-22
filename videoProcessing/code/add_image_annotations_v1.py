# ADD VIDEO ANNOTATIONS
# Version 1: Add bounding boxes (regardless of category) according to annotations given in the relevant CSV file for a particular image of the video

import cv2
import pandas as pd
import matplotlib.pyplot as plt

# EXTRA: For passing arguments to this script in command line:
from sys import argv
'''
For notes on my use of `argv` from `sys`, see...
"Use of `argv` from `sys` in my video processing programs"
... in "https://github.com/pranigopu/computerVision/blob/main/videoProcessing/workingNotes.md"
'''

#================================================
# Getting the annotations data

data = pd.read_csv('../annotations.csv')
maxFrameIndex = max(data['frameIndex'])

#================================================
# Getting the video file

fileName = '../videos/' + argv[1] + '.mp4'
capture = cv2.VideoCapture(fileName)

#================================================
# Creating a multiplier to obtain the frame number for the given frame index

'''
The annotations dataset has the column `frameIndex`, but these are
indices of a set of frames that are evenly spread across the
video for which annotations are provided. Given that the frames
are evenly spread and start from the first frame, we can use the
following code to obtain the approximate a multiplier that can be
used to obtain frame numbers from frame indices. Note that frame
numbers are necessary for us to navigate the video effectively.
'''
numFrames = capture.get(cv2.CAP_PROP_FRAME_COUNT)
multiplier = numFrames / maxFrameIndex

#================================================
# Retrieving the image of a particular frame in the video

chosenFrameIndex = int(argv[2])
chosenFrameNumber = round(chosenFrameIndex * multiplier)
for frame in range(chosenFrameNumber):
    moreFramesToRead, image = capture.read()
    if not moreFramesToRead:
        break
# NOTE: If the frame index is too high, the image will be that of the last frame

capture.release()

#================================================
# Adding annotations for the frame at `chosenFrameNumber`

frameData = data.query(f'frameIndex == {chosenFrameIndex}')
for _, row in frameData.iterrows():
    point1 = int(row['box2d.x1']), int(row['box2d.y1'])
    point2 = int(row['box2d.x2']), int(row['box2d.y2'])
    cv2.rectangle(image, point1, point2, (0, 0, 255), 3)
    # NOTE: OpenCV images follow the BGR (blue-green-red) colour format

#================================================
# Displaying annotated image

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.show()