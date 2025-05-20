import shutil
import os
import sys

#create function with two arguments
def copy_file(source,destination):

#check whether the source file is available or not if not available then it will print error and return function
    if not os.path.isfile(source):
        print("error")
        return
    try:
        shutil.copy2(source,destination)
        print(f"file copy from '{source}' to '{destination}' ")
    except Exception as e:
        print(f"error")

#checks without running script directly code executes
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python copy_file.py <source_file_path> <destination_file_path>")
    else:
        copy_file(sys.argv[1],sys.argv[2])
    