a=int(input())
x = [int(a) for a in input().split()]
max=x[0]
length=len(x)

for i in range(1,length):
    if x[i]>max:
        max=x[i]
print(max)
