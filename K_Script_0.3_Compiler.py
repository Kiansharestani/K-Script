if not __name__ == "__main__" :
    def prn(text) :
        print(text)
    def inp(text) :
        return input(text)
    def stop(time) :
        import time
        if time == 0 :
            return
        elif time < 0 :
            raise ValueError("Time cannot be negative.")
        else :
            import time
        time.sleep(time)
    def clear() :
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    def terminal(bash) :
        import os
        os.system(bash)
    def is_main():
        if __name__ == "__main__":
            return True
        else:
            return False
    def shutdown() :
        import os
        if os.name == 'win32' or os.name == 'nt':
            os.system("shutdown /s /t 1")
    def restart() :
        import os
        import sys
        if os.name == 'win32' or os.name == 'nt':
            os.system("shutdown /r /t 1")
        if os.name == 'win32' or os.name == 'nt':
            os.system("shutdown /r /t 1")
        sys.exit()
    def eval(code) :
        try:
            exec(code)
        except Exception as e:
            print(f"K Script Error: {e}")
    def import_module(module_name):
        try:
            module = __import__(module_name)
            return module
        except ImportError as e:
            print(f"Error importing module {module_name}: {e}")
            return None
    def import_from(module_name, class_name):
        try:
            module = __import__(module_name, fromlist=[class_name])
            return getattr(module, class_name)
        except ImportError as e:
            print(f"Error importing {class_name} from {module_name}: {e}")
            return None
    def import_all(module_name):
        try:
            module = __import__(module_name)
            return {name: getattr(module, name) for name in dir(module) if not name.startswith('_')}
        except ImportError as e:
            print(f"Error importing all from {module_name}: {e}")
            return None
    def import_all_from(module_name):
        try:
            module = __import__(module_name)
            return {name: getattr(module, name) for name in dir(module) if not name.startswith('_')}
        except ImportError as e:
            print(f"Error importing all from {module_name}: {e}")
            return None
    def request_get(url):
        import requests
        try:
            response = requests.get(url)
            return {
                "status_code": response.status_code,
                "text": response.text,
                "headers": dict(response.headers),
                "ok": response.ok,
                "reason": response.reason,
                "url": response.url
            }
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return {
                "status_code": None,
                "text": None,
                "headers": None,
                "ok": False,
                "reason": str(e),
                "url": url
            }
    def request_post(url, data=None):
        import requests
        try:
            response = requests.post(url, data=data)
            return {
                "status_code": response.status_code,
                "text": response.text,
                "headers": dict(response.headers),
                "ok": response.ok,
                "reason": response.reason,
                "url": response.url
            }
        except requests.RequestException as e:
            print(f"Error posting to {url}: {e}")
            return {
                "status_code": None,
                "text": None,
                "headers": None,
                "ok": False,
                "reason": str(e),
                "url": url
            }
    def request_put(url, data=None):
        import requests
        try:
            response = requests.put(url, data=data)
            return {
                "status_code": response.status_code,
                "text": response.text,
                "headers": dict(response.headers),
                "ok": response.ok,
                "reason": response.reason,
                "url": response.url
            }
        except requests.RequestException as e:
            print(f"Error putting to {url}: {e}")
            return {
                "status_code": None,
                "text": None,
                "headers": None,
                "ok": False,
                "reason": str(e),
                "url": url
            }
    def request_delete(url):
        import requests
        try:
            response = requests.delete(url)
            return {
                "status_code": response.status_code,
                "text": response.text,
                "headers": dict(response.headers),
                "ok": response.ok,
                "reason": response.reason,
                "url": response.url
            }
        except requests.RequestException as e:
            print(f"Error deleting {url}: {e}")
            return {
                "status_code": None,
                "text": None,
                "headers": None,
                "ok": False,
                "reason": str(e),
                "url": url
            }
    def request_head(url):
        import requests
        try:
            response = requests.head(url)
            return {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "ok": response.ok,
                "reason": response.reason,
                "url": response.url
            }
        except requests.RequestException as e:
            print(f"Error fetching headers from {url}: {e}")
            return {
                "status_code": None,
                "headers": None,
                "ok": False,
                "reason": str(e),
                "url": url
            }
    def request_options(url):
        import requests
        try:
            response = requests.options(url)
            return {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "ok": response.ok,
                "reason": response.reason,
                "url": response.url
            }
        except requests.RequestException as e:
            print(f"Error fetching options from {url}: {e}")
            return {
                "status_code": None,
                "headers": None,
                "ok": False,
                "reason": str(e),
                "url": url
            }
    def request_patch(url, data=None):
        import requests
        try:
            response = requests.patch(url, data=data)
            return {
                "status_code": response.status_code,
                "text": response.text,
                "headers": dict(response.headers),
                "ok": response.ok,
                "reason": response.reason,
                "url": response.url
            }
        except requests.RequestException as e:
            print(f"Error patching {url}: {e}")
            return {
                "status_code": None,
                "text": None,
                "headers": None,
                "ok": False,
                "reason": str(e),
                "url": url
            }
    def request_json(url):
        import requests
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching JSON from {url}: {e}")
            return None
        except ValueError as e:
            print(f"Error parsing JSON from {url}: {e}")
            return None
    def request_text(url):
        import requests
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching text from {url}: {e}")
            return None
    def request_headers(url):
        import requests
        try:
            response = requests.head(url)
            response.raise_for_status()
            return dict(response.headers)
        except requests.RequestException as e:
            print(f"Error fetching headers from {url}: {e}")
            return None
    def request_status_code(url):
        import requests
        try:
            response = requests.get(url)
            return response.status_code
        except requests.RequestException as e:
            print(f"Error fetching status code from {url}: {e}")
            return None
    def request_ok(url):
        import requests
        try:
            response = requests.get(url)
            return response.ok
        except requests.RequestException as e:
            print(f"Error checking if {url} is OK: {e}")
            return False
    def request_reason(url):
        import requests
        try:
            response = requests.get(url)
            return response.reason
        except requests.RequestException as e:
            print(f"Error fetching reason from {url}: {e}")
            return None
    def request_url(url):
        import requests
        try:
            response = requests.get(url)
            return response.url
        except requests.RequestException as e:
            print(f"Error fetching URL from {url}: {e}")
            return None
    def file_open(file_path, mode, encoding):
        if not encoding:
            encoding = 'utf-8'
        try:
            file = open(file_path, mode, encoding=encoding)
        except FileNotFoundError:
            print(f"File {file_path} not found.")
            return None
        except IOError as e:
            print(f"Error opening file {file_path}: {e}")
            return None
    def file_read(file_path, encoding='utf-8'):
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except FileNotFoundError:
            print(f"File {file_path} not found.")
            return None
        except IOError as e:
            print(f"Error reading file {file_path}: {e}")
            return None
    def file_write(file_path, content, mode='w', encoding='utf-8'):
        if not encoding:
            encoding = 'utf-8'
        try:
            with open(file_path, mode, encoding=encoding) as file:
                file.write(content)
                return True
        except IOError as e:
            print(f"Error writing to file {file_path}: {e}")
            return False
    def is_file_exists(file_path):
        import os
        return os.path.isfile(file_path)
    def is_directory_exists(dir_path):
        import os
        return os.path.isdir(dir_path)
    def create_directory(dir_path):
        import os
        try:
            os.makedirs(dir_path, exist_ok=True)
            return True
        except OSError as e:
            print(f"Error creating directory {dir_path}: {e}")
            return False
    def delete_file(file_path):
        import os
        try:
            os.remove(file_path)
            return True
        except FileNotFoundError:
            print(f"File {file_path} not found.")
            return False
        except OSError as e:
            print(f"Error deleting file {file_path}: {e}")
            return False
    def delete_directory(dir_path):
        import os
        try:
            os.rmdir(dir_path)
            return True
        except FileNotFoundError:
            print(f"Directory {dir_path} not found.")
            return False
        except OSError as e:
            print(f"Error deleting directory {dir_path}: {e}")
            return False
    def list_directory(dir_path):
        import os
        try:
            return os.listdir(dir_path)
        except FileNotFoundError:
            print(f"Directory {dir_path} not found.")
            return None
        except OSError as e:
            print(f"Error listing directory {dir_path}: {e}")
            return None
    def get_current_directory():
        import os
        return os.getcwd()
    def set_current_directory(dir_path):
        import os
        try:
            os.chdir(dir_path)
            return True
        except FileNotFoundError:
            print(f"Directory {dir_path} not found.")
            return False
        except OSError as e:
            print(f"Error changing directory to {dir_path}: {e}")
            return False
    def get_file_size(file_path):
        import os
        try:
            return os.path.getsize(file_path)
        except FileNotFoundError:
            print(f"File {file_path} not found.")
            return None
        except OSError as e:
            print(f"Error getting size of file {file_path}: {e}")
            return None
    def get_directory_size(dir_path):
        import os
        total_size = 0
        try:
            for dirpath, dirnames, filenames in os.walk(dir_path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    total_size += os.path.getsize(fp)
            return total_size
        except FileNotFoundError:
            print(f"Directory {dir_path} not found.")
            return None
        except OSError as e:
            print(f"Error getting size of directory {dir_path}: {e}")
            return None
    def get_file_extension(file_path):
        import os
        _, ext = os.path.splitext(file_path)
        return ext if ext else None
    def get_file_name(file_path):
        import os
        return os.path.basename(file_path) if file_path else None
    def script_file_name() :
        return __name__
    def opinion_to_K_Script() :
        print("Thank you for opinioning K_Script. We hope you enjoy using it!")
        import webbrowser
        webbrowser.open("https://github.com/Kiansharestani/K_Script/issues")
    def K_Script_version() :
        return "0.3"
    def K_Script_version_number() :
        return 0.3
    def K_Script_version_name() :
        return "K_Script 0.3"
    def K_Script_version_date() :
        return "2023-10-01"
    def K_Script_version_info() :
        return {
            "version": K_Script_version(),
            "version_number": K_Script_version_number(),
            "version_name": K_Script_version_name(),
            "version_date": K_Script_version_date()
        }
    def K_Script_version_full() :
        return f"{K_Script_version_name()} ({K_Script_version_number()}) - {K_Script_version_date()}"
    def K_Script_version_full_info() :
        return {
            "full_version": K_Script_version_full(),
            "version_info": K_Script_version_info()
        }
    def K_Script_Documentation() :
        import webbrowser
        webbrowser.open("https://github.com/Kiansharestani/K_Script/README.md")
    def K_Script_Codes() :
        return "0.3 version compiler : +730 Lines Codes !!"
    def K_Script_Compiler() :
        import webbrowser
        webbrowser.open("https://github.com/Kiansharestani/K_Script/realsess/0.3/K_Script_0.3_Compiler.py")
    def K_Script_Developer() :
        print("K_Script Developer: Kian Sharestani")
    def K_Script_Developer_GitHub() :
        import webbrowser
        webbrowser.open("https://github.com/Kiansharestani")
    def K_Script_Developer_Website() :
        import webbrowser
        webbrowser.open("https://kiansharestani.github.io")
    def K_Script_Developer_Email() :
        print("K_Script Developer Email: ksharestani@gmail.com")
    def create_new_empty_window(title, geometry, resizable):
        import tkinter as tk
        root = tk.Tk()
        root.title(title)
        root.resizable(resizable, resizable)
        try :
            root.geometry(geometry)
        except tk.TclError:
            print("Invalid geometry format. Use 'widthxheight' (e.g., '800x600').")
            return None
        root.mainloop()
    def create_new_window_with_text(title, geometry, resizable, text):
        import tkinter as tk
        root = tk.Tk()
        root.title(title)
        root.resizable(resizable, resizable)
        try:
            root.geometry(geometry)
        except tk.TclError:
            print("Invalid geometry format. Use 'widthxheight' (e.g., '800x600').")
            return None
        text_widget = tk.Text(root)
        text_widget.insert(tk.END, text)
        text_widget.pack(expand=True, fill=tk.BOTH)
        root.mainloop()
    def system_info():
        import platform
        return {
            "system": platform.system(),
            "node": platform.node(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "architecture": platform.architecture(),
            "CPU" : platform.processor(),
            "platform": platform.platform(),
            "python_version": platform.python_version(),
            "python_implementation": platform.python_implementation(),
            "python_build": platform.python_build(),
            "python_compiler": platform.python_compiler(),
            "python_branch": platform.python_branch(),
            "python_revision": platform.python_revision(),
            "python_version_tuple": platform.python_version_tuple(),
            "python_version_info": platform.python_version_info
        }
    def keyboard(key):
        import keyboard
        try:
            if keyboard.is_pressed(key):
                return True
            else:
                return False
        except Exception as e:
            print(f"Error checking key {key}: {e}")
            return False
    def mouse_click(button):
        import mouse
        try:
            if mouse.is_pressed(button):
                return True
            else:
                return False
        except Exception as e:
            print(f"Error checking mouse button {button}: {e}")
            return False
    def mouse_position():
        import mouse
        try:
            return mouse.get_position()
        except Exception as e:
            print(f"Error getting mouse position: {e}")
            return None
    def mouse_scroll(direction):
        import mouse
        try:
            if direction == 'up':
                mouse.wheel(1)
            elif direction == 'down':
                mouse.wheel(-1)
            else:
                print("Invalid direction. Use 'up' or 'down'.")
        except Exception as e:
            print(f"Error scrolling mouse: {e}")
    def mouse_move(x, y):
        import mouse
        try:
            mouse.move(x, y)
        except Exception as e:
            print(f"Error moving mouse to ({x}, {y}): {e}")
    def mouse_click_at(x, y, button='left'):
        import mouse
        try:
            mouse.move(x, y)
            if button == 'left':
                mouse.click(mouse.LEFT)
            elif button == 'right':
                mouse.click(mouse.RIGHT)
            elif button == 'middle':
                mouse.click(mouse.MIDDLE)
            else:
                print("Invalid button. Use 'left', 'right', or 'middle'.")
        except Exception as e:
            print(f"Error clicking mouse at ({x}, {y}): {e}")
    def mouse_drag(x, y):
        import mouse
        try:
            mouse.drag(x, y)
        except Exception as e:
            print(f"Error dragging mouse to ({x}, {y}): {e}")
    def mouse_double_click(x, y, button='left'):
        import mouse
        try:
            mouse.move(x, y)
            if button == 'left':
                mouse.double_click(mouse.LEFT)
            elif button == 'right':
                mouse.double_click(mouse.RIGHT)
            elif button == 'middle':
                mouse.double_click(mouse.MIDDLE)
            else:
                print("Invalid button. Use 'left', 'right', or 'middle'.")
        except Exception as e:
            print(f"Error double-clicking mouse at ({x}, {y}): {e}")
    def create_window_with_button(title, geometry, resizable, button_text, button_command):
        if button_command.endswith('()'):
            button_command = button_command[:-2]
        else :
            pass
        import tkinter as tk
        root = tk.Tk()
        root.title(title)
        root.resizable(resizable, resizable)
        try:
            root.geometry(geometry)
        except tk.TclError:
            print("Invalid geometry format. Use 'widthxheight' (e.g., '800x600').")
            return None
        button = tk.Button(root, text=button_text, command=button_command)
        button.pack(expand=True, fill=tk.BOTH)
        root.mainloop()
    def internet_conection_status() :
        import requests
        response = requests.get("https://kiansharestani.github.io/", timeout=10)
        if response.status_code == 200 or 403 or 404 or 500 or 502 or 503 or 504 or 505 or 511 or 521 or 522 or 523 or 524 or 525 or 526 or 527 or 528 or 529 or 530 or 531 or 532 or 533 or 534 or 535 or 536 or 537 or 538 or 539 or 540 or 541 or 542 or 543 or 544 or 545 or 546 or 547 or 548 or 549 or 550 :
            return True
        else :
            return False
    def copy_to_clipboard(text):
        import pyperclip
        try:
            pyperclip.copy(text)
        except Exception as e:
            print(f"Error copying text to clipboard: {e}")
    def paste_from_clipboard():
        import pyperclip
        try:
            return pyperclip.paste()
        except Exception as e:
            print(f"Error pasting text from clipboard: {e}")
            return None
    def clear_clipboard():
        import pyperclip
        try:
            pyperclip.copy('')
        except Exception as e:
            print(f"Error clearing clipboard: {e}")
    def webcam_capture(output_file):
        import cv2
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not open webcam.")
            return False
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(output_file, frame)
            cap.release()
            cv2.destroyAllWindows()
            return True
    def microphone_record(output_file, duration=5):
        import sounddevice as sd
        import numpy as np
        import wave
        fs = 44100
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
        sd.wait()
        with wave.open(output_file, 'wb') as wf:
            wf.setnchannels(2)
            wf.setsampwidth(2)
            wf.setframerate(fs)
            wf.writeframes(recording.tobytes())
        return None
    def show_image(image_path):
        from PIL import Image
        import matplotlib.pyplot as plt
        try:
            img = Image.open(image_path)
            plt.imshow(img)
            plt.axis('off')
            plt.show()
        except Exception as e:
            print(f"Error displaying image {image_path}: {e}")
    def play_audio(audio_file):
        import playsound
        try:
            playsound.playsound(audio_file)
        except Exception as e:
            print(f"Error playing audio file {audio_file}: {e}")
    def create_text_file(file_path, content):
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            return True
        except IOError as e:
            print(f"Error creating text file {file_path}: {e}")
            return False

    def read_text_file(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Text file {file_path} not found.")
            return None
    def create_binary_file(file_path, content):
        try:
            with open(file_path, 'wb') as file:
                file.write(content)
            return True
        except IOError as e:
            print(f"Error creating binary file {file_path}: {e}")
            return False
    def read_binary_file(file_path):
        try:
            with open(file_path, 'rb') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Binary file {file_path} not found.")
            return None
        except IOError as e:
            print(f"Error reading binary file {file_path}: {e}")
            return None
    def create_json_file(file_path, data):
        import json
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            return True
        except IOError as e:
            print(f"Error creating JSON file {file_path}: {e}")
            return False
    def read_json_file(file_path):
        import json
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"JSON file {file_path} not found.")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file {file_path}: {e}")
            return None
else :
    def compiler_error() :
        import time
        print("This Code is not for User Use. This Program is The K_Script Compiler. Please Don't Edit or Delete This File.")
        time.sleep(5)
    compiler_error()