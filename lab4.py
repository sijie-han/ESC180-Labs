def duplicate(list0):
    for i in range(1,len(list0)):
        if list0[i]== list0[i-1]:
            return True
    return False
print(duplicate([1,2,3,4,5]))
print(duplicate([1,2,3,4,4]))

def match_pattern(list1, list2):
    for i in range(len(list1)-len(list2)):
        if list1[i:i+len(list2)] == list2:
            return True
    return False
print(match_pattern([4, 10, 2, 3, 50,100], [10, 2, 3, 50]))

def list1_start_with_list2(list1, list2):
    if len(list1)< len(list2):
        return False
    for i in range(len(list2)):
        if list2[i] != list1[i]:
            return False
    return True
print(list1_start_with_list2([2,3,4],[2,5]))

def lists_are_the_same(list1, list2):
    for i in range(min(len(list1),len(list2))):
        if list1[i] != list2[i]:
            return  False
    return True
def list_to_str(lis):
    string = "["
    for num in lis:
        string += str(num)
    return string+"]"
def count_evens(L):
    sum = 0
    for num in L:
        if num %2 == 0:
            sum += 1
    return sum
print(count_evens([1,2,3,4]))

def euclid_gcd(m,n):
    if m<n:
        m,n=n,m
    if m%n == 0:
        return n
    return euclid_gcd(n,m%n)

def euclid_fraction(n, m):
    if n%m == 0:
        return n//m
    bigger = max(n,m)
    smaller = min(n,m)
    while bigger % smaller != 0:
        bigger, smaller = smaller, bigger% smaller
    gcd = smaller
    num = n//gcd
    den = m//gcd
    return str(num)+"/"+str(den)
print(euclid_fraction(4,2))

def next(y,m,d):
    pass

