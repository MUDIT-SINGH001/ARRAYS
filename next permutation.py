import math
l=list(map(int,input().split()))
s=l.copy()
n=len(l)
k=0
while(k<=n):
    for i in range(n-1,0,-1):
        l[i],l[i-1]=l[i-1],l[i]
        if(l>s):
            #print(l)
            break
    k=k+1
    if(l>s):
        break
if(l<=s):           
    s.sort()
    print(s)
else:
    print(l)
