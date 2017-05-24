import re


def treeLevelSum(tree, k):
    counter = -1
    total = 0
    for x in re.findall(r"\(|\)|\d+", tree):
        if x == '(':
            counter += 1
        elif x == ')':
            counter -= 1
        elif counter == k:
            total += int(x)
    return total


if __name__ == '__main__':
    tree = "(0(5(6()())(14()(9()())))(7(1()())(23()())))"
    print treeLevelSum(tree, 2)
