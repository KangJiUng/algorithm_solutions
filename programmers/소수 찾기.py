from itertools import permutations


def solution(numbers):
    answer = 0
    numbers = list(numbers)
    candidate = set()

    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            candidate.add(int("".join(p)))

    for c in candidate:
        if c < 2:
            continue

        for i in range(2, c):
            if c % i == 0:
                break

        else:
            answer += 1

    return answer


# 추가 풀이(루트 n 이용)
from itertools import permutations


def solution(numbers):
    answer = 0
    numbers = list(numbers)
    candidate = set()

    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            candidate.add(int("".join(p)))

    for c in candidate:
        if c < 2:
            continue

        for i in range(2, int(c**0.5) + 1):
            if c % i == 0:
                break

        else:
            answer += 1

    return answer
