n = int(input())
def f(x):
    return x * (x + 1) // 2
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
cnt = 0
l, r = 0, 1
while l < n:
    if f(r) - f(l) > n:
        l += 1
    elif f(r) - f(l) < n:
        r += 1
    else:
        cnt += 1
        l += 1
        r += 1
print(cnt)
