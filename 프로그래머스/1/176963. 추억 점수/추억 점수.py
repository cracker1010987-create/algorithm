def solution(name, yearning, photo):
    scores = {name[i] : yearning[i] for i in range(len(name))}
    score = [sum([scores.get(person, 0) for person in people]) for people in photo]
    return score