def tripleSum(x, a):
    if len(a) < 3:
        return False
    a.sort()
    print a
    for i in range(len(a) - 2):
        l = i + 1
        n = len(a) -1
        while l < n:
            sum_ = a[i] + a[l] + a[n]
            if sum_ == x:
                return True
            elif sum_ > x:
                n -= 1
            else:
                l += 1
    return False


if __name__ == '__main__':
    x = 15
    a = [14, 1, 2, 3, 8, 15, 3]
    y = 8
    b = [1, 1, 2, 5, 3]
    z = 165
    f1 = [142, 712, 254, 869, 548, 645, 663, 758, 38, 860, 724]
    f2 = [742, 530, 779, 317, 36, 191, 843, 289, 107, 41, 943, 265]
    f3 = [649, 447, 806, 891, 730, 371, 351, 7, 102, 394, 549, 630]
    f4 = [624, 85, 955, 757, 841, 967, 377, 932, 309, 945, 440, 627]
    f5 = [324, 538, 539, 119, 83, 930, 542, 834, 116, 640, 659, 705]
    f6 = [931, 978, 307, 674, 387, 22, 746, 925, 73, 271, 830, 778]
    f7 = [574, 98, 513]
    f = f1+f2+f3+f4+f5+f6+f7
    print tripleSum(x, a)
    print tripleSum(y, b)
    print tripleSum(z, f)
