import re
import subprocess
from time import sleep
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_DIRS = ['./memo/', './tests/']


class EventHandler(FileSystemEventHandler):
    def is_compiled_file(filename):
        return re.search('\.py\.[0-9a-f]{20,}\.py$', filename, re.IGNORECASE)

    def log(event):
        current_time = datetime.now().strftime('%H:%M:%S.%f')
        print(f'[{current_time}] \'{event.src_path}\' {event.event_type}.')

    def on_created(self, event):
        if EventHandler.is_compiled_file(event.src_path):
            return

        EventHandler.log(event)

    def on_modified(self, event):
        if event.is_directory or EventHandler.is_compiled_file(event.src_path):
            return

        subprocess.run(['pipenv', 'run', 'test'])
        EventHandler.log(event)

    def on_deleted(self, event):
        if EventHandler.is_compiled_file(event.src_path):
            return

        EventHandler.log(event)


def main():
    observer = Observer()
    event_handler = EventHandler()
    for path in WATCH_DIRS:
        observer.schedule(event_handler, path, recursive=True)
    observer.start()

    # start message
    print('===================')
    print('::: WATCH START :::')
    print('===================')
    print('')
    print('watching paths:')
    for path in WATCH_DIRS:
        print(f'  {path}')
    print('')

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
