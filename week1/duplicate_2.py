ls = [1,1,1,1]
seen = set()
dupl = []
for i in range(0, len(ls)):
    print(ls[i])
    if ls[i] in seen:
        print(ls[i])
        if ls[i] not in dupl:
            dupl.append(ls[i])
    else:
        seen.add(ls[i])

print(seen)
print(dupl)