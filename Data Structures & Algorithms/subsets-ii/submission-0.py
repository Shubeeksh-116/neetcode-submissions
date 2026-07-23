class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = len(nums)
        nums.sort()

        def x(i, c):
            
            res.append(c[:])

            for j in range(i, len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue

                c.append(nums[j])
                x(j+1,c)
                c.pop()

        x(0,[])
        return res   
               