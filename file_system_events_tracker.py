import sys
import time
import random
import os
import shutil
import FileSystemEventHandler
import Observer
import FileMovementHandler

from watchdog.observers
from watchdog.events


from_dir = "C:\Users\tartu\Desktop\arquivoss do projeto"




class FileEventHandler(fileSystemEventHandler):

    def on_created(self, event):
        print(f"Ola, {event.src_path} foi criado")

    def on_deleted(self, event):
        print (f"Opa! Alguem excluiu {event.src_path}!")


event_handler = FileMovementHandler()
observer = Observer() 
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()   

try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()    