class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        left_prod = []

        for i in range(len(nums)):
            if i == 0:
                left_prod.append(left)
            else:
                left = left*nums[i-1]
                left_prod.append(left)

        right = 1
        right_prod = []
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                right_prod.append(right)
            else:
                right = right*nums[i+1]
                right_prod.append(right)
            
        right_prod.reverse()

        result = []
        for i, j in zip(left_prod, right_prod):
            result.append(i*j)

        return result

