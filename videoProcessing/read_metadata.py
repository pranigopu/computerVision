# READ METADATA
# Get video metadata

#------------------------------------
# Reference: https://www.geeksforgeeks.org/how-to-get-properties-of-python-cv2-videocapture-object/
#------------------------------------

import cv2 # OpenCV for Python

# EXTRA: For passing argument to this script in command line:
import sys
'''
For notes on my use of `sys` here, see...
"Use of `sys` in my video processing programs"
... in "https://github.com/pranigopu/computerVision/blob/main/videoProcessing/workingNotes.md"
'''

#================================================
fileName = sys.argv[1] + '.mp4'
capture = cv2.VideoCapture(fileName)

# The following is done for  convenience in looping over information:
propertyIndexList = [cv2.CAP_PROP_FRAME_COUNT, cv2.CAP_PROP_FPS, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FRAME_WIDTH]
propertyNameList = ['Frame count', 'Frame rate', 'Frame height', 'Frame width']
# NOTE: `CAP_PROP` => "Capture Property" (i.e. property of video capture)

print(f'Properties of "{fileName}":')
for propertyName, propertyIndex in zip(propertyNameList, propertyIndexList):
    print(f'{propertyName} \t: {capture.get(propertyIndex)}')

# Releasing the video capture object:
capture.release()
'''
NOTE: This function closes the video file or capturing device
whose data is being referred to by the video capture object. This
function is not necessary for this program, since we exit right
after reading the metadata. However, it is good practice to use it
once a `cv2.VideoCapture` object is dealt with, since it 
deallocates memory and clears the `capture` pointer, thereby also
minimising wasteful computation (this is more relevant for longer
programs).
'''

#================================================
# EXTRA: What are the property indices?
print('\nProperty indices:')
for propertyName, propertyIndex in zip(propertyNameList, propertyIndexList):
    print(f'{propertyName} \t: {propertyIndex}')

'''
From the output of the above loop, we see that the constants that
refer to properties in `cv2` (e.g. `cv2.CAP_PROP_FPS`) are
integers, i.e. they are indices, wherein each index corresponds to
a particular property. Based on the given integer, `capture.get`
retrieves the corresponding property of the video captured in the
`cv2.VideoCapture` object `capture`. Of course, you can directly
pass integers. E.g.: `capture.get(5)` retrieves the frame rate
(in FPS) of the video captured in the `capture` object.
'''