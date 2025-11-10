from itertools import cycle


def solution(answers):
    answer = []
    supoza1 = [1, 2, 3, 4, 5]
    supoza2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supoza3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    supoza_score = [0, 0, 0]

    for a, s1, s2, s3 in zip(answers, cycle(supoza1), cycle(supoza2), cycle(supoza3)):
        if a == s1:
            supoza_score[0] += 1
        if a == s2:
            supoza_score[1] += 1
        if a == s3:
            supoza_score[2] += 1

    max_score = max(supoza_score)

    answer = [i + 1 for i, score in enumerate(supoza_score) if score == max_score]
    # answer = [i + 1 for i in range(3) if supoza_score[i] == max_score]

    return answer
