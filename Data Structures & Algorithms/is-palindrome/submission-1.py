class Solution:
    def isPalindrome(self, s: str) -> bool:
        #we can just reverse the string and check if its equal to our string

        newString = ''

        for c in s:
            if c.isalnum():
                newString += c.upper()
        return newString == newString[::-1]