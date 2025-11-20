# 자카드 유사도 J(A, B) = (두 집합의 교집합 크기) / (두 집합의 합집합 크기)
# 다중집합의 교집합: min / 다중집합의 합집합: max
# 문자열은 두 글자씩 끊어서 다중집합의 원소로
# 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다.
# 대문자와 소문자의 차이는 무시
# 유사도 값에 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력

from collections import Counter


def solution(str1, str2):
    str1_set = [
        (str1[i] + str1[i + 1]).lower()
        for i in range(len(str1) - 1)
        if (str1[i] + str1[i + 1]).isalpha()
    ]
    str2_set = [
        (str2[i] + str2[i + 1]).lower()
        for i in range(len(str2) - 1)
        if (str2[i] + str2[i + 1]).isalpha()
    ]

    # 여기부터 검색 도움
    # Counter로 다중집합 생성
    # ex) counter1 = Counter({'aa': 2, 'bb': 1})
    counter1 = Counter(str1_set)
    counter2 = Counter(str2_set)

    # 교집합(각 원소의 최소 개수), 합집합(최대 개수)
    # Counter 사용 시 min, max 자동
    # ex) inter = Counter({'aa': 1, 'bb': 1})
    inter = counter1 & counter2
    union = counter1 | counter2

    # 교집합, 합집합 크기 계산
    # ex) print(inter.values()) -> dict_values([1, 1])
    inter_len = sum(inter.values())
    union_len = sum(union.values())

    # 둘 다 공집합이면 유사도 1
    if union_len == 0:
        return 65536

    return int((inter_len / union_len) * 65536)
