import re
import subprocess
import os
from time import sleep
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent


class EventHandler(FileSystemEventHandler):
    def is_compiled_file(filename: str) -> bool:
        return bool(
            re.search('\.py\.[0-9a-f]{20,}\.py$', filename, re.IGNORECASE))

    def log(event: FileSystemEvent):
        current_time = datetime.now().strftime('%H:%M:%S.%f')
        print(f'[{current_time}] \'{event.src_path}\' {event.event_type}.')

    def on_created(self, event: FileSystemEvent):
        if EventHandler.is_compiled_file(event.src_path):
            return

        EventHandler.log(event)

    def on_modified(self, event: FileSystemEvent):
        if event.is_directory or EventHandler.is_compiled_file(event.src_path):
            return

        subprocess.run(['pipenv', 'run', 'typecheck', event.src_path])
        subprocess.run(['pipenv', 'run', 'test'])
        EventHandler.log(event)

    def on_deleted(self, event: FileSystemEvent):
        if EventHandler.is_compiled_file(event.src_path):
            return

        EventHandler.log(event)


def main():
    if not os.path.exists('./.env'):
        print('ERROR: Not found .env!')
        return

    watch_paths = os.getenv('WATCH_PATHS', '').split(',')
    observer = Observer()
    event_handler = EventHandler()
    for path in watch_paths:
        observer.schedule(event_handler, path, recursive=True)
    observer.start()

    # start message
    print('===================')
    print('::: WATCH START :::')
    print('===================')
    print('')
    print('watching paths:')
    for path in watch_paths:
        print(f'  {path}')
    print('')

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    main()
