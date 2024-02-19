class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        mp = set()

        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            while j < k:
                temp_sum = nums[i]+nums[j]+nums[k]
                if temp_sum == 0 and tuple([nums[i], nums[j], nums[k]]) not in mp:
                    res.append([nums[i], nums[j], nums[k]])
                    mp.add(tuple([nums[i], nums[j], nums[k]]))
                    k-=1
                    j+=1
                elif temp_sum < 0:
                    j += 1
                else:
                    k -= 1
                    
        return res
