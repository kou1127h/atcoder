H, W = list(map(int, input().split()))
map = []
skip_row = []
skip_col = []
for i, h in enumerate(range(H)):
    a = [i for i in input()]
    if "#" not in a:
        skip_row.append(i)
    map.append(a)

for w in range(W):
    black = 0
    for h in range(H):
        if map[h][w] == "#":
            black += 1
            break
    if black == 0:
        skip_col.append(w)

for i, item in enumerate(map):
    if i in skip_row:
        continue
    plt = ""
    for j, col in enumerate(item):
        if j in skip_col:
            continue
        plt += col
    print(plt)
