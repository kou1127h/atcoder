a, b, c, d = list(map(int, input().split()))
n = 0
# a + b * n =< d * (c * n)

ans = 0
# 1かいめ
left_1 = a + b
right_1 = d * c
diff_1 = left_1 - right_1


# 2かいめ
left_2 = a + b * 2
right_2 = d * c * 2

diff_2 = left_2 - right_2

if diff_1 <= diff_2:
    ans = -1
else:
    i = 3
    while True:
        left = a + (b * i)
        right = d * c * i
        diff = left - right
        if diff <= 0:
            ans = i
            break
        i += 1

if diff_1 <= 0:
    ans = 1
elif diff_2 <= 0:
    ans = 2

print(ans)
