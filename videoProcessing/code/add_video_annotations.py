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

# To see progress par in loops:
import tqdm

#================================================
# Getting the annotations data

data = pd.read_csv('../annotations.csv')
maxFrameIndex = max(data['frameIndex'])

#================================================
# Getting the video file

fileName = '../videos/' + sys.argv[1] + '.mp4'
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
# Creating a colour map according to categories:

# Using the `review_annotations.py` code, we see that there are 4 categories as mentioned in the colour map...
colourMap = {'car': (0, 0, 255), 'bus': (0, 255, 0), 'pedestrian': (255, 0, 0), 'bicycle': (255, 255, 0)}
# NOTE: OpenCV images follow the BGR (blue-green-red) colour format

#================================================
# Creating a `cv2.VideoWriter` object to create a video output

# Obtaining the relevant metadata for the construction of annotated video:
frameHeight = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
frameWidth = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
# NOTE: The above need to be integers to be valid arguments in the video writer initialiser
fps = capture.get(cv2.CAP_PROP_FPS)
# Creating the video writer object:
outputFileName = '../videos/0001542f-7c670be8--annotated.mp4'
videoCodec = 'mp4v'
videoCodecFourccCode = cv2.VideoWriter.fourcc(*videoCodec)
# NOTE 1: `*` as used here is the unpacking operation; to learn more, see: https://github.com/pranigopu/computerVision/blob/main/information.md#unpacking-operation
# NOTE 2: `cv2.VideoWriter.fourcc` accepts four separate character arguments which it concatenates into a FOURCC code, which it uses to return a corresponding numeric version of the code
output = cv2.VideoWriter(outputFileName, videoCodecFourccCode, fps, (frameWidth, frameHeight))

#================================================
# Adding annotations for all frames

for frame in tqdm.tqdm(range(int(numFrames))):
    moreFramesToRead, image = capture.read()
    if not moreFramesToRead:
        break
    
    # Obtaining the relevant annotation rows for the current frame:
    relevantFrameNumber = data.query('frameNumber <= @frame')['frameNumber'].max()
    frameData = data.query('frameNumber == @relevantFrameNumber')
    
    # Adding annotations for the frame's image:
    try: # To handle NaN values (if any)
        for _, row in frameData.iterrows():
            point1 = int(row['box2d.x1']), int(row['box2d.y1'])
            point2 = int(row['box2d.x2']), int(row['box2d.y2'])
            colour = colourMap[row['category']]
            cv2.rectangle(image, point1, point2, colour, 3)
    except:
        pass
    output.write(image)

capture.release()
output.release()