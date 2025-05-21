import json
import sys

def write_json_file(filename,content):
    with open(filename,'w') as file:
        json.dump(content,file,indent=4)
        print(f"write content {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename> ")
    else:
        sample_data = {
            "name": "vinit"
        }
        write_json_file(sys.argv[1],sample_data)