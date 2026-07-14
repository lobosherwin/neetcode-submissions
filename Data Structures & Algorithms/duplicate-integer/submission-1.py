class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        Map = set()
        for i in range(len(nums)):
            if nums[i] in Map:
                return True
            Map.add(nums[i])
        return False
            