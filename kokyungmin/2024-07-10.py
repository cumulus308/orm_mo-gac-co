# https://100.pyalgo.co.kr/?page=10#
# 10번 문제


def solution(data):
    b = [x[0] for x in data if sum(x[1:])>=350]
    return sorted(b)
