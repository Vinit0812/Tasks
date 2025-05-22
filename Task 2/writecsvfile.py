import csv
import sys

def write_csv_file(filename):
    data = [
        ["name", "age"], # sample data that will be print in the csv file
        ["vinit", "22"]
    ]
    with open(filename, 'w', newline="") as f:
        writer = csv.writer(f) # write the content inside the file
        writer.writerows(data) 
        print(f"Written to {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
    else:
        write_csv_file(sys.argv[1])
