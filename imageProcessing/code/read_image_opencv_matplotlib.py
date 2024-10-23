# READ IMAGES USING OPENCV AND MATPLOTLIB (TO COMPARE)

# For image handling:
import cv2
import matplotlib.pyplot as plt

# To load multiple file paths from a folder:
from glob import glob

# EXTRA: For passing arguments to this script in command line:
from sys import argv
# NOTE: This is a non-essential feature; it is for my own convenience
'''
EXPECTED COMMAND LINE ARGUMENTS:
1) Image index (i.e. the index of the image file path as loaded by `glob`)
2) Image display scale
'''

#================================================
imageFiles = glob('../images/*.jpg')
imageIndex = int(argv[1])
imageFromOpenCV = cv2.imread(imageFiles[imageIndex])
imageFromMatplotlib = plt.imread(imageFiles[imageIndex])

'''
NOTE: Both `imageFromOpenCV` and `imageFromMatplotlib` have the
same shape. However, their colour channels are ordered differently.
To demonstrate, see `imageFromOpenCV` displayed by Matplotlib.
'''

#================================================
# Displaying images to compare

# Setting the dimensions of the display:
scale = float(argv[2])
n = float(max(imageFromOpenCV.shape[0], imageFromOpenCV.shape[1]))
height = scale * imageFromOpenCV.shape[0] / n
width = scale * imageFromOpenCV.shape[1] / n
# NOTE: `imageFromMatplotlib` can also be used here, since the dimensions are the same

# Creating the subplot grid for all images to be displayed
if width > height:
    fig, axs = plt.subplots(3, 1, figsize=(width, height*3), tight_layout=True) # If image is more landscape, stack vertically
else:
    fig, axs = plt.subplots(1, 3, figsize=(width*3, height), tight_layout=True) # If image is more portrait, stack horizontally

#------------------------------------
# Displaying without changing the order of colour channels (i.e. the 3rd dimension of the image arrays):
axs[0].imshow(imageFromOpenCV), axs[0].axis('off'), axs[0].set_title('OpenCV (original)')

# Displaying after convering the order of the colour channels as needed:
imageFromOpenCV = cv2.cvtColor(imageFromOpenCV, cv2.COLOR_BGR2RGB) # Because OpenCV follows the BGR (blue, green, red) colour order while Matplotlib follows the RGB (red, green, blue) colour order
axs[1].imshow(imageFromOpenCV), axs[1].axis('off'), axs[1].set_title('OpenCV (reordered)') # "reordered" => reordered colour channels

# Displaying the iage as read by Matplotlib (for reference):
axs[2].imshow(imageFromMatplotlib), axs[2].axis('off'), axs[2].set_title('Matplotlib')

#------------------------------------
plt.show()
