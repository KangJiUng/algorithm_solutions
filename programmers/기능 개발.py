# 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses
# 각 작업의 개발 속도가 적힌 정수 배열 speeds
# 각 배포마다 몇 개의 기능이 배포되는지를 return


def solution(progresses, speeds):
    answer = []

    while progresses:
        # 하루치 작업 업데이트
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        # 맨 앞 기능이 완료된 경우에만 배포
        count = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        # 배포가 일어나지 않으면 배포의 날이라고 하지 않음
        if count > 0:
            answer.append(count)

    return answer
