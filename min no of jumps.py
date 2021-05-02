a=list(map(int,input().split()))
c=0
i=0

while(i<len(a)):
    i=i+a[i]
    if(a[i]==0):
        print(-1)
        break
    c=c+1
    if(i>=len(a)-1):
        break
    
       
print(c)



#2 3 1 1 2 4 2 0 1 1
