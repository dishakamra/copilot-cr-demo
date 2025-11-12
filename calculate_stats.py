# calculate_stats.py
"""
Module for calculating basic statistics on numeric data.
Provides functions to compute sum, average, maximum, and minimum values.
"""
from typing import Dict, Sequence, Union


def calculate_statistics(numbers: Sequence[Union[int, float]]) -> Dict[str, float]:
    """
    Calculate basic statistics for a list of numbers.
    
    Args:
        numbers: Sequence of numeric values to analyze
        
    Returns:
        Dictionary containing:
            - sum: Total of all numbers
            - average: Mean value
            - max: Largest number
            - min: Smallest number
            
    Raises:
        ValueError: If numbers list is empty
        TypeError: If numbers is not a sequence
    """
    if not isinstance(numbers, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    
    if not numbers:
        raise ValueError("Cannot calculate statistics for an empty list")
    
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    return {
        "sum": float(total),
        "average": float(average),
        "max": float(maximum),
        "min": float(minimum)
    }


def main():
    """Main function to demonstrate statistics calculation."""
    nums = [10, 20, 30, 40, 50]
    stats = calculate_statistics(nums)
    
    print("Statistics Summary:")
    print(f"  Sum: {stats['sum']}")
    print(f"  Average: {stats['average']:.2f}")
    print(f"  Maximum: {stats['max']}")
    print(f"  Minimum: {stats['min']}")


if __name__ == "__main__":
    main()