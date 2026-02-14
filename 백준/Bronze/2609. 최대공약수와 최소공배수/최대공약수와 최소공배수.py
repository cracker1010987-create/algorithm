a, b = map(int,input().split())

m = 1
for i in range(min(a, b),0,-1):
    if a % i == 0 and b % i == 0:
        m = i
        break

n = a * b // m
print(m)
print(n)