# info 배열 = "개발언어 직군 경력 소울푸드 점수"
# query의 각 문자열은 "[조건] X" 형식 -> '-' 표시는 해당 조건을 고려하지 않겠다는 의미
# [조건]은 "개발언어 and 직군 and 경력 and 소울푸드" 형식
# X는 코딩테스트 점수를 의미

from itertools import combinations

# bisect: 정렬된 리스트에서 특정 값이 처음 등장하는 위치를 빠르게 찾아주는 모듈
# bisect_left: 정렬된 리스트에서 target 이상 값이 처음 등장하는 위치(index)를 찾는 함수
from bisect import bisect_left


def solution(info, query):
    answer = []
    db = {}

    # 나올 수 있는 16가지 경우의 수 모두 key로 저장
    for i in info:
        parts = i.split()  # split은 최소한만
        cond = parts[:4]
        score = int(parts[4])

        for r in range(5):
            # r: 0 -> “-” 없음
            # r: 1 -> (0), (1), (2), (3)
            # r: 2 -> (0,1), (0,2), (0,3), (1,2), (1,3), (2,3), ...
            # ...
            for comb in combinations(range(4), r):
                temp = cond[:]

                # 조합으로 정해진 위치에만 "-" 지정
                for idx in comb:
                    temp[idx] = "-"

                key = f"{temp[0]} {temp[1]} {temp[2]} {temp[3]}"

                if key not in db:
                    db[key] = []

                db[key].append(score)

    # info 저장 완성 후, 각 key의 점수 리스트 정렬 → bisect용 준비
    for key in db:
        db[key].sort()

    for q in query:
        q = q.replace(" and ", " ")
        parts = q.split()

        # query key 생성
        key = f"{parts[0]} {parts[1]} {parts[2]} {parts[3]}"
        target = int(parts[4])

        # 매칭되는 정보가 없으면 0
        if key not in db:
            answer.append(0)
            continue

        # bisect로 target 이상인 사람 수 세기
        arr = db[key]
        idx = bisect_left(arr, target)  # 해당 idx 이후는 다 조건에 포함
        answer.append(len(arr) - idx)

    return answer
