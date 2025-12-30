class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while right > left: 
            length = right - left
            curr_height = min(height[right], height[left])
            new_area = length * curr_height

            if new_area > max_area:
                max_area = new_area
                
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max_area
