def check_prime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

n = int(input())
arr = list(map(int,input().split()))
ans = 0
for i in arr:
    check = check_prime(i)
    if check:
        ans += 1
print(ans)
