class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)-2):
            if nums[i] == -10**5:
                break
            elif nums[i] == nums[i+1]:
                j = i + 2
                while nums[j] == nums[i]:
                    del nums[j]
                    nums.append(-10**5)

        for num in nums:
            if num != -10**5:
                c += 1

        return c
