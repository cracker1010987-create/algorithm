def solution(my_string):
    parts = my_string.split()
    answer = int(parts[0])
    for i in range(1, len(parts), 2):
        cal = parts[i]
        next_num = int(parts[i+1])
        if cal == '+':
            answer += next_num
        else:
            answer -= next_num
            
    return answer