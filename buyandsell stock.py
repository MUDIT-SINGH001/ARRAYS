a=list(map(int,input().split()))
n=len(a)
m=0
l=0
h=n-1
while(l<=h):
        if(a[l]<a[h]):
            m=max(m,a[h]-a[l])
            h=h-1
        elif(a[l]>a[h]):
            h=h-1
        elif(l==h):
            l=l+1
            h=n-1
print(m)    
            
