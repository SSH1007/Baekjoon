while 1:
    c, d = map(int, input().split())
    if c == 0 and d == 0:
        break
    print(min(30*c+40*d, 35*c+30*d, 40*c+20*d))