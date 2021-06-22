N = int(input())
ans_list = []


def dfs(item, count):
    if count == N:
        ans_list.append("".join(item))
    else:
        new_count = count + 2
        new_item = item + ["()"]
        dfs(new_item, new_count)

        for i in range(len(item)):
            new_item = item[0:i] + [f"({item[i]})"] + item[i+1:]
            new_count = count + 2
            dfs(new_item, new_count)


if N % 2 == 0:
    start = ["()"]
    count = 2
    dfs(start, count)

ans = list(set(ans_list))
ans.sort()
for item in ans:
    print(item)
