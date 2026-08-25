class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_count = Counter(nums)
        
        for v in nums_count.values():
            if v > 1:
                return True
        
        return False