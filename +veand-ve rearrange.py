l=[-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
n=len(l)
l1=[]
mi=l[0]
i=1

while(len(l)!=0):
    i=0
    while(i!=len(l)):
        mi=min(mi,l[i])
        if(mi<0):
            l1.append(mi)
            l.remove(mi)
            i=0
            break
        else:
            i=i+1
        
    i=0
    while(i<len(l)):
        mi=l[i]
        if(mi>0):
            l1.append(mi)
            l.remove(mi)
            i=0
            break
        else:
            i=i+1
    
     

print(l1)        
        
    
