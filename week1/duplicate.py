ls = [1,8,4,6,9,4,2,6,715,58,6,3,2,595,4,6,6,52,6,5,6,2,2]
dupl = []
for i in range(0, len(ls)):
    #print(ls[i])
    for j in range(i+1, len(ls)):
        #print(ls[j])
        if ls[i] == ls[j]:
            #print("found")
            if ls[j] not in dupl:
                dupl.append(ls[j])
            break

print(dupl)