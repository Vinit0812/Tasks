import csv
import sys

#create function that pass one argument
def read_csv_file(filename):
    with open(filename,newline="") as f: #open file and newline for it will not add any blank line
        reader = csv.reader(f) # read the file
        for row in reader:
            print(row)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:python script.py <filename>")
    else:
        read_csv_file(sys.argv[1])