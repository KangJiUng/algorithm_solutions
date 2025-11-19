# 각 음은 1분에 1개씩 재생
# m은 음 1개 이상 1439개 이하
# musicinfos는 [음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보]
# 네오가 찾으려는 음악의 제목을 구하여라
# 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환
# 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환


def cal_play_time(s, e):
    start_hour = int(s.split(":")[0]) * 60
    start_min = int(s.split(":")[1])
    start = start_hour + start_min

    end_hour = int(e.split(":")[0]) * 60
    end_min = int(e.split(":")[1])
    end = end_hour + end_min

    play_time = end - start
    return play_time


def normalize(s):
    s = (
        s.replace("C#", "c")
        .replace("D#", "d")
        .replace("F#", "f")
        .replace("G#", "g")
        .replace("A#", "a")
    )

    # 테스트 34 특수 케이스용 추가 처리
    # B# → C (시샾은 도와 동일)
    # E# → F (미샾은 파와 동일)
    s = s.replace("B#", "C").replace("E#", "F")

    return s


def solution(m, musicinfos):
    answer = []
    m = normalize(m)

    for idx, info in enumerate(musicinfos):
        start, end, title, sheet = info.split(",")

        play_time = cal_play_time(start, end)

        sheet = normalize(sheet)

        melody = ""

        if len(sheet) > play_time:
            melody = sheet[:play_time]

        elif len(sheet) < play_time:
            n = 0
            for _ in range(play_time):
                melody += sheet[n]
                n += 1
                if n == len(sheet):
                    n = 0
        else:
            melody = sheet

        if m in melody:
            answer.append((play_time, idx, title))

    if not answer:
        return "(None)"

    answer.sort(key=lambda x: (-x[0], x[1]))

    return answer[0][2]
