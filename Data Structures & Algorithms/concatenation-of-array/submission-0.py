class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = nums.copy()
        res+=nums.copy()

        return res