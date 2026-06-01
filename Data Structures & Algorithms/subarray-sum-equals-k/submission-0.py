class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curS = 0
        pre = {0:1}
        
        for n in nums:
            curS += n
            if curS-k in pre:
                res+=pre[curS-k]
            pre[curS] = 1+pre.get(curS, 0)
        
        return res