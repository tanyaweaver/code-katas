from itertools import product


def phone_buttons(numbers):
    result = []
    if not numbers:
        return result
    reference = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    letters = [reference[x] for x in numbers]
    return sorted(''.join(a) for a in product(*letters))
    # cur_list = list(reference[numbers[0]])
    # for number in numbers[1:]:
    #     extra_list = []
    #     while len(cur_list) != 0:
    #         cur_element = cur_list.pop()
    #         for letter in reference[number]:
    #             extra_list.append(cur_element + letter)
    #     cur_list = extra_list
    # return sorted(cur_list)
