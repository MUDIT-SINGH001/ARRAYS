a=list(map(int,input().split()))
n=len(a)
l=[]
m=0
j=n-1
for i in range(n-2,0,-1):
    if(a[i]>a[i-1] and a[i]>a[0]):
        m=max(m,a[i]-a[0])
        
        #print(m)
    elif(a[i]<a[i-1]):
        j=i
        m=0
l.append(m)
print(m)
m=0

while(j<n-1):
    m=max(m,a[n-1]-a[j])
    j+=1
l.append(m)
print(m)
print(sum(l))
