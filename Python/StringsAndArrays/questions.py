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
