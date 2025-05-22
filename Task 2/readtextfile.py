import sys

def read_file(fname):
    with open(fname,'r') as f: #open the text file
        data = f.read() # read the content inside the file
        f = print(data)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <file name>")
    else:
        read_file(sys.argv[1])



