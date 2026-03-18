import heapq


def solution(book_time):
    answer = 0

    # "HH:MM" -> 분 단위 변환
    def to_minute(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m

    # 시작 시간, 종료 시간 기준으로 분 단위 변환 후 정렬
    times = []
    for start, end in book_time:
        s = to_minute(start)
        e = to_minute(end) + 10  # 청소 시간 10분 추가
        times.append((s, e))

    times.sort()

    rooms = []  # 각 방의 다음 사용 가능 시간 저장

    for start, end in times:
        # 가장 빨리 비는 방을 재사용할 수 있으면 꺼내기
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)

        heapq.heappush(rooms, end)

    answer = len(rooms)

    return answer
