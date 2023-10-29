def gcd(m,n):
    for i in range(1,min(m,n)+1):
        if m%i == 0 and n%i == 0:
            max_now = i
    return max_now

print(gcd(30,31))
def back_gcd(m,n):
    for i in range(min(m,n),0,-1):
        if m%i == 0 and n%i == 0:
            return i
print(back_gcd(30,20))

def euclid_gcd(m,n):
    if m<n:
        m,n=n,m
    if m%n == 0:
        return n
    return euclid_gcd(n,m%n)
print(euclid_gcd(30,20))