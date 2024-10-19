<h1>VIDEO PROCESSING</h1>

---

**Contents**:

- [Learning outcomes](#learning-outcomes)
- [Resources](#resources)
- [Organised view of the code](#organised-view-of-the-code)

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
- <details><summary><a href="https://github.com/pranigopu/computerVision/blob/main/videoProcessing/workingNotes.md">Working Notes</a></summary>A document containing working notes on technical details, problems and solutions based on personal experiences.</details>

# Organised view of the code
Each code (except for `review_annotations.py`) accepts the file name (without extension) as a command line argument, and may accept additional command line arguments, as detailed below. I implemented my code in this way for convenience in rerunning the scripts and for also offering a degree of flexibility.

1. <details><summary><a href="https://github.com/pranigopu/computerVision/blob/main/videoProcessing/convert_mov_to_mp4.py"><code>convert_mov_to_mp4.py</code></a></summary>Converts the MOV file taken from the online database to an MP4 file, which is more convenient for storing and video processing. Takes the file name (without extension) as a command line argument. Also serves as an introduction to FFmpeg and the subprocess module.</details>
2. <details><summary><a href="https://github.com/pranigopu/computerVision/blob/main/videoProcessing/read_metadata.py"><code>read_metadata.py</code></a></summary>Reads the metadata from a specified video. Takes the file name (without extension) as a command line argument. Also serves as an introduction to OpenCV's video capture object. An output can be seen <a href="https://github.com/pranigopu/computerVision/blob/main/videoProcessing/output--pull_images_from_video_v1.png">here</a></details>
3. <details><summary><a href="https://github.com/pranigopu/computerVision/blob/main/videoProcessing/pull_images_from_video_v1.py"><code>pull_images_from_video_v1.py</code></a></summary>Iteratively reads and displays video frames (starting from the first frame) until the user indicates otherwise or until the last frame has been read. from a specified video. Takes the file name (without extension) as a command line argument. Also serves as an introduction to reading video frames and displaying images using Matplotlib. An output can be seen <a href="https://github.com/pranigopu/computerVision/blob/main/videoProcessing/output--pull_images_from_video_v2.png">here</a></details>
4. <details><summary><a href="https://github.com/pranigopu/computerVision/blob/main/videoProcessing/pull_images_from_video_v2.py"><code>pull_images_from_video_v2.py</code></a></summary>Reads and displays a specified number of video frames (starting from the first frame) evenly spread across the video. from a specified video. Takes the file name (without extension) and the number of frames to display as command line arguments. Advances the conceptual and practical grasp of the ideas introduced in <code>pull_images_from_video_v1.py</code>.</details>
5. <details><summary><a href="https://github.com/pranigopu/computerVision/blob/main/videoProcessing/add_image_annotations_v1.py"><code>add_image_annotations_v1.py</code></a></summary>Reads and displays a specified video frame and adds bounding boxes according to the annotations in <code>annotations.csv</code> (without differentiating categories). Takes the file name (without extension) and a frame number as command line arguments. Serves as an introduction to querying a dataset and adding bounding boxes.</details>
6. <details><summary><a href="https://github.com/pranigopu/computerVision/blob/main/videoProcessing/add_image_annotations_v2.py"><code>add_image_annotations_v2.py</code></a></summary>Reads and displays a specified video frame and adds bounding boxes according to the annotations in <code>annotations.csv</code>, using different colours to differentiate categories. Takes the file name (without extension) and a frame number as command line arguments. Just adds some flair to <code>add_image_annotations_v1.py</code>.</details>
7. <details><summary><a href="https://github.com/pranigopu/computerVision/blob/main/videoProcessing/add_video_annotations.py"><code>add_video_annotations.py</code></a></summary>Adds bounding boxes coloured according to categories for all the frames of the video and creates a new video from the annotated frames. Takes the file name (without extension) as a command line argument. Also serves as an introduction to OpenCV's video writer object.</details>
8. <details><summary><a href="https://github.com/pranigopu/computerVision/blob/main/videoProcessing/compress_video.py"><code>compress_video.py</code></a></summary>Uses FFmpeg (run as a subprocess) to compress a specified video. Is meant to compress the annotated video, but can be used more broadly too. Takes the file name (without extension) and the FFmpeg preset (explained in the source code) as command line arguments. Also serves as a gateway to some tools in video/audio processing, such as constant frame rate (CRF) and FFmpeg presets (both explained in the source code).</details>