a=[0,9,8,7,6,1,0,2,3,0]
n=len(a)
a.append(0)
for i in range(0,n):
        a[n-i]=a[n-i-1]
a[0]=a[n]
a.pop()
print(a)
