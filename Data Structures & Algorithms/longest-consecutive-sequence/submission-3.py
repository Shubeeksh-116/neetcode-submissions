class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        s = set(nums)
        l = 0

        for n in nums:
            if not n-1 in s:
                c = 1
                while n+1 in s:
                    c+=1
                    n+=1
                l = max(l, c)
            else:
                continue
        
        return l
