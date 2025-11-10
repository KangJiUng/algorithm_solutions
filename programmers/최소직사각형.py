def solution(sizes):
    w = 0
    h = 0

    for i in sizes:
        i.sort()

    for i in sizes:
        w = max(w, i[0])
        h = max(h, i[1])

    return w * h
