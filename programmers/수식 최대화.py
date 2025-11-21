# 계산된 결과가 음수라면 해당 숫자의 절댓값으로 변환
# 같은 연산자끼리는 앞에 있는 것의 우선순위가 더 높습니다.

from itertools import permutations


def solution(expression):
    answer = 0
    operator = ["+", "-", "*"]
    operator_priority = list(permutations(operator))

    nums, operators = [], []
    num = ""
    for i in expression:
        if i.isdigit():
            num += i
        else:
            nums.append(int(num))
            operators.append(i)
            num = ""
    nums.append(int(num))  # 마지막 숫자 추가

    # 연산자 우선순위 조합
    for priority in operator_priority:
        # 반복문 돌 때마다 초기화해야해서 원본 사용 불가
        temp_nums = nums.copy()
        temp_ops = operators.copy()

        # 연산자 하나씩 돌기
        for op in priority:
            # 연산자 op를 모두 연산
            while op in temp_ops:
                idx = temp_ops.index(op)  # 연산자 위치
                a = temp_nums[idx]  # 연산자 기준 앞
                b = temp_nums[idx + 1]  # 연산자 기준 뒤

                if op == "+":
                    result = a + b
                elif op == "-":
                    result = a - b
                elif op == "*":
                    result = a * b

                # 이미 연산한 부분 반영
                temp_nums[idx : idx + 2] = [result]
                # 이미 사용한 연산자 제거(반복문마다 초기화하기 때문에 pop 사용 가능)
                temp_ops.pop(idx)

        answer = max(answer, abs(temp_nums[0]))

    return answer
