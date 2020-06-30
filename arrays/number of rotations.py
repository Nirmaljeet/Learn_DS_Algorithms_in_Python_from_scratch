def countrotations(arr, n): 
  
    
    min = arr[0] 
    for i in range(0, n): 
      
        if (min > arr[i]): 
          
            min = arr[i] 
            min_index = i 
          
    return min_index; 
arr = [2, 3, 4, 5, 1]
n = len(arr)
print(countrotations(arr, n))