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
# xを一つも持っていない
# def check(item):
#     for item

# for i in range(10 ** 4):
