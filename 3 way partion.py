def threeWayPartition(self, arr, a, b):
	    # code here 
	    start = 0
        end = len(arr) - 1
        i = 0
  
    # Traverse elements from left
        while i <= end:
  
       
            if arr[i] < a:
                temp = arr[i]
                arr[i] = arr[start]
                arr[start] = temp
                i += 1
                start += 1
      
        
            elif arr[i] > b:
                temp = arr[i]
                arr[i] = arr[end]
                arr[end] = temp
                end -= 1
      
            else:
                i += 1
