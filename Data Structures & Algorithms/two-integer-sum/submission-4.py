class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        help_dict = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            
            if comp in help_dict:
                return [help_dict[comp], i]
                
            help_dict[nums[i]] = i