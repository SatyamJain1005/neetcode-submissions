class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = {}

        for i in strs:
            if ''.join(sorted(i)) in mapp.keys():
                mapp[''.join(sorted(i))].append(i)
            else:
                mapp[''.join(sorted(i))] = [i]

        return list(mapp.values())