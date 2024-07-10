# https://100.pyalgo.co.kr/?page=10#
# 10번 문제

# # 원래 풀었던 방법
# def solution(data):
#     b = [x[0] for x in data if sum(x[1:])>=350]
#     return sorted(b)

# 다른 방법 1
op_list = []


def solution(data):
    for x in data:  # data를 순회합니다.
        if sum(x[1:]) >= 350:  # x의 인데스 1부터 끝까지의 합이 350 이상일 경우를 구합니다.
            op_list.append(x[0])  # op_list에 능력치 합이 350이 넘는 op캐릭터의 이름을 리스트에 추가합니다.
    return sorted(op_list)  # op_list를 알파벳순으로 정렬하여 리턴합니다.


solution([["Licat", 98, 92, 85, 97], ["Mura", 95, 32, 51, 30], ["Binky", 98, 98, 51, 32]])
