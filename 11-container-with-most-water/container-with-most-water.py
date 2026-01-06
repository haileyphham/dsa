class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        curr_max = 0

        while left < right:
            min_height = min(height[left], height[right])
            width = right - left
            total_area = min_height * width
            curr_max = max(curr_max, total_area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return curr_max


        