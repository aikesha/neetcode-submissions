class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        if len(nums) == 2 and k == 1:
            return [nums[0]]
        
        my_dict = {}

        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1
        
        group = [[] for _ in range(len(nums)+1)]
        for num, count in my_dict.items():
            group[count].append(num)
        
        result = []
        for count in range(len(group)-1, 0, -1):
            for num in group[count]:
                result.append(num)
                if len(result) == k:
                    return result

        



        