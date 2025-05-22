import re 
import sys

def check_number(contact):
    pattern = r'^[0-9]\d{9}'
    return re.fullmatch(pattern,contact) is not None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <number>")
    contact = sys.argv[1]
    if check_number(contact):
        print("valid number")
    else:
        print("invalid")

