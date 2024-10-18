# ADD VIDEO ANNOTATIONS
# Add bounding boxes according to annotations given in the relevant CSV file for the whole video

import cv2
import pandas as pd
import matplotlib.pyplot as plt

# EXTRA: For passing argument to this script in command line:
import sys
'''
For notes on my use of `sys` here, see...
"Use of `sys` in my video processing programs"
... in "https://github.com/pranigopu/computerVision/blob/main/videoProcessing/workingNotes.md"
'''

#================================================
# Getting the annotations data

data = pd.read_csv('annotations.csv')
maxFrameIndex = max(data['frameIndex'])

#================================================
# Getting the video file

fileName = sys.argv[1] + '.mp4'
capture = cv2.VideoCapture(fileName)

#================================================
# Adding a new column to store frame numbers for the given frame indices

'''
The annotations dataset has the column `frameIndex`, but these are
indices of a set of frames that are evenly spread across the
video for which annotations are provided. Given that the frames
are evenly spread and start from the first frame, we can use the
following code to obtain the approximate a multiplier that can be
used to obtain frame numbers from frame indices. Note that frame
numbers are necessary for us to navigate the video effectively.
Here, we are making a separate column for frame numbers for
convenience, since we shall be dealing with a lot more frames.
'''
numFrames = capture.get(cv2.CAP_PROP_FRAME_COUNT)
multiplier = round(numFrames / maxFrameIndex)
data['frameNumber'] = (data['frameIndex'] * multiplier).round().astype('int')

#================================================
# Adding annotations for all frames

for _, row in data.iterrows():
    point1 = int(row['box2d.x1']), int(row['box2d.y1'])
    point2 = int(row['box2d.x2']), int(row['box2d.y2'])
    cv2.rectangle(image, point1, point2, (0, 0, 255), 3)
    # NOTE: OpenCV images follow the BGR (blue-green-red) colour format

capture.release()