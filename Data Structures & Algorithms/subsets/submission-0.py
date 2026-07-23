class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def x(i,c):
            if i==len(nums):
                res.append(c[:])
                return
            # dont pick
            x(i+1,c)

            # pick
            c.append(nums[i])
            x(i+1,c)
            c.pop()
        
        x(0,[])
        return res