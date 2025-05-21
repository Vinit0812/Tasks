import json
import sys

def read_json_file(filename):
    with open(filename,'r') as file:
        data = json.load(file)
        print("json content:",data)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python josn_read_file <filename>")
    else:
        read_json_file(sys.argv[1])
