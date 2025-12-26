from collections import defaultdict


def solution(gems):
    answer = []
    total_gem_kind = len(set(gems))
    count = defaultdict(int)
    left = 0
    best_len = len(gems)

    for right in range(len(gems)):
        count[gems[right]] += 1

        while len(count) == total_gem_kind:
            if right - left < best_len:
                best_len = right - left
                answer = [left + 1, right + 1]

            count[gems[left]] -= 1

            if count[gems[left]] == 0:
                del count[gems[left]]

            left += 1

    return answer
