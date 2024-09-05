import sys
sys.path.append("./")

import os

def clear_directory(directory_path):
    # Kiểm tra xem thư mục có tồn tại không
    if not os.path.isdir(directory_path):
        raise ValueError(f"{directory_path} is not a valid directory")
    # Lấy danh sách các file và thư mục trong thư mục
    files = os.listdir(directory_path)
    # Xóa từng file
    for file_name in files:
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):  # Kiểm tra xem có phải là file không
            os.remove(file_path)

# clear Node
link1 = os.path.join(os.path.dirname(__file__),"..","Node")
clear_directory(link1)

# generate Node
link_macro = link1 = os.path.join(os.path.dirname(__file__),"..","Extension","DefineNode.py")
with open(link_macro,"w") as file_macro:
    link1 = os.path.join(os.path.dirname(__file__),"..","..","ServiceApp")
    for data1 in os.listdir(link1):
        link2 = os.path.join(link1,data1)
        for data2 in os.listdir(link2):
            if("listNode" in data2):
                # tao file Node
                link_dirNode = os.path.join(os.path.dirname(__file__),"..","Node")
                nameNode = f"Region_{data1.strip().split("_")[1]}.py"
                link_Nodefile = os.path.join(link_dirNode,nameNode)

                # ghi macro region
                file_macro.write(f"Region_{data1.strip().split("_")[1]} = 'Region_{data1.strip().split("_")[1]}'\n")

                # ghi noi dung node
                with open(link_Nodefile,"w") as fileNode:
                    fileNode.write(f"import sys\n")
                    fileNode.write(f"sys.path.append('/')\n\n")
                    fileNode.write(f"import RTRQ.Extension.Node_Default as Node_Default\n\n")
                    link3 = os.path.join(link2,data2)
                    with open(link3,"r") as file:
                        for data in file:
                            fileNode.write(f"{data.strip()} = Node_Default.NodeEvent()\n")
                            file_macro.write(f"Node_{data1.strip().split("_")[1]}_{data.strip().split("_")[1]} = '{data.strip()}'\n")

                #print loading
                print(f"Generated Node {data1}")


