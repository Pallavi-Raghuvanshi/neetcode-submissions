class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        w = 0

        left = 0
        right = n-1
        while left < right:

            if heights[left] <= heights[right]:
                w = max(w, heights[left] * (right - left))
                left += 1
            elif heights[left] >= heights[right]:
                w = max(w, heights[right] * (right - left))
                right -= 1

        return w


