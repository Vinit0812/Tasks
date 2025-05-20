import shutil
import os
import sys

def copy_file_folder(source, destination):
    if not os.path.exists(source):
        print("Error: Source path does not exist.")
        return
    try:
        if os.path.isfile(source):
            shutil.copy2(source, destination)
            print(f"File copied from '{source}' to '{destination}'")
        elif os.path.isdir(source):
            if os.path.exists(destination):
                if os.path.isdir(destination):
                    shutil.rmtree(destination)
                else:
                    os.remove(destination)

            shutil.copytree(source, destination)
            print(f"Folder copied from '{source}' to '{destination}'")
    except Exception as e:
        print(f"Error during copy: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python copy_file_folder.py <source_path> <destination_path>")
    else:
        copy_file_folder(sys.argv[1], sys.argv[2])
