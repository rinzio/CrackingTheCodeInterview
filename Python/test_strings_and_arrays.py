import pytest

from StringsAndArrays.questions import (
    is_unique,
    is_permutation,
    urlify,
    is_palperm,
    one_edit_away,
    compress,
)

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
@pytest.mark.parametrize("test_input, expected", [
    ("tactcoa", True),
    ("abcd", False),
    ("", True),  # Test empty string
])
def test_is_palperm(test_input, expected):
    assert is_palperm(test_input) == expected

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
@pytest.mark.parametrize("test_input, expected", [
    ("aaabbccccaa", "a3b2c4a2"),
    ("abc", "a1b1c1"),
    ("", ""),  # Test empty string
])
def test_compress(test_input, expected):
    assert compress(test_input) == expected
