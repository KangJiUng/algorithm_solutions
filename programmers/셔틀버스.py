# 셔틀은 09:00부터 운행
# 셔틀 운행 횟수 n
# 셔틀 운행 간격 t(분)
# 한 셔틀에 탈 수 있는 최대 크루 수 m
# 크루가 대기열에 도착하는 시각을 모은 배열 timetable(HH:MM)


def solution(n, t, m, timetable):
    answer = ""
    START = 540

    for i in range(len(timetable)):
        hh, mm = timetable[i].split(":")
        timetable[i] = int(hh) * 60 + int(mm)

    timetable.sort()

    idx = 0

    for i in range(n):
        bus_time = START + i * t
        cnt = 0

        while cnt < m and idx < len(timetable) and timetable[idx] <= bus_time:
            idx += 1
            cnt += 1

        if i == n - 1:
            if cnt < m:
                con_time = bus_time
            else:
                con_time = timetable[idx - 1] - 1

    hour = con_time // 60
    minute = con_time % 60

    # d: 정수
    # 2: 최소 2자리
    # 0: 빈자리는 0으로 채움
    answer = f"{hour:02d}:{minute:02d}"

    return answer
