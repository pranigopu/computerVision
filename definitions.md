<h1> DEFINITIONS </h1>

---

**Contents**:

- [Language binding](#language-binding)
- [Glue code](#glue-code)
- [API](#api)
- [Pipe](#pipe)

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