# app.py
import sys
from calculate_stats import calculate_statistics
from io_utils import read_numbers_from_file

def run(path: str) -> None:
    """Run statistics calculation on numbers from a file."""
    nums = read_numbers_from_file(path)
    result = calculate_statistics(nums)
    
    # Pretty print output
    print("Statistics Summary:")
    print(f"  Sum: {result['sum']}")
    print(f"  Average: {result['average']:.2f}")
    print(f"  Maximum: {result['max']}")
    print(f"  Minimum: {result['min']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python app.py <filename>")
        sys.exit(1)
    run(sys.argv[1])