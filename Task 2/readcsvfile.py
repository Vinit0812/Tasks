import csv
import sys

def read_csv_file(filename):
    with open(filename,newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:python script.py <filename>")
    else:
        read_csv_file(sys.argv[1])