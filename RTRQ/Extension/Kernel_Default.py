import sys
sys.path.append("./")

import os
import importlib

class Kernel:
    def __init__(self) -> None:
        None

    def getlist_Region(self):
        list_node = []
        path = os.path.join(os.path.dirname(__file__),"..","Node")
        for data in os.listdir(path):
            if ".py" in data:
                data = data.split(".")[0].strip()
                list_node.append(data)
        return list_node

    def getlist_Node(self,Region):
        Region = importlib.import_module(f"RTRQ.Node.{Region}")
        List_Node = []
        global_vars = vars(Region) 
        for name,value in global_vars.items():
            if ("Node" in name or "handle" in name or "data" in name) and not "Default" in name:
                List_Node.append(name)
        return List_Node

    def get_Node(self,Region,Node):
        Region = importlib.import_module(f"RTRQ.Node.{Region}")
        Event_value = getattr((Region),Node).value
        return Event_value

    def set_Node(self,Region,Node,value):
        Region = importlib.import_module(f"RTRQ.Node.{Region}")
        getattr((Region),Node)._value = value

    def active_Node(self,Region,Node,value):
        Region = importlib.import_module(f"RTRQ.Node.{Region}")
        getattr((Region),Node).active(value)

    def register_Method(Self,Region,Node,name_method,method):
        Region = importlib.import_module(f"RTRQ.Node.{Region}")
        getattr((Region),Node).add_callback(name_method,method)

    def unregister_Method(Self,Region,Node,name):
        Region = importlib.import_module(f"RTRQ.Node.{Region}")
        getattr((Region),Node).rm_callback(name)

    def getlist_Method(Self,Region,Node):
        Region = importlib.import_module(f"RTRQ.Node.{Region}")
        data = getattr((Region),Node).list_callback()
        return data

kernel = Kernel()