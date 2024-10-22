# CONVERT MOV FILE TO MP4
# Converts a given MOV to MP4

# NOTE: Both the versions achieve the same effect.

import subprocess

# EXTRA: For passing arguments to this script in command line:
from sys import argv
'''
For notes on my use of `argv` from `sys`, see...
"Use of `argv` from `sys` in my video processing programs"
... in "https://github.com/pranigopu/computerVision/blob/main/videoProcessing/workingNotes.md"
'''

#================================================
# Version 1

import ffmpeg # Only version 1 needs this import
inputFile = '../videos/' + argv[1] + '.mov'
outputFile = '../videos/' + argv[1] + '.mp4'
subprocess.run(['cmd', '/c'])
ffmpeg.input(inputFile).output(outputFile).run()

'''
NOTE: Why use `subprocess.run(['cmd', '/c'])`? See...
"Issues with commands through Python's subprocess module"
... in "https://github.com/pranigopu/computerVision/blob/main/videoProcessing/workingNotes.md".
'''

#================================================
# Version 2
# The same as version 1 except for the first and last lines.
'''
inputFile = '../data/' + argv[1] + '.mov'
outputFile = '../data/' + argv[1] + '.mp4'
subprocess.run(['ffmpeg', '-i', inputFile, outputFile])
'''

#================================================
# Comparing the two code versions

'''
Version 1 offers coding convenience the Python binding for FFmpeg
(here, the Python binding used was `ffmpeg-python`, but there are
others available). Note that both versions require you to install
FFmpeg in your system, since `ffmpeg-python` only acts as a
wrapper for FFmpeg.
'''