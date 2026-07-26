class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
                return 0
        nums.sort()
        # d = {}
        count = 1
        maxn = 1
        for i in range(len(nums) - 1):
            if nums[i] ==  nums[i + 1]:
                continue
            elif nums[i + 1] ==  nums[i] + 1:
                # d[i] = num[i]
                count += 1
                maxn = max(maxn, count)
            else:    
                count = 1
        return maxn
              
