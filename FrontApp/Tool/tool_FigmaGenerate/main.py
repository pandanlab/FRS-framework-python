import sys
sys.path.append("./")

import FrontApp.Tool.tool_FigmaGenerate.module.Tkinter_generate as genera_tkinter
genera_tkinter.generate()
import subprocess
subprocess.run("python FrontApp/Tool/tool_FigmaGenerate/output/root.py".split())