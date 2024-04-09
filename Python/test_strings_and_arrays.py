import pytest

from StringsAndArrays.questions import *

# Test is_unique function
@pytest.mark.parametrize("test_input, expected", [
    ("abcdefg", True),
    ("aabbcc", False),
    ("", True),  # Test empty string
])
def test_is_unique(test_input, expected):
    assert is_unique(test_input) == expected

# Test is_permutation function
@pytest.mark.parametrize("a, b, expected", [
    ("abc", "bca", True),
    ("abcd", "abbc", False),
    ("", "", True),  # Test empty strings
])
def test_is_permutation(a, b, expected):
    assert is_permutation(a, b) == expected

# Test urlify function
@pytest.mark.parametrize("test_input, expected", [
    ("Mr John Smith", "Mr%20John%20Smith"),
    ("", ""),  # Test empty string
])
def test_urlify(test_input, expected):
    assert urlify(test_input) == expected

# Test is_palperm function
@pytest.mark.parametrize("string, expected", [
    ("tactcoa", True),
    ("abcd", False),
    ("", True),  # Test empty string
])
def test_is_palperm(string, expected):
    assert is_palperm(string) == expected

# Test one_edit_away function
@pytest.mark.parametrize("a, b, expected", [
    ("pale", "ple", True),
    ("pales", "pale", True),
    ("pale", "bale", True),
    ("pale", "bake", False),
    ("", "", True),  # Test empty strings
])
def test_one_edit_away(a, b, expected):
    assert one_edit_away(a, b) == expected

# Test compress function
@pytest.mark.parametrize("string, expected", [
    ("aaabbccccaa", "a3b2c4a2"),
    ("abc", "a1b1c1"),
    ("", ""),  # Test empty string
])
def test_compress(string, expected):
    assert compress(string) == expected

@pytest.mark.parametrize("matrix, expected", [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
    ([[1]], [[1]]),  # Test a single element matrix
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
     [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]])
])
def test_rotate_90(matrix, expected):
    assert rotate_90(matrix) == expected
