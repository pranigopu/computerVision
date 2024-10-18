# CONVERT MOV FILE TO MP4
# Converts a given MOV to MP4

# NOTE: Both the versions achieve the same effect.

import subprocess
import ffmpeg

# EXTRA: For passing argument to this script in command line:
import sys
'''
For notes on my use of `sys` here, see...
"Use of `sys` in my video processing programs"
... in "https://github.com/pranigopu/computerVision/blob/main/videoProcessing/workingNotes.md"
'''

#================================================
# Version 1
name = sys.argv[1]
print(name, type(name))
inputFile = name + '.mov'
outputFile = name + '.mp4'
subprocess.run(['cmd', '/c'])
ffmpeg.input(inputFile).output(outputFile).run()

'''
NOTE: Why use `subprocess.run(['cmd', '/c'])`? See...
"Issues with commands through Python's subprocess module"
... in "https://github.com/pranigopu/computerVision/blob/main/videoProcessing/workingNotes.md".
'''

#================================================
# Version 2
# The same as version 1 except for the last line.
'''
name = sys.argv[1]
inputFile = name + '.mov'
outputFile = name + '.mp4'
subprocess.run(['ffmpeg', '-i', inputFile, outputFile])
'''

#================================================
# Comparing the two code versions
'''
The advantage of version 1 is that you only need to install
the Python binding for FFmpeg (here, the Python binding used
was `ffmpeg-python`, but there are others available), which
is very easy to do using pip (e.g. `pip install ffmpeg-python`).
Version 2 is convenient if you already have FFmpeg installed
in your system; however installing FFmpeg directly into your
system is somewhat more complicated.
'''