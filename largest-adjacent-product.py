def solution(inputArray):
    array_len = len(inputArray)
    product_arr = []
    
    for n in range(array_len - 1):
        product_arr.append(inputArray[n] * inputArray[n+1])
    
    return max(product_arr)

