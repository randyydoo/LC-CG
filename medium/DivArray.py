class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        res = []
        nums.sort()
        temp = []
        for num in nums:
            if not temp or num-temp[0] <= k and len(temp) < 3:
                temp.append(num)
            else:
                if len(temp) == 3:
                    res.append(temp)
                temp = [num]

        if len(temp) == 3:
            res.append(temp)

        return res if len(res) == len(nums)//3 else []
