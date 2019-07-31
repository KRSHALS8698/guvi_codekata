a,b=input().split(" ")
x = [int(a) for a in input().split()]
s=0;
for i in range(int(b)):
    s=s+x[i]
print(s)
