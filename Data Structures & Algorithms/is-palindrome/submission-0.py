class Solution:
    def isPalindrome(self, s: str) -> bool:
        end = len(s)
        ss = ""
        for i in range(end):
            if s[i].isalnum():
                ss += s[i].lower()
        s1 = ""
        for i in range(end - 1, - 1, -1):
            if s[i].isalnum():
                s1 += s[i].lower()
        return s1 == ss
            