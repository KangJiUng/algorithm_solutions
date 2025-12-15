from collections import deque


def one_char_diff(a, b):
    return sum(x != y for x, y in zip(a, b)) == 1


def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque()
    visited = [0] * len(words)

    queue.append((begin, 0))

    while queue:
        current, count = queue.popleft()

        if current == target:
            return count

        for i in range(len(words)):
            if visited[i] == 0 and one_char_diff(current, words[i]):
                visited[i] = 1
                queue.append((words[i], count + 1))

    return 0
