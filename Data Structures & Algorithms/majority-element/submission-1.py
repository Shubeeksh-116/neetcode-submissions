class Solution:

    # Boyer-Moore Voting Algorithm.
    # when majority elements >n/2, this will work
    
    def majorityElement(self, nums: List[int]) -> int:
        
        c, r = 0, 0

        for n in nums:
            if c ==0:
                r = n
            c+=(1 if n==r else -1)
        
        return r