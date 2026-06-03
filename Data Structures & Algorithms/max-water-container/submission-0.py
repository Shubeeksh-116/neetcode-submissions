class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ma = 0
        i,j = 0,len(heights)-1

        while i<j:
            a = min(heights[i],heights[j])*(j-i)
            if a>ma: ma=a

            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return ma