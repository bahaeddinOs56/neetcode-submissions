class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if len(s2) == len(s1):
            return Counter(s1) == Counter(s2)
        l = 0
        r = l + len(s1) - 1
        while r < len(s2) and l < len(s2):
            s3 = list(s1)
            while l <= r:
                if s2[r] in s3:
                    s3.remove(s2[r])
                    r -= 1
                else:
                    break
            l += 1
            r = l + len(s1) - 1 
            if len(s3) == 0:
                return True
        return False

        