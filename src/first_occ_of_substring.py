def strstr(s, x):
    i = 0
    while i < (len(s) - len(x) + 1):
        if s[i] == x[0]:
            no_match = False
            j = i + 1
            k = 1
            while j < len(s) and k < len(x):
                if s[j] == x[k]:
                    j += 1
                    k += 1
                else:
                    no_match = True
                    i = j
                    break
            if not no_match:
                return i
        else:
            i += 1
    return -1


if __name__ == '__main__':
    st1 = 'sst'
    st2 = 'st'
    print strstr(st1, st2)
