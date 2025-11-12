def solution(s):
    answer = ""
    numbers = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    num = ""

    for i in s:
        num += i
        if num in numbers:
            answer += str(numbers.index(num))
            num = ""
        if i.isdigit():
            answer += i
            num = ""

    return int(answer)
