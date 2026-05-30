def solution(arr):
    answer = []
    curr = 10
    for i in arr:
        if curr != i:
            answer.append(i)
        curr = i
    return answer