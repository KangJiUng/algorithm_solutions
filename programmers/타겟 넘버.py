# 검색 도움 받음
# deque: 양쪽에서 빠르게 데이터를 넣고 뺄 수 있는 큐 자료구조
from collections import (
    deque,
)


def solution(numbers, target):
    queue = deque()

    # 큐 초기화: (현재까지의 합, 현재 인덱스)
    queue.append((0, 0))

    # 타겟 넘버를 만들 수 있는 경우의 수
    count = 0

    # 큐가 빌 때까지 반복 (탐색을 계속 진행)
    while queue:
        # 튜플 언패킹 -> queue.append((0, 0))에서 current_sum: 첫 번째 값, index: 두 번째 값
        current_sum, index = queue.popleft()

        # 모든 숫자를 다 사용한 경우 (인덱스가 배열 길이와 같으면 끝까지 탐색 완료)
        if index == len(numbers):
            # 그때의 누적합이 목표값(target)과 같으면 경우의 수 +1
            if current_sum == target:
                count += 1
            # 다음 탐색은 필요 없으니 continue (while 다음 반복으로 넘어감)
            continue

        # 아직 숫자 다 사용 안 함 -> 다음 숫자를 사용할 차례
        # 현재 인덱스의 숫자를 더하거나 뺀 두 가지 새로운 상태를 큐에 추가한다
        # index + 1을 하는 이유: 다음 단계로 넘어가서, 다음 numbers[index]를 사용할 준비를 하는 것
        queue.append((current_sum + numbers[index], index + 1))
        queue.append((current_sum - numbers[index], index + 1))

    # 모든 경우를 탐색한 후 count 반환
    return count
