import os
import signal
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import sys
sys.path.append("./")

# Global variable to keep track of the running process
process = None

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global process  # Declare that we're using the global variable
        if event.is_directory:
            return
        
        # File changed, restart the script
        print("File changed, restarting script...")
        
        # Terminate the previous process if it exists
        if process and process.poll() is None:  # Check if process is still running
            process.send_signal(signal.SIGTERM)  # Send SIGTERM to stop it gracefully
            process.wait()  # Wait for the process to exit
        
        # Start a new process
        try:
            process = subprocess.Popen(["python", "FrontApp/extension/activate.py"])
        except Exception as e:
            print(f"Error running script: {e}")

# Path to the directory you want to monitor
directory_to_watch = 'FrontApp'

# Set up the watchdog observer
observer = Observer()
event_handler = ChangeHandler()
observer.schedule(event_handler, path=directory_to_watch, recursive=True)

# Start the observer
observer.start()