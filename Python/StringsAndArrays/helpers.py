def one_replace_away(a: str, b: str) -> bool:
    # Assuming both strings are same length
    diffs = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diffs += 1
        if diffs > 1:
            return False
    return True

def one_insert_away(shortest: str, longest: str) -> bool:
    s, l = 0, 0
    while s < len(shortest) and l < len(longest):
        if shortest[s] != longest[l]:
            if s != l:
                return False
            l += 1
        else:
            s += 1
            l += 1
    return True
