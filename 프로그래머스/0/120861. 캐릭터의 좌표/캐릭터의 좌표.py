def solution (keyinput, board):
    max_x = board[0] // 2
    max_y = board[1] // 2
    x,y = 0,0
    
    for key in keyinput:
        nx,ny = x,y #임시좌표 생성
        if key ==  "up":
            ny += 1
        elif key == "down":
            ny -= 1
        elif key == "right":
            nx += 1
        else:
            nx -= 1
        if -max_x <= nx <= max_x and -max_y <= ny <= max_y:
            x,y = nx, ny
    
    return [x,y]