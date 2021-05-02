l=list(map(str,input().split(',')))
l1=[]
for i in range(0,len(l)):
    l1.append(int(l[i]))
s=sum(l1)
se=set(l1)
s1=sum(se)
print(abs(s1-s))
