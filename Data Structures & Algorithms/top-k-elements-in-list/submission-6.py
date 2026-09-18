class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_ = {}

        for i in nums:
            if i not in hash_.keys():
                hash_[i] = 0
            
            hash_[i] += 1

        return sorted(sorted(hash_, key=lambda x: hash_[x], reverse=True)[:k])
        