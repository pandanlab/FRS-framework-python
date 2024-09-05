import sys
sys.path.append("./")

from RTRQ.Extension.Kernel_Default import *
import RTRQ.Extension.DefineNode as Macro
import os

class obj_test:
    def __init__(self,id) -> None:
        self.linkfile = os.path.join(os.path.dirname(__file__),"asset","hello.txt")
        self.id = id
        None

    def writeData(self,data):
        with open(self.linkfile,"w") as file:
            file.write(data)
        None

    def readData(self,data):
        data = ""
        with open(self.linkfile,"r") as file:
            data = file.readline().strip()
            kernel.set_Node(Macro.Region_test,Macro.Node_test_handleRead,data)

        return data

hello = obj_test("testv1")
kernel.register_Method(Macro.Region_test,Macro.Node_test_handleWrite,hello.id,hello.writeData)
kernel.register_Method(Macro.Region_test,Macro.Node_test_handleRead,hello.id,hello.readData)