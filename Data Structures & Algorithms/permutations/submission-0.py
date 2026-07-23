class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def x(c):
            if len(c) == len(nums):
                res.append(c[:])
                return

            for n in nums:
                if n in c:
                    continue
                c.append(n)
                x(c)
                c.pop()
            
        x([])
        return res
