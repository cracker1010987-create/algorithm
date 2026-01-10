n = int(input())

for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * (i + 1) - 1))
for t in range(n - 1):
    print(" " * (t + 1) + "*" * (2 * (n - t - 1) - 1))