class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 1
        tot = 1
        
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]:
                continue
            else:
                nums[c] = nums[i]
                c+=1
                tot +=1
            
        return tot