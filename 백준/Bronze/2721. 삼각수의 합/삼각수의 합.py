def sum_thr(x):
    return x * (x + 1) // 2
def solve():
    t = int(input())
    for i in range(t):
        n = int(input())
        w = 0
        for j in range(1, n + 1):
            ans = sum_thr(j + 1)
            w += j * ans
        print(w)
solve()