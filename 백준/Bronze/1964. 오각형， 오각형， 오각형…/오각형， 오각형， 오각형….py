n = int(input())
if n == 1:
    print(5)
else:
    dot = 5
    inc = 7
    for i in range(2, n + 1):
        dot += inc
        inc += 3
    print(dot % 45678)
