def sumOfTwo(a, b, v):
    if not a or not b:
        return False
    a_ = set(a)
    for integer in b:
        if (v-integer) in a_:
            return True
    return False
