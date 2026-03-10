import sys
from collections import Counter

input = sys.stdin.readline


def solution(n, words):
    result = 0

    base_counter = Counter(words[0])

    for i in range(1, n):
        diff_cnt = 0

        # 제시된 단어 길이가 두 자 이상 차이날 경우
        if abs(len(words[0]) - len(words[i])) > 1:
            continue

        compare_counter = Counter(words[i])

        # 제시된 단어 길이가 같은 경우
        if len(words[0]) == len(words[i]):
            for key in set(base_counter.keys()) | set(compare_counter.keys()):
                diff_cnt += abs(base_counter[key] - compare_counter[key])

            if diff_cnt == 0 or diff_cnt == 2:
                result += 1

        # 제시된 단어 길이가 한 자만 차이날 경우
        # 첫 번째 단어가 더 긺
        if len(words[0]) - len(words[i]) == 1:
            for key in set(base_counter.keys()) | set(compare_counter.keys()):
                diff_cnt += abs(base_counter[key] - compare_counter[key])

            if diff_cnt == 1:
                result += 1

        # i번째 단어가 더 긺
        if len(words[i]) - len(words[0]) == 1:
            for key in set(base_counter.keys()) | set(compare_counter.keys()):
                diff_cnt += abs(base_counter[key] - compare_counter[key])

            if diff_cnt == 1:
                result += 1

    return result


if __name__ == "__main__":
    n = int(input())
    words = [input().strip() for _ in range(n)]

    print(solution(n, words))
