class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        temp = [] 
        ans = []
        #create bucket
        for i in range(len(nums) + 1):
            temp.append([])

        for i in nums:
            if i in dic:
                dic[i] += 1
            else: 
                dic[i] = 1
        #insert num into bucket with same # freq
        for num,freq in dic.items():
            temp[freq].append(num)

        for i in reversed(range(0,len(temp))):
            if len(temp[i]) is not 0:
                for num in temp[i]:
                    ans.append(num)
            if len(ans) == k:
                return ans
            
