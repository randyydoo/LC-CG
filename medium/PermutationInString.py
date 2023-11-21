class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = {} 
        for i in s1:
            if i in dic1:
                dic1[i] += 1
            else:
                dic1[i] = 1
        for i in range(len(s2) - len(s1) + 1):
            dic2 = {}
            count = 0
            for j in range(i, len(s2)):
                if s2[j] in dic2:
                    dic2[s2[j]] += 1
                else:
                    dic2[s2[j]] = 1
                count += 1
                if dic1 == dic2:
                    return True 
                if count == len(s1):
                    break
        return False
