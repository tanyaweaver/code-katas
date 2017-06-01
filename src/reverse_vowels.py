def reverse_vowels_of_string(s):
    vowels = 'aoeiu'
    if not s:
        return s
    s_ = list(s)
    i = 0
    j = len(s_) - 1
    while True:
        while i < j and s_[i].lower() not in vowels:
            i += 1
        while j > i and s_[j].lower() not in vowels:
            j -= 1
        if i < j:
            s_[i], s_[j] = s_[j], s_[i]
            i += 1
            j -= 1
        else:
            break

    s = ''.join(s_)
    return s
