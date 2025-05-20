import shutil
import os
import sys

def nested_folder(s,d):
    if not os.path.isdir(s):
        print("error")
        return
    try:
#check whether the folder exist or not if exist then remove directly
        if os.path.exists(d):
            shutil.rmtree(d)
        shutil.copytree(s,d)
        print(f"folder copied from '{s}' to '{d}' ")
    except FileExistsError:
        print("file already exist")
    except Exception as e:
        print("error")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python nested_folder.py <source_folder> <destination_folder>")
    else:
        nested_folder(sys.argv[1],sys.argv[2])