import sys

def write_text_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
        print(f"Write to '{filename}' ")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <filename> <content>")
    else:
        write_text_file(sys.argv[1], sys.argv[2])
