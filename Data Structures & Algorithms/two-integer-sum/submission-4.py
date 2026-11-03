class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        group = dict()
        for ind, num in enumerate(nums):
            difference = target - num
            if difference in group:
                return [group[difference], ind]
            group[num] = ind