import sys
sys.path.append("./")

import FrontApp.Tool.tool_FigmaGenerate.module.getFigma  as getFigma
import FrontApp.Tool.tool_FigmaGenerate.module.system_os as system_os
import os

import tkinter as tk

def convert_newlines_to_text(text):
    return text.replace('\n', '\\n')

def get_dpi():
    root = tk.Tk()
    dpi = root.winfo_fpixels('1i')  # Lấy số pixel trên mỗi inch
    root.destroy()
    return dpi


def position(Horizontal,Vertical):
    h,v = "",""
    if  (str(Horizontal).lower()=="left") : h = "w"
    elif(str(Horizontal).lower()=="right"): h = "e"
    if  (str(Vertical).lower()=="top")    : v = "n"
    elif(str(Vertical).lower()=="bottom") : v = "s"
    rs = v+h
    if  (rs==""): 
        return "center"
    return rs

def weight(data):
    if(data==None):
        weight  = "normal"
        return weight
    else:
        weight  = "bold"
        return weight
    
def rgb_to_hex(r,g,b):
    r = int(round(r * 255, 20))
    g = int(round(g * 255, 20))
    b = int(round(b * 255, 20))
    return "#{:02X}{:02X}{:02X}".format(r, g, b)

class Node_Label:
    def __init__(self,obj_data,parent):
        self.root_tag = "tk"
        self.tag     = "Label"
        self.type    = "Empty"
        self.id      = obj_data["id"]
        self.name    = obj_data["name"]

        self.width   = obj_data["absoluteBoundingBox"]["width"]
        self.height  = obj_data["absoluteBoundingBox"]["height"]

        self.x       = float(obj_data["absoluteBoundingBox"]["x"]) - float(parent.x)
        self.y       = float(obj_data["absoluteBoundingBox"]["y"]) - float(parent.y)

        self.bg = parent.bg
        for data in obj_data["fills"]:
            if data["type"] == "SOLID":
                self.bg = rgb_to_hex(data["color"]["r"],data["color"]["g"],data["color"]["b"])
        self.text = ""

class Node_Button:
    def __init__(self,obj_data,parent):
        self.root_tag = "tk"
        self.tag     = "Button"
        self.type    = "Empty"
        self.id      = obj_data["id"]
        self.name    = obj_data["name"]

        self.width   = obj_data["absoluteBoundingBox"]["width"]
        self.height  = obj_data["absoluteBoundingBox"]["height"]

        self.x       = float(obj_data["absoluteBoundingBox"]["x"]) - float(parent.x)
        self.y       = float(obj_data["absoluteBoundingBox"]["y"]) - float(parent.y)

        self.bg = parent.bg
        for data in obj_data["fills"]:
            if data["type"] == "SOLID":
                self.bg = rgb_to_hex(data["color"]["r"],data["color"]["g"],data["color"]["b"])
        self.text = ""

class Node_LabelImage:
    def __init__(self,obj_data,parent):
        self.root_tag = "tk"
        self.tag     = "Label"
        self.type    = "Image"
        self.id      = obj_data["id"]
        self.name    = obj_data["name"]

        self.width   = obj_data["absoluteBoundingBox"]["width"]
        self.height  = obj_data["absoluteBoundingBox"]["height"]

        self.x       = float(obj_data["absoluteBoundingBox"]["x"]) - float(parent.x)
        self.y       = float(obj_data["absoluteBoundingBox"]["y"]) - float(parent.y)

        self.bg = parent.bg
        for data in obj_data["fills"]:
            if data["type"] == "SOLID":
                self.bg = rgb_to_hex(data["color"]["r"],data["color"]["g"],data["color"]["b"])
        self.text = ""

class Node_ButtonImage:
    def __init__(self,obj_data,parent):
        self.root_tag = "tk"
        self.tag     = "Button"
        self.type    = "Image"
        self.id      = obj_data["id"]
        self.name    = obj_data["name"]

        self.width   = obj_data["absoluteBoundingBox"]["width"]
        self.height  = obj_data["absoluteBoundingBox"]["height"]

        self.x       = float(obj_data["absoluteBoundingBox"]["x"]) - float(parent.x)
        self.y       = float(obj_data["absoluteBoundingBox"]["y"]) - float(parent.y)

        self.bg = parent.bg
        for data in obj_data["fills"]:
            if data["type"] == "SOLID":
                self.bg = rgb_to_hex(data["color"]["r"],data["color"]["g"],data["color"]["b"])
        self.text = ""

class Node_ButtonImage2:
    def __init__(self,obj_data,parent):
        self.root_tag = "tk"
        self.tag     = "Label"
        self.type    = "Image"
        self.id      = obj_data["id"]
        self.name    = obj_data["name"]

        self.width   = obj_data["absoluteBoundingBox"]["width"]
        self.height  = obj_data["absoluteBoundingBox"]["height"]

        self.x       = float(obj_data["absoluteBoundingBox"]["x"]) - float(parent.x)
        self.y       = float(obj_data["absoluteBoundingBox"]["y"]) - float(parent.y)

        self.bg = parent.bg
        for data in obj_data["fills"]:
            if data["type"] == "SOLID":
                self.bg = rgb_to_hex(data["color"]["r"],data["color"]["g"],data["color"]["b"])
        self.text = ""
    
class Node_LabelText:
    def __init__(self,obj_data,parent):
        self.root_tag = "tk"
        self.tag  = "Label"
        self.type = "Text"
        self.id = obj_data["id"]
        self.name    = obj_data["name"]
        self.text = ""

        self.width = obj_data["absoluteBoundingBox"]["width"]
        self.height = obj_data["absoluteBoundingBox"]["height"]

        self.x = float(obj_data["absoluteBoundingBox"]["x"]) - float(parent.x)
        self.y = float(obj_data["absoluteBoundingBox"]["y"]) - float(parent.y)

        self.bg = parent.bg
        for child in obj_data["children"]:
            if(child["type"] == "RECTANGLE"):
                for data in child["fills"]:
                    if data["type"] == "SOLID":
                        self.bg = rgb_to_hex(data["color"]["r"],data["color"]["g"],data["color"]["b"])
            if(child["type"] == "TEXT"):
                for data in child["fills"]:
                    if data["type"] == "SOLID":
                        self.fg = rgb_to_hex(data["color"]["r"],data["color"]["g"],data["color"]["b"])
                self.text    = convert_newlines_to_text(child["characters"])
                self.family  = child["style"]["fontFamily"]
                self.size    = int(child["style"]["fontSize"])*72/get_dpi()
                self.weight  = weight(child["style"]["fontPostScriptName"])
                self.anchor  = position(child["style"]["textAlignHorizontal"],child["style"]["textAlignVertical"])
                self.justify = str(child["style"]["textAlignHorizontal"]).lower()

class Node_Combobox:
    def __init__(self,obj_data,parent):
        self.root_tag = "ttk"
        self.tag  = "Combobox"
        self.type = "combobox"
        self.id   = obj_data["id"]
        self.name = obj_data["name"]
        self.text = ""

        self.width = obj_data["absoluteBoundingBox"]["width"]
        self.height = obj_data["absoluteBoundingBox"]["height"]

        self.x = float(obj_data["absoluteBoundingBox"]["x"]) - float(parent.x)
        self.y = float(obj_data["absoluteBoundingBox"]["y"]) - float(parent.y)

        self.bg = parent.bg
        for data in obj_data["fills"]:
            if data["type"] == "SOLID":
                self.bg = rgb_to_hex(data["color"]["r"],data["color"]["g"],data["color"]["b"])
        self.text = ""

class Node_Listbox:
    def __init__(self,obj_data,parent):
        self.root_tag = "tk"
        self.tag  = "Listbox"
        self.type = "listbox"
        self.id   = obj_data["id"]
        self.name = obj_data["name"]
        self.text = ""

        self.width = obj_data["absoluteBoundingBox"]["width"]
        self.height = obj_data["absoluteBoundingBox"]["height"]

        self.x = float(obj_data["absoluteBoundingBox"]["x"]) - float(parent.x)
        self.y = float(obj_data["absoluteBoundingBox"]["y"]) - float(parent.y)
        
        self.bg = parent.bg
        for data in obj_data["fills"]:
            if data["type"] == "SOLID":
                self.bg = rgb_to_hex(data["color"]["r"],data["color"]["g"],data["color"]["b"])
        self.text = ""


class Node_Text:
    def __init__(self,obj_data,parent):
        self.root_tag = "tk"
        self.tag  = "Text"
        self.type = "text"
        self.id   = obj_data["id"]
        self.name = obj_data["name"]
        self.text = ""

        self.width = obj_data["absoluteBoundingBox"]["width"]
        self.height = obj_data["absoluteBoundingBox"]["height"]

        self.x = float(obj_data["absoluteBoundingBox"]["x"]) - float(parent.x)
        self.y = float(obj_data["absoluteBoundingBox"]["y"]) - float(parent.y)
        
        self.bg = parent.bg
        for data in obj_data["fills"]:
            if data["type"] == "SOLID":
                self.bg = rgb_to_hex(data["color"]["r"],data["color"]["g"],data["color"]["b"])
        self.text = ""

class Node_ButtonText:
    def __init__(self,obj_data,parent):
        self.root_tag = "tk"
        self.tag  = "Button"
        self.type = "Text"
        self.id = obj_data["id"]
        self.name    = obj_data["name"]
        self.text = ""

        self.width = obj_data["absoluteBoundingBox"]["width"]
        self.height = obj_data["absoluteBoundingBox"]["height"]

        self.x = float(obj_data["absoluteBoundingBox"]["x"]) - float(parent.x)
        self.y = float(obj_data["absoluteBoundingBox"]["y"]) - float(parent.y)

        self.bg = parent.bg
        for child in obj_data["children"]:
            if(child["type"] == "RECTANGLE"):
                for data in child["fills"]:
                    if data["type"] == "SOLID":
                        self.bg = rgb_to_hex(data["color"]["r"],data["color"]["g"],data["color"]["b"])
            if(child["type"] == "TEXT"):
                for data in child["fills"]:
                    if data["type"] == "SOLID":
                        self.fg = rgb_to_hex(data["color"]["r"],data["color"]["g"],data["color"]["b"])
                self.text    = convert_newlines_to_text(child["characters"])
                self.family  = child["style"]["fontFamily"]
                self.size    = int(child["style"]["fontSize"])*72/get_dpi()
                self.weight  = weight(child["style"]["fontPostScriptName"])
                self.anchor  = position(child["style"]["textAlignHorizontal"],child["style"]["textAlignVertical"])
                self.justify = str(child["style"]["textAlignHorizontal"]).lower()

class Node_Frame:
    def __init__(self,obj_data):
        self.id = obj_data["id"]
        self.name = obj_data["name"]
        self.type = obj_data["type"]
        self.x  = obj_data["absoluteBoundingBox"]["x"]
        self.y  = obj_data["absoluteBoundingBox"]["y"]
        self.elements = []

        self.bg = "#ffffff"
        for data in obj_data["fills"]:
            if data["type"] == "SOLID":
                self.bg = rgb_to_hex(data["color"]["r"],data["color"]["g"],data["color"]["b"])

        for child in obj_data["children"]:
            data = str(child["name"]).split("_")[0]
            if  (data == "btn"):
                child = Node_Button(child,self)
            elif(data == "lb"):
                child = Node_Label(child,self)
            elif(data == "btnImage"):
                child = Node_ButtonImage(child,self)
            elif(data == "btnImage2"):
                child = Node_ButtonImage2(child,self)
            elif(data == "lbImage"):
                child = Node_LabelImage(child,self)
            elif(data == "lbText"):
                child = Node_LabelText(child,self)
            elif(data == "btnText"):
                child = Node_ButtonText(child,self)
            elif(data == "combobox"):
                child = Node_Combobox(child,self)
            elif(data == "listbox"):
                child = Node_Listbox(child,self)
            elif(data == "textarea"):
                child = Node_Text(child,self)
            self.elements.append(child)



class Node_Canvas:
    def __init__(self,obj_data):
        self.id = obj_data["id"]
        self.name = obj_data["name"]
        self.type = obj_data["type"]
        self.childrens = []
        for child in obj_data["children"]:
            child = Node_Frame(child)
            self.childrens.append(child)


class Node_Document:
    def __init__(self,obj_data):
        self.id = obj_data["id"]
        self.name = obj_data["name"]
        self.type = obj_data["type"]
        self.childrens = []
        for child in obj_data["children"]:
            child = Node_Canvas(child)
            self.childrens.append(child)

class obj_Figma:
    def __init__(self,obj_json):
        self.obj_Figna = obj_json
        self.documents = []
        self.documents.append(Node_Document(self.obj_Figna["document"]))
    