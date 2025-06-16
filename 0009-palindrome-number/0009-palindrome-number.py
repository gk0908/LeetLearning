class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If x is negative or if x ends with a 0 but is not 0, it can't be a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # The number is a palindrome if the first half is equal to the second half
        # or the second half without the middle digit (for odd lengths)
        return x == reversed_half or x == reversed_half // 10
