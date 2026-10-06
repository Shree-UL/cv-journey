ls = [1, 2, 3, 4, 5]
rev_ls = []
for i in range(0, len(ls)):
    last = ls.pop()
    rev_ls.append(last)

print(rev_ls)