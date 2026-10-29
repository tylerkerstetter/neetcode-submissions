class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        currMax = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            width = abs(left - right)
            height = min(heights[left], heights[right])
            area = width * height
            if area > currMax:
                currMax = area
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return currMax