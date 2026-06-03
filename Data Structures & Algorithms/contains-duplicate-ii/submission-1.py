class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        for i in range(len(nums)):
            j=i+1
            while j<=i+k:
                if j<len(nums) and nums[i]==nums[j]:
                    return True
                j+=1
        return False