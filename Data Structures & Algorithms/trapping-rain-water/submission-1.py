from typing import List

class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
            
        n = len(heights)
        # 1. Correct variable initialization
        left, right = 0, n - 1
        leftmax, rightmax = 0, 0
        total_water = 0

        # 2. Added missing loop to traverse the map
        while left < right:
            # 3. Decide which pointer to move based on the smaller wall
            if heights[left] < heights[right]:
                if heights[left] >= leftmax:
                    leftmax = heights[left]  # Update new left max height
                else:
                    total_water += leftmax - heights[left]  # Trap water
                left += 1
            else:
                if heights[right] >= rightmax:
                    rightmax = heights[right]  # Update new right max height
                else:
                    total_water += rightmax - heights[right]  # Trap water
                right -= 1
                
        return total_water