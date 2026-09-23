class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        un_nums = sorted(list(set(nums)))
        last = 0
        count = 0
        max_count = 0
        for i in range(len(un_nums)):
            if i == 0:
                last = un_nums[i]
                count += 1
            else:
                if last == un_nums[i]-1:
                    count += 1
                else:
                    count = 1
                last = un_nums[i]

            if count > max_count:
                max_count = count

        return max_count