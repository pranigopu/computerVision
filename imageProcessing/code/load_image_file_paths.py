# LOAD IMAGE FILE PATHS

from glob import glob

#================================================
imageFiles = glob('../images/*.jpg')
'''
NOTE: If the `images` folder has only images, it is enough to do...

`imageFiles = glob('../images/*')`

... which loads all file paths within the `images` folder. However,
the extension-based loading of file paths suits my needs better,
since there is also a markdown file in the `images` folder to give
details about the images.
'''

# Viewing the datatype of the return value and its elements:
print('\nDATATYPE INSPECTION:')
print(f'imageFiles\t: {type(imageFiles)}')
print(f'imageFiles[0]\t: {type(imageFiles[0])}')

# Listing file paths:
print('\nIMAGE FILE PATHS (WITH INDICES):')
for i, imageFile in enumerate(imageFiles):
    print(f'{i}) {imageFile}')

# To add a space after last line:
print()