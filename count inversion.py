l=list(map(int,input().split()))
c=0

for i in range(0,6):
        j=i+1
        while(j!=7):
            if(l[i]>l[j]):
                c=c+1
                j=j+1
            else:
                j=j+1
print(c)            
