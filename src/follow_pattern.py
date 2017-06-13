from collections import defaultdict


def areFollowingPatterns(strings, patterns):
    strings_ = defaultdict(list)
    patterns_ = defaultdict(list)
    for index, string in enumerate(strings):
        strings_[string].append(index)
    for index, pattern in enumerate(patterns):
        patterns_[pattern].append(index)
    print 'strings_', strings_
    print 'patterns_', patterns_
    print strings_.values() == patterns_.values()
    return strings_.values() == patterns_.values()


s = ['dog', 'cat', 'cat']
d = ['a', 'b', 'b']
areFollowingPatterns(s, d)
