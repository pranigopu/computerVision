<h1>WORKING NOTES</h1>

---

**Contents**:

- [Installing FFmpeg](#installing-ffmpeg)
  - [Option 1: Use a Python binding](#option-1-use-a-python-binding)
  - [Option 2: Install FFmpeg in the system (Windows)](#option-2-install-ffmpeg-in-the-system-windows)
- [Issues with commands through Python's subprocess module](#issues-with-commands-through-pythons-subprocess-module)
  - [Issue history](#issue-history)
  - [An easy solution](#an-easy-solution)

---

# Installing FFmpeg
## Option 1: Use a Python binding
I used `ffmpeg-python`, but you can also use `python-ffmpeg`, which is a different implementation for a similar purpose. To install `ffmpeg-python`, enter `pip install ffmpeg-python` in the terminal/command prompt (make sure the Python package installed `pip` is installed first). Of course, with this option, you can access FFmpeg's functionalities only through Python.

## Option 2: Install FFmpeg in the system (Windows)
**FFmpeg.org** only provides source code, which means you must seek an FFmpeg build if you want FFmpeg compiled and ready. For a Windows build, check `ffmpeg-release-full.7z` [here](https://www.gyan.dev/ffmpeg/builds/#release-builds). Notice the `.7z` extension; this is the archive format of [7-Zip](https://www.7-zip.org/), a free and open-source file archiver. Hence, to extract the aforementioned FFmpeg build, install 7-Zip and use it on the build by right-clicking on the build's ZIP file and selecting the 7-Zip option (which becomes available once 7-Zip is installed). Once extracted, you get an extracted `ffmpeg-release-full.7z` folder: rename it to `FFmpeg` and move it to the hard-drive's root directory. Then, to make the FFmpeg's functionalities accessible to a script or a command line interface (e.g. through Command Prompt), you must set the [`PATH` variable](https://github.com/pranigopu/computerVision/information.md#path-variable-in-windows) (an environment variable in Windows) to the path of the FFmpeg build's executables. This can be done in Windows command line as follows:

```
setx /m PATH "C:\ffmpeg\bin;%PATH%"
```

<details>
<summary>Click for explanation</summary>
<code>setx</code> creates or modifies environment variables in the user or system environment, without requiring programming or scripting. <code>/m</code> specifies that the variable must be set in the system environment (this must be specified since the default setting is the local environment, i.e. for the current user's environment only). Reference: <a href="https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/setx"><code>setx</code> from <b>learn.microsoft.com</b> (documentation)</a>.
<br><br>
<code>PATH</code> is the environment variable which must be reassigned. <code>"C:\ffmpeg\bin;%PATH%"</code> is the value that must be assigned to the <code>PATH</code> variable (to learn more about the use of the percent symbol % in Windows command line to represent variable values, click <a href="https://github.com/pranigopu/computerVision/information.md#percent-character-in-windows-command-line">here</a>). Here, <code>%PATH%</code> represents the value of the <code>PATH</code> variable, which is a string of folder paths separated by semicolons. Hence, <code>"C:\ffmpeg\bin;%PATH%"</code> is actually a string where the folder path <code>C:\ffmpeg\bin</code> is concatenated (along with a semicolon to separate it from other folder paths) to the current value of the <code>PATH</code> variable, which is itself a string of folder paths separated by semicolons.
</details>

---

Doing this will make `ffmpeg` a usable command.

---

> **References**:
> 
> - [_Easily Download and Install FFmpeg on a Windows PC_ by Nicole Levine from **wikiHow.com**](https://www.wikihow.com/Install-FFmpeg-on-Windows)
> - [7-zip.org](https://www.7-zip.org/)
> - [_FFmpeg Builds - binaries for Windows_ by Gyan Doshi from **CODEX FFMPEG**](https://www.gyan.dev/ffmpeg/builds/#release-builds)

# Issues with commands through Python's subprocess module
## Issue history
When first trying to run FFmpeg through the Python binding `ffmpeg-python`, the interpreter threw the following error:

<details>
<summary>Click to see error message</summary>
<pre>
Traceback (most recent call last):
  File "C:\Users\prana\Documents\computerVision\videoProcessing\convert_from_mov_to_mp4.py", line 12, in <module>
    ffmpeg.input(inputFile).output(name + '.mp4').run()
  File "C:\Users\prana\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\ffmpeg\_run.py", line 313, in run
    process = run_async(
              ^^^^^^^^^^
  File "C:\Users\prana\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\ffmpeg\_run.py", line 284, in run_async
    return subprocess.Popen(
           ^^^^^^^^^^^^^^^^^
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified
</pre>
</details>

Since my video file's given path was correct, I tried running 'dir' to check the working of the `subprocess` module itself:

<details>
<summary>Click to see error message</summary>
<pre>
Traceback (most recent call last):
  File "C:\Users\prana\Documents\computerVision\videoProcessing\convert_mov_to_mp4.py", line 12, in <module>
    subprocess.call(['dir'])
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\subprocess.py", line 389, in call
    with Popen(*popenargs, **kwargs) as p:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\subprocess.py", line 1538, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [WinError 2] The system cannot find the file specified
</pre>
</details>

Now, note that both `dir` and the previous `ffmpeg` commands involve accessing files or folders, and since the error was a `FileNotFoundError`, I tried running a command that does not involve accessing files or folders, namely `getmac`, which displays the MAC address of every network controller on a system. This command worked as intended; this is a hint to the cause of the problem, but I shall pursue this hint later.

## An easy solution
One fix for the `FileNotFoundError` was to use the following:

**For using FFmpeg via the** `ffmpeg-python` **Python binding**:

```python
subprocess.run(['cmd', '/c'])
ffmpeg.input(inputFile).output(outputFile).run()
```

**For the** `dir` **command**:

```python
subprocess.run(['cmd', '/c', ''])
```

Hence, a solution was to prefix the commands with `cmd /c` (note that `cmd` is a command while `/c` is an option within this command); to see information on `cmd`, enter `cmd /?` in Command Prompt. According to this information, `cmd` starts a new instance of the Windows XP command interpreter, whereas `/c` carries out the command specified by the following string and then terminates. This fixed the issue previously seen.