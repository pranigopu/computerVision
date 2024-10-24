# PULL IMAGES FROM VIDEO
# Version 1: Iteratively display images frame-wise

import cv2 # OpenCV for Python
import matplotlib.pyplot as plt # For image display functionality

# EXTRA: For passing arguments to this script in command line:
from sys import argv
'''
For notes on my use of `argv` from `sys`, see...
"Use of `argv` from `sys` in my video processing programs"
... in "https://github.com/pranigopu/computerVision/blob/main/videoProcessing/workingNotes.md"
'''

#================================================
fileName = '../videos/' + argv[1] + '.mp4'
capture = cv2.VideoCapture(fileName) # Opening and capturing the frames of the vide file
moreFramesToRead = True

#------------------------------------
# Retrieving images per frame iteratively until file end or user indicates

while moreFramesToRead:
    moreFramesToRead, image = capture.read()
    '''
    NOTE ON `.read`:
    `.read` starts reading the video's frames from the first frame.
    Each time it is called for a given `cv2.VideoCapture` object, it
    updates the current frame number such that the i-th call reads the
    i-th frame. Per call, it returns a boolean indicating that there
    are more frames to read (true => no, false => yes, i.e. the last
    frame has been reached).

    Per call, it also returns the image corresponding to the frame.
    The image is an array of dimensions (h, w, 3), where h and w are
    the height and width of the video. The 3rd dimension represents
    the BGR (blue, green and red) channels; hence, it has the size 3.
    Note that each channel contains an array of values for the
    corresponding colour, and any colour can be constructed from some
    combination of blue, green and red.
    '''

    #------------------------------------
    # Converting the colour order

    '''
    NOTE: WHY CONVERT COLOUR ORDER?
    Note that the colour order of OpenCV is different from the colour
    order used by `matplotlib.pyplot` (OpenCV uses BGR, whereas
    Matplotlib uses RGB), which means a conversion (essentially
    reshaping the 3rd dimension of the NumPy array representing the
    image) is needed to accurately display the image using
    `matplotlib.pyplot.imshow`.
    '''
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # NOTE: `cv2.COLOR_BGR2RGB` is an integer constant representing the colour conversion option for BGR-to-RBG

    #------------------------------------
    # Displaying the image

    plt.imshow(image)
    plt.show()
    # TIP: You can use the following to remove axes and just show the image:
    '''
    fig, ax = plt.subplot()
    ax.imshow()
    ax.axis('off')
    plt.show()
    '''

    #------------------------------------
    if input('Continue? (y/n) ') == 'n':
        break

#================================================
capture.release() # Releasing the `cv2.VideoCapture` object from memory