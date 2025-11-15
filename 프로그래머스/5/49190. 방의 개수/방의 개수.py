# 방향 벡터 0~7 까지
vect = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def solution(arrows):
    answer = 0
    visit_nodes = set()
    visited_edges = set()
    x,y = 0,0
    visit_nodes.add((x,y))

    for way in arrows:
        for _ in range(2):
            next_x,next_y = x+vect[way][0], y+vect[way][1]
            edge = ((x,y),(next_x,next_y))
            reverse_edge = ((next_x,next_y),(x,y))
            x,y = next_x,next_y


            if (x,y) in visit_nodes:
                if edge not in visited_edges: # 순방향만 저장해도 역방향은 무조건 저장되니까 다른 한쪽을 검사할 필요가 없다.
                    answer+=1
            visit_nodes.add((x, y))
            visited_edges.add(edge)
            visited_edges.add(reverse_edge)

    return answer

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
print(solution([6, 4, 2, 0, 6, 4, 2, 0] ))
print(solution([4, 1, 4, 7, 4, 1, 4, 7] ))
print(solution([0, 6, 4, 2, 7, 2, 5]))