# app.py
from calculate_stats import calc
from io_utils import read_numbers_from_file

def run(path):
    nums = read_numbers_from_file(sys.path)
    result = calc(nums)
    print("Stats:", result)

if __name__ == "__main__":
    import sys
    run(sys.argv[1])