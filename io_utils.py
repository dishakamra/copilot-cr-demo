"""
Module for file I/O utilities.
Provides functions to read numeric data from files.
"""
import os
from typing import List


def read_numbers_from_file(path: str) -> List[float]:
    """
    Read numbers from a file with space or comma separators.
    
    Parses a text file containing numbers separated by spaces, commas,
    or a combination of both. Invalid values are skipped.
    
    Args:
        path: Path to the file to read
        
    Returns:
        List of floating-point numbers parsed from the file
        
    Raises:
        FileNotFoundError: If the specified file does not exist
        ValueError: If the path is not a file
        PermissionError: If the file cannot be read due to permissions
    """
    # Validate file exists and is a file
    if not os.path.exists(path):
        raise FileNotFoundError(f"File does not exist: {path}")
    
    if not os.path.isfile(path):
        raise ValueError(f"Path is not a file: {path}")
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            txt = f.read().strip()
            parts = txt.replace(",", " ").split()
            nums = []
            
            for p in parts:
                try:
                    nums.append(float(p))
                except ValueError:
                    # Skip non-numeric values silently
                    # Could add logging here in production
                    continue
                    
            return nums
            
    except PermissionError:
        raise PermissionError(f"Permission denied reading file: {path}")
    except UnicodeDecodeError:
        raise ValueError(f"File is not a valid text file: {path}")