import shutil
import os
import sys

def copy_folder(source,destination):
    if not os.path.isdir(source):
        print("error")
        return
    
#it check destinantion folder is created if not the it will crete automaticaly
    os.makedirs(destination,exist_ok= True)

#it iterate over the list
    for item in os.listdir(source):
            s = os.path.join(source,item)
            
#check inside the folder is file or not
            if os.path.isfile(s):
                shutil.copy2(s,os.path.join(destination,item))
    print(f"copy file from '{source}' to '{destination}' ")
if __name__ == "__main__":
     if len(sys.argv) !=3:
          print("usage: python copy_folder.py <source_folder_path> <destination_folder_path>")
     else:
          copy_folder(sys.argv[1],sys.argv[2])
