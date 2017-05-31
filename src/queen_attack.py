# O(queens.length*querries.length)


def under_queen_attack(n, queens, queries):
    result = []
    for query in queries:
        attack_status = False
        for queen in queens:
            horizontal = query[0] == queen[0]
            vertical = query[1] == queen[1]
            diagonal = abs(queen[0] - query[0]) == abs(queen[1] - query[1])
            attack_status = (horizontal or vertical or diagonal)
            if attack_status is True:
                break
        result.append(attack_status)
    return result
