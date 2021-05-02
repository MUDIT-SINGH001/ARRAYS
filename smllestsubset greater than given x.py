a=list(map(int,input().split()))
x=int(input())
l=[]
for i in range(0,len(a)-1):
    dif=x-a[i]
    c=1
    for j in range(i+1,len(a)):
    
        dif=dif-a[j]
        if(dif>=0):
            c=c+1
            
        else:
            c=c+1
            l.append(c)
            print(c)
            break
print(min(l))
