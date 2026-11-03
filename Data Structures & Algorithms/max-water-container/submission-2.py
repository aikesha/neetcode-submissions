class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 1

        left, right = 0, len(heights) - 1

        while left < right:
            current_area = (right - left) * min(heights[left], heights[right])
            if max_area < current_area or len(heights) == 2:
                max_area = current_area
            if heights[left] > heights[right]:
                right -= 1
            else: 
                left += 1
        
        return max_area

        