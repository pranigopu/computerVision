<h1>INFORMATION</h1>

---

**Contents**

- [Python-related](#python-related)
  - [`pip`](#pip)
  - [`sys`](#sys)
  - [Unpacking operation](#unpacking-operation)
- [Windows-related](#windows-related)
  - [Environment variables in Windows](#environment-variables-in-windows)
  - [`PATH` variable in Windows](#path-variable-in-windows)
  - [Percent character in Windows command line](#percent-character-in-windows-command-line)
- [Multimedia-related](#multimedia-related)
  - [Video and audio codecs](#video-and-audio-codecs)
  - [FOURCC](#fourcc)
- [General](#general)
  - [7-Zip](#7-zip)
  - [Codebase](#codebase)
  - [Runtime environment](#runtime-environment)

---

# Python-related
## `pip`
`pip` is the package installer for Python and can be used to install packages from the Python Package Index and other indexes.

> **Reference**: [`pip` (documentation)](https://pypi.org/project/pip/)

## `sys`
The `sys` module in Python provides various functions and variables that are used to manipulate different parts of the Python [runtime environment](#runtime-environment), i.e. the software platform through which Python scripts are run. It allows operating directly on the interpreter as it provides access to the variables and functions that interact directly with the interpreter. For example, the `sys` module provides the variables `stdin`, `stdout` and `stderr` for better control over input or output. Specifically, `stdin` can be used to get input from the command line directly.

> **Reference**: [_Python sys Module_ from **GeeksForGeeks.org**](https://www.geeksforgeeks.org/python-sys-module/)

## Unpacking operation
The unpacking operation is the asterisk (*) prefixed to a list, tuple or string so that its elements can be passed as separate parameters to a function. Examples of usage are as follows:

1.<br>

```python
def myFunction(a, b, c):
  print(a + b + c)

myList = [1, 2, 3]
myFunction(*myList)
```

Output:

`6`

2.<br>

```python
def myFunction(a, b, c):
  print(c + b + c)

myString = 'cat'
myFunction(*myString)
```

Output:

`tac`

> **References**
>
> - [_Packing and Unpacking Arguments in Python_ from **GeeksForGeeks.org**](https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/)
> - [_How to Use the Unpacking Operators (*, **) in Python?_ by Daniel Diaz from **geekflare.com**](https://geekflare.com/python-unpacking-operators/)

# Windows-related
## Environment variables in Windows
Environment variables can be used to refer to important files or information, e.g. as pointers to important directories, or as storage for information about your computer (e.g. version of Windows, the number of available processor cores, etc.). Environment variables be read by any program or script that runs on your computer.

**NOTE**: _Environment variables can be defined either for individual user accounts or on a system-wide basis (i.e. for all current and potential user accounts)._

> **Reference**: [_How to Edit Environment Variables on Windows 10 or 11_ by Nick Lewis from **HowToGeek.com**](https://www.howtogeek.com/787217/how-to-edit-environment-variables-on-windows-10-or-11/)

## `PATH` variable in Windows
A key [environment variable](#environment-variables-in-windows) is `PATH`, which defines the folders that must be checked for executables when a command is run in a terminal or a script. E.g. you can type `notepad` into Command Prompt to launch it immediately, whereas you get an error if you type `chrome`; this is because the Notepad executable is in a folder defined in the `PATH` while the Chrome executable is not.

**NOTE**: _An executable can be run from Command Prompt by specifying its relative path (relative to the current working directory). However,_ `PATH` _makes certain executables as accessible as commands._

By default, `PATH` only points to a few Windows folders, but more can be added. A folder can be added to `PATH` through Command Prompt or through a GUI method (as explained [here](https://www.howtogeek.com/787217/how-to-edit-environment-variables-on-windows-10-or-11/#how-to-edit-environment-variables)). Note that `PATH` is in fact one long string, which means adding a folder to it amounts to concatenating the folder's path to the string of paths in `PATH` and then assigning `PATH` to the whole string after concatenatino. The folder paths in `PATH` are separated by semicolons.

> **Reference**: [_How to Edit Environment Variables on Windows 10 or 11_ by Nick Lewis from **HowToGeek.com**](https://www.howtogeek.com/787217/how-to-edit-environment-variables-on-windows-10-or-11/)

## Percent character in Windows command line
**NOTE**: _A CMD shell is an instance of the Windows' command interpreter_ `Cmd.exe`. _Applications like Command Prompt can be used to create a CMD shell and thereby access Windows' command line functionality. For convenience, I shall refer to Windows' command interpreter as CMD._

See the section "How the CMD shell command line parser evaluates variables" in [`syntax-percent.html` from **ss64.com**](https://ss64.com/nt/syntax-percent.html). To focus on a specific usage that I found useful to know about, if CMD finds a percent character (i.e. the % character), if the next character is anything other than another percent character, CMD treats everything up to the next percent sign as the name of a variable and replaces it with the value of that variable. For example, `%PATH%` replaces the name of the `PATH` variable (an environment variable in Windows) with its value (which is a string of folder paths separated by semicolons).

# Multimedia-related
## Video and audio codecs
**Codec = Encoder + Decoder**

A codec is software or hardware that compresses and decompresses digital video or audio (video codec for video and audio codec for audio). In the context of video/audio compression, codec is a portmanteau of encoder and decoder, while a device that only compresses is typically called an encoder, and one that only decompresses is a decoder.

**NOTE**: _The compression is typically lossy and thus the compressed video/audio file lacks some information present in the original file. Hence, the decompressed file has lower quality than the original uncompressed file because there is insufficient information to accurately reconstruct the original file._

- Audio codec examples: AAC, MP3, FLAC, WAV
- Video codec examples: H.264 (AVC), H.265 (HEVC), VP9, AV1

> **References**
>
> - [_Video codec_ from **Wikipedia**](https://en.wikipedia.org/wiki/Video_codec)
> - [_Unlocking the Mystery of Codecs: What You Need to Know Now_ by Paul Gill from **Lifewire.com**](https://www.lifewire.com/what-exactly-is-odec-2483426)
> - [_AAC, MP3, FLAC: Deep Dive into Audio Codec Nuances_ by Anne from **coconut.co**](https://www.coconut.co/articles/aac-mp3-flac-audio-codec-guide)
> - [_Understanding Codecs: A Beginner’s Guide to Audio & Video Conversion_ from **mediamojo.com**](https://themediamojo.com/index.php/codecs)

## FOURCC
**_Also wrttten as 4CC_**

FOURCC is short for "four character code", and is an identifier for a video codec, compression format, color or pixel format used in media files. Each for the four characters in this context is a 8 bits (i.e. 1 byte) value, thus a FOURCC always takes up exatly 32 bits (i.e. 4 bytes) in a file. The four characters in a FOURCC is generally limited to be within the human-readable characters in the ASCII table so that it is easy to convey and communicate what the FOURCCs are within a media file.

# General
## 7-Zip
7-Zip is a free and open-source file archiver, a utility used to place groups of files within compressed containers known as "archives". It is developed by Igor Pavlov and was first released in 1999. 7-Zip has its own archive format called 7z, but can read and write several others.

> **References**:
> 
> - [`7-Zip` from **Wikipedia**](https://en.wikipedia.org/wiki/7-Zip)
> [7-zip.org](https://www.7-zip.org/)

## Codebase
A codebase is the complete collection of source code used to build an application or project. It includes all the code, configurations, scripts, and documentation required to define and run the application.

> **Reference**: [_What is a Codebase_ from **PhoenixNap.com**](https://phoenixnap.com/glossary/what-is-a-codebase)

## Runtime environment
_Also called runtime system._

A software platform that provides an environment for executing code; hence, it is the hardware and software infrastructure that supports the running of a particular [codebase](#codebase) in real-time. Most programming languages have some form of runtime environment in which programs run, which addresses a number of issues that may include (among others):

- Application memory management
- How the program accesses variables
- Mechanisms for passing parameters between procedures
- Interfacing with the operating system (OS)

The compiler or interpreter makes assumptions depending on the nature of the runtime environment used to generate correct code. Typically, the runtime environment has some responsibility in setting up and managing the stack and heap (which are data structures respectively used to keep track function calls and allocate memory dynamically). The runtime environment may also have features such as garbage collection (i.e. the management of unused memory), threads (i.e. a well-defined segment of a process) or other dynamic features built into the language.

> **Reference**:
>
> - [_Runtime system_ from **Wikipedia**](https://en.wikipedia.org/wiki/Runtime_system)
> - [_Runtime Environment_ by Margaret Rouse from **Technopedia**](https://www.techopedia.com/definition/5466/runtime-environment-rte)