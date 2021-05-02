a=list(map(int,input().split()))
c=0
lo=0
h=1
while(lo<h and lo<len(a)):
    if(sum(a[lo:h])==0 and h<=len(a)):
        print(a[lo:h])
        c=c+1
        break
    elif(h==len(a)):
        lo=lo+1
        h=lo+1
    else:
        h=h+1
        
        
        
if(c>0):
    print("YES")
else:
    print("NO")
