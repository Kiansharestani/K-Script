if not __name__ == "__main__" :
    def init() :
        import time
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
        os.system("shutdown /s /t 1" if os.name == 'nt' else "shutdown -h now")
    def restart() :
        import os
        os.system("shutdown /r /t 1" if os.name == 'nt' else "shutdown -r now")
    def exit() :
        import sys
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

else :
    def compiler_error() :
        import time
        print("This Code is not for User Use. This Program is The K_Script Compiler. Please Don't Edit or Delete This File.")
        time.sleep(5)
    compiler_error()
