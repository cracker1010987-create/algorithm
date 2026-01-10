n = int(input().strip())

for _ in range(n):
    name, year = input().split()
    year = int(year)

    if year == 2026:
        print(name)