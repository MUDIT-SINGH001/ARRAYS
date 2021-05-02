l=[]
a=[[0,0]]
print(a[0][1])
for i in range(0,4):
    l.append(list(map(int,input().split())))
l.sort()    
print(l)
i=0
k=0
while(i!=4):
    if(a[k][1]<=l[i][0]):
        j=i+1    
        while(j!=4):
                if(l[i][1]>=l[j][0]):
                    l[i][1]=max(l[i][1],l[j][1])
                    j=j+1
                            
                else:
                    a.append(l[i])
                    i=i+1
                    k=k+1
                    break
        if(j==4):
              if(l[j-1][0]<=l[i][1]):
                    l[i][1]=max(l[j-1][1],l[i][1])
                    a.append(l[i])
                    break
                
                            
              else:
                    a.append(l[j-1])
                    k=k+1
                    i=i+1
                    break
                    
              
    else:
          i=i+1
a.remove(a[0])          
print(a)            
#a.append(l[i])          
                    
