s=int(input())
n=0
while s>0:
    a=s % 10
    n=n+(a*a)
    s=s//10
print n
