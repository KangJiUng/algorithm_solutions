# 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용
# 가장 오랫동안 참조되지 않은 페이지를 교체하는 기법
from collections import deque


def solution(cacheSize, cities):
    answer = 0
    page = deque()

    for i in cities:
        i = i.lower()

        if cacheSize == 0:
            answer += 5
            continue

        # page에 도시이름이 이미 있을 때(cache hit)
        if i in page:
            answer += 1
            page.remove(i)
            page.append(i)

        # page에 도시이름이 없을 때(cache miss)
        elif i not in page:
            answer += 5
            if len(page) == cacheSize:
                page.popleft()
            page.append(i)

    return answer
