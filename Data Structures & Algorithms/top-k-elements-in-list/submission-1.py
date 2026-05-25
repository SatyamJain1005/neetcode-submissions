class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_check = {}
        for i in nums:
            if i in freq_check:
                freq_check[i] += 1
            else:
                freq_check[i] = 1

        sorted_ = sorted(freq_check.items(), key=lambda tup: tup[1], reverse=True)
        return [i[0] for i in sorted_[:k]]


        