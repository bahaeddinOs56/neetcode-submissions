class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = l + 1
        res = 0
        a = []
        if len(s) > 0:
            a.append(s[l])
        if len(s) == 1:
            return 1
        while r < len(s) and l < len(s):
            if s[r] not in a:
                a.append(s[r])
                res = max(res, len(a))
                r += 1
            else:
                a.remove(s[l])
                l += 1
        return res
