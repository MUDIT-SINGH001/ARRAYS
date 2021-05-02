a=list(map(int,input().split()))
c=0
l=0
n=7
h=n-1
while(l<=h):
    if(a[l]>a[h]):
        h=h-1
        c=c+1
    elif(a[l]<a[h]):
        h=h-1
    elif(a[l]==a[h] and l!=n-1):
        h=n-1
        l=l+1
    else:
            break
print(c)        
