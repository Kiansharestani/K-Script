# K Script 0.3

**K Script** is a simple and educational scripting language developed by Kian. This project includes a compiler ( [K_Script_0.3_Compiler.py(Don't Download)](K_Script_0.3_Compiler.py) ) and a quick start guide for writing basic programs.
### Warning !!
- **K Script Version 0.3 now is not puplished. please wait until 7 June 2026 for puplish K Script 0.3 .**
---

## What's New in 0.3

- **File and Directory Management:** Read, write, delete, check existence, list contents, get size, and more for files and directories.
- **Advanced HTTP Requests:** Support for GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS, plus direct JSON and text fetching.
- **Clipboard Functions:** Copy, paste, and clear clipboard content.
- **Mouse and Keyboard Functions:** Click, move, get position, scroll, drag, double-click, and key press detection.
- **System Information:** Get detailed system and Python environment info.
- **GUI Functions:** Create windows, show text, and add buttons using Tkinter.
- **Hardware Access:** Webcam capture, microphone recording, play audio, and show images.
- **Text, Binary, and JSON File Utilities:** Create, read, and write files in various formats.
- **Improved Error Handling:** More robust error messages and handling throughout.
- **Version and Developer Info:** Functions to get version and developer details.
- **Cleaner, More Modular Codebase:** Over 700 lines of organized code.

---

## Major Differences from 0.2

- Many new functions for file, directory, system, mouse, keyboard, and clipboard operations.
- Full support for all HTTP request types and direct JSON/text fetching.
- GUI and hardware-related functions (webcam, microphone, image, audio).
- Version and developer info functions.
- Much larger and more professional codebase.

---

## Features

- Simple and easy-to-understand syntax  
- Great for learning programming basics  
- Supports variables, printing output, and getting user input  
- Full HTTP request support  
- Terminal and system commands  
- Dynamic code execution  
- Module importing  
- File and directory management  
- Clipboard, mouse, and keyboard utilities  
- GUI and hardware functions

---

## Quick Start

### 1. Download the Compiler
1. Download And Install New Oficial [python](python.org)
2. Download the K Script compiler from:

- [GitHub](https://github.com/Kiansharestani/K-Script-compiler)
- [Google Sites](https://sites.google.com/view/download-k-script-compiler)

Place the compiler file in your project folder and rename it to `K_Script.py`.

### 2. Create a Script File

Create a file with the `.ks` Format and write your code.

### 3. Example Code

```python
from K_Script import *
prn("Hello, World")
```

---

## Some Important 0.3 Functions

```python
# File management
file_write("test.txt", "Hello!", "w")
content = file_read("test.txt")
delete_file("test.txt")

# Advanced HTTP requests
result = request_put("https://example.com", data={"a":1})
json_data = request_json("https://api.example.com/data")

# Clipboard
copy_to_clipboard("Copied text")
text = paste_from_clipboard()

# Mouse and keyboard
mouse_move(100, 200)
if keyboard("a"):
    prn("A key pressed")

# System info
info = system_info()
prn(info["system"])

# GUI window
create_new_window_with_text("Title", "400x300", True, "Hello!")

# Webcam and microphone
webcam_capture("photo.jpg")
microphone_record("audio.wav", duration=3)
```

---

## Developer

- Developed by Kian
- Related projects: KDB

---

## License

All rights reserved © Kian Script Software Foundation (2026)
