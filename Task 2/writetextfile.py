import sys

def write_text_file(filename, content):
    lines = content.split('\\n') #it will break the content in diffrent line
    with open(filename, 'w') as f:
        f.writelines(line + '\n' for line in lines)
        print(f"Write to '{filename}' ")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <filename> <content>")
    else:
        write_text_file(sys.argv[1], sys.argv[2])
