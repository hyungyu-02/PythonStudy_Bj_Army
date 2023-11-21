#백트래킹
n, m = map(int, input().split())
grp = []

def bt(recent):
    if len(grp) == m:
        print(' '.join(map(str, grp)))
        return
    for i in range(recent, n+1):
        grp.append(i)
        bt(i)
        grp.pop()

bt(1)