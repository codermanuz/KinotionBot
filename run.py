import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"{event.src_path} o'zgartirildi. Skript qayta ishga tushirilmoqda\.\.\.")
            subprocess.run(["python", self.script])

if __name__ == "__main__":
    path = "."  # Kuzatiladigan papka
    script = "main.py"  # Kuzatiladigan skript nomi

    event_handler = ChangeHandler(script)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()