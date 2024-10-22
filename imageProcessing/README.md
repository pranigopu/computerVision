<h1>IMAGE PROCESSING</h1>

---

**Contents**:

- [Learning outcomes](#learning-outcomes)
- [Resources](#resources)
- [Organised view of the code](#organised-view-of-the-code)

---

# Learning outcomes
Using Python:

- Load a whole folder of images into one array
- View images and view their separate colour channels
- See the image's metadata
- Manipulate image colour
- Apply filters to the image (e.g. sharpen, blur, etc.)
- Save image

# Resources
- [_Image Processing with OpenCV and Python_ by Rob Mulla from **YouTube.com**](https://www.youtube.com/watch?v=kSqxn6zGE0c)
- [`workingNotes.md` (my personal notes for tips, issues and solutions)](https://github.com/pranigopu/computerVision/blob/main/imageProcessing/workingNotes.md)

# Organised view of the code
1. <details><summary><a href="https://github.com/pranigopu/computerVision/blob/main/imageProcessing/code/load_image_file_paths.py"><code>load_image_file_paths.py</code></a></summary>Loads and displays all the image file paths from the image folder. Also serves as an introduction to the <code>glob</code> function from the <code>glob</code> module.</details>
2. <details><summary><a href="https://github.com/pranigopu/computerVision/blob/main/imageProcessing/code/display_image_matplotlib.py"><code>display_image_matplotlib.py</code></a></summary>Loads and displays an image as specified by an index number and according to the specified scale, using Matplotlib. Takes the image index number, display options and display scale as command line arguments (these arguments are explained in the source code). Also serves as an introduction to reading images using Matplotlib.</details>
3. <details><summary><a href="https://github.com/pranigopu/computerVision/blob/main/imageProcessing/code/display_image_opencv_vs_matplotlib.py"><code>display_image_opencv_vs_matplotlib.py</code></a></summary>Loads and displays an image as specified by an index number and according to the specified scale, using Matplotlib and OpenCV, with the aim of comparing the two methods of reading images to show differences in the ordering of the colour channels. Takes the image index number and display scale as command line arguments (these arguments are explained in the source code). Also serves as an introduction to reading images using OpenCV and using Matplotlib.</details>
4. <details><summary><a href="https://github.com/pranigopu/computerVision/blob/main/imageProcessing/code/separate_colour_channels.py"><code>separate_colour_channels.py</code></a></summary>Shows the different colour channels of an image (as read by Matplotlib). Takes the image index number as a command line argument. Also serves as an introduction to the colour mapping option on <code>matplotlib.pyplot.imshow</code>.</details>
5. <details><summary><a href="https://github.com/pranigopu/computerVision/blob/main/imageProcessing/code/filter_image.py"><code>filter_image.py</code></a></summary>Applies a specified filter to a specified image, which is displayed according to the specified scale and (if specified) saved. Takes the image index, filter name, display scale and an optional argument (indicating whether to save the image or not) as command line arguments (arguments are explained in the source code). Also serves as an introduction to convolutional image filtering and the concept of bit depth.</details>