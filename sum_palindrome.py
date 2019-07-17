r=input()
sum=0
rev=0
while(r!=0):
    a=r%10;
    sum=sum+a;
    r=r/10;
print sum
b=sum
while(b!=0):
    digit=b%10;
    rev=rev*10+digit;
    b=b/10;
print rev
if(rev==sum):
    print ("YES")
else:
    print ("NO")
