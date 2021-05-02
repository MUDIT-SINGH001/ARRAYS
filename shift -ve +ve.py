arr=list(map(int,input().split()))
for i in range(0,len(arr)):
    if(arr[i]>0):
        arr[len(arr)-i-1]=arr[i]
print(arr)        
