a=list(map(int,input().split()))
n=len(a)
lo=0
h=1
prod=0
for i in range(0,n):
    m=1    
    for j in range(i,n):
        m=m*a[j]
        prod=max(prod,m)
        #print(prod)
        
    
print(prod)    
            
