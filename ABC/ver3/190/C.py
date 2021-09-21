N, M = list(map(int, input().split()))
conditions = []
for m in range(M):
    conditions.append(list(map(int, input().split())))
K = int(input())

choice = []

for k in range(K):
    choice.append(list(map(int, input().split())))

ans = 0
for i in range(2**K):
    dishes = [False] * N
    temp = 0
    for j in range(K):
        if (i >> j) & 1:
            dishes[choice[j][0] - 1] = True
        else:
            dishes[choice[j][1] - 1] = True
    for item in conditions:
        if dishes[item[0] - 1] == True and dishes[item[1] - 1] == True:
            temp += 1

    ans = max(ans, temp)

print(ans)
