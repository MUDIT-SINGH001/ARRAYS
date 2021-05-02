a=list(map(int,input().split()))
m=int(input())
a.sort()
i=0
j=m
mi2=max(a)
while(j<=len(a)):
    ma=max(a[i:j])
    mi=min(a[i:j])
    mi2=min(mi2,ma-mi)
    j+=1
    i+=1
    
print(mi2)   
    
    
    
