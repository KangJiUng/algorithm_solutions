# 풀이 1 - 시간 초과
# import itertools

# def solution(numbers):
#     answer = '0'
#     numbers = list(map(str, numbers))
#     nums = itertools.permutations(numbers, len(numbers))


#     for i in nums:
#         cur_num = ''.join(i)
#         if int(cur_num) > int(answer):
#             answer = cur_num


#     return answer


# 풀이 2 (cmp_to_key 몰랐음, 검색)
from functools import cmp_to_key


def solution(numbers):
    numbers = list(map(str, numbers))  # 문자열로 변환

    # return 음수 : 먼저 들어온 요소가 앞으로 정렬됨
    # return 양수 : 나중에 들어온 요소가 앞으로 정렬됨(먼저 들어온 요소보다 앞에 배치됨)
    # return 0 : 바뀌지 않음
    def compare(a, b):
        if a + b > b + a:
            return -1  # a가 앞으로
        elif a + b < b + a:
            return 1  # b가 앞으로
        else:
            return 0  # 같으면 그대로

    # 비교 함수로 정렬
    numbers.sort(key=cmp_to_key(compare))

    # 결과 합치기 (000 방지)
    return str(int("".join(numbers)))
