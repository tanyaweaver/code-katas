def common_elements1(l1, l2):
    if l1 and l2:
        return list(set(l1).intersection(set(l2)))


def common_elements2(l1, l2):
    if l1 and l2:
        return [x for x in l1 if x in set(l2)]
