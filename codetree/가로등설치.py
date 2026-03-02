# N: 거리의 크기 (좌표 1부터 N까지 존재)
# M: 초기에 존재하는 가로등의 개수
# L1, L2, …, Lm: 초기에 존재하는 각 가로등의 위치 정보
# 가로등 추가: 200
# D번 가로등 제거: 300 D
# 최소 전력 계산 명령(400)이 주어질 때마다 최소 소비 전력 값에 2를 곱해 출력
# 검색, AI 도움

import heapq


def main():
    q = int(input())

    lamps = []
    prev_idx = []
    next_idx = []

    max_gap_heap = []
    min_heap = []
    max_heap = []

    N = 0

    def add_lamp():
        while max_gap_heap:
            neg_gap, left_pos_key, left_id, right_id = heapq.heappop(max_gap_heap)

            # 삭제된 가로등이거나
            # 현재 서로 인접하지 않으면 무시
            if (
                lamps[left_id] is None
                or lamps[right_id] is None
                or next_idx[left_id] != right_id
            ):
                continue
            break

        left = lamps[left_id]
        right = lamps[right_id]

        new_pos = (left + right + 1) // 2
        new_id = len(lamps)

        lamps.append(new_pos)
        prev_idx.append(left_id)
        next_idx.append(right_id)

        next_idx[left_id] = new_id
        prev_idx[right_id] = new_id

        # 최소힙이라서 음수로 넣음
        # 동점이면 left_pos가 작은 구간이 먼저 나오도록 left_pos도 같이 넣음
        heapq.heappush(max_gap_heap, (-(new_pos - left), left, left_id, new_id))
        heapq.heappush(max_gap_heap, (-(right - new_pos), new_pos, new_id, right_id))

        heapq.heappush(min_heap, (new_pos, new_id))
        heapq.heappush(max_heap, (-new_pos, new_id))

    def delete_lamp(d):
        if lamps[d] is None:
            return

        left_id = prev_idx[d]
        right_id = next_idx[d]

        # 가로등 제거
        lamps[d] = None

        # 이웃 연결
        if left_id is not None:
            next_idx[left_id] = right_id
        if right_id is not None:
            prev_idx[right_id] = left_id

        # 새 구간이 생기면 힙에 추가 (둘 다 살아있는 경우만)
        if left_id is not None and right_id is not None:
            # left_id/right_id는 살아있어야 gap 계산 가능
            if lamps[left_id] is not None and lamps[right_id] is not None:
                gap = lamps[right_id] - lamps[left_id]
                heapq.heappush(max_gap_heap, (-gap, lamps[left_id], left_id, right_id))

    # r은 가장 가로등에서 멀리 떨어진 점의 거리
    def calculate():
        # 가장 왼쪽 가로등
        while min_heap:
            pos, idx = min_heap[0]
            if lamps[idx] != pos:
                heapq.heappop(min_heap)
            else:
                break

        if not min_heap:
            return 0

        leftmost = min_heap[0][0]

        # 가장 오른쪽 가로등
        while max_heap:
            neg_pos, idx = max_heap[0]
            pos = -neg_pos
            if lamps[idx] != pos:
                heapq.heappop(max_heap)
            else:
                break

        if not min_heap:
            return 0

        rightmost = -max_heap[0][0]

        # 내부 최대 간격
        max_gap = 0
        while max_gap_heap:
            neg_gap, left_pos_key, left_id, right_id = max_gap_heap[0]
            if (
                lamps[left_id] is None
                or lamps[right_id] is None
                or next_idx[left_id] != right_id
            ):
                heapq.heappop(max_gap_heap)
            else:
                max_gap = -neg_gap
                break

        return max(2 * (leftmost - 1), 2 * (N - rightmost), max_gap)

    for _ in range(q):
        cmds = list(map(int, input().split()))
        cmd = cmds[0]

        if cmd == 100:
            N, M = cmds[1], cmds[2]

            lamps = [None] + cmds[3:]
            prev_idx = [None] * (M + 1)
            next_idx = [None] * (M + 1)

            max_gap_heap = []
            min_heap = []
            max_heap = []

            for i in range(1, M + 1):
                heapq.heappush(min_heap, (lamps[i], i))
                heapq.heappush(max_heap, (-lamps[i], i))

                if i > 1:
                    prev_idx[i] = i - 1
                    gap = lamps[i] - lamps[i - 1]
                    heapq.heappush(max_gap_heap, (-gap, lamps[i - 1], i - 1, i))
                if i < M:
                    next_idx[i] = i + 1

        elif cmd == 200:
            add_lamp()

        elif cmd == 300:
            delete_lamp(cmds[1])

        elif cmd == 400:
            print(calculate())


main()
