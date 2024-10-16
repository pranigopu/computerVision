<h1>WORKING NOTES</h1>

---

**Contents**:

- [Issues with commands through Python's subprocess module](#issues-with-commands-through-pythons-subprocess-module)
  - [Issue history](#issue-history)
  - [An easy solution](#an-easy-solution)

---

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
<summary>CLick to see error message</summary>
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

Hence, a solution was to prefix the commands with `cmd /c` (note that `cmd` is a command while `/c` is an option within this command); to see information on `cmd`, enter `cmd /?` in Command Prompt. According to this information, `cmd` starts a new instance of the Windows XP command interpreter, whereas `/c` carries out the command specified by the following string and then terminates. This fixed the issues previously seen.