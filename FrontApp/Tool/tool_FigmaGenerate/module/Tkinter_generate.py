import sys
sys.path.append("./")

import FrontApp.Tool.tool_FigmaGenerate.module.getFigma  as getFigma
import FrontApp.Tool.tool_FigmaGenerate.module.Tkinter_obj  as Tkinter_obj
import FrontApp.Tool.tool_FigmaGenerate.module.system_os as system_os
import os


def generate():
    #//chuan bi du lieu
    obj_data = getFigma.get_Figma().getDesigned()
    obj_figma = Tkinter_obj.obj_Figma(obj_data)

    # chuan bi link thu muc
    linkpath_Asset = os.path.join(os.path.dirname(__file__),"..","output","Asset")
    linkpath_Page = os.path.join(os.path.dirname(__file__),"..","output","Page")
    system_os.create_or_recreate_directory(linkpath_Asset)
    system_os.create_or_recreate_directory(linkpath_Page)

    # quet doi tuong
    for document in obj_figma.documents:
        for page in document.childrens:
            for frame in page.childrens:
                link_file_frame = os.path.join(linkpath_Page,f"{frame.name}")
                link_Image_frame = os.path.join(linkpath_Asset,f"{frame.name}")
                system_os.create_or_recreate_directory(link_Image_frame)
                with open(f"{link_file_frame}.py","w",encoding='utf-8') as file:
                    file.write("import sys\n")
                    file.write("sys.path.append('./')\n\n")
                    file.write("import tkinter as tk\n")
                    file.write("from tkinter import font,ttk\n")
                    file.write("import os\n")
                    file.write("import pathlib\n")
                    file.write("from PIL import Image, ImageTk\n\n")
                    file.write("class Frame_Box:\n")
                    file.write("\tdef __init__(self,main):\n")
                    file.write("\t\tself.root = main\n")
                    file.write("\t\tself.style = ttk.Style()\n")
                    file.write("\t\tself.style.theme_use('clam')\n")
                    file.write(f"\t\tself.frameBox = tk.Frame(main.root,bg='{frame.bg}')\n")
                    file.write("\t\tself.setup()\n")
                    file.write("\t\tself.configure()\n")
                    file.write("\t\tself.place()\n\n")
                    file.write("\tdef close(self):\n")
                    file.write("\t\tNone\n\n")


                    # viet ham setup()
                    file.write("\tdef setup(self):\n")
                    for element in frame.elements:
                        # khai bao element
                        line_element = f"\t\tself.{element.name}={element.root_tag}.{element.tag}(self.frameBox)\n"
                        file.write(line_element)
                        # khai bao Image
                        if(element.type == "Image"):
                            line_Image = f"\t\tself.image_{element.name} = ImageTk.PhotoImage(Image.open(pathlib.Path(os.path.join(os.path.dirname(__file__),'..','Asset','{frame.name}','{element.name}.png')).as_posix()).resize(({element.width},{element.height})))\n"
                            file.write(line_Image)

                            link_image = getFigma.get_Figma().getLinkImage(element.id)
                            pathFile = os.path.join(link_Image_frame,f"{element.name}.png")
                            getFigma.get_Figma().getImage(link_image,pathFile)
                        # khai bao bo sung

                    # vet ham place()
                    file.write("\t\tNone\n\n")
                    file.write("\tdef place(self):\n")
                    for element in frame.elements:
                        line_place = f"\t\tself.{element.name}.place(x={element.x},y={element.y},width={element.width},height={element.height})\n"
                        file.write(line_place)
                    file.write("\t\tNone\n\n")

                    # viet ham configure()
                    file.write("\tdef configure(self):\n")
                    for element in frame.elements:
                        if(element.root_tag == "tk"):
                            # cau hinh Image
                            if(element.type == "Image"):
                                line_configure = f"\t\tself.{element.name}.configure(image=self.image_{element.name})\n"
                                file.write(line_configure)

                            #cau hinh text
                            if(element.type == "Text"):
                                line = f"\t\tself.font = font.Font(family='{element.family}', size={int(element.size)}, weight='{element.weight}')\n"
                                file.write(line)
                                line_configure = f"\t\tself.{element.name}.configure(font=self.font,anchor='{element.anchor}',justify='{element.justify}',borderwidth=0,padx=0,pady=0)\n"
                                file.write(line_configure)
                                line_configure = f"\t\tself.{element.name}.configure(fg='{element.fg}')\n"
                                file.write(line_configure)
                                line_configure = f"\t\tself.{element.name}.configure(text='{str(element.text)}')\n"
                                file.write(line_configure)

                            # cau hinh bg
                            line_configure = f"\t\tself.{element.name}.configure(bg='{str(element.bg)}')\n"
                            file.write(line_configure)

                        elif (element.root_tag == "ttk"):
                            if(element.type == "combobox"):
                                line_configure = f"\t\tself.style.configure('{element.name}.TCombobox',background='{element.bg}',foreground='white',bordercolor='{element.bg}',fieldbackground='{element.bg}')\n"
                                file.write(line_configure)
                                line_configure = f"\t\tself.{element.name}.configure(style='{element.name}.TCombobox')\n"
                                file.write(line_configure)

                    file.write("\t\tNone\n\n")