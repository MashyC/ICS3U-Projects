arr = [64, 25, 12, 22, 11]
n=len(arr)  


for i in range(n):
      
    #Set the minimum index 
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
              
    #     	
    arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)
