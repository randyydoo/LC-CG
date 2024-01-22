class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(l, r, flag):
            i = -1
            while l<=r:
                mid = l+(r-l)//2
                if nums[mid] < target:
                    l = mid+1
                elif nums[mid] > target:
                    r = mid-1
                else:
                    i = mid
                    if flag:
                        l = mid+1
                    else:
                        r = mid-1
            return i
        
        l = search(0,len(nums)-1, False)
        r = search(0,len(nums)-1, True)
        return [l,r]
