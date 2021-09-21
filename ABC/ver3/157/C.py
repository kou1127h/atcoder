N, M = list(map(int, input().split()))
num = [0] * N
changed = [False] * N

available = True
for i in range(M):
    s, c = list(map(int, input().split()))
    s -= 1
    if changed[s] == False:
        if N != 1 and s == 0 and c == 0:
            available = False
        num[s] = c
        changed[s] = True
    elif changed[s] == True and num[s] != c:
        available = False

if N != 1 and num[0] == 0 and available:
    num[0] = 1

if not available:
    print(-1)

else:
    for i, item in enumerate(num):
        print(item, end="")
