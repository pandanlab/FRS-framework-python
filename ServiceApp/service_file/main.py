import sys
sys.path.append("./")

import subprocess
import time
import os
import RTRQ.Node.Region_file as Node

# Thêm đường dẫn hiện tại vào sys.path
sys.path.append("./")

class obj_File:
    def __init__(self, id_obj):
        # Khởi tạo kernel driver
        self.id = id_obj
        None 

    def start(self):
        self.nameDriver = "myDriver.ko"
        self.link_fileDriver = os.path.join(os.path.dirname(__file__),self.nameDriver)
        self.runCMD(f"sudo insmod {self.link_fileDriver}")
        self.runCMD("sudo chmod 666 /dev/dev_kimsonfast")

    def runCMD(self,data):
        result = subprocess.run(data, shell=True, check=True)
        #print(result)

    def setLed(self,data):
        self.runCMD(f"echo {data} > /dev/dev_kimsonfast")

    def getButton(self,data):
        self.runCMD(f"head -n 1 /dev/dev_kimsonfast")

    def close(self):
        self.runCMD(f"sudo rmmod {str(self.nameDriver).split('.')[0]}")
        pass

# Khởi tạo đối tượng
hello = obj_File(1)
Node.Node_handleStart.add_callback(hello.id,lambda data: hello.start())
Node.Node_handleStop.add_callback(hello.id,lambda data: hello.close())
Node.Node_handlewriteData.add_callback(hello.id,hello.setLed)
Node.Node_handlereadData.add_callback(hello.id,hello.getButton)


# while 1:
#     data = input("user : ")
#     if("start" in data):
#         Node.Node_handleStart.active(data)
#     elif("stop" in data):
#         Node.Node_handleStop.active(data)
#     elif("write" in data):
#         Node.Node_handlewriteData.active(data)
#     elif("read" in data):
#         Node.Node_handlereadData.active(data)
#     else:
#         print(data)