def binary_search(l, num):
    if not l:
        return False
    low = 0
    hi = len(l) - 1
    while low <= hi:
        guess = (low + hi)/2
        if l[guess] == num:
            return True
        elif l[guess] > num:
            hi = guess - 1
        else:
            low = guess + 1
    return False
