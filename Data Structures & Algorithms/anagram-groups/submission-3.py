class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_ = {}

        for i in strs:
            if ''.join(sorted(i)) in map_:
                map_[''.join(sorted(i))].append(i)
            else:
                map_[''.join(sorted(i))] = [i]


        return sorted(map_.values(), key=len)
        