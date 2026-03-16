# 해설, AI 참고
import sys

input = sys.stdin.readline

H_MAX = 1_000_000
SCORE = 1_000_000


class SegmentTree:
    def __init__(self, max_size):
        self.base = 1
        while self.base < max_size:
            self.base *= 2

        # (dp, height)
        self.tree = [(0, 0) for _ in range(self.base * 2)]

    def query(self, left, right):
        # [left, right] 구간의 (최대 dp, 그 dp를 만든 가장 큰 높이)
        if left > right:
            return (0, 0)

        left += self.base
        right += self.base
        result = (0, 0)

        while left <= right:
            if left % 2 == 1:
                result = max(result, self.tree[left])
                left += 1

            if right % 2 == 0:
                result = max(result, self.tree[right])
                right -= 1

            left //= 2
            right //= 2

        return result

    def update(self, idx, value):
        # 높이 idx의 현재 대표 dp를 value로 갱신
        idx += self.base
        self.tree[idx] = (value, idx - self.base)

        idx //= 2
        while idx > 0:
            self.tree[idx] = max(self.tree[idx * 2], self.tree[idx * 2 + 1])
            idx //= 2


def hiking(idx, heights):
    # idx는 1-index로 들어오므로 실제 위치는 idx-1
    best_dp, best_height = seg.query(0, H_MAX)
    return (dp[idx - 1] + best_dp - 1) * SCORE + best_height


if __name__ == "__main__":
    q = int(input())

    # 첫 줄은 100 명령이 보장됨
    cmds = list(map(int, input().split()))
    n = cmds[1]
    first_heights = cmds[2:]

    heights = []
    dp = []

    # 같은 높이의 dp 기록 스택
    height_dp = [[] for _ in range(H_MAX + 1)]

    seg = SegmentTree(H_MAX + 1)

    # 초기 산들 반영
    for h in first_heights:
        best_before, _ = seg.query(0, h - 1)
        cur_dp = best_before + 1

        heights.append(h)
        dp.append(cur_dp)
        height_dp[h].append(cur_dp)

        seg.update(h, cur_dp)

    for _ in range(q - 1):
        cmds = list(map(int, input().split()))

        if cmds[0] == 200:
            h = cmds[1]

            # 나보다 낮은 높이들 중 최대 dp
            best_before, _ = seg.query(0, h - 1)
            cur_dp = best_before + 1

            heights.append(h)
            dp.append(cur_dp)
            height_dp[h].append(cur_dp)

            seg.update(h, cur_dp)

        elif cmds[0] == 300:
            h = heights.pop()
            dp.pop()
            height_dp[h].pop()

            # 같은 높이 산이 남아 있으면 그 마지막 dp, 없으면 0
            if height_dp[h]:
                seg.update(h, height_dp[h][-1])
            else:
                seg.update(h, 0)

        else:  # 400
            idx = cmds[1]
            print(hiking(idx, heights))
