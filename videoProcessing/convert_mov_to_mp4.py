# NOTE: Both the versions achieve the same effect.

#================================================
# VERSION 1
import subprocess
import ffmpeg
name = '0001542f-7c670be8'
inputFile = name + '.mov'
outputFile = name + '.mp4'
subprocess.call(['cmd', '/c'])
ffmpeg.input(inputFile).output(outputFile).run()

'''
NOTE: Why use `subprocess.call(['cmd', '/c'])`? See...

"Issues with commands through Python's subprocess module"

... in the implementation notes.
'''

#================================================
# VERSION 2
# The same as version 1 except for the last line.
'''
import subprocess
import ffmpeg
name = '0001542f-7c670be8'
inputFile = name + '.mov'
outputFile = name + '.mp4'
subprocess.run(['ffmpeg', '-i', inputFile, outputFile])
'''

#================================================
# COMPARING THE TWO CODE VERSIONS
'''
The advantage of version 1 is that you only need to install
the Python binding for FFmpeg (here, the Python binding used
was `ffmpeg-python`, but there are others available), which
is very easy to do using PIP (e.g. `pip install ffmpeg-python`).
Version 2 is convenient if you already have FFmpeg installed
in your system; however installing FFmpeg directly into your
system is somewhat more complicated.
'''