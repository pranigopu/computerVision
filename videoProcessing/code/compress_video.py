# COMPRESS VIDEO

# To make commands to the system in a command shell:
import subprocess

# EXTRA: For passing argument to this script in command line:
import sys
'''
For notes on my use of `sys` here, see...
"Use of `sys` in my video processing programs"
... in "https://github.com/pranigopu/computerVision/blob/main/videoProcessing/workingNotes.md"
'''

#================================================
inputFileName = '../videos/' + sys.argv[1] + '.mp4'
outputFileName = inputFileName + '--compressed.mp4'
subprocess.run(['ffmpeg', '-i', inputFileName, '-crf', '18', '-preset', sys.argv[2], '-vcodec', 'libx264', outputFileName])
# NOTE 1: `-crf` here refers to "constant rate factor"; for more information, see: https://github.com/pranigopu/computerVision/blob/main/information.md#constant-rate-factor-crf
# NOTE 2: `-preset` refers to the encoding speed to compression ratio; for more information, see the longer note below note 4
# NOTE 3: `-vcodec` refers to video codec; for the definition of codecs, see: https://github.com/pranigopu/computerVision/blob/main/definitions.md#video-and-audio-codecs
# NOTE 4: `libx264` is the video codec used for compression

'''
FURTHER NOTE ON `-preset`:
A slower preset will provide better compression, which, for
example, if you target a certain file size or constant bit rate,
you will achieve better quality with a slower preset. Similarly,
for constant quality encoding, you will simply save bitrate by
choosing a slower preset.

Reference: https://trac.ffmpeg.org/wiki/Encode/H.264#a2.Chooseapresetandtune
'''