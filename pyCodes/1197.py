#Minimun Spanning Tree(MST), Kruskal Algorithm
import sys
input = sys.stdin.readline
V, E = map(int, input().split())

val = [list(map(int, input().split())) for _ in range(E)]
val.sort(key=lambda x:x[2])

totalVal = 0

def check():
    global num
    hits = 1
    visited = [False]*(V+1)
    
    q = []
    q.append(val[0][0])
    visited[val[0][0]] = True
    while q:
        cur = q.pop(0)
        for i in range(num):
            if val[i][0] == cur and not visited[val[i][1]]:
                q.append(val[i][1])
                visited[val[i][1]] = True
                hits += 1
            elif val[i][1] == cur and not visited[val[i][0]]:
                q.append(val[i][0])
                visited[val[i][0]] = True
                hits += 1
    
    if hits == V:
        return True
    else:
        return False               

def linking():
    global totalVal, num
    if num >= E:
        return
    totalVal += val[num][2]
    num += 1
    if check():
        return
    else:
        linking()
    return

num = 0
linking()
print(totalVal)