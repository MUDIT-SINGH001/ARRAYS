a=list(map(int,input().split()))
n=len(a)
x=int(input())
l=0
h=n-1
f=0
while(l<n-2):
    s=a[l]+a[h]
    print(s)
    N=(x-s)
    print(N)
    
    if N in (a[l+1:h]) and N>0:
            f=1
            print("yes")
            break
        
    elif(h>l+2):
            h-=1
    else:
            l+=1
            h=n-1
  
if (f==0):
    print("No")
