class Solution:
    def frequency(self,string):
        hashMap = {}
        for s in string:
            if s not in hashMap:
                hashMap[s] = 1
            else:
                hashMap[s] += 1
        return hashMap

    def is_palindrome(self,s):
        hashMap = self.frequency(s)
        count = 0
        for k, v in hashMap.items():  # Correct iteration order
            if v % 2 != 0:
                count += 1
        return count <= 1  # Direct boolean return

# Example Usage
solution = Solution()  # Create an instance of the class
print(solution.is_palindrome("code"))  # Output: False
print(solution.is_palindrome("aab"))   # Output: True
print(solution.is_palindrome("carerac")) # Output: True