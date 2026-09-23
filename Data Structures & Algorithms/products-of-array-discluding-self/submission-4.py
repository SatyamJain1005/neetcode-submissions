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
        right_prod = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                right_prod.append(right)
            else:
                right *= nums[i+1]
                right_prod[i] = right

        result = []
        for i, j in zip(left_prod, right_prod):
            result.append(i*j)

        return result

