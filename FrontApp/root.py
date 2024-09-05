import sys
sys.path.append("./")

import tkinter as tk
import os

class Root:
    def __init__(self) -> None:
        # init root
        self.root = tk.Tk()
        self.window_width = 1000
        self.window_height = 600
        directory = os.path.join(os.path.dirname(__file__),"Env")
        self.file_position = os.path.join(directory, 'window_position')
        self.file_size = os.path.join(directory, 'window_size')
        self.load_window_position(self.window_width, self.window_height)
        self.load_window_size()
        self.root.geometry(f"{self.window_width}x{self.window_height}+{self.x}+{self.y}")
        self.box_frame = None

        # Bind root
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.bind('<Configure>',self.move_window) 

        # init page
        self.change_index(1)

    def move_window(self,event):
        self.box_frame.frameBox.place(x=0, y=0, width=self.root.winfo_width(), height=self.root.winfo_height())

    def load_window_position(self, default_width, default_height):
        self.x = (self.root.winfo_screenwidth() - default_width) // 2
        self.y = (self.root.winfo_screenheight() - default_height) // 2

        if os.path.exists(self.file_position):
            with open(self.file_position, "r") as file:
                try:
                    saved_x, saved_y = map(int, file.read().split(","))
                    self.x = saved_x
                    self.y = saved_y
                except ValueError:
                    pass 

    def load_window_size(self):
        if os.path.exists(self.file_size):
            with open(self.file_size, "r") as file:
                try:
                    saved_x, saved_y = map(int, file.read().split(","))
                    self.window_width = saved_x
                    self.window_height = saved_y
                except ValueError:
                    pass  

    def save_window(self):
        with open(self.file_position, "w") as file:
            file.write(f"{self.root.winfo_x()},{self.root.winfo_y()}")

        with open(self.file_size, "w") as file:
            file.write(f"{self.root.winfo_width()},{self.root.winfo_height()}")


    def on_closing(self):
        self.save_window()
        if self.box_frame:
            self.box_frame.close()
            self.box_frame.frameBox.destroy() 
            del self.box_frame
        self.root.destroy()

    def change_Frame(self, page):
        if self.box_frame:
            self.box_frame.frameBox.destroy() 
            del self.box_frame
        self.box_frame = page.Frame_Box(self)
        self.box_frame.frameBox.place(x=0, y=0, width=self.window_width, height=self.window_height)

    def change_index(self, number):
        if number   == 1: 
            import FrontApp.Page.Frame1 as page1
            self.change_Frame(page1)
        elif number == 2: 
            import FrontApp.Page.Frame2 as page2
            self.change_Frame(page2)
        elif number == 3: 
            import FrontApp.Page.Frame3 as page3
            self.change_Frame(page3)
        elif number == 4: 
            import FrontApp.Page.Frame4 as page4
            self.change_Frame(page4)
            
    def run(self):
        self.root.update_idletasks()
        self.root.update()
        self.root.mainloop()
