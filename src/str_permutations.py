def str_permutation(string):
    all_perm = set()
    all_perm = helper_perm(string, 0, all_perm)
    result = list(all_perm)
    result.sort()
    return result


def helper_perm(string, i, all_perm):
    if not string:
        return all_perm
    if i == len(string) - 1:
        all_perm.add(string)
        return all_perm
    else:
        for j in range(i, len(string)):
            string_l = list(string)
            string_l[i], string_l[j] = string_l[j], string_l[i]
            string = ''.join(string_l)
            helper_perm(string, i+1, all_perm)
            string_l[i], string_l[j] = string_l[j], string_l[i]
            string = ''.join(string_l)

    return all_perm
