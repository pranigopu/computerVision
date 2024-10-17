<h1>INFORMATION</h1>

---

**Contents**

- [7-Zip](#7-zip)
- [`pip`](#pip)
- [Environment variables in Windows](#environment-variables-in-windows)
- [`PATH` variable in Windows](#path-variable-in-windows)
- [Percent character in Windows command line](#percent-character-in-windows-command-line)

---

# 7-Zip
7-Zip is a free and open-source file archiver, a utility used to place groups of files within compressed containers known as "archives". It is developed by Igor Pavlov and was first released in 1999. 7-Zip has its own archive format called 7z, but can read and write several others.

> **References**:
> 
> - [`7-Zip` from **Wikipedia**](https://en.wikipedia.org/wiki/7-Zip)
> [7-zip.org](https://www.7-zip.org/)

# `pip`
`pip` is the package installer for Python and can be used to install packages from the Python Package Index and other indexes.

> **Reference**: [`pip` (documentation)](https://pypi.org/project/pip/)

# Environment variables in Windows
Environment variables can be used to refer to important files or information, e.g. as pointers to important directories, or as storage for information about your computer (e.g. version of Windows, the number of available processor cores, etc.). Environment variables be read by any program or script that runs on your computer.

**NOTE**: _Environment variables can be defined either for individual user accounts or on a system-wide basis (i.e. for all current and potential user accounts)._

> **Reference**: [_How to Edit Environment Variables on Windows 10 or 11_ by Nick Lewis from **HowToGeek.com**](https://www.howtogeek.com/787217/how-to-edit-environment-variables-on-windows-10-or-11/)

# `PATH` variable in Windows
A key [environment variable](#environment-variables-in-windows) is `PATH`, which defines the folders that must be checked for executables when a command is run in a terminal or a script. E.g. you can type `notepad` into Command Prompt to launch it immediately, whereas you get an error if you type `chrome`; this is because the Notepad executable is in a folder defined in the `PATH` while the Chrome executable is not.

**NOTE**: _An executable can be run from Command Prompt by specifying its relative path (relative to the current working directory). However,_ `PATH` _makes certain executables as accessible as commands._

By default, `PATH` only points to a few Windows folders, but more can be added. A folder can be added to `PATH` through Command Prompt or through a GUI method (as explained [here](https://www.howtogeek.com/787217/how-to-edit-environment-variables-on-windows-10-or-11/#how-to-edit-environment-variables)). Note that `PATH` is in fact one long string, which means adding a folder to it amounts to concatenating the folder's path to the string of paths in `PATH` and then assigning `PATH` to the whole string after concatenatino. The folder paths in `PATH` are separated by semicolons.

> **Reference**: [_How to Edit Environment Variables on Windows 10 or 11_ by Nick Lewis from **HowToGeek.com**](https://www.howtogeek.com/787217/how-to-edit-environment-variables-on-windows-10-or-11/)

# Percent character in Windows command line
**NOTE**: _A CMD shell is an instance of the Windows' command interpreter_ `Cmd.exe`. _Applications like Command Prompt can be used to create a CMD shell and thereby access Windows' command line functionality. For convenience, I shall refer to Windows' command interpreter as CMD._

See the section "How the CMD shell command line parser evaluates variables" in [`syntax-percent.html` from **ss64.com**](https://ss64.com/nt/syntax-percent.html). To focus on a specific usage that I found useful to know about, if CMD finds a percent character (i.e. the % character), if the next character is anything other than another percent character, CMD treats everything up to the next percent sign as the name of a variable and replaces it with the value of that variable. For example, `%PATH%` replaces the name of the `PATH` variable (an environment variable in Windows) with its value (which is a string of folder paths separated by semicolons).