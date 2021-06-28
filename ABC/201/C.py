S = list(input())

must_have = []
maybe = []
do_not_have = []

for i, s in enumerate(S):
    if s == "o":
        must_have.append(i)
    elif s == "x":
        do_not_have.append(i)
    else:
        maybe.append(i)

count = 0

# ◯を全種類持っている


def check_true(item):
    temp = []
    for i in item:
        for j in must_have:
            if i == str(j):
                temp.append(i)
    temp = list(set(temp))
    return len(temp) == len(must_have)

# xを一つも持っていない


def check_false(item):
    ans = True
    for i in item:
        if int(i) in do_not_have:
            ans = False
    return ans


def check(item):
    string = str(item).zfill(4)
    ans_true = check_true(string)
    ans_false = check_false(string)
    return ans_true and ans_false


count = 0
for i in range(10 ** 4):
    ans = check(i)
    if ans:
        count += 1

print(count)
