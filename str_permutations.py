def str_permutation(string):
    all_perm = set()
    all_perm = helper_perm(string, 0, len(string)-1, all_perm)
    result = list(all_perm)
    result.sort()
    return result


def helper_perm(string, i, n, all_perm):
    if i == n:
        all_perm.add(string)
        return all_perm
    else:
        for j in range(i, n + 1):
            string_l = list(string)
            string_l[i], string_l[j] = string_l[j], string_l[i]
            string = ''.join(string_l)
            helper_perm(string, i+1, n, all_perm)
            string_l[i], string_l[j] = string_l[j], string_l[i]
            string = ''.join(string_l)

    return all_perm


if __name__ == '__main__':
    string = 'ABC'
    string = 'AAB'
    print str_permutation(string)
