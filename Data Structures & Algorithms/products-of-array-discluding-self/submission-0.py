class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    n[i] *= nums[j]
        return n 