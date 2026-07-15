class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.replace(" "," ")
        newS = ""
        for c in s:
            if c.isalnum():
                newS+=c.lower()

        return newS == newS[::-1]