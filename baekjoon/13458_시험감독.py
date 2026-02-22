# 총감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 B명이고, 부감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 C명
# 각각의 시험장에 총감독관은 오직 1명만, 부감독관은 여러 명

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0

for students in a:
    answer += 1  # 총감독관
    remain = students - b
    if remain > 0:
        # 올림 연산
        answer += (remain + c - 1) // c

print(answer)
