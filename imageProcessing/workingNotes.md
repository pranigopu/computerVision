<h1>WORKING NOTES</h1>

**_Image Processing_**

---

**Contents**

- [Packages used](#packages-used)
  - [Matplotlib](#matplotlib)
  - [OpenCV](#opencv)
  - [`glob`](#glob)

---

# Packages used
## Matplotlib
Matplotlib is a Python library for visualisation. It is a comprehensive library for creating static, animated, and interactive visualizations in Python. I have used this library to read, display and save images (OpenCV can read and save images but not display them).

> **Reference**: [**matplotlib.org**](https://matplotlib.org/)

## OpenCV
OpenCV (i.e. Open Source Computer Vision) is an open source computer vision library, originally developed by Intel but now operated by the non-profit Open Source Vision Foundation (OpenCV Foundation). It contains functions for accessing and processing image and video data as well. The `opencv-python` is a library of pre-built CPU-only OpenCV packages for Python, i.e. it has binary packages that already contain statically built OpenCV binaries (hence, OpenCV need not be installed in your system on its own).

---

**NOTE 1**: `opencv-python` is to be imported as `cv2`.

**NOTE 2**: OpenCV can read and save images but not display them.

---

> **References**:
>
> - [**OpenCV.org**](https://opencv.org/)
> - [`opencv-python` (documentation)](https://pypi.org/project/opencv-python/)
> - [_OpenCV Tutorial in Python_ from **GeeksForGeeks.org**](https://www.geeksforgeeks.org/opencv-python-tutorial/)

## `glob`
It is a module that offers Unix style pathname pattern expansion. It is a powerful tool for working with file paths and retrieving a list of file or directory paths based on specific patterns. It simplifies the process of finding files and directories that match certain criteria within a directory structure. I have used this to store multiple images from a folder into an array in a single line of code.

> **References**:
>
> - [`glob` — Unix style pathname pattern expansion (documentation)](https://docs.python.org/3/library/glob.html)
> - [_Python Glob Module Tutorial (With Examples)_ from **MachineLearningTutorials.org**](https://machinelearningtutorials.org/python-glob-module-tutorial-with-examples/)