# DISPLAY IMAGE USING MATPLOTLIB

# For image handling:
import matplotlib.pyplot as plt

# To load multiple file paths from a folder:
from glob import glob

# EXTRA: For passing arguments to this script in command line:
from sys import argv
# NOTE: This is a non-essential feature; it is for my own convenience
'''
EXPECTED COMMAND LINE ARGUMENTS:

1) Image index (i.e. the index of the image file path as loaded by `glob`)
2) Display options (put all desired characters in a single string)
    a = show the image's type and shape (as read by Matplotllib)
    b = show the distribution of the image's pixel values
    c = show the image
3) Image display scale
'''

#================================================
imageFiles = glob('../images/*.jpg')
imageIndex = int(argv[1]) # Image index must be given as a command line argument
image = plt.imread(imageFiles[imageIndex])

#================================================
# Inspecting the image array

if 'a' in argv[2]:
    print('\nINSPECTING IMAGE ARRAY:')
    print(type(image))
    print(image.shape)

#================================================
# Plotting the image's pixel values, i.e. the image array's cell values

if 'b' in argv[2]:
    print('\nPLOTTING THE DISTRIBUTION OF THE IMAGE ARRAY\'S PIXEL VALUES:')
    plt.hist(image.flatten(), bins=50)
    plt.title('Distribution of the image\'s pixel values')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

#================================================
# Displaying the image

if 'c' in argv[2]:
    print('\nDISPLAYING THE IMAGE')
    # Dynamically deciding the display dimensions based on the given scale:
    scale = float(argv[3])
    n = float(max([image.shape[0], image.shape[1]]))
    height = scale * image.shape[0] / n
    width = scale * image.shape[1] / n

    # Displaying the image:
    fig, ax = plt.subplots(figsize=(width, height), tight_layout=True)
    ax.imshow(image)
    ax.axis('off')
    plt.show()

# To add a space after last line:
print()