a1 = [2, 3, 5, 8]
a2 = [10, 12, 14, 16, 18, 20]
a1=a1+a2
a1.sort()

n=len(a1)
if(n%2==0):
    m=n//2
    med=a1[m-1]+a1[m]
    print(med//2)
else:
    m=(n+1)//2
    #print(m)
    print(a1[m-1])
