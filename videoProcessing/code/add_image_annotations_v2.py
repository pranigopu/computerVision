# ADD VIDEO ANNOTATIONS
# Version 2: Add bounding boxes (category wise) according to annotations given in the relevant CSV file for a particular image of the video

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
# The following code is from `add_image_annotations_v1.py` (see this source file for clarity on the code's logic)

fileName = '../videos/' + argv[1] + '.mp4'
capture = cv2.VideoCapture(fileName)
numFrames = capture.get(cv2.CAP_PROP_FRAME_COUNT)
multiplier = numFrames / maxFrameIndex
chosenFrameIndex = int(argv[2])
chosenFrameNumber = round(chosenFrameIndex * multiplier)
capture = cv2.VideoCapture(fileName)
for frame in range(chosenFrameNumber):
    moreFramesToRead, image = capture.read()
    if not moreFramesToRead:
        break
capture.release()

#================================================
# Creating a colour map according to categories:

# Using the `review_annotations.py` code, we see that there are 4 categories as mentioned in the colour map...
colourMap = {'car': (0, 0, 255), 'bus': (0, 255, 0), 'pedestrian': (255, 0, 0), 'bicycle': (255, 255, 0)}
# NOTE: OpenCV images follow the BGR (blue-green-red) colour format

#================================================
# Adding bounding boxes for the frame at `chosenFrameNumber`

frameData = data.query(f'frameIndex == {chosenFrameIndex}')
for _, row in frameData.iterrows():
    point1 = int(row['box2d.x1']), int(row['box2d.y1'])
    point2 = int(row['box2d.x2']), int(row['box2d.y2'])
    try:
        colour = colourMap[row['category']]
    except:
        continue
    cv2.rectangle(image, point1, point2, colour, 3)
    # NOTE: OpenCV images follow the BGR (blue-green-red) colour format

#================================================
# Displaying annotated image

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.show()