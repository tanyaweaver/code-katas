def is_palindrome(s):
    if s is None:
        return False
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True


def is_palindorme2(s):
    if s is None:
        return False
    return s == s[::-1]
