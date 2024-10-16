<h1>IMPLEMENTATION NOTES</h1>

---

**Contents**:

- [Issues with commands through Python's subprocess module](#issues-with-commands-through-pythons-subprocess-module)

---

# Issues with commands through Python's subprocess module
When first trying to run FFmpeg through the Python binding `ffmpeg-python`, the interpreter threw the following error:

<details>
<summary>Click to see error message</summary>

<code>
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
</code>

</details>

Since my video file's given path was correct, tried running 'dir', a regular command

```
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
```