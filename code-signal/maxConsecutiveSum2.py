def solution(inputArray):
    curr_max, global_max = inputArray[0], inputArray[0]
    
    for i in range(1, len(inputArray)):
        num = inputArray[i]
        curr_max = max(num, curr_max + num)
        
        if global_max < curr_max:
            global_max = curr_max

    return global_max
