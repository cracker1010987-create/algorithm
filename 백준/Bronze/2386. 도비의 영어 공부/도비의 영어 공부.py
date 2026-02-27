while True:
    line = input()
    if line == '#':
        break
    target = line[0]
    sentence = line[2:]
    count = 0
    for char in sentence:
        if char == target or char == target.upper():
            count += 1

    print(target, count)