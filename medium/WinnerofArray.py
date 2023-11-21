class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        c = 0
        if k > max(arr):
            return max(arr)
        while 1:
            if arr[0] > arr[1]:
                c += 1
                arr.append(arr[1])
                del arr[1]
            else:
                c = 1
                arr.append(arr[0])
                del arr[0]
            if c == k:
                return arr[0]
