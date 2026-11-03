class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in my_dict and i != my_dict[diff]:
                return [my_dict[diff], i]
            my_dict[num] = i
        '''left, right = 0, len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                return [left, right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1'''


        