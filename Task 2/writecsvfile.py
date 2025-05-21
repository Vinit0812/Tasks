import csv
import sys

def write_csv_file(filename):
    data = [
        ["name", "age"],
        ["vinit", "22"]
    ]
    with open(filename, 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
        print(f"Written to {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
    else:
        write_csv_file(sys.argv[1])
