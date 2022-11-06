n = int(input())
for i in range(n):
    x,y = list(map(int, input().split()))
    if (y-x) % 8 == 0:
        print((y-x) // 8)
    else:
        print(((y-x) // 8) + 1)

