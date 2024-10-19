<h1>DEFINITIONS</h1>

---

**Contents**:

- [Language binding](#language-binding)
- [Glue code](#glue-code)
- [API](#api)
- [Pipe](#pipe)
- [Video and audio codecs](#video-and-audio-codecs)
  - [Codebase](#codebase)
  - [Runtime environment](#runtime-environment)

---

# Language binding
In programming, a binding for a given programming language is an [API](#api) that provides [glue code](#glue-code) that allows the given language to use a foreign library (a library written in another language) or an operating system service that is not native to the given language.

> **Reference**: [_Language binding_ from **Wikipedia](https://en.wikipedia.org/wiki/Language_binding)

# Glue code
In programming, a glue code is code that allows otherwise incompatible components to work with each other (i.e. interoperate).

> **Reference**: [_Glue code_ from **Wikipedia](https://en.wikipedia.org/wiki/Glue_code)

# API
An API, i.e. an application programming interface is a software that serves as an interface between two programs, thus allowing interoperability and interaction between these programs. There are two paradigms in APIs: synchronous and asynchronous. A synchronous API (sync API) blocks the code's execution until the API receives the code's request's response; hence, it deals in blocking operations. An asynchronous API (async API) does not block the code's execution and handles requests in the background; hence, it deals in non-blocking operations. Sync APIs ensure sequential execution of code, whereas async APIs ensure that the code does not need to remain idle when waiting for a response.

> **References**:
>
> - [_API_ from **Wikipedia**](https://en.wikipedia.org/wiki/API)
> - [_Synchronous vs. Asynchronous API Calls_ by BaseCS101 from **Medium.com**](https://medium.com/javarevisited/synchronous-vs-asynchronous-api-calls-2023-updated-e4fa7b851914)
> - [_The Differences Between Synchronous and Asynchronous APIs_ by Kristopher Sandoval from **NordicAPIs.com**](https://nordicapis.com/the-differences-between-synchronous-and-asynchronous-apis/)

# Pipe
A one-way connection between two processes wherein one process' output becomes the other's input.

> **Reference**: [_pipe() System call_ from **GeeksForGeeks.org**](https://www.geeksforgeeks.org/pipe-system-call/)

# Video and audio codecs
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