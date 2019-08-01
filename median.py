import statistics
a=int(input())
x = [int(a) for a in input().split()]
print(statistics.median(x))