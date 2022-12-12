import training_set_build
import file_details
import fileshiftwidget
import csv
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

# Overriding the event class and on_created function, the function get all the necessary details about the file and
# put them into a csv file, and then calls the function to start the UI


class Event(LoggingEventHandler):
    def on_created(self, event):
        cur_dits = file_details.file_dits()
        cls = training_set_build.file_classification(cur_dits)
        cur_dits.append(cls)
        if cur_dits[2] != event.src_path and not event.src_path.endswith((".tmp", "crdownload")):
            return
        with open("files_data.csv", "a", encoding="utf-8") as cur_file:
            writer = csv.writer(cur_file)
            writer.writerow(cur_dits)
        fileshiftwidget.new_file_alert(cur_dits)

# The main function, creates an observer over the Downloads directory and act when a file is created in the directory


if __name__ == "__main__":
    logging.basicConfig(filename='exemple.log', level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    event_handler = Event()
    observer = Observer()
    observer.schedule(event_handler, 'C:\\Users\\zeldi\\Downloads', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()