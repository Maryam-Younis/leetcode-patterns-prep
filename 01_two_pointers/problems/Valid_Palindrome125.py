class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sLowerLetters = []
        for char in s:  
            if char.isalnum():
                sLowerLetters.append(char.lower())

        s = sLowerLetters

        left = "" # String pointer to left of palindrome
        right = "" # string pointer to right of palindrome
        lc = 0
        rc = len(s)-1

        for num in range(0, len(s)):
            left = s[lc]
            right = s[rc]

            if left == right:
                lc+=1 
                rc-=1
            elif rc < lc:
                return True
            else:
                return False
        return True