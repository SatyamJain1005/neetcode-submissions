class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_ = set()
        for i in nums:
            if i in check_:
                return True

            check_.add(i)
        return False