class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        left_prod = []

        for i in range(len(nums)):
            if i == 0:
                left_prod.append(left)
            else:
                left *= nums[i-1]
                left_prod.append(left)

        right = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                left_prod[i] *= right
            else:
                right *= nums[i+1]
                left_prod[i] *= right

        result = left_prod

        return result

