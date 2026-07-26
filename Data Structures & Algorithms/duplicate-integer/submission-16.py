class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # count = Counter(nums)
        # for n, c in count.items():
        #     if c >= 2: return True
        # return False

        # count = Counter(nums)
        # if count.most_common(1)[0][1] >= 2 : return True
        # return False
        # nums.sort()
        # for num in range(len(nums) - 1): 
        #     if nums[num] == nums[num + 1] : return True
        # return False
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
        if len(seen) < len(nums): return True
        return False