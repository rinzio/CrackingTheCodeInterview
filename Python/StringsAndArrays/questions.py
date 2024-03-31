import helpers


# 1.1 Implement an algorithm to determine if all
#     characters on a string in are unique
def is_unique(s: str) -> bool:
    return len(set(s)) == len(s)


# 1.2 Given two strings a & b write an algorithm
#     to determine if b is permutation of a
def is_permutation(a: str, b: str) -> bool:
    for i in set(b):
        if a.count(i) != b.count(i):
            return False
    return True


# 1.3 Write a function to replace spaces with
#     %20 as in an URL
def urlify(s: str) -> str:
    return "%20".join(s.split())


# 1.4 Permutation of a palindrome, write a function
#     to determine wether a string is a palindrome
#     or is not.
def is_palperm(s: str) -> bool:
    odds = 0

    for c in set(s):
        if s.count(c) % 2 != 0:
            odds += 1

    return odds <= 1


# 1.5 One edit away, write and algorithm to determine
#     if two strings are just one edit away, like
#     replacing one letter or inserting or removing
#     just one letter
def one_edit_away(a: str, b: str) -> bool:
    a_length, b_length = len(a), len(b)
    if a_length == b_length:
        return helpers.one_replace_away(a, b)

    if a_length + 1 == b_length:
        return helpers.one_insert_away(a, b)
    elif a_length - 1 == b_length:
        return helpers.one_insert_away(b, a)

    return False
