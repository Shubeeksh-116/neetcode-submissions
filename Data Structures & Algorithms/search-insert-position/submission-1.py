class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
            l,r = 0, len(nums)-1

            while l<=r and l!=r+1:
                m = (l+r)//2
                if nums[m]>target:
                    r = m-1
                elif nums[m]<target:
                    l = m+1
                else:
                    return m
            return l