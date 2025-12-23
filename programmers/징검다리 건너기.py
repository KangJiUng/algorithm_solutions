def solution(stones, k):
    left, right = 0, max(stones)
    answer = 0

    while left <= right:
        mid = (left + right) // 2  # 건너는 친구들 수
        cnt = 0  # 연속으로 못 밟은 돌 개수
        possible = True

        for stone in stones:
            if stone - mid < 0:  # 마지막 사람이 밟고 0이 되는 것 제외 주의
                cnt += 1
                if cnt >= k:
                    possible = False
                    break
            else:
                cnt = 0

        if possible:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer
