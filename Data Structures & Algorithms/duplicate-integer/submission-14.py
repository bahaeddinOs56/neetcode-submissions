class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return True
        # return False
        nums.sort()
        for i, num in enumerate(nums):
            if i < len(nums) - 1 and num == nums[i + 1]:
                return True
        return False