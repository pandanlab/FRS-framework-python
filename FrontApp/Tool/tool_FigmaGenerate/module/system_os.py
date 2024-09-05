import os
import shutil

def create_or_recreate_directory(directory_path):
    if os.path.exists(directory_path):
        shutil.rmtree(directory_path)
    os.makedirs(directory_path)
    print(f"Thư mục '{directory_path}' đã được tạo lại.")