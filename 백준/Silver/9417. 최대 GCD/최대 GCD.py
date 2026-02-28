def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(1,len(arr)):
        for j in range(i):
            x, y = arr[i], arr[j]
            if gcd(x, y) > ans:
                ans = gcd(x, y)
    print(ans)