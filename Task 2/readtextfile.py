import sys

def read_file(fname):
    try:
        f = open(fname, 'r') 
        data = f.read()
        print(data)
        f.close()
    except FileNotFoundError:
        print("not exist:", fname)
    except Exception as e:
        print("error:", e)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <file name>")
    else:
        read_file(sys.argv[1])

