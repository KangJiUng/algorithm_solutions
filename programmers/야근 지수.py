import heapq


def solution(n, works):
    answer = 0

    # heapq는 최소 힙이므로 음수 이용
    heap = [-w for w in works]
    heapq.heapify(heap)

    for _ in range(n):
        x = -heapq.heappop(heap)
        if x == 0:
            break
        heapq.heappush(heap, -(x - 1))

    for i in heap:
        answer += i**2

    return answer
