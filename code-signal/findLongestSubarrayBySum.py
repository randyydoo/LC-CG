def solution(s, arr):
        
    left, right = 0, 0
    curr_sum = 0 
    ans = [-1]
    
    while right <= len(arr) - 1:
        curr_sum += arr[right] 
        
        while left < right and  curr_sum > s:
            curr_sum -= arr[left]
            left += 1
             
        if curr_sum == s and (ans[0] == -1 or (ans[1] - ans[0] < (right + 1) - (left + 1))):
            ans = [left+1, right+1]
            
        right += 1   
        
    return ans
