class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}

        for i in strs:
            a = sorted(i)
            key = ''.join(a)
            if key not in out:
                out[key] = []

            out[key].append(i)
            
        return list(out.values())
        