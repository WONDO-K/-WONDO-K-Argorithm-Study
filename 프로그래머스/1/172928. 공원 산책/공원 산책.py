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
        way, block = command.split()
        dx,dy = vector[way]

        for cnt in range(1,int(block)+1):
            nx = x + dx * cnt
            ny = y + dy * cnt
            if not (0 <= nx < n and 0 <= ny < m) or park[nx][ny] == 'X':
                break
        else:
            x,y = nx,ny
    return [x,y]