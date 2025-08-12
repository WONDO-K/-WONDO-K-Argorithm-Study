from itertools import combinations
import sys

def get_min_city_chicken_distance(n, m, city_map):
    home = []
    store = []
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                home.append((i,j))
            elif city_map[i][j] == 2:
                store.append((i,j))

    # 치킨집 m개 모든 조합
    dist = sys.maxsize
    for chicken in combinations(store,m):
        total = 0
        for hx,hy in home:
            min_dist = sys.maxsize
            for cx,cy in chicken:
                min_dist = min(min_dist,abs(hx-cx)+abs(hy-cy))
            total += min_dist
        dist = min(dist,total)

    return dist


n,m = map(int,input().split())
city_map = [list(map(int,input().split())) for _ in range(n)]
print(get_min_city_chicken_distance(n,m,city_map))