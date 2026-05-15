def solution(sides):
    answer = []
    a, b = max(sides), min(sides)
    for c in range(1, a + b):
        if c <= a and a < b + c:
            answer.append(c)
        elif c > a and c < a + b:
            answer.append(c)
            
    return len(answer)