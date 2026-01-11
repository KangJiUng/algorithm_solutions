import heapq


# AI 도움  / 정확도 42, 효율성 57이라 개선 필요
def solution(food_times, k):
    # 전체 먹는 시간보다 k가 크거나 같으면 끝까지 다 먹은 상태
    if sum(food_times) <= k:
        return -1

    # (음식 시간, 음식 번호) 형태로 최소 힙 구성
    heap = []
    for i, time in enumerate(food_times):
        heapq.heappush(heap, (time, i + 1))

    prev = 0  # 모든 음식에 동일하게 적용된 누적 제거량(진짜 누적 X, 지금 우리는 여기까지 와 있다는 위치 정보)
    length = len(food_times)

    while heap:
        now = heap[0][0]  # 현재 가장 작은 절대 시간

        # 이번 층을 통째로 제거하는 데 필요한 시간
        # prev를 누적해서 지금까지 모든 음식에서 공통으로 깎인 총량을 기억해두고,
        # 각 음식의 ‘절대 시간(now)’에서 그걸 빼서 지금 시점에서 실제로 더 깎을 수 있는 양을 계산한다
        spend = (now - prev) * length

        # 이번 층을 통째로 제거하는 데 필요한 시간이 중단될 시간보다 적으면
        if k >= spend:
            k -= spend
            prev = now
            heapq.heappop(heap)  # 완전히 끝난 음식 제거
            length -= 1
        else:
            break

    # 남은 음식들 중에서 k % length 번째 음식 찾기
    remaining = sorted(heap, key=lambda x: x[1])
    return remaining[k % length][1]
