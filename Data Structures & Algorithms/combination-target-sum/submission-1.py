class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def x(i, c):
            if sum(c)==target:
                res.append(c[:])
                return 
            
            if sum(c)>target:
                return
            

            for j in range(i, len(nums)):
                c.append(nums[j])
                x(j, c)
                c.pop()
        
        x(0, [])

        return res
