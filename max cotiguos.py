l=list(map(int,input().split()))
a=[]
n=len(l)
j=0
s1=[]
for i in range(0,n):
    s=l[i]
    j=i
    while(j!=n+1):
        s=max(s,sum(l[i:j+1]))
        j=j+1
        if(s>=l[i]):
            s1=s
            #print(s1)
    a.append(s1)
#print(a)
print(max(a))
