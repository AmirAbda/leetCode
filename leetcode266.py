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
        for k, v in hashMap.items(): 
            if v % 2 != 0:
                count += 1
        return count <= 1  

# Example Usage
solution = Solution()  
print(solution.is_palindrome("code")) 
print(solution.is_palindrome("aab"))  
print(solution.is_palindrome("carerac")) 