def merge_sort(arr):
    
    n = len(arr)
    if n < 2:
        return arr
    
    mid = int(n/2)
    left = arr[:mid]
    right = arr[mid:]

    return merge(merge_sort(left), merge_sort(right))
        

        
def merge(left, right):
        
    result = []
    i = 0
    j = 0
    while len(result) < len(left) + len(right): 
        if left[i] <= right[j]:
            result.append(left[i])
            i  += 1
        else:
            result.append(right[j])
            j += 1
        
        if j == len(right):
            result += left[i:]
        
        if i == len(left):
            result += right[j:]
           
    return result
    