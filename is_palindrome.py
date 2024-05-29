def is_palindrome(s):
    left=0
    right=len(s)-1
    while left < right:
        if s[left]!=s[right]:
            return False 
        left+=1
        right-=1
    return True 
s="racecar"
s_2="banana"
sol=is_palindrome(s)
sol_2=is_palindrome(s_2)
print(sol)
print(sol_2)

        