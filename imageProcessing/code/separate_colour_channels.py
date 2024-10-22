# SEPARATE COLOUR CHANNELS (FOR DEMO PURPOSES)

# For image handling:
import matplotlib.pyplot as plt

# To load multiple file paths from a folder:
from glob import glob

# EXTRA: For passing arguments to this script in command line:
from sys import argv
# NOTE: This is a non-essential feature; it is for my own convenience
'''
EXPECTED COMMAND LINE ARGUMENT:
Image index (i.e. the index of the image file path as loaded by `glob`)
'''

#================================================
imageFiles = glob('../images/*.jpg')
imageIndex = int(argv[1])
image = plt.imread(imageFiles[imageIndex])

# Determining the appropriate display dimensions:
n = float(max([image.shape[0], image.shape[1]]))
height = 5 * image.shape[0] / n
width = 5 * image.shape[1] / n

# Creating the subplot grid:
fig, axs = plt.subplots(1, 4, figsize=(width*3, height), tight_layout=True)

# Displaying each colour channel separately (along with the full image for reference):
axs[0].imshow(image), axs[0].axis('off'), axs[0].set_title('Full image')
axs[1].imshow(image[:, :, 0], cmap='Reds'), axs[1].axis('off'), axs[1].set_title('Red channel')
axs[2].imshow(image[:, :, 1], cmap='Greens'), axs[2].axis('off'), axs[2].set_title('Green channel')
axs[3].imshow(image[:, :, 2], cmap='Blues'), axs[3].axis('off'), axs[3].set_title('Blue channel')

plt.show()