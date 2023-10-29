pi = 0
for i in range(1001):
    pi += (-1)**i/(2*i+1)
pi = pi*4
print(pi)