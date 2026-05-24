def solution(n, lost, reserve):
    for i in range(1, n + 1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)
    lost.sort()
    reserve.sort()
    answer = n - len(lost)
    for i in range(len(reserve)):
        for j in range(len(lost)):
            if lost[j] == reserve[i] + 1 or lost[j] == reserve[i] - 1:
                lost[j] = 32
                reserve[i] = 32
                answer += 1
            # print(f"{j},{i}: {lost[j]}, {reserve[i]},  {lost}, {reserve}, {answer}")
    return answer
   
