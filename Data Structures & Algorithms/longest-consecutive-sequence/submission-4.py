class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #nums.sort()
        if not nums:
            return 0
        max_len = 1
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_len = 1
                while num + current_len in num_set:
                    current_len += 1
                max_len = max(current_len, max_len)
        return max_len






        