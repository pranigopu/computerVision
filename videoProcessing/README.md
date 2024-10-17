<h1>VIDEO PROCESSING</h1>

---

**Contents**:

- [Learning outcomes](#learning-outcomes)
- [Resources](#resources)
- [Packages useful for video processing](#packages-useful-for-video-processing)
  - [`ffmpeg-python` (imported as `ffmpeg`)](#ffmpeg-python-imported-as-ffmpeg)
  - [`subprocess`](#subprocess)
  - [OpenCV](#opencv)

---

# Learning outcomes
Using Python:

- Access and view videos
- See the video's metadata
- Iterate through the video's frames
- Add annotations to the video
- Generate a new video by combining images

# Resources
- [_Video Data Processing with Python and OpenCV_ by Rob Mulla](https://www.youtube.com/watch?v=AxIc-vGaHQ0)

# Packages useful for video processing
## `ffmpeg-python` (imported as `ffmpeg`)
FFmpeg (Fast Forward Moving Picture Experts Group) is a free and open source software project containing a suite of libraries and programs for handling multimedia files and streams, including video and audio. `ffmpeg-python` in Python is a [Python binding](https://github.com/pranigopu/computerVision/definitions#language-binding) for FFmpeg. Note that `python-ffmpeg` (also imported as `ffmpeg`) is another Python binding for FFmpeg. Both bindings provide [synchronous and asynchronous APIs](https://github.com/pranigopu/computerVision/definitions#api). To install `ffmpeg-python`, enter `pip install ffmpeg-python` in the terminal/command prompt.

**NOTE**: _Installing both_ `ffmpeg-python` _and_ `python-ffmpeg` _is ill-advised since both are identified during imports as_ `ffmpeg` _(which means you would be using only the first Python binding installed). If you have one installed but want to switch to another, uninstall the one you currently have first._

> **References**:
>
> - [**FFmpeg.org**](https://ffmpeg.org/)
> - [`python-ffmpeg` (documentation)](https://pypi.org/project/python-ffmpeg/)

## `subprocess`
A built-in module in Python that allows you to spawn child processes (subprocesses), connect to their input/output/error [pipes](https://github.com/pranigopu/computerVision/definitions#pipe) and obtain their return codes (e.g. returned status, returned value, etc.). It is a valuable tool to execute external functions and commands in Python instead of manually running them in a terminal application (e.g. video format conversion commands). Thus, it seamlessly integrates external programming into one's Python workflow.

> **References**:
>
> - [_Python subprocess module_ from **GeeksForGeeks.org**](https://www.geeksforgeeks.org/python-subprocess-module/)
> - [`subprocess` — Subprocess management (documentation)](https://docs.python.org/3/library/subprocess.html)

## OpenCV
OpenCV (i.e. Open Source Computer Vision) is an open source computer vision library, originally developed by Intel but now operated by the non-profit Open Source Vision Foundation (OpenCV Foundation). It contains functions for accessing and processing image and video data as well.

> **References**:
>
> - [**OpenCV.org**](https://opencv.org/)
> - [`opencv-python` (documentation)](https://pypi.org/project/opencv-python/)
> - [_OpenCV Tutorial in Python_ from **GeeksForGeeks.org**](https://www.geeksforgeeks.org/opencv-python-tutorial/)