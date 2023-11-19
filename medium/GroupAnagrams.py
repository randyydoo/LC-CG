class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic ={}
        ans = []
        for word in strs:
            if tuple(sorted(word)) in dic:
                dic[tuple(sorted(word))].append(word)
            else:
                dic[tuple(sorted(word))] = [word]
        for lists in dic.values():
            ans.append(lists)
        return ans
