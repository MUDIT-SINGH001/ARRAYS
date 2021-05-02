import math
n=int(input())
k=int(input())
d=math.ceil(n//k)
l=[]
a=list(map(int,input().split()))
a.sort()
for i in range(n):
    co=a.count(a[i])
    if(co>d):
        if a[i] not in l:
            l.append(a[i])
        
print(l)    
