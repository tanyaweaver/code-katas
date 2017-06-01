from collections import defaultdict


def dna_repeats(s):
    import pdb; pdb.set_trace()
    result = []
    if len(s) < 10:
        return result
    d_ = set()
    for i in range(len(s) - 9):
        sequence = s[i:i+10]
        if sequence in d_:
            if sequence not in result:
                result.append(sequence)
        else:
            d_.add(sequence)
    return result


string = 'aaaaaaaaaaa'
dna_repeats(string)
