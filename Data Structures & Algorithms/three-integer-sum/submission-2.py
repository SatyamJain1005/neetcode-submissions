class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):
            target = -nums[i]
            sorted_arr = nums[i+1:]
            left = 0
            right = len(sorted_arr)-1
            
            while left < right:
                if sorted_arr[left]+sorted_arr[right] == target:
                    res = sorted([nums[i], sorted_arr[left], sorted_arr[right]])
                    if res not in output:
                        output.append(res)
                    left += 1
                elif sorted_arr[left]+sorted_arr[right] < target:
                    left += 1
                else:
                    right -= 1

        return output
