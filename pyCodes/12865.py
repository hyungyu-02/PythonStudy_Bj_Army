n, k = map(int, input().split())
items = []
for _ in range(n):
    w, v = map(int, input().split())
    items.append((w,v))

maxVal = 0
bag = []

def bt(W, V, idx):
    if idx == n:
        if maxVal < V:
            maxVal = V
        return
    for i in range(idx, n):
        if W + items[i][0] <= k:
            bag.append(items[i])
            bt(W + items[i][0], V + items[i][1], idx+1)
            bag.pop()
        else:
            if maxVal < V:
                maxVal = V
bt(0,0,0)
print(maxVal)