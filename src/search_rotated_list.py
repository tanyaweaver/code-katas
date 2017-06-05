def find_num_rotated(l):
    if not l:
        return 0
    low = 0
    high = len(l) - 1
    while low < high:
        i = (low + high)/2
        if l[i] < l[-1]:  # guess is before the rotation pivot
            if i != 0:
                if l[i - 1] < l[i]:
                    high = i - 1
                else:
                    return i
            else:
                return 0
        elif l[i] >= l[-1]:  # guess is after the rotation pivot
            if i != len(l) - 1:
                if l[i + 1] > l[i]:
                    low = i + 1
                else:
                    return i + 1
            else:
                return 0
    return 0


def search(l, num):
    if not l:
        return False
    num_rotations = find_num_rotated(l)
    if num < l[-1]:
        l = l[num_rotations:]
    elif num > l[-1]:
        l = l[:num_rotations]
    else:
        return True
    low, high = 0, len(l) - 1
    while low <= high:
        i = (low + high)/2
        if l[i] == num:
            return True
        elif l[i] > num:
            high = i - 1
        else:
             low = i + 1
    return False
