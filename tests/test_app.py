# tests/test_app.py
"""
Comprehensive test suite for the statistics calculation application.
Tests cover calculate_stats, io_utils, and integration scenarios.
"""
import pytest
import tempfile
import os
from calculate_stats import calculate_statistics
from io_utils import read_numbers_from_file


# ===== Tests for calculate_statistics =====

def test_calc_basic():
    """Test basic statistics calculation with positive integers."""
    data = [1, 2, 3]
    r = calculate_statistics(data)
    assert r["sum"] == 6
    assert r["average"] == 2
    assert r["max"] == 3
    assert r["min"] == 1


def test_empty_list_raises_error():
    """Test that empty list raises ValueError."""
    with pytest.raises(ValueError, match="empty list"):
        calculate_statistics([])


def test_single_element():
    """Test statistics with a single element."""
    result = calculate_statistics([42])
    assert result["sum"] == 42
    assert result["average"] == 42
    assert result["max"] == 42
    assert result["min"] == 42


def test_negative_numbers():
    """Test statistics with negative numbers."""
    result = calculate_statistics([-5, -10, 0, 5])
    assert result["sum"] == -10
    assert result["average"] == -2.5
    assert result["max"] == 5
    assert result["min"] == -10


def test_floats():
    """Test statistics with floating-point numbers."""
    result = calculate_statistics([1.5, 2.5, 3.5])
    assert result["sum"] == 7.5
    assert result["average"] == 2.5
    assert result["max"] == 3.5
    assert result["min"] == 1.5


def test_mixed_int_float():
    """Test statistics with mixed integers and floats."""
    result = calculate_statistics([1, 2.5, 3])
    assert result["sum"] == 6.5
    assert result["average"] == pytest.approx(2.1666666666)
    assert result["max"] == 3
    assert result["min"] == 1


def test_all_same_values():
    """Test statistics when all values are identical."""
    result = calculate_statistics([5, 5, 5, 5])
    assert result["sum"] == 20
    assert result["average"] == 5
    assert result["max"] == 5
    assert result["min"] == 5


def test_large_numbers():
    """Test statistics with large numbers."""
    result = calculate_statistics([1e10, 2e10, 3e10])
    assert result["sum"] == 6e10
    assert result["average"] == 2e10


def test_invalid_input_type():
    """Test that non-list/tuple input raises TypeError."""
    with pytest.raises(TypeError, match="must be a list or tuple"):
        calculate_statistics("not a list")  # type: ignore


def test_tuple_input():
    """Test that tuples are accepted as input."""
    result = calculate_statistics((1, 2, 3))
    assert result["sum"] == 6
    assert result["average"] == 2


# ===== Tests for read_numbers_from_file =====

def test_read_valid_numbers_space_separated():
    """Test reading space-separated numbers from a file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("1 2 3 4 5")
        fname = f.name
    try:
        result = read_numbers_from_file(fname)
        assert result == [1.0, 2.0, 3.0, 4.0, 5.0]
    finally:
        os.unlink(fname)


def test_read_with_commas():
    """Test reading comma-separated numbers from a file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("1,2,3,4,5")
        fname = f.name
    try:
        result = read_numbers_from_file(fname)
        assert result == [1.0, 2.0, 3.0, 4.0, 5.0]
    finally:
        os.unlink(fname)


def test_read_mixed_separators():
    """Test reading numbers with mixed commas and spaces."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("1, 2 3,4 5")
        fname = f.name
    try:
        result = read_numbers_from_file(fname)
        assert result == [1.0, 2.0, 3.0, 4.0, 5.0]
    finally:
        os.unlink(fname)


def test_file_not_found():
    """Test that non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError, match="does not exist"):
        read_numbers_from_file("nonexistent_file_xyz.txt")


def test_mixed_valid_invalid():
    """Test reading file with mix of valid numbers and invalid text."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("1 abc 3 def 5")
        fname = f.name
    try:
        result = read_numbers_from_file(fname)
        assert result == [1.0, 3.0, 5.0]
    finally:
        os.unlink(fname)


def test_read_floats_from_file():
    """Test reading floating-point numbers from file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("1.5 2.7 3.14159")
        fname = f.name
    try:
        result = read_numbers_from_file(fname)
        assert result == [1.5, 2.7, 3.14159]
    finally:
        os.unlink(fname)


def test_read_negative_numbers():
    """Test reading negative numbers from file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("-1 -2 -3")
        fname = f.name
    try:
        result = read_numbers_from_file(fname)
        assert result == [-1.0, -2.0, -3.0]
    finally:
        os.unlink(fname)


def test_read_empty_file():
    """Test reading an empty file returns empty list."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("")
        fname = f.name
    try:
        result = read_numbers_from_file(fname)
        assert result == []
    finally:
        os.unlink(fname)


def test_directory_path_raises_error():
    """Test that passing a directory raises ValueError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        with pytest.raises(ValueError, match="not a file"):
            read_numbers_from_file(tmpdir)


def test_whitespace_only_file():
    """Test file with only whitespace returns empty list."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("   \n\t  \n  ")
        fname = f.name
    try:
        result = read_numbers_from_file(fname)
        assert result == []
    finally:
        os.unlink(fname)


# ===== Integration Tests =====

def test_full_workflow():
    """Test complete workflow: write file, read numbers, calculate stats."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write("10, 20, 30, 40, 50")
        fname = f.name
    
    try:
        # Read numbers from file
        numbers = read_numbers_from_file(fname)
        
        # Calculate statistics
        stats = calculate_statistics(numbers)
        
        # Verify results
        assert stats["sum"] == 150
        assert stats["average"] == 30
        assert stats["max"] == 50
        assert stats["min"] == 10
    finally:
        os.unlink(fname)