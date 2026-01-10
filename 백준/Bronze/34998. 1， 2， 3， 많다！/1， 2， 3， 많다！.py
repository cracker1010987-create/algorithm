N = int(input())

for _ in range(N):
    X = int(input())
    num = input().split()

    total = 0
    for i in range(0, len(num), 2):
        if num[i] == '!':
            total += 10
        else:
            total += int(num[i])

    if total >= 10:
        print('!')
    else:
        print(total)