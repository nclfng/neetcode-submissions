class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # feature, pattern, tools
        newnums = set(nums)
        return len(newnums) != len(nums)