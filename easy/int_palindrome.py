# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# 

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        #METHOD 1: convert x into string and slice
        string = str(x)
        return string == string[::-1]
        
        #Method 2: Iterativly
        i = 0
        length = len(string) -1
        while i >= length:
            if string[i] != string[length]:
                return False
            i += 1
            length -= 1
        return True
        
