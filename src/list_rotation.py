from collections import deque


def rotation1(l, num):
    l_ = deque(l)
    return l_.rotate(num)


def list_rotation(l, num):
    if l and num and num != 0 and abs(num) < len(l):
        if num > 0:
            return l[len(l)-num:] + l[:len(l)-num]
        elif num < 0:
            return l[-num:] + l[:-num]
    else:
        return l
