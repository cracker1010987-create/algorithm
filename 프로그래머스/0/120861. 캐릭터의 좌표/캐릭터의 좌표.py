def solution(keyinput, board):
    locate = [0, 0]
    max_x, max_y = (board[0] - 1) // 2, (board[1] - 1) // 2
    
    for i in keyinput:
        if i == "left":
            if locate[0] > -max_x:
                locate[0] -= 1
        elif i == "right":
            if locate[0] < max_x:
                locate[0] += 1
        elif i == "up":
            if locate[1] < max_y:
                locate[1] += 1
        elif i == "down":
            if locate[1] > -max_y:
                locate[1] -= 1
                
    return locate