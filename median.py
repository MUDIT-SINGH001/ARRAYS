a=list(map(int,input().split()))
n=int(input())

a.sort()
if(n%2==0):
    m=n//2
    med=a[m-1]+a[m]
    print(med//2)
else:
    m=(n+1)//2
    print(m)
    print(a[m-1])
