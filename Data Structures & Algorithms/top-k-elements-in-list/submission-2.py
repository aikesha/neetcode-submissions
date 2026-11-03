class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        if len(nums) == 2 and k == 1:
            return [nums[0]]
        
        my_dict = {}

        for num in nums:
            my_dict[num] = my_dict.get(num, 0) + 1
        
        group = [[] for _ in range(len(nums)+1)]
        for num, count in my_dict.items():
            group[count].append(num)
        
        result = []
        for count in range(len(group)-1, 0, -1):
            for num in group[count]:
                result.append(num)
                if len(result) == k:
                    return result

        



        