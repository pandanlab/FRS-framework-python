import sys
sys.path.append('./')

import tkinter as tk
from tkinter import font,ttk
import os
import pathlib
from PIL import Image, ImageTk

class Frame_Box:
	def __init__(self,main):
		self.root = main
		self.style = ttk.Style()
		self.style.theme_use('clam')
		self.frameBox = tk.Frame(main.root,bg='#FDFDFD')
		self.setup()
		self.configure()
		self.place()

	def close(self):
		None

	def setup(self):
		self.lb_Header=tk.Label(self.frameBox)
		self.btnImage2_exit=tk.Label(self.frameBox)
		self.image_btnImage2_exit = ImageTk.PhotoImage(Image.open(pathlib.Path(os.path.join(os.path.dirname(__file__),'..','Asset','Frame2','btnImage2_exit.png')).as_posix()).resize((24.0,24.0)))
		self.btnImage2_back=tk.Label(self.frameBox)
		self.image_btnImage2_back = ImageTk.PhotoImage(Image.open(pathlib.Path(os.path.join(os.path.dirname(__file__),'..','Asset','Frame2','btnImage2_back.png')).as_posix()).resize((20.0,20.0)))
		self.btnImage2_next=tk.Label(self.frameBox)
		self.image_btnImage2_next = ImageTk.PhotoImage(Image.open(pathlib.Path(os.path.join(os.path.dirname(__file__),'..','Asset','Frame2','btnImage2_next.png')).as_posix()).resize((20.0,20.0)))
		self.btnImage2_home=tk.Label(self.frameBox)
		self.image_btnImage2_home = ImageTk.PhotoImage(Image.open(pathlib.Path(os.path.join(os.path.dirname(__file__),'..','Asset','Frame2','btnImage2_home.png')).as_posix()).resize((30.0,30.0)))
		None

	def place(self):
		self.lb_Header.place(x=0.0,y=0.0,width=1000.0,height=30.0)
		self.btnImage2_exit.place(x=972.0,y=3.0,width=24.0,height=24.0)
		self.btnImage2_back.place(x=30.0,y=5.0,width=20.0,height=20.0)
		self.btnImage2_next.place(x=52.0,y=5.0,width=20.0,height=20.0)
		self.btnImage2_home.place(x=0.0,y=0.0,width=30.0,height=30.0)
		None

	def configure(self):
		self.lb_Header.configure(bg='#305C47')
		self.btnImage2_exit.configure(image=self.image_btnImage2_exit)
		self.btnImage2_exit.configure(bg='#315C48')
		self.btnImage2_back.configure(image=self.image_btnImage2_back)
		self.btnImage2_back.configure(bg='#315C48')
		self.btnImage2_next.configure(image=self.image_btnImage2_next)
		self.btnImage2_next.configure(bg='#315C48')
		self.btnImage2_home.configure(image=self.image_btnImage2_home)
		self.btnImage2_home.configure(bg='#315C48')
		None
