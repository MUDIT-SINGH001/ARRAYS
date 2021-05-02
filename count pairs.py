n,k=map(int,input().split())
a=list(map(int,input().split()))
c=0
l=0
h=n-1
while(l<=h and l!=n):
            if(k==a[l]+a[h] and l<h):
                h=h-1
                c=c+1
            
            elif(l==h):
                l=l+1
                h=n-1
            else:
                h=h-1
            
print(c)
