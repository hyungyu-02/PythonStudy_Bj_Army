import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

size = 1
def bound(num, lev):
    global size
    
    if lev == bound:
        if num == s:
            ans += 1
        return
    