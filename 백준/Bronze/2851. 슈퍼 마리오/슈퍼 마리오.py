mushrooms = [int(input()) for _ in range(10)]
total = 0

for i in mushrooms:
    before = total
    total += i
    if total >= 100:
        if (100 - before) < (total - 100):
            print(before)
        else:
            print(total)
        break
else:
    print(total)