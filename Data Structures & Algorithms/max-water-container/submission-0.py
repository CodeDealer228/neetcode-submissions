class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        max_l = len(heights)
        r = max_l - 1
        ans = (min(heights[l], heights[r]) * (r-l))
        while l < r:
            ans = max(ans, min(heights[l], heights[r]) * (r-l))  # ✅ ПЕРЕД сдвигом
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return ans

                    

