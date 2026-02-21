check = [False, False] + [True] * 9999
for i in range(2, 10001):
    if check[i]:
        for j in range(i * 2, 10001, i):
            check[j] = False

m = int(input())
n = int(input())

primes = []
for i in range(m, n + 1):
    if check[i]:
        primes.append(i)

if primes:
    print(sum(primes))
    print(primes[0])
else:
    print(-1)