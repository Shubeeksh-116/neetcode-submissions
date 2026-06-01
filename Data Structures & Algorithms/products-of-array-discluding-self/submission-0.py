class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        prefix = [1]
        for i in range(len(nums)-1):
            pre = pre*nums[i]
            
            prefix.append(pre)
        
        post = 1
        postfix = [1]
        for i in range(len(nums)-1, 0, -1):
            post = post*nums[i]
            postfix=[post]+postfix
        
        res = []
        for i in range(len(nums)):
            res.append(prefix[i]*postfix[i])
            
        return res
