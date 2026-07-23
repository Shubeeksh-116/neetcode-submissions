class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates[:]
        nums.sort()
        res = []

        def x(i, c):
            if sum(c)==target:
                res.append(c[:])
                return 
            
            if sum(c)>target:
                return
            

            for j in range(i, len(nums)):
                if j>i and nums[j]== nums[j-1]:
                    continue

                c.append(nums[j])
                x(j+1, c)
                c.pop()
        
        x(0, [])

        return res
