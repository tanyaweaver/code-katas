from collections import defaultdict, Counter


def anagrams1(s1, s2):
    'O(n) time, O(n) extra space'
    if not s1 or not s2:
        return False
    dict_s1 = defaultdict(int)
    dict_s2 = defaultdict(int)
    for letter in s1:
        dict_s1[letter] += 1
    for letter in s2:
        dict_s2[letter] += 1
    return dict_s1 == dict_s2


def anagrams2(s1, s2):
    'O(nlogn) time, no extra space'
    if not s1 or not s2:
        return False
    return sorted(s1) == sorted(s2)


def anagrams3(s1, s2):
    if not s1 or not s2:
        return False
    return Counter(s1) == Counter(s2)
