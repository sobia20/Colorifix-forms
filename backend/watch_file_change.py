import time  
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler  


if __name__ == '__main__':
    observer = Observer()
    observer.schedule(PatternMatchingEventHandler(), path='./data.json')
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()