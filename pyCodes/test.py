import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)
dR = [0, 0, -1, 1]
dC = [-1, 1, 0, 0]
             
while True:
    w, h = map(int, read().split())
    if w == 0 and h == 0:
        break
    
    land = []
    for _ in range(h):
        land.append(list(map(int, read().split())))
    visited = []
    visited = [[0 for _ in range(w)] for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            print(visited[i][j])
            
    