# 차분 배열 + 누적합 + 슬라이딩 윈도우
# 시청자들의 누적 재생시간이 가장 많이 나오는 곳에 공익광고를 삽입
# 공익광고가 들어갈 시작 시각을 구해서 return


# AI 도움
def solution(play_time, adv_time, logs):
    answer = ""

    if play_time == adv_time:
        return "00:00:00"

    def time_to_sec(t):
        return int(t[0:2]) * 3600 + int(t[3:5]) * 60 + int(t[6:8])

    def sec_to_time(s):
        h = s // 3600
        m = (s % 3600) // 60
        s = s % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

    play_time_sec = time_to_sec(play_time)
    adv_time_sec = time_to_sec(adv_time)

    # 시간축 생성 (여유칸 포함)
    timeline = [0] * (play_time_sec + 2)

    # 로그를 차분 배열로 표시 (+1 시작 / -1 종료)
    for log in logs:
        start = time_to_sec(log[:8])
        end = time_to_sec(log[9:])
        timeline[start] += 1
        timeline[end] -= 1

    # 누적합 -> 각 초의 시청자 수 반영
    for i in range(1, play_time_sec + 1):
        timeline[i] += timeline[i - 1]

    # 누적합 -> 0초부터의 누적 시청 시간
    for i in range(1, play_time_sec + 1):
        timeline[i] += timeline[i - 1]

    # 첫 광고 구간 (0 ~ adv-1) 미리 계산
    max_watch = timeline[adv_time_sec - 1]
    max_start = 0

    # i는 광고 구간의 끝점
    # 끝점은 adv_time_sec 이상부터 가능
    for i in range(adv_time_sec, play_time_sec):

        # end - start + 1 = adv_time_sec
        # 구간 합 = 누적합[end] - 누적합[start-1]
        current = timeline[i] - timeline[i - adv_time_sec]

        if current > max_watch:
            max_watch = current
            max_start = i - adv_time_sec + 1

    answer = sec_to_time(max_start)

    return answer
