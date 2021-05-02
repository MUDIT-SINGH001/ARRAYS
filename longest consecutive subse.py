n=int(input())
a=list(map(int,input().split()))
a.sort()
l=list(set(a))
k=l[0]
i=0
c=0
while(i!=n and k<=max(l)):
    
    if(k==l[i]):
        k=k+1
        i=i+1
        c=c+1
    else:
        break
print(c)    
    
