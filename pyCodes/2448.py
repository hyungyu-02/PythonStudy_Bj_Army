#recursion
n = int(input())
star = [[' ']*n*2 for _ in range(n)]

def draw(i, j, size):
    if size == 3:
        star[i][j] = '*'
        star[i+1][j-1] = '*'
        star[i+1][j+1] = '*'
        for k in range(-2, 3):
            star[i+2][j+k] = '*'
    else:
        dev = size//2
        draw(i, j, dev)
        draw(i+dev, j-dev, dev)
        draw(i+dev, j+dev, dev)
draw(0, n-1, n)
for s in star:
    print("".join(s))