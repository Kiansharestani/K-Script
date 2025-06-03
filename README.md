# K Script 0.2

**K Script** is a simple and educational scripting language developed by Kian. This project includes a compiler (`K_Script_0.2.py`) and a quick start guide for writing basic programs.

---

## What's New in 0.2

- Modular structure with more functions (including HTTP GET/POST support)
- HTTP GET and POST functions now return detailed response info:
  - `status_code`, `text`, `headers`, `ok`, `reason`, `url`
- Improved error handling and stability
- Enhanced compatibility with different environments
- Updated and expanded documentation
- Cleaner codebase and better organization

---

## Features

- Simple and easy-to-understand syntax  
- Great for learning programming basics  
- Supports variables, printing output, and getting user input  
- HTTP GET and POST request support with detailed response info
- Terminal and system commands:
  - `clear()` — Clear the terminal screen
  - `terminal(cmd)` — Run a terminal/command prompt command
  - `shutdown()` — Shutdown the computer
  - `restart()` — Restart the computer
  - `exit()` — Exit the script
  - `stop(seconds)` — Pause execution for a number of seconds
  - `is_main()` — Check if the script is running as main
- Dynamic code execution:
  - `eval(code)` — Evaluate and run Python code
- Module importing:
  - `import_module(name)`, `import_from(module, name)`, `import_all(module)`, `import_all_from(module)`

---

## Quick Start

### 1. Download the Compiler

Download the K Script compiler from:

- [GitHub](https://github.com/Kiansharestani/K-Script-compiler)
- [Google Sites](https://sites.google.com/view/download-k-script-compiler)

Place the compiler file in your project folder and rename it to `K_Script.py`.

### 2. Create a Script File

Create a file with the `.kpy`File and start write your code.

### 3. Example Code

```python
from K_Script import *
prn("Hello, World")
```

---

## Command Reference

### Define a Variable

```python
name = "Kian"
age = 20
greeting = f"Hello, {name}"
```

### Print Output

```python
prn("Hello, World")
```

### Get User Input

```python
user_input = inp("Enter your name: ")
```

### Pause Execution

```python
stop(2)  # pauses for 2 seconds
```

### Clear Terminal

```python
clear()
```

### Run Terminal Command

```python
terminal("echo Hello from terminal")
```

### Check if Main

```python
if is_main():
    prn("This is the main script.")
```

### Shutdown Computer

```python
shutdown()
```

### Restart Computer

```python
restart()
```

### Exit Program

```python
exit()
```

### Evaluate Python Code

```python
eval("prn('Evaluated code!')")
```

### Import Modules

```python
mod = import_module("math")
sqrt = import_from("math", "sqrt")
all_math = import_all("math")
all_from_math = import_all_from("math")
```

### Send a GET Request

```python
result = request_get("https://example.com")
prn(result["status_code"])
prn(result["text"])
```

### Send a POST Request

```python
result = request_post("https://example.com", data={"key": "value"})
prn(result["status_code"])
prn(result["text"])
```

---

## Notes

- K Script is developed in Python.
- Script files use the `.kpy` extension.
- You can set the language mode to Python in editors like Visual Studio Code.

---

## Developer

- Developed by Kian
- Related projects: KData

---

## License

All rights reserved © Kian Script Software Foundation (2026)
- Developed by Kian

---

## License

All rights reserved © Kian Script Software Foundation (2026)
