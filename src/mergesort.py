def merge(l1, l2):
    result = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    if i < len(l1):
        result = result + l1[i:]
    if j < len(l2):
        result = result + l2[j:]
    return result


def merge_sort(l):
    if not l:
        return l
    if len(l) <= 1:
        return l
    left = merge_sort(l[:len(l)/2])
    right = merge_sort(l[len(l)/2:])
    return merge(left, right)
