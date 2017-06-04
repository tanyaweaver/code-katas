def common_elements1(l1, l2):
    if l1 and l2:
        return list(set(l1).intersection(set(l2)))


def common_elements2(l1, l2):
    if l1 and l2:
        return list(set([x for x in l1 if x in set(l2)]))


def common_elements3(l1, l2):
    """
    Solution if both lists are sorted.
    """
    i, j = 0, 0
    result = []
    if not l1 or not l2:
        return None
    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            result.append(l1[i])
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            i += 1
        else:
            j += 1
    return list(set(result))
