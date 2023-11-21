class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:   
        l, r = 0, len(numbers)-1
        while 1:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1,r+1]
            elif s > target:
                r -= 1
            else:
                l += 1
