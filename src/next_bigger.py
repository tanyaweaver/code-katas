def next_bigger(l):
    result = [-1 for _ in l]
    seen = []
    i, j = 0,1
    while j < len(l):
        while seen and l[seen[-1]] < l[j]:
            result[seen[-1]] = l[j]
            seen.pop()
        if l[j] > l[i]:
            result[i] = l[j]
        else:
            seen.append(i)
        i += 1
        j += 1
    return result
