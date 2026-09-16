class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = {}

        for i in nums:
            if i in dict_:
                dict_[i] += 1
            else:
                dict_[i] = 1

        return sorted(dict_, key=lambda x: dict_[x], reverse=True)[:k]
        