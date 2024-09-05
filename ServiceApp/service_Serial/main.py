import sys
sys.path.append("./")

import serial
import serial.tools.list_ports
import RTRQ.Node.Region_Serial as Node
import threading
import time
import subprocess

class obj_Serial:
    def __init__(self,id_obj):
        self.root = serial.Serial()     
        self.listPort = self.getListport()
        self.listBaud = [9600,115200]
        self.port     = self.listPort[0]
        self.baud     = self.listBaud[1]
        self.timeout  = 0

        self.stop  = threading.Event()
        self.pause = threading.Event()
        self.ex_wait = threading.Event()
        self.id = id_obj

    def getListport(self):
        listPort = []
        for data in list(serial.tools.list_ports.comports()):
            data = str(data).split()[0].strip()
            listPort.append(data)
        return listPort
    
    def configure_Serial(self,data:list):
        self.port    = data[0]
        self.baud    = int(data[1])
        self.timeout = int(data[2])

    def open(self):
        if self.root.is_open:
            return
        self.root.port = self.port
        self.root.baudrate = self.baud
        self.root.timeout = self.timeout
        self.root.open()

    def close(self):
        if self.root.is_open:
            self.root.close()

    def write_data(self,data):
        try:
            data = str(data).encode()
            self.root.write(data)
            self.ex_wait.clear()
        except Exception as e:
            print(f"Error writing data: {e}")

    def read_data(self):
        try:
            if self.root.in_waiting > 0:
                Node.Node_handlereadData.value = self.root.readline().decode().strip()
                print(Node.Node_handlereadData.value)
                self.ex_wait.set()
        except:
            None

    def loop_Serial(self):
        while not self.stop.is_set():
            self.pause.wait()
            self.read_data()
            time.sleep(0.001)
        self.close()

    def startSerial(self):
        if not self.root.is_open:
            self.stop.clear()
            self.pause.set()
            self.open()
            time.sleep(1)
            threading.Thread(target=self.loop_Serial,daemon=True).start()

    def stopSerial(self):
        self.stop.set()

    def pauseSerial(self):
        self.pause.clear()

    def resumeSerial(self):
        self.pause.set()

    

hello = obj_Serial("v1")
hello.ex_wait.set()
Node.Node_handleStart.add_callback(hello.id,lambda data: hello.startSerial())
Node.Node_handleStop.add_callback(hello.id,lambda data: hello.stopSerial())
Node.Node_handleConfigure.add_callback(hello.id,hello.configure_Serial)
Node.Node_handlewriteData.add_callback(hello.id,hello.write_data)


# while 1:
#     hello.ex_wait.wait()
#     data = input("user : ")
#     if "start" in data :
#         hello.startSerial()
#     elif "setbaud" in data:
#         Node.Node_handleConfigure.value = [hello.port,data.split()[1],hello.timeout]
#     elif "stop" in data:
#         hello.stopSerial()
#     elif "pause" in data:
#         hello.pauseSerial()
#     elif "resume" in data:
#         hello.resumeSerial()
#     elif "clear" in data:
#         subprocess.run('clear', shell=True) 
#     else:
#         hello.write_data(data)