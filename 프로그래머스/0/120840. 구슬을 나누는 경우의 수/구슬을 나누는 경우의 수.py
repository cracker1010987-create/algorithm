def solution(balls, share):
    bs = balls - share
    pac_n = 1
    pac_m = 1
    pac_mn = 1
    for i in range(1, balls + 1):
        pac_n *= i
    for i in range(1, share + 1):
        pac_m *= i
    for i in range(1, bs + 1):
        pac_mn *= i
    answer = pac_n // (pac_mn * pac_m)
    
    return answer