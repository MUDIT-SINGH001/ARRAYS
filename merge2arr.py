n=int(input())
m=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr1.sort()
arr2.sort()
for i in range(0,n+m):
    if(n<=m):
        if(i==n):
            break
        if(arr1[n-i-1]>arr2[i]):
            arr1[n-i-1],arr2[i]=arr2[i],arr1[n-i-1]
       
    else:
        if(i==m):
            break
        if(arr1[n-i-1]>arr2[i]):
            arr1[n-i-1],arr2[i]=arr2[i],arr1[n-i-1]
        
             
arr1.sort()
arr2.sort()
print(' '.join(map(str,(arr1+arr2))))           
