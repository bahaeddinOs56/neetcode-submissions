class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums1 =[]
        for i, num in enumerate(nums):
            nums1.append([num, i])
        l = 0
        r = len(nums) - 1
        nums1.sort()
        while l < r:
            csum = nums1[l][0] + nums1[r][0]
            if csum == target:
                return sorted([nums1[l][1], nums1[r][1]])
                l += 1
                r -= 1
            elif csum < target:
                l += 1
            else:
                r -= 1
        return []
            