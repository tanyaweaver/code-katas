def compare_strings(s1, s2):
    match = False
    if s1 and s2 and len(s1) == len(s2):
        i = 0
        while i < len(s1):
            if s1[i] != s2[i]:
                break
            i += 1
        if i == len(s1):
            match = True
    return match


def regex_matching(pattern, test):
    # import pdb; pdb.set_trace()
    match = False
    if pattern[0] == '^' and pattern[-1] == '$':
        match = compare_strings(pattern[1:-1], test)
    elif pattern[0] == '^':
        match = compare_strings(pattern[1:], test[:len(pattern)-1])
    elif pattern[-1] == '$':
        match = compare_strings(pattern[:-1], test[len(test) - len(pattern) + 1:])
    else:
        string = test
        while not match and string and len(string) >= len(pattern):
            index = string.find(pattern[0])
            if index != -1:
                match = compare_strings(pattern, string[index:index+len(pattern)])
                if not match:
                    string = string[index + 1:]
            else:
                break
    return match


# if __name__ == '__main__':
#     pattern = 'abcdef'
#     test = 'abcdefr'
#     print regex_matching(pattern, test)
