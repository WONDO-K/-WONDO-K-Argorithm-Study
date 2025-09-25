vector = {
    'N' : [-1,0],
    "S" : [1,0],
    "W" : [0,-1],
    "E" : [0,1]
}

def solution(park, routes):
    flag = False
    n, m = len(park), len(park[0])

    for i in range(n):
        for j in range(m):
            if park[i][j] == 'S':
                x,y = i,j
                flag=True
                break
        if flag:
            break


    for command in routes:
        origin_x, origin_y = x, y
        command = command.split()
        way, block = command[0],int(command[1])
        dx,dy = vector[way][0],vector[way][1]

        for _ in range(block):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and park[nx][ny] != 'X':
                x, y = nx, ny
            else:
                x,y = origin_x,origin_y
                break
    return [x,y]


