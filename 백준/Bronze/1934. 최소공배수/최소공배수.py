import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):

    a, b = map(int, sys.stdin.readline().split())

    A, B = a, b

    x, y = a, b
    while y != 0:
        x, y = y, x % y
    gcd = x

    lcm = (A * B) // gcd
    print(lcm)
