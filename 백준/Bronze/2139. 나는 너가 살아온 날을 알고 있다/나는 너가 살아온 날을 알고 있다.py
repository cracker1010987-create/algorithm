def is_leap_year(x):
    if x % 400 == 0:
        return True
    elif x % 100 == 0:
        return False
    elif x % 4 == 0:
        return True
    else:
        return False


check = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    d, m, y = map(int, input().split())
    if (d, m, y) == (0, 0, 0):
        break
    if is_leap_year(y):
        check[1] = 29
    else:
        check[1] = 28
    day = 0
    for i in range(m - 1):
        day += check[i]
    day += d
    print(day)




