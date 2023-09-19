n = int(input())
if n <= 2:
    print(n)
else:
    num = 2
    while num < n:
        num *= 2
    num /= 2
    print((int)(n-num)*2)