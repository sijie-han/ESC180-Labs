import time
def time_func(f,x,n):
    start = time.time()
    for i in range(n):
        f(x)
    end = time.time()
    return (end - start)/n

import matplotlib.pyplot as plt
ns = [1,100,10000,1000000,100000000]
inputs = []


def times(a,b):
    if b == 0:
        return 0
    return times(a,b-1)+a
def linear_search(e,L):
    if L[0] == e:
        return 0
    return linear_search(e,L[1:])+1
#print(linear_search(5,[1,2,3,4,5,6,7,8,9,10]))
def interleave(L1,L2):
    if L1 == [] or L2 == []:
        return L1+L2
    return [L1[0],L2[0]]+interleave(L1[1:],L2[1:])
print(interleave([1,2,3,4],[4,5,6,7]))

def reverse_loop(L):
    if L == [] or len(L) == 1:
        return L    
    return [L[-1]]+reverse_loop(L[1:-1])+[L[0]]
#print(reverse_loop([1,2,3,4,5]))


def reverse_loop_helper(L,index=0):
    L[index],L[-index-1] = L[-index-1],L[index]
    if index == len(L)//2:
        return L
    return reverse_loop_helper(L,index+1)
#print(reverse_loop_helper([1,2,3,4,5,6,7,8,9,10]))

#print (reverse_loop([1,2,3,4,5,6,7,8,9,10]))
def zigzag2(L,index):
    if index == len(L)//2:
        print(L[0],L[-1],end=" ")
        return
    if index == 0:
        print(L[len(L)//2],end=" ")
    else:
        print(L[len(L)//2-index],end=" ")
        print(L[len(L)//2+index],end=" ")
    zigzag2(L,index+1)
#zigzag2([1,2,3,4,5,6,7,8,9],0)

def zigzag3(L):
    n = len(L)
    if n == 0:
        return
    if n%2 == 1:
        print(L[len(L)//2],end=" ")
        L = L[:len(L)//2]+L[len(L)//2+1:]
    else:
        print(L[len(L)//2],end=" ")
        print(L[len(L)//2+1],end=" ")
        L = L[:len(L)//2]+L[len(L)//2+2:]
    zigzag3(L)
zigzag3([1,2,3,4,5,6,7,8,9])




