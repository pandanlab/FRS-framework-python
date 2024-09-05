import sys
sys.path.append("./")

import os
from pathlib import Path
import subprocess

def copy_and_modify_file(source_file, destination_file,list_data):
    try:
        with open(source_file, 'r') as src:
            lines = src.readlines()
        
        with open(destination_file, 'w') as dst:
            for i, line in enumerate(lines):
                if i == 10:  
                    for data in list_data:
                        line_add = f"\t\t('{data}', '{data}'),\n"
                        dst.write(line_add)
                dst.write(line)
        
        print(f"Build Success")
    except FileNotFoundError:
        print(f"File {source_file} không tồn tại.")
    except IOError as e:
        print(f"Đã xảy ra lỗi I/O: {e}")

source_file = 'FrontApp/extension/main.spec'
destination_file = 'build.spec'

link1 = "ServiceApp"
list_dir = []
for data1 in os.listdir(link1):
    link2 = os.path.join(link1,data1)
    for data in os.listdir(link2):
        if(data == "asset"):
            path = Path(os.path.join(link2,data))
            path = path.as_posix()
            list_dir.append(path)

copy_and_modify_file(source_file, destination_file,list_dir)
subprocess.run(f"pyinstaller {destination_file}".split())