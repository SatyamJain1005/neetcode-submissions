class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        helper_ = {}
        for i in nums:
            if i not in helper_:
                helper_[i] = 1
            else:
                helper_[i] += 1
        
        if sum(helper_.values()) == len(helper_.keys()):
            return False
        else:
            return True
        