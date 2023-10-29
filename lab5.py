
L = [["CIV", 92],
     ["180", 98],
     ["103", 99],
     ["194", 95]]
print(L[2][1])

def get_nums(L):
    res = []
    for lis in L:
        res.append(lis[1])
    return res
print(get_nums(L))

def lookup(L,num):
    for i in L:
        if i[1]== num:
            return i[0]
print(lookup(L,95))
