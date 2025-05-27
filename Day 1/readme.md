#  File Processor Async – Node.js Event Loop Demo

A micro project to demonstrate **Node.js asynchronous behavior** and how the **event loop** handles different types of asynchronous tasks using:

- File system operations (`fs.promises`)
- Timers (`setTimeout`)
- Immediate callbacks (`setImmediate`)
- Microtasks (`process.nextTick`)
- `async/await` for sequential async control

---

##  Purpose

This project is built to help understand:

- How asynchronous functions interact with the Node.js **event loop**
- The order of execution for:
  - Microtasks (e.g. `process.nextTick`)
  - Macrotasks (e.g. `setTimeout`, `setImmediate`)
  - Promises (`async/await`)
- How `fs.promises.readFile` is handled without blocking the main thread

---

##  Features Demonstrated

-  Asynchronous file reading using Promises (`fs.promises`)
-  Use of `async` / `await` for sequential flow
-  Execution order of `process.nextTick`, `setTimeout`, `setImmediate`
-  Console-based logs to visualize the Node.js event loop