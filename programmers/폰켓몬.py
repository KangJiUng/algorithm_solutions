# N마리 폰켓몬의 종류 번호가 담긴 배열 nums
# N/2마리의 폰켓몬을 선택하는 방법 중, 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아, 그때의 폰켓몬 종류 번호의 개수를 return

from itertools import combinations_with_replacement

# 풀이 1 - 시간 초과
"""
def solution(nums):
    answer = 0
    max = 0
    ponketmon_pair = list(combinations_with_replacement(nums, len(nums)//2))

    for i in range(len(ponketmon_pair)):
        max = 0
        type = {}

        for j in range(len(ponketmon_pair[i])):
            if ponketmon_pair[i][j] not in type:
                type[ponketmon_pair[i][j]] = 0
                max += 1

        if answer < max:
            answer = max

    return answer
"""


# 풀이 2
# 종류 개수 < N/2: 종류가 적으니까, 모든 종류 다 골라도 중복 없이 끝남 -> 종류 최댓값 = 종류 개수
# 종류 개수 ≥ N/2:	종류는 충분하지만 고를 수 있는 수가 제한됨 ->	종류 최댓값 = N/2
def solution(nums):
    answer = 0

    # 종류 수
    kind = len(set(nums))
    # 고를 수 있는 수
    limit = len(nums) // 2

    answer = min(kind, limit)

    return answer
