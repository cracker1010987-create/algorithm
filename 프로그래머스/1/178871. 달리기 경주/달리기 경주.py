def solution(players, callings):
    rank = {players[i]: i for i in range(len(players))}
    
    for i in callings:
        curr = rank[i]
        next_rank = curr - 1
        next_player = players[next_rank]
        players[curr], players[next_rank] = players[next_rank], players[curr]
        
        rank[i] = next_rank
        rank[next_player] = curr
        
    return players