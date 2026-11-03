class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        '''group = []

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            group.append(product)
        return group'''

        left , result = [], []
        product_left = 1
        product_right = 1

        for i in range(len(nums)):
            left.append(product_left)
            product_left *= nums[i]
        
        right = [1] * len(nums)
        for j in range(len(nums)-1, -1, -1):
            right[j] = product_right
            product_right *= nums[j]

        for k in range(len(nums)):
            result.append(left[k] * right[k])
        
        return result


            

        