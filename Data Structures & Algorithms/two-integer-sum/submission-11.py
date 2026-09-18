class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_ = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_.keys():
                return sorted([i, hash_[target - nums[i]]])

            hash_[nums[i]] = i
        
            
        