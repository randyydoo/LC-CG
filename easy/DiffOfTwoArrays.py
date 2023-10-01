class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = [[], []]

        for num in nums1:
            if num not in nums2 and num not in ans[0]:
                ans[0].append(num)

        for num in nums2:
            if num not in nums1 and num not in ans[1]:
                ans[1].append(num)
        
        return ans
