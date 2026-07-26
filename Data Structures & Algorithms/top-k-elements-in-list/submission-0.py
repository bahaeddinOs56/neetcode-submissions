class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        num = count.most_common(k)
        return [n[0] for n in num]