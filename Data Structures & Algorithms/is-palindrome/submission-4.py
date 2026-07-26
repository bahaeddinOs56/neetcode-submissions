class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        # if right < 2 :
        #     return False
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

        # end = len(s)
        # ss = ""
        # for i in range(end):
        #     if s[i].isalnum():
        #         ss += s[i].lower()
        # s1 = ""
        # for i in range(end - 1, - 1, -1):
        #     if s[i].isalnum():
        #         s1 += s[i].lower()
        # return s1 == ss
            