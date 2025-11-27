# 사전에 있으면 색인 번호 출력, 없으면 사전에 등록
# 사전 추가는 현재 거(w) + 다음 한 글자(c)


def solution(msg):
    answer = []
    dict = {chr(ord("A") + i): i + 1 for i in range(26)}

    i = 0
    while i < len(msg):
        w = msg[i]

        # w 확장 (i+1 글자부터)
        j = i + 1
        while j <= len(msg) and w in dict:
            if j == len(msg) or w + msg[j] not in dict:
                break
            w += msg[j]
            j += 1

        # 가장 긴 w 출력
        answer.append(dict[w])

        # 사전 추가: w + 다음 글자(c)
        if j < len(msg):
            dict[w + msg[j]] = len(dict) + 1

        # i를 w 길이만큼 앞으로 점프
        i += len(w)

    return answer
