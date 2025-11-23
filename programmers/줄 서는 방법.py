# 풀이 1 - 시간 초과
from itertools import permutations


def solution(n, k):
    answer = []
    result = list(permutations(range(1, n + 1)))

    for i in result[k - 1]:
        answer.append(i)

    return answer


# 풀이 2 - 검색 도움
# n개의 원소로 만들 수 있는 순열 개수는 n!
# 사전순으로 순열을 나열하면, 맨 앞자리가 같은 순열끼리 ((n-1)!) 개씩 묶임
# 예시 -> n = 4, k = 9
# 1) 4개의 숫자 → 4! = 24개 순열이므로 각 맨 앞자리가 같은 블록은 (4-1)! = 6개씩 들어 있음
# 2) k=9가 속한 곳은 7~12 범위, 즉 두 번째 블록 -> 맨 앞 숫자 = 2
# 3) 2로 시작하는 블록은 전체 순열 중 7번째~12번째에 해당. 이제 그 안에서 9번째 순열(k = 9)이 몇 번째인지 찾아야 함
# 4) 그 다음 단계의 “3번째 순열” 계산 (7번째가 이 블록의 첫 번째 순열, 8번째가 두 번째 순열, 9번째가 세 번째 순열)
# 이래서 정답률이 49%구나...
import math


def solution(n, k):
    answer = []
    numbers = list(range(1, n + 1))
    k -= 1  # 인덱스 값 고려

    for i in range(n, 0, -1):
        # 한 블록당 몇 개씩?
        fact = math.factorial(i - 1)
        # 몇 번째 블록인지 구하기
        # 한 블록의 크기 = (n-1)!
        # 전체를 블록 단위로 나누면, k-1이 속한 블록의 번호는 block_index = (k-1) // (n-1)!
        idx = k // fact

        # 찾은 숫자는 answer에 넣으면서 numbers에서 pop(중복 숫자 x이므로)
        answer.append(numbers.pop(idx))

        # 블록 안에서 몇 번째인지 구하기
        k %= fact

    return answer
