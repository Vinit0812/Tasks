import re
import sys

# create function for main cheking
def check_email(email):
    pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}$' #(email pattern)
    return re.fullmatch(pattern,email) is not None 

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <email>")
    email = sys.argv[1]
    if check_email(email):
        print("valid email")
    else:
        print("invalid email")
